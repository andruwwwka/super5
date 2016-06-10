$(function() {

	//server json
	var serverJson = $('[name="training_response"]').val();
	serverJson = JSON.parse(serverJson);

	//copy server json into exercises arr. All exercises in a row, avoiding sets.
	var exercises = [];
	copyServerJson();

	//for swapIframeClass()
	var iframeA = $('#player1');
	var iframeB = $('#player2');
	var iframeAIsActive = true;

	//for vimeo api
	var iframe1 = $('#player1')[0];
	var iframe2 = $('#player2')[0];
	var player1 = $f(iframe1);
	var player2 = $f(iframe2);

	//to switch players and check current and next player
	var playPlayer1 = false;
	var playPlayer2 = false;

	//counters
	var setCounter = 0;
	var iframeSrcCounter = 0;
	var exerciseCounter = 0;

	//prepare before play
	setIframeSrc(iframe1, exercises[0].id);
	setIframeSrc(iframe2, exercises[1].id);
	iframeSrcCounter++;


	$('.btn-workout.-start').on('click', function(e){
		e.preventDefault();

		$('.video_preview, .training-player-l').toggleClass('hidden');
		playPlayer1 = true;
		player1.api('play');
	})


	player1.addEvent('ready', function() {
		if (playPlayer1) { player1.api('play'); }
		if (!playPlayer1) setTimeout(function() { player1.api('play'); player1.api('pause'); }, 1000);

		player1.addEvent('playProgress', onPlayProgress);
	});

	player2.addEvent('ready', function() {
		if (playPlayer2) { player2.api('play'); }
		if (!playPlayer2) setTimeout(function() { player2.api('play'); player2.api('pause'); }, 1000);

		player2.addEvent('playProgress', onPlayProgress);
	});


	function onPlayProgress(data, id) {
		if (data.seconds >= exercises[exerciseCounter].duration ) {
			var currentPlayer = playPlayer1 ? player1 : player2;
			var nextPlayer = playPlayer1 ? player2 : player1;
			var currentIframe = playPlayer1 ? iframe1 : iframe2;

			currentPlayer.api('unload');

			if (iframeSrcCounter < exercises.length) {

				exerciseCounter++;
				iframeSrcCounter++;

				if (iframeSrcCounter < exercises.length) {
					setIframeSrc(currentIframe, getExerciseLink( exercises[iframeSrcCounter].id ));
					//setTimeout(function() { currentPlayer.api('play'); currentPlayer.api('pause'); }, 1000);
				}

				swapPlayingPlayer();
				swapIframeClass();
				nextPlayer.api('play');
			}
		}
	}



	function copyServerJson() {

		for (set in serverJson[0].sets) {
			for (exercise in serverJson[0].sets[set].video_exercise) {
				var id = getExerciseLink( serverJson[0].sets[set].video_exercise[exercise].link );
				var duration = getExerciseLength( serverJson[0].sets[set].video_exercise[exercise].length );
				exercises.push({ 'id': id, 'duration': duration });
			}
		}
	}

	function getExerciseLink(str) {
		return str.slice(-9);
	}

	function getExerciseLength(str) {
		var exerciseLength = str.split(':');
		var secondsSum = 0;

		for (var i=0; i<exerciseLength.length; i++) {
			switch (i) {
				case 0:
					secondsSum += +exerciseLength[i] * 3600;
					break;
				case 1:
					secondsSum += +exerciseLength[i] * 60;
					break;
				case 2:
					secondsSum += +exerciseLength[i];
					break;
			}
		}
		return secondsSum;
	}

	function swapPlayingPlayer() {
		playPlayer1 = !playPlayer1, playPlayer2 = !playPlayer1;
	}

	function swapIframeClass() {
		if (iframeAIsActive) {
			iframeA.removeClass('active').addClass('hidden');
			iframeB.removeClass('hidden').addClass('active');
		}
		else {
			iframeB.removeClass('active').addClass('hidden');
			iframeA.removeClass('hidden').addClass('active');
		}
		iframeAIsActive = !iframeAIsActive;
	}

	function setIframeSrc(iframe, video_id) {
		iframe.src = 'https://player.vimeo.com/video/'+ video_id +'?api=1&player_id='+ iframe.id;
	}
});

(function () {
	'use strict';

	if (document.querySelector('[data-show-modal]')) {
		var callModalBtns = document.querySelectorAll('[data-show-modal]');
		initDefault(callModalBtns); // default init
    }

	var animate = false;

	//default modal init
	function initDefault(callModalBtns) {
		for (var i = 0; i < callModalBtns.length; i++) {
			callModalBtns[i].onclick = function () {
				var callBtn = this;
				var calledModal = document.querySelector('.'+this.dataset.showModal);
				if (this.dataset.animateOnOpen && this.dataset.animateOnClose) {animate = true;}

				// Open modal
				openModal(calledModal);
				if (animate) animateOnOpen(callBtn, calledModal);

				// Close modal
				calledModal.onclick = function(event) {
					if (animate) {
						animateOnClose(callBtn, calledModal);
						setTimeout(function() {
							closeModal(calledModal);
						}, 1000);
					}
					else {
						closeModal(calledModal);
					}
				}
				calledModal.querySelector('.modal-c_close').onclick = function(event) {
					if (animate) {
						animateOnClose(callBtn, calledModal);
						setTimeout(function() {
							closeModal(calledModal);
						}, 1000);
					}
					else {
						closeModal(calledModal);
					}
				}
				calledModal.querySelector('.modal-c_center').onclick = function(event) {
					event.stopPropagation(); // to prevent onclick on parent el
				}
			}
		}
	}

	// foo drops
	// Open modal
	function openModal(calledModal) {
        calledModal.classList.add('open');
	}
	// Close modal
	function closeModal(calledModal) {
		calledModal.classList.remove('open');
	}
	// Animate on open
	function animateOnOpen(callBtn, calledModal) {
	calledModal.querySelector('.modal-c_animated').classList.remove(callBtn.dataset.animateOnClose);
	calledModal.querySelector('.modal-c_animated').classList.add(callBtn.dataset.animateOnOpen);
	}
	// Animate on close
	function animateOnClose(callBtn, calledModal) {
	calledModal.querySelector('.modal-c_animated').classList.remove(callBtn.dataset.animateOnOpen);
	calledModal.querySelector('.modal-c_animated').classList.add(callBtn.dataset.animateOnClose);
	}

})();

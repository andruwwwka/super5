// JavaScript Document
var allposition=0;
$(document).ready(function() {
	allposition=$(".all").offset();
//console.log("position:",allposition.left);
	//$(".left_side").css({left:allposition.left});
	
	
	$(window ).resize(function(){
		allposition=$(".all").offset();
//console.log("position:",allposition.left);
		//$(".left_side").css({left:allposition.left});
	});
		
		
	$(".archive_menu").on("click","li",function(){
		$(this).siblings("li").find("ul").slideUp();
		var child_ul=$(this).children("ul");
		child_ul.slideDown();
	});
		
		
/* Emulate a SELECT */		
	$(".select_field_container").on("click",".select_btn, .select_value_title",function(){
		var select_container=$(this).parents(".select_field_container");
		$(this).siblings(".select_list").slideToggle("fast",function(){
			if(select_container.find(".select_list").is(":visible"))
				select_container.addClass("active");
			else
				select_container.removeClass("active");
		});
	});
	$(".select_field_container").on("click",".select_list li",function(){
		
		$(this).parents(".select_field_container").find("li").removeClass("selected");
		var selected_val=$(this).data("select_val");
		var selected_title=$(this).text();
		$(this).parents(".select_field_container").find(".select_value_title").text(selected_title);
		$(this).parents(".select_field_container").find(".select_value").val(selected_val);
			
		$(this).addClass("selected");
		$(this).parent(".select_list").slideToggle("slow");
		$(this).parents(".select_field_container").removeClass("active");
	});
/* /Emulate a SELECT */		


/* Emulate a RADIO */		
	$(".radio_group").on("click",".radio_field",function(){
		var radio_group=$(this).parents(".radio_group");
		radio_group.find(".radio_field").removeClass("checked");
		radio_group.find(".radio_val").val($(this).data("radio_val"));
		$(this).addClass("checked");
	});
/* /Emulate a RADIO */		



/* Emulate a CHECKBOX */		
	$("form").on("click",".checkbox_container",function(){
		$(this).toggleClass("checked");
		if($(this).is(".checked"))
			$(this).find(".checkbox_value").val($(this).data("checkbox_val"));
		else
			$(this).find(".checkbox_value").val("");
	});
/* /Emulate a CHECKBOX */	

	$('#totop').on("click", function() {
		window.scrollTo(0,0);
	});


	var userPk = document.getElementsByName("user_pk")[0].value;
	function get_notification() {
		$.ajax({
			type: 'get',
			url: '/rest/extend_notifications/',
			data: {'user_pk': userPk, },
			success: function(data){
				//console.log(data);
				callSwal(data);
				for (var ind in data){
					$.ajax({
						type: 'get',
						url: '/extend_notifications/sended/',
						data: {'id': data[ind]['id'] }
					});
				}
			}
		});
    }
    var timerId=setInterval(get_notification, 30000);


	function callSwal (data) {
		if (!data.length) { return }
		swal({
			title: data,
			text: "",
			type: "success"
		});
	}

	// checkbox control in wizard master (personal-data-master page)
	if ($('.wizard-days-count').length) {
	var wizardCountEl = $('.wizard-days-count');
	var wizardDaysTotal = +(wizardCountEl.text());
	var wizardDaysLeft = wizardDaysTotal;
	$('.training-days-list_label').on('click', function() {
		var input = $(this).parent().find('input');
		// if days left 0 and current checkbox isnt checked - return
		if (wizardDaysLeft == 0 && !input.prop('checked')) {return;}
		// switch checkbox state
		input.prop('checked') ? input.prop('checked', false) : input.prop('checked', true);

		var checked = 0;
		$('.training-days-list input').each(function() {
			if($(this).prop('checked')) checked++;
		});
		wizardDaysLeft = wizardDaysTotal - checked;
		wizardCountEl.text(wizardDaysLeft);
	})
}



});

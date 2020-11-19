/**
 * This code fill change hamburegr button from lines to cross sign
 */
$(document).ready(function(){
	$('#hamburger-button').click(function(){
		$(this).toggleClass('open');
	});
});
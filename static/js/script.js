$(document).ready(function () {
	/**
	* This function fill change hamburegr button from lines to cross sign on small devices
	*/
	$('#hamburger-button').click(function () {
		$(this).toggleClass('open');
	});
	/**
	* This function fill change hamburegr button from lines to cross sign on medium devices
	*/
	$('#hamburger-button-medium').click(function () {
		$(this).toggleClass('open');
	});

	/**
	 * This fucntion was found on https://www.w3schools.com/howto/howto_css_smooth_scroll.asp#section1, traget - element changed also added -=57px to scrollTop function to adjust navigation size to scrolled elemenet
	 */
	$(".scroll-icon").on('click', function (event) {
		if (this.hash !== "") {
			event.preventDefault();
			let hash = this.hash;

			$('html, body').animate({
				scrollTop: $(hash).offset().top -= 57
			}, 800, function () {
				window.location.hash = hash;
			});
		}
	});
});
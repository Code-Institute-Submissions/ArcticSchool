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
		// animate button and close navbar medium devices
		if ($('#hamburger-button-medium').hasClass('open')) {
			$('#hamburger-button-medium').click();
		}
		// animate button and close navbar small devices
		if ($('#hamburger-button').hasClass('open')) {
			$('#hamburger-button').click();
		}
		if (this.hash !== "") {
			event.preventDefault();
			let hash = this.hash;
			$('html, body').animate({
				scrollTop: $(hash).offset().top -= 57
			}, 800);
		}
	});

	/**
	 * This function will show the 'go to the top' button and scroll smoothly to the top of the page when button is clicked
	 * Code Snippet from https://codepen.io/joshuamasen/pen/OYaYbL
	 */
	const scrollToTopButton = document.getElementById('back-to-top');
	const scrollFunc = () => {
		let y = window.scrollY;
		if (y > 0) {
			scrollToTopButton.className = "top-link show";
		} else {
			scrollToTopButton.className = "top-link hide";
		}
	};
	window.addEventListener("scroll", scrollFunc);
	const scrollToTop = () => {
		const c = document.documentElement.scrollTop || document.body.scrollTop;
		if (c > 0) {
			window.requestAnimationFrame(scrollToTop);
			window.scrollTo(0, c - c / 10);
		}
	};
	scrollToTopButton.onclick = function (e) {
		e.preventDefault();
		scrollToTop();
	}


	/**
	 * This function will count number of existing classes on the page to determine divider for container height
	 */
	let categoryClass = $('div .category-block').length;
	categoryClass = categoryClass/2
	$("div .category-block").css( { height: `calc((100vh - 59px) / ${categoryClass})` } );
});

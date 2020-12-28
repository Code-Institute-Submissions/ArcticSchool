$(document).ready(function () {
	// NAVIGATION
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


	// LESSONS PAGE
	/**
	 * This function will count number of existing classes on the page to determine divider for container height
	 */
	let categoryClass = $('div .category-block').length;
	//check if categoryClass result is odd - if odd make it even
	if (categoryClass % 2 != 0) {
		categoryClass = categoryClass + 1
	}
	categoryClass = categoryClass / 2
	$("div .category-block").css({ height: `calc((100vh - 59px) / ${categoryClass})` });

	/**
	 * This function will equalize lessons cards height - solution found on
	 * https://stackoverflow.com/questions/11688250/setting-equal-heights-for-divs-with-jquery
	 */
	$('#lessons-container').each(function () {
		let highestCard = 0;
		$('.card', this).each(function () {
			if ($(this).height() > highestCard) {
				highestCard = $(this).height();
			}
		});
		$('.card', this).height(highestCard);
	});

	/**
	* This function will add class to side navigation when scrolled to predefined point
	*/
	$(window).scroll(function () {
		let scroll = $(window).scrollTop();
		// top section height
		let top_section_height = $(".about-lessons-result").height()
		//>=, not <=
		if (scroll >= top_section_height) {
			//clearHeader, not clearheader - caps H
			$(".filter-box").addClass("fixed-filters");
		}
		else {
			$(".filter-box").removeClass("fixed-filters");
		}
	});

	/**
	 * This function will show more elements.cards
	 * Load more content with jQuery - May 21, 2013 c 2013 @ElmahdiMahmoud
	*/
	$(function () {
		$(".card").slice(0, 12).show();
		$("#loadMore").on('click', function (e) {
			e.preventDefault();
			$(".card:hidden").slice(0, 12).slideDown();
			if ($(".card:hidden").length == 0) {
				$("#load").fadeOut('slow');
			}

			// get number of visisble cards and pass value to bottoms count section
			let cards_on_page = $('.card:visible').length;
			$(".cards-count").html(cards_on_page);
			// check visible card count
			check_count();
			change_load_number();
			getQueryVariable();
		});
		// run check count function
		check_count();
		// run chabge load number function
		change_load_number();

		// get number of cards to show and pass value to LoadMore() span element
		function change_load_number() {
			let all_cards = Number($('.total-count').html());
			let cards_on_page = $('.card:visible').length;
			let cards_to_show;
			cards_to_show = all_cards - cards_on_page;
			if (cards_to_show < 12) {
				cards_to_show = cards_to_show;
				$('.visible-cards-count').html(cards_to_show);
			}
			else {
				cards_to_show = 12;
				$('.visible-cards-count').html(cards_to_show);
			}
		}
	});

	/**
	 * This function will change load button to unavailable when all cards are loaded
	 */
	function check_count() {
		let cards_on_page = $('.card:visible').length;
		let total_count = Number($('.total-count').html());
		if (cards_on_page != total_count || cards_on_page === 0) {
		} else {
			$('.show-more').addClass('show-disable');
			$('.visible-cards-count').html('0');
		}
	};

	/**
	 * This function will reload Lessons page and display/filter lessons with selected Sort Option only
	 */
	$('#sort-selector').change(function () {
		let selector = $(this);
		let currentUrl = new URL(window.location);
		let selectedVal = selector.val();
		if (selectedVal != "reset") {
			let sort = selectedVal.split("_")[0];
			let direction = selectedVal.split("_")[1];
			currentUrl.searchParams.set("sort", sort);
			currentUrl.searchParams.set("direction", direction);
			window.location.replace(currentUrl);
		} else {
			currentUrl.searchParams.delete("sort");
			currentUrl.searchParams.delete("direction");
			window.location.replace(currentUrl);
		}
	})

	// Levels checkbox listener
	/**
	 * This functill listen to filter - level checkbox change.
	 */
	$('input[name=level_checkbox]').change(function () {
		var lvl_List = "";
		$('input[type=checkbox]').each(function () {
			if (this.checked) {
				let lvl_lable = '"#' + $(this).next('label').text() + '"';
				alert(lvl_lable);
				$(lvl_lable).toggle();
			} else {
				let lvl_lable = '#' + $(this).next('label').text();
				$(lvl_lable).toggle();
			}
		});
		console.log(lvl_List);
	});

	/**
	 * This function will add special id to anchor element to set 'category-selected' style
	 */
	$(function () {
		let pathname = window.location.href;
		// check if path name contains
		if (pathname.search("=") < 0) { } else {
			pathname = pathname.split('=')[1];
			let last_sign = pathname.search("&");

			if (last_sign <= 0) {
				// add categroy.name-selected class to element when window href doesn't contains category or filtering
				category_selected = pathname + '-selected';
				$('.pathname').html(pathname);
				let my_id = '#' + pathname;
				$(my_id).addClass('category-selected');
			} else {
				// add category.name-selected class to element when category is filtered
				category_selected = pathname.substring(0, last_sign); + '-selected';
				$('.pathname').html(category_selected);
				let my_id = '#' + category_selected;
				$(my_id).addClass('category-selected');
			}
		}
	});

	// TEAM PAGAE
	/**
	 * This function will change button caption onClick
	 */
	$(function () {
		$('#read-more-button').click(function () {
			if ($(this).html() != 'Hide') {
				$(this).html('Hide');
			} else {
				$(this).html('About Me');
			}
		});
	});

});
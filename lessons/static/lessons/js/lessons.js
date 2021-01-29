/**
 * This function will count number of existing classes on the page to determine divider for container height
 */
let categoryClass = $('div .category-block').length;
//check if categoryClass result is odd - if odd make it even
if (categoryClass % 2 !== 0) {
    categoryClass = categoryClass + 1;
}
categoryClass = categoryClass / 2;
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
    let top_section_height = $(".about-lessons-result").height();
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
        if ($(".card:hidden").length === 0) {
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
}

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
});

// Levels checkbox listener
/**
 * This functill listen to filter - level checkbox change.
 */
$('input[name=level_checkbox]').change(function () {
    let currentUrl = new URL(window.location);
    $('input[type=checkbox]').each(function () {
        if (this.checked) {
            let lvl_label = '"#' + $(this).next('label').text() + '"';
            console.log(lvl_label);

        } else {
        }
    });
});

/**
 * This function will toggle discount bar and change hide element
 */
$('#close-discount').click(function () {
    $('#discount-banner').toggle('d-none');
    // set close discount value to true
    sessionStorage.setItem('display_discount', 'False');
});

/**
 * This function will check for display_discount when lessons page is open
 */
window.onload = $(function () {
    if (sessionStorage.getItem('display_discount') === null) {
        $('#discount-banner').removeClass('d-none');
    }
});
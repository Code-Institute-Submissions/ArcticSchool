/**
 * This function will equalize lessons cards height - solution found on
 * https://stackoverflow.com/questions/11688250/setting-equal-heights-for-divs-with-jquery
 */
window.onload = function () {
    $('#my-level').each(function () {
        let highestCard = 0;
        $('.level-container', this).each(function () {
            if ($(this).height() > highestCard) {
                highestCard = $(this).height();
            }
        });
        $('.level-container', this).height(highestCard);
    });

    $('.our-proof').each(function () {
        let highestCard = 0;
        $('.card-body', this).each(function () {
            if ($(this).height() > highestCard) {
                highestCard = $(this).height();
            }
        });
        $('.card-body', this).height(highestCard);
    });
}
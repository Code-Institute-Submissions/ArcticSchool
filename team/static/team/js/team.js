/**
 * This function will change button caption onClick
 */
$(function () {
    $('.read-more-button').click(function () {
        if ($(this).html() != 'Hide') {
            $(this).html('Hide');
        } else {
            $(this).html('About Me');
        }
    });
});
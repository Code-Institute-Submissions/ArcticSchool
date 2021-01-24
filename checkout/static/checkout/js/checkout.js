/**
 * This funtcion will change Country field syle
 * when value is different than default
 */
let countrySelected = $('#id_country').val();
if (!countrySelected) {
    $('#id_country').css('color', '#ced4da');
};
$('#id_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#ced4da');
    } else {
        $(this).css('color', '#495057');
    }
});


$('.InputElement').bind('keyup', function () {
    if (allFilled()) $('#submit-button').removeAttr('disabled');
});

function allFilled() {
    let filled = true;
    $('.InputElement').each(function () {
        if ($(this).val() == '') filled = false;
    });
    return filled;
}

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
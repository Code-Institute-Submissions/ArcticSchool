/**
 * This function will remove item from booked lessons bag and update the 'bag' and reload page
 */
$('.remove-lesson').click(function (e) {
    let csrfToken = "{{ csrf_token }}";
    let lessonId = $(this).attr('id').split('remove_')[1];
    let url = `/booking/remove/${lessonId}`;
    let data = { 'csrfmiddlewaretoken': csrfToken };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
});
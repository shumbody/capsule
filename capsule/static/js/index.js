var alertTemplate = Handlebars.compile($('#alert-template').html());

$('.form-memory').submit(function(e) {
    e.preventDefault();
    var serialized = $(this).serializeArray();
    if (isPostValid(serialized)) {
        $.post('add/', serialized, function (data) {
            $('.form-memory').find('input[type=text], textarea').val('');
            renderSuccessAlert(data)
        });
    } else {
        renderErrorAlert()
    }
});

function renderSuccessAlert(data) {
    var date = new Date(data.message.date);
    var dateString = date.toLocaleTimeString();

    var tmpData = {
        modifiers: 'alert-success',
        header: data.header,
        message: 'You saved a memory at ' + dateString
    }
    var html = alertTemplate(tmpData);
    $('#alert-center').html(html);
}

function renderErrorAlert() {
    var tmpData = {
        modifiers: 'alert-danger',
        header: 'Yikes!',
        message: 'Did you forget to fill something out?'
    }
    var html = alertTemplate(tmpData);
    $('#alert-center').html(html);
}

function isPostValid(serialized) {
    return serialized.reduce(function(a, b) {
        return a.value !== '' && b.value !== '';
    });
}

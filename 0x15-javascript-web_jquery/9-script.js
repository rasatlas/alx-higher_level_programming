let path = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
let response;
$.get(path, function (response) {
    $("DIV#hello").append(`${response.hello}`);
});
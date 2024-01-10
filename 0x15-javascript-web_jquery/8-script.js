let path = 'https://swapi-api.alx-tools.com/api/films/?format=json';
let response;
$.get(path, function (response) {
    for (let i = 0; i < response.results.length; i++) {
        $("UL#list_movies").append(`<li>${response.results[i].title}</li>`);
    }
});
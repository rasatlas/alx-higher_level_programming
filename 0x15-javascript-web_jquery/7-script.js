let path = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
let response;
$.get(path, function(response){
    $("DIV#character").append(response.name)
});
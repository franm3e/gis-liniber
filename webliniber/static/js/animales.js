
window.onload = function() {
    init();
};


function init() {
    load_animals_table();
};

function load_animals_table() {
    $.get("get_animals").done(function( data ) {
        JSON.parse(data).forEach(function (animal, index) {
            add_animal_to_table(animal.fields, index + 1);
        });
    }).fail(function( data ) {

    });
}

function add_animal_to_table(animal_data, index) {
    $('#tabla_animales tr:last').after(
        '<tr>' +
        '<th>' + index + '</th>' +
        '<td>' + ((animal_data.nombre) ? animal_data.nombre : '') + '</td>' +
        '<td>' + ((animal_data.organismo) ? animal_data.organismo : '') + '</td>' +
        '<td>' + ((animal_data.instalacion) ? animal_data.instalacion : '') + '</td>' +
        '<td>' + ((animal_data.frecuencia) ? animal_data.frecuencia : '') + '</td>' +
        '<td>' + ((animal_data.telefono) ? animal_data.telefono : '') + '</td>' +
        '<td>' + ((animal_data.activo) ? '<i class="bi bi-check-lg" style="color: green;"></i>' : '') + '</td>' +
        '</tr>'
    );
}
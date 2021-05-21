
window.onload = function() {
    init();
};


function init() {
    load_map();
    //set_autocomplete();
};

function load_map() {
    const map = L.map('map_canvas').setView([37.869632, -4.787501], 8);

    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/light_nolabels/{z}/{x}/{y}.png', {
        maxZoom: 18
    }).addTo(map);

    var client = new carto.Client({
        apiKey: 'Qo2idq33DQrBQrBbcvG16w',
        username: 'franm3e'
    });

    const areasDistribucion2016Dataset = new carto.source.Dataset('table_rea_de_distribucion_de_linces_2016');
    const areasDistribucion2016Style = new carto.style.CartoCSS('#layer { polygon-fill: #23A731; polygon-opacity: 0.25; ::outline {line-width: 1; line-color: #FFFFFF; line-opacity: 0.5;}}');
    const areasDistribucion2016 = new carto.layer.Layer(areasDistribucion2016Dataset, areasDistribucion2016Style);

    areasDistribucion2016

    client.addLayers([areasDistribucion2016]);

    client.getLeafletLayer().addTo(map);
}


function set_autocomplete() {
    var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];

    $("#animal_search").autocomplete({
      source: availableTags
    });
}
/**
 * Created with PyCharm.
 * User: Andrey Smirnov (mail@ansmirnov.ru)
 * Date: 12.04.14
 * Time: 13:42
 */

function load_points() {
    jQuery.ajax({
        url: '/items/',
        success: function (data) {
            for (var i = 0; i < data.items.length; i++) {
                var point = data.items[i];
                var myGeoObject = new ymaps.GeoObject({
                    geometry: {
                        type: "Point",// тип геометрии - точка
                        coordinates: [parseFloat(point.geo_E), parseFloat(point.geo_N)] // координаты точки
                    }
                });
                myMap.geoObjects.add(myGeoObject);
            }
        },
        dataType: 'JSON',
        method: "GET"
    })

}

function labelClick(id) {

}

ymaps.ready(init);
var myMap;

function init() {
    myMap = new ymaps.Map("map", {
        center: [58.05, 38.85],
        zoom: 12
    });
    myMap.controls.add('mapTools');
    myMap.controls.add('zoomControl');
    load_points();
}
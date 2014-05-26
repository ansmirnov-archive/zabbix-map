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
                //var myGeoObject = new ymaps.GeoObject({
                //    geometry: {
                //        type: "Point",// тип геометрии - точка
                //        // координаты точки
                //        coordinates: [parseFloat(point.geo_E), parseFloat(point.geo_N)]
                //    }
                //});
                //myMap.geoObjects.add(myGeoObject);
                var myPlacemark = new ymaps.Placemark(
		// Координаты метки
		[parseFloat(point.geo_E), parseFloat(point.geo_N)] , {
                    // Свойства
                    // Текст метки
                    hintContent: [point.name,parseFloat(point.geo_E), parseFloat(point.geo_N)]
                });     
                // Добавление метки на карту
		myMap.geoObjects.add(myPlacemark);
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
    myMap.behaviors.enable("scrollZoom");
    load_points();
}
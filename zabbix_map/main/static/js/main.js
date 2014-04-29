/**
 * Created with PyCharm.
 * User: Andrey Smirnov (mail@ansmirnov.ru)
 * Date: 12.04.14
 * Time: 13:42
 */

function mapClick(e) {
    var coord = e.get('coordPosition');
    var url = '/click/'+coord
    jQuery.ajax({
        url: '/click/'+coord,
        success: function (data) {
            for (var i = 0; i < data.points.length; i++) {
                var point = data.points[i];
                var arr=point.coords.split(',');
                var myGeoObject = new ymaps.GeoObject({
                    geometry: {
                        type: "Point",// тип геометрии - точка
                        coordinates: [parseFloat(arr[1]), parseFloat(arr[0])] // координаты точки
                    }
                });
                myMap.geoObjects.add(myGeoObject);
                myGeoObject.events.add('click', function (e) {labelClick(i)})
                $('#info').html($('#info').html() + '<div class="item">test</div>');
            }
            alert(data.points);
        },
        dataType: 'JSON',
        method: "GET"
    })
}

function labelClick(id){

}

    ymaps.ready(init);
    var myMap;

    function init(){
        myMap = new ymaps.Map ("map", {
            center: [55.76, 37.64],
            zoom: 7
        });
        myMap.controls.add('mapTools');
        myMap.controls.add('zoomControl');
        myMap.events.add('click', mapClick)
    }
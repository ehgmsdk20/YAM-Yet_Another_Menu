var places = new kakao.maps.services.Places();

const lat = document.getElementById("lat").value.replaceAll("'","");
const lng = document.getElementById("lng").value.replaceAll("'","");
const rad = document.getElementById("radius").value;
var callback = function(result, status) {
    if (status === kakao.maps.services.Status.OK) {
        console.log(result);
        for ( var i=0; i<result.length; i++ ) {

            document.getElementById("result").innerText += result[i].place_name;
            document.getElementById("result").innerHTML += "<br>";
        }
    }
};
// 공공기관 코드 검색
places.categorySearch('FD6', callback, {
    // Map 객체를 지정하지 않았으므로 좌표객체를 생성하여 넘겨준다.
    location: new kakao.maps.LatLng(lat, lng),
    radius: rad
});



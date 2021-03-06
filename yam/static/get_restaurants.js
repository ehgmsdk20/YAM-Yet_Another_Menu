var places = new kakao.maps.services.Places();

var callback = function(result, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
        console.log(result);
        console.log(pagination.current);
        for ( var i=0; i<result.length; i++ ) {
            document.getElementById("result").value += result[i].place_name;
            document.getElementById("result").value += ",";
            
        }
        if (pagination.hasNextPage) {
            pagination.nextPage();
        }
        else {
            var url = "{% url 'crawling:result' 'rest_list' %}".replace('rest_list', document.getElementById("result").value);
            window.location.href=url;
        }
    }
};
// 공공기관 코드 검색
places.categorySearch('FD6', callback, {
    // Map 객체를 지정하지 않았으므로 좌표객체를 생성하여 넘겨준다.
    location: new kakao.maps.LatLng(lat, lng),
    radius: rad,
    page: 1,
    sort: "distance"
});



$(document).ready(function() {
    
    if (navigator.geolocation) {
          // 現在の位置情報取得を実施
          navigator.geolocation.getCurrentPosition(
          // 位置情報取得成功時
          function (pos) {
                  var location = pos.coords.latitude;
                  location += "," + pos.coords.longitude;
                  document.getElementById("location").innerHTML = location;
          },
          // 位置情報取得失敗時
          function (pos) {
                  var location ="位置情報が取得できませんでした<br />再読み込みでやり直してみてください";
                  alert(location);
                  //document.getElementById("infotext").innerHTML = location;
          });
      } else {
          window.alert("本ブラウザではGeolocationが使えません。");
      }
    
$("#btn_start").click(function(){
            console.log('start');
            $("#id_text").val("1");
            console.log($("#id_text").val());
            $("#frm_dakoku").submit();
        });
        $("#btn_end").click(function(){
            $("#id_text").val("0");
            $("#frm_dakoku").submit();
            console.log('end');
        });
});
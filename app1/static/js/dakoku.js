$(document).ready(function() {
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
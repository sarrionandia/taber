$(document).ready(function () {
    $('#id_ogsp1').on("keyup", update_total_speaks);
    $('#id_ogsp2').on("keyup", update_total_speaks);
    $('#id_oosp1').on("keyup", update_total_speaks);
    $('#id_oosp2').on("keyup", update_total_speaks);
    $('#id_cgsp1').on("keyup", update_total_speaks);
    $('#id_cgsp2').on("keyup", update_total_speaks);
    $('#id_cosp1').on("keyup", update_total_speaks);
    $('#id_cosp2').on("keyup", update_total_speaks);
    update_total_speaks();
});

function update_total_speaks(){
    console.log("Updating");
    var og_speaks = parseInt($('#id_ogsp1').val()) + parseInt($('#id_ogsp2').val());
    var oo_speaks = parseInt($('#id_oosp1').val()) + parseInt($('#id_oosp2').val());
    var cg_speaks = parseInt($('#id_cgsp1').val()) + parseInt($('#id_cgsp2').val());
    var co_speaks = parseInt($('#id_cosp1').val()) + parseInt($('#id_cosp2').val());
    $('#total_og').html(og_speaks);
    $('#total_oo').html(oo_speaks);
    $('#total_cg').html(cg_speaks);
    $('#total_co').html(co_speaks);
}
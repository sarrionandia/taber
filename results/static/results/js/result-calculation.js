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
    var og_speaks = parseInt($('#id_ogsp1').val()) + parseInt($('#id_ogsp2').val());
    var oo_speaks = parseInt($('#id_oosp1').val()) + parseInt($('#id_oosp2').val());
    var cg_speaks = parseInt($('#id_cgsp1').val()) + parseInt($('#id_cgsp2').val());
    var co_speaks = parseInt($('#id_cosp1').val()) + parseInt($('#id_cosp2').val());
    $('#total_og').html(og_speaks);
    $('#total_oo').html(oo_speaks);
    $('#total_cg').html(cg_speaks);
    $('#total_co').html(co_speaks);

    if ((og_speaks != oo_speaks)
    && (og_speaks != cg_speaks)
    && (og_speaks != co_speaks)
    && (oo_speaks != cg_speaks)
    && (oo_speaks != co_speaks)
    && (cg_speaks != co_speaks)){
        console.log("All speaker totals are unique");
        $('#err_total_speaks').hide();
        $('#btn_save_result').attr('disabled', false);
    }
    else {
        console.log("Speaker totals are not unique");
        $('#err_total_speaks').show();
        $('#btn_save_result').attr('disabled', true);
    }

}
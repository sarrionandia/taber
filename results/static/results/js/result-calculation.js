$(document).ready(function () {
    $('#id_ogsp1').on("keyup", function(){update_total_speaks(this)});
    $('#id_ogsp2').on("keyup", function(){update_total_speaks(this)});
    $('#id_oosp1').on("keyup", function(){update_total_speaks(this)});
    $('#id_oosp2').on("keyup", function(){update_total_speaks(this)});
    $('#id_cgsp1').on("keyup", function(){update_total_speaks(this)});
    $('#id_cgsp2').on("keyup", function(){update_total_speaks(this)});
    $('#id_cosp1').on("keyup", function(){update_total_speaks(this)});
    $('#id_cosp2').on("keyup", function(){update_total_speaks(this)});
    $('#btn_save_result').on("click", update_preview);
    update_total_speaks();
});

function update_preview() {

}

function update_total_speaks(element){
    var elements = ['#id_ogsp1',
                    '#id_ogsp2',
                    '#id_oosp1',
                    '#id_oosp2',
                    '#id_cgsp1',
                    '#id_cgsp2',
                    '#id_cosp1',
                    '#id_cosp2'];
    var fields_entered = true;

    elements.forEach(function(entry) {
        var element = $(entry);
        if (!element.val()){
            element.parent().addClass('has-error');
            fields_entered = false;
        } else {
            element.parent().removeClass('has-error');
        }
    });

    var og_speaks = parseInt($('#id_ogsp1').val()) + parseInt($('#id_ogsp2').val());
    var oo_speaks = parseInt($('#id_oosp1').val()) + parseInt($('#id_oosp2').val());
    var cg_speaks = parseInt($('#id_cgsp1').val()) + parseInt($('#id_cgsp2').val());
    var co_speaks = parseInt($('#id_cosp1').val()) + parseInt($('#id_cosp2').val());
    $('#total_og').html(og_speaks);
    $('#total_oo').html(oo_speaks);
    $('#total_cg').html(cg_speaks);
    $('#total_co').html(co_speaks);


    var fields_unique = true;
    if ((og_speaks != oo_speaks)
    && (og_speaks != cg_speaks)
    && (og_speaks != co_speaks)
    && (oo_speaks != cg_speaks)
    && (oo_speaks != co_speaks)
    && (cg_speaks != co_speaks)){
        $('#err_total_speaks').hide();
    }
    else {
        $('#err_total_speaks').show();
        fields_unique = false;
    }
    var button_should_show = !(fields_entered && fields_unique);
    $('#btn_save_result').attr('disabled', button_should_show);

}
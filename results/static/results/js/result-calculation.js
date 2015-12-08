var elements = ['#id_ogsp1',
                    '#id_ogsp2',
                    '#id_oosp1',
                    '#id_oosp2',
                    '#id_cgsp1',
                    '#id_cgsp2',
                    '#id_cosp1',
                    '#id_cosp2'];

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
    elements.forEach(function(entry) {
        $(entry + '_prev').html($(entry).val());
    });

}

function update_total_speaks(element){
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
    $('#total_og_prev').html(og_speaks);
    $('#total_oo').html(oo_speaks);
    $('#total_oo_prev').html(oo_speaks);
    $('#total_cg').html(cg_speaks);
    $('#total_cg_prev').html(cg_speaks);
    $('#total_co').html(co_speaks);
    $('#total_co_prev').html(co_speaks);

    var speaks = {
        'OG' : og_speaks,
        'OO' : oo_speaks,
        'CG' : cg_speaks,
        'CO' : co_speaks,
    };
    var teamPositions = getSortedTeams(speaks);
    $('#' + teamPositions[0] + '_pos').html("4th");
    $('#' + teamPositions[1] + '_pos').html("3rd");
    $('#' + teamPositions[2] + '_pos').html("2nd");
    $('#' + teamPositions[3] + '_pos').html("1st");

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

function getSortedTeams(obj) {
    var keys = []; for(var key in obj) keys.push(key);
    return keys.sort(function(a,b){return obj[a]-obj[b]});
}

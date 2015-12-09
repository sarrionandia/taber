function save_result(debateid, csrf) {
        $.ajax({
        type: 'POST',
        url: '/results/edit/' + debateid + '/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'ogsp1' : $('#id_ogsp1').val(),
            'ogsp2' : $('#id_ogsp2').val(),
            'oosp1' : $('#id_oosp1').val(),
            'oosp2' : $('#id_oosp2').val(),
            'cgsp1' : $('#id_cgsp1').val(),
            'cgsp2' : $('#id_cgsp2').val(),
            'cosp1' : $('#id_cosp1').val(),
            'cosp2' : $('#id_cosp2').val(),

        },
        success: function () {
            window.location.replace('/results/');
        },
        error: function (request, error) {
            alert("Couldn't update " + name);
        }
    });
}
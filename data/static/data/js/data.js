$( document ).ready(function() {
    $('[data-toggle="tooltip"]').tooltip()
});

function delete_inst(inst_id) {
    $('#inst_' + inst_id).find('button').attr('disabled', true);

    var request = $.post("/data/institution/" + inst_id + "/delete/",
        {institution: inst_id},
        function() {
            })

        .fail(function(){
            alert('Unable to delete institution ' + inst_id);
            $('#inst_' + inst_id).find('button').attr('disabled', false);
        })

        .success(function() {
            $('#inst_' + inst_id).toggle({ effect: "scale", direction: "vertical" });
        });



    }

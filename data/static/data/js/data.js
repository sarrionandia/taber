$( document ).ready(function() {
    $('[data-toggle="tooltip"]').tooltip()
});

function delete_inst(inst_id) {
    $.post("/data/institution/" + inst_id + "/delete/",
        {institution: inst_id},
        function() {
            $('#inst_' + inst_id).toggle({ effect: "scale", direction: "vertical" });
            });

    }

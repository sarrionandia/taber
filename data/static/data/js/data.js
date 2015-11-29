$( document ).ready(function() {
    $('[data-toggle="tooltip"]').tooltip()
    $('#inst_name_input').on("keyup", function(){
        $('#inst_create').attr('disabled', ($('#inst_name_input').val().length <= 0));
    });
    $('#inst_create').on("click", create_institution);

});

function create_institution() {
    $('#inst_create').attr('disabled', true);
    var name = $('#inst_name_input').val();
    var request = $.post("/data/institution/create/",
        {'name': name},
        function(data) {

            var response = jQuery.parseJSON(data);

            var inst = response.id;
            var name = response.name;

            $('#inst_list').prepend(
                $('<li/>')
                    .addClass('row')
                    .attr('id', 'inst_'+ inst)
                    .append(
                        $('<span/>')
                            .addClass('col-sm-10')
                            .addClass('institution_name')
                            .html(name)
                    )
                    .append(
                        $('<div/>')
                            .addClass('col-sm-2')
                            .addClass('institution_controls')
                            .append(
                                $('<button/>')
                                    .addClass('btn')
                                    .addClass('btn-danger')
                                    .addClass('delete-institution')
                                    .attr('data-toggle', 'tooltip')
                                    .attr('title', 'This will delete all teams and judges')
                                    .attr('data-placement', 'top')
                                    .attr('onclick', 'delete_inst(' + inst + ');')
                                    .html("Delete")
                            )
                    )
            );
            $('#inst_name_input').val('');
            $('#inst_create').attr('disabled', false);

        })

        .fail(function(){
            alert("Unable to create institution");
        })

        .success(function() {

        });

}

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

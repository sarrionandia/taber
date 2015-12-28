$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip()
    $('#inst_name_input').on("keyup", function (e) {
        if (e.keyCode == 13) {
            create_institution();
        }
        $('#inst_create').attr('disabled', ($('#inst_name_input').val().length <= 0));
    });
    $('#inst_create').on("click", create_institution);
    $('.institution_name').on("change", function () {
        update_institution(event.target.id.substring(11), this.value);
    });
    $('.create_team_form').on('submit', function (e) {
        e.preventDefault();
        return false;
    })
});

function update_institution(id, name) {
    $.ajax({
        type: 'POST',
        url: '/data/institution/' + id + '/update/',
        data: {
            'name': name
        },
        success: function () {

        },
        error: function (request, error) {
            alert("Couldn't update " + name);
        }
    });
}

function create_institution() {
    $('#inst_create').attr('disabled', true);
    $('#inst_name_input').attr('disabled', true);

    var name = $('#inst_name_input').val();
    var request = $.post("/data/institution/create/",
        {'name': name},
        function (data) {

            var response = jQuery.parseJSON(data);

            var inst = response.id;
            var name = response.name;

            $('#inst_list').prepend(
                $('<li/>')
                    .addClass('row')
                    .attr('id', 'inst_' + inst)
                    .append(
                        $('<input/>')
                            .addClass('col-sm-10')
                            .addClass('institution_name')
                            .attr('value', name)
                            .attr('id', 'inst_input_' + inst)
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
            $('#inst_name_input').attr('disabled', false);
            $('#inst_name_input').focus();
            $('.institution_name').on("change", function () {
                update_institution(event.target.id.substring(11), this.value);
            });
        })

        .fail(function () {
            alert("Unable to create institution");
            $('#inst_create').attr('disabled', false);
            $('#inst_name_input').attr('disabled', false);

        })

        .success(function () {

        });

}

function delete_inst(inst_id) {
    $('#inst_' + inst_id).find('button').attr('disabled', true);

    var request = $.post("/data/institution/" + inst_id + "/delete/",
        {institution: inst_id},
        function () {
        })

        .fail(function () {
            alert('Unable to delete institution ' + inst_id);
            $('#inst_' + inst_id).find('button').attr('disabled', false);
        })

        .success(function () {
            $('#inst_' + inst_id).toggle({effect: "scale", direction: "vertical"});
        });
}

function delete_team(team_id) {
    $.ajax({
        type: 'POST',
        url: '/data/team/' + team_id + '/delete/',
        data: {},
        success: function () {
            $('#t_' + team_id).remove();
        },
        error: function (request, error) {
            alert("Server error: Couldn't delete team");
        }
    });
}

function create_team(inst_id) {
    $('#t_form_' + inst_id + ' :input').prop("disabled", true);
    $.ajax({
        type: 'POST',
        url: '/data/team/create/',
        data: $('#t_form_' + inst_id).serialize(),
        success: function (data) {
            var resp = jQuery.parseJSON(data);
            $('#t_form_' + inst_id + ' :input').prop("disabled", false);
            $('#t_form_' + inst_id).trigger('reset');
            $('<tr />')
                .attr('id', 't_' + resp['id'])
                .append(
                    $('<td />')
                        .html(resp['name'])
                )
                .append(
                    $('<td />')
                        .html(resp['speaker1'])
                )
                .append(
                    $('<td />')
                        .html(resp['speaker2'])
                )
                .append(
                    $('<td />')
                        .append(
                            $('<button />')
                                .addClass('btn')
                                .addClass('btn-danger')
                                .addClass('btn-sm')
                                .attr('onclick', 'delete_team(' + resp['id'] + ');')
                                .attr('type', 'submit')
                                .html("Delete")
                        )
                )
                .insertBefore('.form_row_' + inst_id);
        },
        error: function (request, error) {
            alert("Couldn't create team");
        }
    });
}

function delete_judge(judge_id){
    $.ajax({
        type: 'POST',
        url: '/data/judge/' + judge_id + '/delete/',
        data: $('#j_form_' + judge_id).serialize(),
        success: function(data) {
            $('#j_' + judge_id).toggle({effect: "scale", direction: "vertical"});
        },
        error: function(request, error) {
            alert("Couldn't delete judge");
        }
    });
}

function add_judge(inst_id) {
    var form = $('#j_create_form_' + inst_id);
    var name = $('#new_judge_name_' + inst_id);
    if (name.val().length < 1) {
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/data/judge/',
        data: form.serialize(),
        success: function(data) {
            alert("Success!");
        },
        error: function(request, error) {
            alert("Failure!");
        }

    });

}
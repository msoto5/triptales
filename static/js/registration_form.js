$(document).ready(function(){
    $("#id_password1, #id_password2").on('keyup', function () {
        if ($("#id_password1").val() == $("#id_password2").val()) {
            $('#passwordHelp').html('Matching').css('color', 'green');
        } else 
            $('#passwordHelp').html('Not Matching').css('color', 'red');
    });
});

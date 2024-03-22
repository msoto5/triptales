$(document).ready(function () {
    feather.replace(); // Redraw the feather icons
    
    $('#like_btn').click(function () {
        var postIdVar;
        postIdVar = $(this).attr('data-postid');
        $.get('/triptales/like_post/', { 'post_id': postIdVar },
            function (data) {
                $('#like_count').html(data);
                var $likeBtn = $('#like_btn');
                $('#like_btn').toggleClass('likebutton-liked');
                if ($likeBtn.hasClass('likebutton-liked')) {
                    $likeBtn.html('<span data-feather="thumbs-down"></span> Unlike');
                } else {
                    $likeBtn.html('<span data-feather="thumbs-up"></span> Like');
                }
                feather.replace(); // Redraw the feather icons
            })
    });

    $('#save_btn').click(function () {
        var postIdVar;
        postIdVar = $(this).attr('data-postid');
        $.get('/triptales/save_post/', { 'post_id': postIdVar },
            function (data) {
                var $saved_btn = $('#save_btn');
                $('#save_btn').toggleClass('savebutton-saved');
                if ($saved_btn.hasClass('savebutton-saved')) {
                    $saved_btn.html('<span data-feather="x"></span> Unsave');
                } else {
                    $saved_btn.html('<span data-feather="bookmark"></span> Save');
                }
                feather.replace(); // Redraw the feather icons
            })
    });

    
});
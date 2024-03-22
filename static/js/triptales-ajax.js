$(document).ready(function () {
    alert('Hello');
    $('#like_btn').click(function () {
        var postIdVar;
        postIdVar = $(this).attr('data-postid');
        $.get('/triptales/like_post/', { 'post_id': postIdVar },
            function (data) {
                $('#like_count').html(data);
                var $likeBtn = $('#like_btn');
                $('#like_btn').toggleClass('likebutton-liked');
                if ($likeBtn.hasClass('likebutton-liked')) {
                    $likeBtn.html('<span data-feather="thumbs-down"></span> Unlike Post');
                } else {
                    $likeBtn.html('<span data-feather="thumbs-up"></span> Like Post');
                }
                feather.replace(); // Redraw the feather icons
            })
    });
});
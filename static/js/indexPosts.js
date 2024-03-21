$(document).ready(function () {
    loadPosts('likes', '#top-posts-container');
    loadPosts('recent', '#recent-posts-container');
});


//gets the posts to be loaded into most liked/recent posted sections
function loadPosts(type, containerId) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        const response = JSON.parse(this.responseText);
        const posts = response.posts;
        let html = '';

        posts.forEach(function (post) {
            const createdAtDate = new Date(post.created_at);
            const formattedCreatedAt = createdAtDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' });
            html += generatePost(post, formattedCreatedAt);
        });
        $(containerId).html(html);
    };
    xhttp.open("GET", "/get_all_posts/" + type + "/", true);
    xhttp.send();
}

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

            html += '<div class="col-md-4 mb-4">';
            html += '<a href="/triptales/posts/detail/' + post.id + '" class="text-decoration-none text-dark">';
            html += '<div class="card h-100">';
            html += '<h5 class="card-header">' + post.title + '</h5>';
            if (post.image) {
                html += '<img src="' + post.image + '" class="card-img-top" alt="' + post.country_name + ' - ' + post.location_name + '">';
            }
            html += '<div class="card-body d-flex flex-column">';
            html += '<h5 class="card-title">' + post.country_name + ' - ' + post.location_name + '</h5>';
            html += '<p class="card-text">' + (post.text) + '</p>'; 
            html += '<p class="card-date">Created at: ' + formattedCreatedAt  + '</p>';
            html += '<a href="/triptales/profile/' + post.author + '" class="card-link">By ' + post.author + '</a>';
            html += '</div></div></a></div>';
        });
        $(containerId).html(html);
    };
    xhttp.open("GET", "/get_all_posts/" + type + "/", true);
    xhttp.send();
}

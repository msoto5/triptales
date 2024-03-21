function generatePost(post, formattedCreatedAt) {
    let html = '';
    html += '<div class="col-md-4 mb-4">';
    html += '<a href="/triptales/posts/detail/' + post.id + '" class="text-decoration-none text-dark">';
    html += '<div class="card h-100">';
    html += '<h5 class="card-header">' + post.title + '</h5>';
    if (post.img_url) {
        html += '<img src="' + post.img_url + '" class="card-img-top" alt="' + post.country_name + ' - ' + post.location_name + '">';
    }
    html += '<div class="card-body d-flex flex-column">';
    html += '<h5 class="card-title">' + post.country_name + ' - ' + post.location_name + '</h5>';
    html += '<p class="card-text">' + post.text + '</p>'; 
    html += '<p class="card-date">Created at: ' + formattedCreatedAt + '</p>';
    html += '<p class="likes">Likes: ' + post.likes + '</p>';
    html += '<a href="/triptales/profile/' + post.author + '" class="card-link">By ' + post.author + '</a>';
    html += '</div></div></a></div>';
    return html;
}
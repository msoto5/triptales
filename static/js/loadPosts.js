$('#sort-type').change(function () {
    loadPosts();
});

$('#filter-type').change(function () {
    loadPosts();
});

function loadPosts() {
    const sortType = $('#sort-type').val();
    const continent = '{{ continent_name }}';
    const filterType = $('#filter-type').val();

    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        const posts = JSON.parse(this.responseText);
        let html = '';

        posts.forEach(function (post) {
            var createdAtDate = new Date(post.created_at);
            var formattedCreatedAt = createdAtDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' });
            html += generatePost(post, formattedCreatedAt);

        });
        $('#posts-container').html(html);
    };
    xhttp.open("GET", "/filter_sort_by/" + sortType + "/" + filterType + "/" + continent + "/", true);
    xhttp.send();
}
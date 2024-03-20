document.getElementById('photo-upload').onchange = function () {
        var preview = document.getElementById('photo-preview');
        preview.innerHTML = '';

        for (var i = 0; i < this.files.length; i++) {
            var reader = new FileReader();
            reader.onload = function (event) {
                var img = document.createElement('img');
                img.src = event.target.result;
                img.classList.add('img-thumbnail');
                preview.appendChild(img);
            }
            reader.readAsDataURL(this.files[i]);
        }
    };
// Initialize Variables
var closePopup = document.getElementById("popupclose");
var overlay = document.getElementById("overlay");
var popup = document.getElementById("popup");
var button = document.getElementById("button");

// Close Popup Event
closePopup.onclick = function() {
    popup.style.animationPlayState = "running"
    overlay.style.animationPlayState = "running"
    setTimeout(()=> {
        overlay.style.display = 'none';
        popup.style.display = 'none';
        $('body').removeClass('scrollDisabled').css('margin-top', 0);
     } ,500);
};

// Close Popup Event
overlay.onclick = function() {
    popup.style.animationPlayState = "running"
    overlay.style.animationPlayState = "running"
    setTimeout(()=> {
        overlay.style.display = 'none';
        popup.style.display = 'none';
        $('body').removeClass('scrollDisabled').css('margin-top', 0);
     } ,500);
};

// Show Overlay and Popup
button.onclick = function() {
    overlay.style.display = 'block';
    popup.style.display = 'block';
    $('body').addClass('scrollDisabled');
    setTimeout(()=> { 
        $('popup').addClass('paused');
        popup.style.animationPlayState = "paused"
        overlay.style.animationPlayState = "paused"
    }, 500);
}

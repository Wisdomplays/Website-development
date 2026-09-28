var number = document.getElementById("number");

var clickCount = 0;

var timer = setInterval(changeNumber, 100);

function changeNumber() {
    number.innerHTML = Math.floor(Math.random() * 100) + 1;
}
function startstop() {
    clickCount = clickCount + 1;

    if(clickCount % 2 == 1) {
        clearInterval(timer);
    }
    else {
        timer = setInterval(changeNumber, 100);
    }
}
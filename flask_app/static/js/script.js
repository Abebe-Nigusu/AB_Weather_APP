function displayMessage(element) {
    alert("Loading weather report...");
}

function removeCookie(element) {

    element.closest(".cookie").remove();
    //element.parentElement.remove();
}

function swapTemperature(element) {

    var allDegreeSpans = document.querySelectorAll(".degree");

    for (var i = 0; i < allDegreeSpans.length; i++) {
        var currentNum = Number(allDegreeSpans[i].innerText);
        var newValue;

        if (element.value === "F") {
            newValue = (currentNum * 9 / 5) + 32;
        }
        else {
            newValue = (currentNum - 32) * 5 / 9;
        }
        allDegreeSpans[i].innerText = Math.round(newValue);
    }
}
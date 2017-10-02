// define several functions
function firstFunction() {
    secondFunction();
    alert(" Im in 1");
}
function secondFunction() {
    thirdFunction();
    alert(" Im in 2");
}
function thirdFunction() {
    fourthFunction(); // had a typo
    alert(" Im in 3");
}
function fourthFunction() {
    headline.innerHTML = "You clicked the headline!";
    alert(" Im in 4");
}

// grab the headline element
// alert(" Im here");
var headline = document.getElementById("mainHeading");
// add a click event handler
headline.onclick = function() {
    // alert(" Im before first");
    firstFunction();
    // alert(" Im here");
};






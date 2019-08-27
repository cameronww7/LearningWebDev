// Let's type this into the console, follow along with the video lecture

var x = document.querySelector("p")

// Show Text
x.textContent

// Reassign Text
x.textContent = "new Text"

// Refresh the page
// Show actual HTML
x.innerHTML

// Edit HTML
x.innerHTML = "This is <strong>BOLD</strong>"

// Can't do that with just textContent

/////////////////
// Attributes //
///////////////
// Edits a special id that has been set in the html
var special = document.querySelector("#special")

// This will look for an anchor tag and return its location
var specialA = y.querySelector("a")

// Finds the href only
specialA.getAttribute("href")

// This changes the href to amazon
specialA.setAttribute("href","https://www.amazon.com")

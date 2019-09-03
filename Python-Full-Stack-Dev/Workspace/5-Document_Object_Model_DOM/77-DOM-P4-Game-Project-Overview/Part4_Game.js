// Restart Game Button
var restart = document.querySelector('#b');

// Grab all the squares
var squares = document.querySelectorAll("td");

// Clear Squares Function
function clearBoard() {
  for (var index = 0; index < squares.length; index++) {
      squares[index].textContent = '';
  }
};

// is an Event Listener that will clean the board if you click restart!
restart.addEventListener('click', clearBoard)

// Create a function that will check the square marker
function changeMarker() {
    if (this.textContent === '') {
      this.textContent = 'X';
      // console.log(marker)
    } else if (this.textContent === 'X') {
      this.textContent = 'O';
    } else {
      this.textContent = '';
    }
};

// Use a for loop to add Event listeners to all the squares
for (var index = 0; index < squares.length; index++) {
    squares[index].addEventListener('click', changeMarker);
};

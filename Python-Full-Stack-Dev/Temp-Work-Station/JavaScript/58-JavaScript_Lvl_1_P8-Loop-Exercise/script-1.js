
/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var index = 0;
while (index < 5) {
  console.log("Hello")
  index++;
}

// For Loop
for (var i = 0; i < 5; i++) {
  console.log("Hello")
}


/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// While Loop
var index = 0;
while (index < 25) {
  if ((index % 2) == 1) {
      console.log(index)
  }
  index++;
}

// For Loop
for (var i = 0; i < 25; i++) {
  if ((i % 2) == 1) {
      console.log(i)
  }
}

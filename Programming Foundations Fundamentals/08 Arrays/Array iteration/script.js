
//check out https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array


var myArray1 = [500, 500, 500, 500, 500];
var myArray2 = [500, "cameron", -500, false, 500.2, 'c'];

var total = 0;
var total2 = 0;

for ( var index = 0 ; index < myArray.length ; index++ ) {
    // add the current element to the total	
    total = total + myArray[index];
}

var i = 0;

while ( i < myArray1.length) {
    total2 = total2 + myArray[index];
    ++i;
}

// after we're done with the loop
alert("The total is: " + total + total2 + myArray2[0] +
        myArray2[1] + myArray2[2] + myArray2[3] +
        myArray2.length);

alert("The total is: " + total + myArray2.reverse + 
        myArray2[0] + myArray2[1] + myArray2[2] + myArray2[3]);
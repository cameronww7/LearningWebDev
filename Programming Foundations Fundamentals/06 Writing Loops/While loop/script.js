var a = 1;

while ( a < 2 ) {
    alert( a );
    a++;
}

for ( a; a < 3; a++ ) {
    alert( a );
}

do {
    alert( a );
    a++;
} while ( a < 4 );

var amount = 0;
var index = 0;

// while ( index < 10 ) {
//     amount = amount + 100;
//     index++;
// }

for ( var index2 = 0; index2 < 10; index2++ ) {
    amount = amount + 100;
}

alert( "the value is: " + amount );
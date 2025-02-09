function readNumber() {
    let num;
  
    do {
        num = prompt("Enter number", 0);
    } while ( !isFinite(num) );
  
    if (num === null || num === '') return null;
  
    return +num;
}
  
alert(`Number: ${readNumber()}`);
function pow(x, n) {
    let result = x;
  
    for (let i = 1; i < n; i++) {
        result *= x;
    }
  
    return result;
    }
  
    let x = prompt("x?", '');
    let n = prompt("n?", '');
  
    if (n >= 1 && n % 1 == 0) {
        alert( pow(x, n) );
    } else {
        alert(`Степень ${n} не поддерживается, используйте натуральное число`);
    }
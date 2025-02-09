let calculator = {
    a,
    b,
    read() {
        a = promt("Number1:", 0); 
        b = promt("Number2:", 0);
    },
    sum() {
        return this.a + this.b;
    },
    mul() {
        return this.a * this.b;
    }
}
calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );
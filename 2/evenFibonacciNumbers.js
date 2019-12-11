let fibonaccilist = [];

function fib(max) {
    var a = 1;
    var b = 0;
    var temp;

    do {
        temp = a;
        a = a + b;
        b = temp;

        if (isEven(b) == true) {
            fibonaccilist.push(b);
        }

        console.log(b);
    } while (b < max);

    return b;
}

function isEven (n) {
    return !!(n && (n%2));
}

function add(accumulator, x) {
    return accumulator + x;
}

fib(4000000);
let evenSum = fibonaccilist.reduce(add, 0);

console.log(fibonaccilist);
console.log('evenSum = ' + evenSum);

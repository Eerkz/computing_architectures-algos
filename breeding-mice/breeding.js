function fibonacci(number) {
    var sqRootOf5 = Math.sqrt(5);

    var Phi = (1+sqRootOf5)/2;
    var phi = (1-sqRootOf5)/2

    return Math.round((Math.pow(Phi, number) - Math.pow(phi, number)) / sqRootOf5);
}

let N = 6;
console.time("execution time:");
for (let i =0; i < 18; i++){
    console.log(fibonacci(N))
}
console.timeEnd("execution time:");

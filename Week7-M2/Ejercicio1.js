function verification(numberExample, callbackPar, CallbackNotPar) {
    if (numberExample % 2 === 0) {
    callbackPar();
    } else {
    CallbackNotPar();
    }
}

verification(2, 
    () => console.log("The number is even!"),
    () => console.log("The number is odd!")

);
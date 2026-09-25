const listOfWords = ["very", "dogs", "cute", "are"]

const printDogs = new Promise(resolve => { setTimeout (() => 
    resolve(listOfWords[1]), 1000);
});

const printAreWithTwoSeconds = new Promise(resolve => { setTimeout(() => 
    resolve(listOfWords[3]), 2000);
});

const printVeryWiththreeSeconds = new Promise(resolve => { setTimeout(()=> 
    resolve(listOfWords[0]), 3000);
});

const printCuteWithFourSeconds = new Promise(resolve => { setTimeout(() => 
    resolve(listOfWords[2]), 4000)
});

Promise.all([printDogs,printAreWithTwoSeconds,printVeryWiththreeSeconds,printCuteWithFourSeconds])
    .then(result => {
        console.log(result.join(" "));
    });
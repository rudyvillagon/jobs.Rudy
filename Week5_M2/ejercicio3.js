const celsiusExample =[23, 33 ,46, 12, 53];
const farenheitExample = celsiusExample.map((element) => {
    return (element*1.8)+32;
})

console.log(farenheitExample)
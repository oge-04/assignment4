function results () {
  
    let numbersInput = document.getElementById("stringInput").value;
    let stringOutput = " ";
    for ( let length = stringInput.length - 1; length >= 0; length -- ) {
      stringOutput += stringInput[length]
    } 
    document.getElementById("stringOutput").innerHTML = stringOutput;
    console.log (stringOutput);
    




    
  }
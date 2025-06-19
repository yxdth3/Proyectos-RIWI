const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  
  readline.question('Introduce tu nombre: ', name => {
    console.log(`Hola ${name}!`);
  
    readline.question('Introduce tu edad: ', age => {
      console.log(`Tu edad es ${age}.`);
      readline.close();
    });
  });

//Capturar datos del usuario

function datosUser(){
    let nameUser = prompt ("Por favor, ingrese el nombre del usuario");
    let ageUser = prompt ("Ahora, digite la edad del usuario");

    //Convertimos los datos ingresados en la variable edad a números
    ageUser = Number(ageUser);

    //Validación de datos y mensajes personalizados
    if (isNaN(ageUser)){  //isNan se usa para determinar si un valor no es numérico
        console.error("ERROR, edad inválida. solo se aceptan números."); //Muestra el error en consola
        alert("ERROR, edad inválida. solo se aceptan números."); //Muestra el error al usuario
    } else if (ageUser < 18){
        alert(`Hola ${nameUser}!, aún eres menor de edad 🥲. Pero sigue aprendiendo y tómalo con calma ✨`);
    } else {
        alert(`Hola ${nameUser}!, ya eres mayor de edad 🤩. Prepárate para las grandes sorpresas y oportunidades que tiene el mundo de la programación ✨`);
    }
}
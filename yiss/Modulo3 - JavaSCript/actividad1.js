// let drinkCoffee = 0

// while (drinkCoffee < 10) {
//   drinkCoffee = drinkCoffee + 1
  
//   if (drinkCoffee === 8) { break }
//   if (drinkCoffee === 5) { continue }

//   console.log('Café')
// }

function agregarCliente(){

    let listClientes = [];

    for(let i=0; i<2; i++);

    let id = prompt ("Ingrese el id del cliente");
    let nombre = prompt ("Ingrese el nombre del cliente");
    let edad = prompt ("Ingrese la edad del cliente");

    let cliente = {}
    cliente.id = id
    cliente.nombre = nombre
    cliente.edad = edad;
    cliente.estado = true;

    let listRole = [];

    if(Number(edad)<18){
        return;
    }

    for(let i=0; i<2; i++){
        let role = {}
        let id = prompt ("Ingresa el id del rol");
        let nombre = prompt ("Ingresa el nombre del rol");
    
        role.id = id;
        role.nombre = nombre;
    
        listRole.push(role);
    }
    
        cliente.role = listRole;
        listClientes.push(cliente);

    const lista = document.getElementById("cliente-lista");

    listClientes.forEach(cliente => {
        const listItem = document.createElement("li");
        listItem.textContent = `Nombre del cliente: ${cliente.nombre} - Edad del cliente: ${cliente.edad} - Estado del cliente: ${cliente.estado}`;
        lista.appendChild(listItem);
    });

    console.log(cliente);

}
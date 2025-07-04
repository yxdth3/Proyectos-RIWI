   
    function registerUsers(){
        let name = document.getElementById("name");
        let age = parseInt(document.getElementById("age").value);
        let email = document.getElementById("email").value;
        let exit = document.getElementById("exit");

        // Validar campos vacíos
        if (!name || isNaN(age) || !email) {
            alert("⚠️ Por favor completa todos los campos");
        return;
        }

        //crear objeto usuario
        let user = {
            name : name,
            age : age,
            email : email
        };

        //crear objeto usuario pero de otra forma
        let user1 = {};
        user1.name = name;
        user1.age = age;
        user1.email = email;
    

        //obtener lista actual de usuarios desde local storage para que los muestre todos
        let users = JSON.parse(localStorage.getItem("users")) || [];

        //verificar si el usuario ya existe
        let existe = users.find(u => u.name === name);
        if (existe){
            alert("⚠️ El usuario ya existe");
            return;
        }

        //agregar nuevo usuario a los existentes
        users.push(user);

        //guardar la lista actualizada al local storage
        localStorage.setItem("users", JSON.stringify(users)); //stringify convierte un objeto o un array en texto JSON

        alert("Usuario registrado con éxito 🤗")
    }

        // Limpiar campos
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("email").value = "";

    // Actualizar vista
    showUsers();

    function showUsers(){
        let users = JSON.parse(localStorage.getItem("users")) || [];  //parse convierte un texto JSON en un objeto o un array
    let salida = "";

    if(users.length === 0){
        salida = "No hay usuarios registrados";
    }else{
        users.forEach((u,i) => {
            salida += (i + 1) + ". " +u.name + u.age + " años - " + u.email + "<br>";
        });
    }

    document.getElementById("exit").textContent = salida;
    }


    function removeUsers(){
        let nameDelete = document.getElementById("deleteName").value;
        let users = JSON.parse(localStorage.getItem("users")) || [];

        let index = users.findIndex(u => u.name === nameDelete);

        if (index !== 1){
            users.splice(index, 1);
            localStorage.setItem("users",JSON.stringify(users));
            alert("Usuario eliminado con éxito");
            showUsers();
        } else {
            alert("Usuario no encontrado.")
        }

        document.getElementById("deleteName").value = "";
    }


    function clearUsers(){
        if (confirm("¿Estás seguro de que quieres eliminar todos los usuarios?")) {
            localStorage.removeItem("users");
            alert("Todos los usuarios han sido eliminados.");
            showUsers();
        }
    }

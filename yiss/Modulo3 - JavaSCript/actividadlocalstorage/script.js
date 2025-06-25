   
    function registerUsers(){
        let name = document.getElementById("name");
        let age = parseInt(document.getElementById("age").value);
        let email = document.getElementById("email").value;

        

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

        //agregar nuevo usuario a los existentes
        users.push(user);

        //guardar la lista actualizada al local storage
        localStorage.setItem("users", JSON.stringify(users));

        alert("Usuario registrado con éxito 🤗")
    }


    function showUsers(){
        let users = JSON.parse(localStorage.getItem("users")) || [];
        document.getElementById("exit").textContent = JSON.stringify(users, null , 2);
    }


    function clearUsers(){
        let users = JSON.parse(localStorage.clear("users")) || [];

    }



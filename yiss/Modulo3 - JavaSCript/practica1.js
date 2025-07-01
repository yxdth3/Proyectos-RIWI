let xhr = new XMLHttpRequest();

xhr.open('GET','url a la que se envía la solicitud',true);

//.onload para cuando la solicitud se completó con éxito
xhr.onload = function(){
    //codigo de respuesta 
}


//.onreadystatechange se dispara cada que el XHMLttpRequest cambia de estado
xhr.onreadystatechange = function(){
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText);
    }
}

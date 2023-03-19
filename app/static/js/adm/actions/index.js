let api = new API('auth');



function authUser(){
    event.preventDefault()
    email = document.getElementById('inputEmail').value
    password = document.getElementById('inputPassword').value

    api.auth(email,password)

}
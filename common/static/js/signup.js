
 function show_password() {
   if (document.getElementById('checkbox').checked == true) {
document.getElementById('floatingPassword').type = 'text'
         document.getElementById('floatingPasswordConfirm').type = 'text'
    }
     else {
         document.getElementById('login_password').type = 'password'
  }
}



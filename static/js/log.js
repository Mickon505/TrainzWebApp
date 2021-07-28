let username = document.getElementById("name");
let password = document.getElementById("pass");

function test(){
    let uname = username.value.toString();
    let passw = password.value.toString();

    console.log(uname, passw);
}


function login(){
    let uname = String(username.value);
    let passw = String(password.value);
    
    try {
        console.log("trying to post data:", typeof(uname), typeof(passw));
        console.log(uname.length , passw.length);
        if (uname.length > 3 && passw.length > 5)
        {
            username.value = "";
            password.value = "";            
            console.log("posting...");
            $.ajax({
                type:'POST',
                url:'/login',
                data:{
                user: uname,
                pw: passw
                },
                success:function()
                {
                console.log("Creds sent");
                location.reload();
                }
            })
        }
    }
    catch(e) {
        console.error(e);
    }
}
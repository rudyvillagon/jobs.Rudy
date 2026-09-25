function togglePassword() {
    const input = document.getElementById("password");
    input.type = input.type === "password" ? "text" : "password";
}

function toggleConfPassword() {
    const input = document.getElementById("Conf_password");
    input.type = input.type === "password" ? "text" : "password";
}


const newUserAccount = async(Name, Email, Password, Address) => {
    const response = await fetch (`https://api.restful-api.dev/objects`, {
    method: "POST",
    headers: {
                "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name : Name,
        data:{
        email : Email,
        password : Password,
        address : Address,
        }
        }) 
    });

    if (!response.ok) {
        throw new Error("Error in the petition: " + response.status);
    }

    return await response.json();
}

document.getElementById("Create_account_botton").addEventListener("click", async () => {

    const name = document.getElementById("Full_name").value;
    const email = document.getElementById("Email").value;
    const password = document.getElementById("password").value;
    const confimPassword = document.getElementById("Conf_password").value;
    const address =  document.getElementById("User_address").value;

    if(password !== confimPassword) {
        alert("The passwords dont match")
        return;
    }

    try{
        const result = await newUserAccount(name, email, password, address);
        alert(`Usuario creado correctamente! Tu id es ${result.id}`);
        window.location.href = "Profile.html";

    }catch (error){
        console.error("Error:",error);
        alert("There is an error creating the account");
    }

    });

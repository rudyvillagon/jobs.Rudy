const newUserAccount = async(Name, Email, Password, Address) => {
    const postNewUser = await fetch (`https://api.restful-api.dev/objects`, {
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

    const data = await postNewUser.json();
    return data;
}

newUserAccount(
    "Juan Reyes",
    "JuanKings@gmail.com",
    "12345",
    "Hacienda Reyes 5290",
).then(result => console.log(result));

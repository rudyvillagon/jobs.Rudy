async function getUserInfo() {
    try {
        const users= await fetch("https://reqres.in/api/users/23",{
            headers: { 'x-api-key': 'reqres_abeaeae3a6e344d48bd4473a9ade0746' }
        });

        if (!users.ok){
            throw new Error("Hay un falló en el proceso ❌");
            
        }
        const data = await users.json();
        console.log(data);
    } catch (error) {
        console.error ("Ocurrió un problema", error)
    }
    
}

getUserInfo();
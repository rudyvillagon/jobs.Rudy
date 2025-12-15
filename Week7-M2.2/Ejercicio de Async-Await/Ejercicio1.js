async function getUserInfo() {
    try {
        const users= await fetch("https://reqres.in/api/users/2",{
            headers: { 'x-api-key': 'reqres_abeaeae3a6e344d48bd4473a9ade0746' }
        });

        if (!users.ok){
            throw new Error("Hay un Error en el proceso:");
            
        }
        const data = await users.json();
        console.log(data);
    } catch (error) {
        console.error ("ocurrió un problema", error)
    }
    
}

getUserInfo();
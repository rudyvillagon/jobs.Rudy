const userId = async(id, Address) => {
    try{
        const getUserForChange = await fetch (`https://api.restful-api.dev/objects/${id}`, {
        method: "PATCH",
        headers: {
                "Content-Type": "application/json"
        },
        body: JSON.stringify({
            data: {
                "address":Address,
            }
        })
    }
);

        if(!getUserForChange.ok){
            throw new Error("-User not Found")
                
        }

        const data = await getUserForChange.json();
        return data;

    } catch (error){
        console.error (error.message)
    }    

}

userId("ff8081819782e69e019b9f87963479c8", "Finca San Carlos").then(result => console.log(result))
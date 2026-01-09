const userId = async(id) => {
    try{
        const getUserInfo = await fetch (`https://api.restful-api.dev/objects/${id}`, {
        method: "GET",
        headers: {
                    "Content-Type": "application/json"
        }});

        if(!getUserInfo.ok){
            throw new Error("-User Information not found-")
        }

        const data = await getUserInfo.json();
        return data;

    } catch (error){
        console.error ("Theres no ID on that Number", error);
    }

}

userId(99).then(result => console.log(result));
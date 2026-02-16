const axios = require('axios');

const userId = async(id, Address) => {
    try{
        const data= { address : Address, };

        const response = await axios.patch(`https://api.restful-api.dev/objects/${id}`,data)
    

    return response.data;

    } catch (error){
        console.error (error.message)
    } 

};

userId("ff8081819782e69e019ba4d86c370456", "Finca Roger").then(result => console.log(result))
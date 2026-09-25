const axios = require('axios');

const userId = async(id) => {
    try{
        const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);

        return response.data;

    } catch (error){
        console.error ("Theres no ID on that Number", error);
    }
}


userId(2).then(result => console.log(result));
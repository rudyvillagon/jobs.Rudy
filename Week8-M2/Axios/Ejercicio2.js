const axios = require('axios');

const userData = {
        name : "Juan Reyes",
        data:{
        email : "JuanKings@gmail.com",
        password : "12345",
        address : "Hacienda Reyes 5290",
        }
        };

axios.post(`https://api.restful-api.dev/objects`, userData)
.then(result => console.log(result))
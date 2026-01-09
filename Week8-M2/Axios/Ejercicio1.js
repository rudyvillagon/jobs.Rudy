const axios = require('axios');

const getElements = async() => {
    const response = await axios.get(`https://api.restful-api.dev/objects`);

    const filterAllElements = response.data.filter(item => item.data);
    filterAllElements.forEach(item => {
        const InfoDetail = Object.entries(item.data)
            .map(([key, value]) => `${key}: ${value}`)
            .join(",");

        console.log(`${item.name} (${InfoDetail})`)

    })
}

getElements();
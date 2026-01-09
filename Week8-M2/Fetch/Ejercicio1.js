const getElements = async () => {
    const response = await fetch  (`https://api.restful-api.dev/objects`);
    const allElements = await response.json();

    const filterAllElements = allElements.filter(item => item.data);

    filterAllElements.forEach(item => {
        const InfoDetail = Object.entries(item.data)
            .map(([key, value]) => `${key}: ${value}`)
            .join(",");

        console.log(`${item.name} (${InfoDetail})`)

    });

}

getElements();


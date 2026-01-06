const userId = [2];

const searchUserInf = userId.map(user => 
    fetch(`https://reqres.in/api/users/${user}`,{
            headers: { 'x-api-key': 'reqres_abeaeae3a6e344d48bd4473a9ade0746' }
        })
        .then(response => {
        if (!response.ok) {
            throw new Error ("There was an error in the process")
            }
            return response.json();
        })
);

Promise.all(searchUserInf)
    .then(user => {
        console.log(user)
    })
    .catch(error => {
        console.error(error.message)
    });
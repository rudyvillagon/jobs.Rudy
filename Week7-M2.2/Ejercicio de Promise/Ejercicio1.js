const pokemonIds = [1,45,73];



const searchPokemonsNames = pokemonIds.map(pokemon =>
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`).then(response => {
        if (!response.ok) {
            throw new Error ("There was an error in the process");
        }
        return response.json();
    })
);

Promise.all(searchPokemonsNames)
    .then(pokemons => {
        pokemons.forEach(pokemon => {
        console.log(pokemon.name)
    });
    })
    .catch(error => {
        console.error(error.message)
    });

        

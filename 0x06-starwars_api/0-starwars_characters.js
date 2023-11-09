#!/usr/bin/node
const fetch = require('node-fetch');
const filmID = process.argv[2];

async function getStarWarsCharacters(filmId) {
  const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  const response = await fetch(endpoint);
  const json = await response.json();
  const characters = json.characters;

  for (const urlCharacter of characters) {
    const characterResponse = await fetch(urlCharacter);
    const characterJson = await characterResponse.json();
    console.log(characterJson.name);
  }
}

getStarWarsCharacters(filmID);
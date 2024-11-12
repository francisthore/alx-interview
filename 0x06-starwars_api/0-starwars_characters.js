#!/usr/bin/node
// Module prints all characters of a Star Wars movie
const request = require('request');
const args = process.argv.slice(2);

const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;

async function fetchCharacterName (url) {
  const options = {
    url,
    json: true
  };
  return new Promise((resolve, reject) => {
    request(options, (err, resp, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body.name);
      }
    });
  });
}

async function fetchCharacterUrls (url) {
  const options = {
    url,
    json: true
  };
  return new Promise((resolve, reject) => {
    request(options, (err, resp, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body.characters);
      }
    });
  });
}

async function printCharacterNames (url) {
  const characterUrls = await fetchCharacterUrls(url);
  const characterPromises = characterUrls.map(charUrl => fetchCharacterName(charUrl));
  const characterNames = await Promise.all(characterPromises);
  characterNames.forEach((character) => {
    console.log(character);
  });
}

printCharacterNames(url);

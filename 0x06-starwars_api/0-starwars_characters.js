#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + movieId,
  method: 'GET'
};

request(options, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, idx) {
  request(characters[idx], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

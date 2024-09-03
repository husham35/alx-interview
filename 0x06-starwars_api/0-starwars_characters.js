#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        } else {
          console.error('Error fetching character:', error);
        }
      });
    });
  } else {
    console.error('Error fetching movie:', error);
  }
});

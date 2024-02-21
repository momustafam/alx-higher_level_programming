#!/usr/bin/node

const request = require('request');
const starWarsUrl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUrl, (_, __, body) => {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (_, __, body) => {
      console.log(JSON.parse(body).name);
    });
  }
});

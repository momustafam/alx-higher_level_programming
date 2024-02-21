#!/usr/bin/node

const request = require('request');

function getDataFrom (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function errHandler (err) {
  console.log(err);
}

function printMovieCharacters (movieId) {
  const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUrl)
    .then(JSON.parse, errHandler)
    .then((res) => {
      const characters = res.characters;
      const promises = [];

      for (let i = 0; i < characters.length; i++) {
        promises.push(getDataFrom(characters[i]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let i = 0; i < results.length; i++) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

printMovieCharacters(process.argv[2]);

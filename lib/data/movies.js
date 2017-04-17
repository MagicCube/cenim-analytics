const nj = require('numjs');


const movies = require('../../data/movies');

const MOVIE_FEATURE_SIZE = movies[0].feature.length;

const movieDict = new Map();
movies.forEach((movie) => {
  movieDict.set(movie.id, movie);
});


function getMovie(id) {
  return movieDict.has(id) ? movieDict.get(id) : null;
}

function getMovieFeature(id) {
  const movie = getMovie(id);
  return movie ? nj.array(movie.feature) : null;
}

function mergeMovieFeatures(ids) {
  const features = ids.map(id => getMovieFeature(id));
  const merged = features.reduce((acc, i) => acc.add(i), nj.zeros([MOVIE_FEATURE_SIZE]));
  return merged;
}


module.exports = {
  MOVIE_FEATURE_SIZE,
  movies,
  getMovie,
  getMovieFeature,
  mergeMovieFeatures
};

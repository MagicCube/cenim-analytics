const nj = require('numjs');

const { MOVIE_FEATURE_SIZE, movies, mergeMovieFeatures } = require('../data/movies');
const checkpoint = require('../../data/models/checkpoint.json');


//const weights = nj.array(checkpoint.weights);
const weights = nj.random([MOVIE_FEATURE_SIZE * 3, 2]);

function getRecommendations(likes) {
  const userFeatures = nj.random([MOVIE_FEATURE_SIZE * 2]);
  const results = movies.map((movie) => {
    const movieFeature = nj.array(movie.feature);
    const userMovieFeatures = nj.concatenate(userFeatures, movieFeature);
    const x = nj.array([userMovieFeatures.valueOf()]);
    const y = nj.dot(x, weights);
    const like = y.get(0, 0);
    const dislike = y.get(0, 1);
    const result = {
      id: movie.id,
      title: movie.title,
      img: movie.images.large,
      rate: {
        like,
        dislike,
        value: like - dislike
      }
    };
    return result;
  });
  results.sort((a, b) => b.rate.value - a.rate.value);
  return results;
}

module.exports = {
  getRecommendations
};

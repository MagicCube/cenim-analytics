const nj = require('numjs');

const { MOVIE_FEATURE_SIZE, movies, mergeMovieFeatures } = require('../data/movies');
const checkpoint = require('../../data/models/checkpoint.json');


const weights = nj.array(checkpoint.weights);

function getRecommendations(likes) {
  const userFeatures = nj.concatenate(mergeMovieFeatures(likes), nj.zeros([MOVIE_FEATURE_SIZE]));
  const results = movies.map((movie) => {
    const movieFeature = movie.feature;
    const userMovieFeatures = nj.concatenate(userFeatures, movieFeature);
    const x = nj.array([userMovieFeatures.valueOf()]);
    const y = nj.dot(x, weights);
    const result = {
      id: movie.id,
      title: movie.title,
      img: movie.images.large,
      rate: {
        like: y.get(0, 0),
        dislike: y.get(0, 1)
      }
    };
    return result;
  });
  results.sort((a, b) => (b.rate.like - b.rate.dislike) - (a.rate.like - b.rate.dislike));
  return results;
}

module.exports = {
  getRecommendations
};

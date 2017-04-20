const nj = require('numjs');

const { MOVIE_FEATURE_SIZE, movies: _movies, mergeMovieFeatures } = require('../data/movies');

const _users = [];

function getRecommendations(likes) {
  if (!likes || likes.length === 0) return [];

  const userFeature = mergeMovieFeatures(likes);
  const users = _users.map((user) => {
    const sim = _computeSim(user.feature, userFeature);
    return {
      id: user.id,
      likes: user.likes,
      dislikes: user.dislikes,
      skips: user.skips,
      sim
    };
  });
  users.sort((a, b) => b.sim - a.sim);
  const sampleUserCount = 20;
  const sampleUsers = [];
  for (let i = 0; i < sampleUserCount; i++) {
    sampleUsers.push(users[i]);
  }
  const sortedMovies = _movies.map((movie) => {
    let rate = 0;
    sampleUsers.forEach((sampleUser) => {
      if (sampleUser.likes.includes(movie.id)) {
        rate += sampleUser.sim * 1;
      } else if (sampleUser.dislikes.includes(movie.id)) {
        rate -= sampleUser.sim * 1;
      } else if (sampleUser.skips.includes(movie.id)) {
        rate -= sampleUser.sim * 0.2;
      }
    });
    return {
      id: movie.id,
      title: movie.title,
      img: movie.images.large,
      rate
    };
  });
  sortedMovies.sort((a, b) => b.rate - a.rate);
  const recommendedMovies = [];
  while (recommendedMovies.length < 20) {
    const movie = sortedMovies.shift();
    if (!likes.includes(movie.id)) {
      recommendedMovies.push(movie);
    }
  }
  return recommendedMovies;
}


function _loadUsers() {
  const userMovies = require('../../data/user-movie.json');
  userMovies.forEach((userMovie) => {
    const user = {
      id: userMovie.id,
      feature: mergeMovieFeatures(userMovie.likes),
      likes: userMovie.likes,
      dislikes: userMovie.dislikes,
      skips: userMovie.skips
    };
    _users.push(user);
  });
}

function _computeSim(a, b) {
  return nj.dot(a, b).valueOf()[0] / (norm(a) * norm(b));
}

function norm(v) {
  return Math.sqrt(nj.power(v, 2).sum());
}


_loadUsers();

module.exports = {
  getRecommendations
};

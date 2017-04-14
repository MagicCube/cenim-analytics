const fs = require('fs');
const path = require('path');

const ratings = require('../../data/ratings.json');

console.log('Preparing...\n');

const OUTPUT_USERS_PATH = path.resolve(__dirname, '../../data/user-movie.json');
const OUTPUT_USERS_ALL_PATH = path.resolve(__dirname, '../../data/user-movie-all.json');

const users = [];
let user = null;
ratings.forEach((rating) => {
  if (user === null || user.id !== rating.sessionId) {
    user = {
      id: rating.sessionId,
      likes: [],
      dislikes: []
    };
    users.push(user);
  }
  if (rating.value === 1) {
    if (!user.likes.includes(rating.movieId)) {
      user.likes.push(rating.movieId);
    }
  } else if (rating.value === -1) {
    if (!user.dislikes.includes(rating.movieId)) {
      user.dislikes.push(rating.movieId);
    }
  }
});

fs.writeFileSync(OUTPUT_USERS_ALL_PATH, JSON.stringify(users));
console.log(`All ${users.length} users have been written to ${OUTPUT_USERS_ALL_PATH}`);

const topQualityUsers = users.filter(u => u.likes.length + u.dislikes.length >= 3);
fs.writeFileSync(OUTPUT_USERS_PATH, JSON.stringify(topQualityUsers));
console.log(`${topQualityUsers.length} top-quality users have been written to ${OUTPUT_USERS_PATH}`);

console.log('\nPreparations done.');

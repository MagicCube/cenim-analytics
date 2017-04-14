const fs = require('fs');
const path = require('path');

const ratings = require('../../data/ratings.json');

console.log('Preparing...\n');

const OUTPUT_SESSIONS_PATH = path.resolve(__dirname, '../../data/sessions.json');
const OUTPUT_SESSIONS_ALL_PATH = path.resolve(__dirname, '../../data/sessions-all.json');

const sessions = [];
let session = null;
ratings.forEach((rating) => {
  if (session === null || session.id !== rating.sessionId) {
    session = {
      id: rating.sessionId,
      likes: [],
      dislikes: []
    };
    sessions.push(session);
  }
  if (rating.value > 0) {
    if (!session.likes.includes(rating.movieId)) {
      session.likes.push(rating.movieId);
    }
  } else if (rating.value < 0) {
    if (!session.dislikes.includes(rating.movieId)) {
      session.dislikes.push(rating.movieId);
    }
  }
});

fs.writeFileSync(OUTPUT_SESSIONS_ALL_PATH, JSON.stringify(sessions));
console.log(`All ${sessions.length} sessions have been written to ${OUTPUT_SESSIONS_ALL_PATH}`);

const topQualitySessions = sessions.filter(s => s.likes.length + s.dislikes.length >= 3);
fs.writeFileSync(OUTPUT_SESSIONS_ALL_PATH, JSON.stringify(topQualitySessions));
console.log(`${topQualitySessions.length} top-quality sessions have been written to ${OUTPUT_SESSIONS_PATH}`);

console.log('\nPreparations done.');

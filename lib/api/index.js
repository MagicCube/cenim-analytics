const cors = require('cors');
const express = require('express');

const { getRecommendations } = require('../model/RecommendationModel');


const router = express.Router();

router.post('/recommendation', (req, res) => {
  const likes = req.body;
  const recommendations = getRecommendations(likes);
  res.send(recommendations);
});

module.exports = router;

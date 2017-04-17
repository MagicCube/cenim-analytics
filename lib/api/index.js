const cors = require('cors');
const express = require('express');


const router = express.Router();

router.post('/recommendation', (req, res) => {
  const ids = req.body;

  res.send([]);
});

module.exports = router;

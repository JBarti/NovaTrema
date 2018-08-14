var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res, next) {
	return res.send('API working properly')
})

router.post('/', function (req, res, next) {

	const file = req.files[Object.keys(req.files)[0]]
	const filename = file.name
	const mimetype = file.mimetype

	if (mimetype.split('/')[0] !== 'image') {
		return res.status(400).send('Sent file is not image')
	}

	file.mv(`static/${filename}`, (err) => {
		if (err) {
			console.log(err)
			return res.status(500).send('Internal server error while uploading picture')
		}
		return res.send(`Successfuly uploaded file ${filename}`)
	})
})

module.exports = router;

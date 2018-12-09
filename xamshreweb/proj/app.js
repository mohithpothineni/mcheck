
const express = require('express')
const bodyParser = require('body-parser');
const app = express()
const port = 8080

var path = require('path');

app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => res.sendFile(path.join(__dirname + '/index.html')))

app.post('/updatemessages', (req, res) =>res.send('called update messages'))

app.post('/message', (req, res) => {res.send(req.body.message)})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

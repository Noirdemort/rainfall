const WebSocketServer = require('ws').Server;
const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const fs = require('fs');
const mongoose = require('mongoose');
const firebase = require('firebase');
const crypto = require('crypto');
const bcrypt = require('bcrypt');
const app = express();

app.use(bodyParser.json());
// Require express and create an instance of it
app.use(express.static('.'))


wss.on('connection',function(ws) {
    // console.log(ws)
    ws.on('message', function(msg){
        if(msg.op=='login'){
            firebase_login(msg)
        }
        if(msg.op=='register'){
            firebase_createuser(msg)
        }
    });
    ws.send('Welcome to server chat!')
});

// on the request to root (localhost:3000/)
app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname+'/index.html'));
});

// Change the 404 message modifing the middleware
app.use(function(req, res, next) {
    res.status(404).send("Sorry, that route doesn't exist. Have a nice day :)");
});

// start the server in the port 3000 !
app.listen(3000, function () {
    console.log('App listening on port 3000.');
});

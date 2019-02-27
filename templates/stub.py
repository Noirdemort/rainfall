

htmlTemplates = {
    'login': """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>Welcome to {title}</h1>
    <p style="text-align: center; font-size: large">
        <strong>Sign in here</strong> <br>
    Username      : <input id="uname" type="username"> <br>
    Password   : <input id="userpass" type="password"> <br>
        <button>Submit</button>
         <a href="register.html">Sign up instead!</a>
    </p>
</body>
</html>
    """,
    'register': """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>Welcome to {title}</h1>

    <p style="text-align: center; font-size: large">
    <strong>Sign up here</strong> <br><br>

       <center><h3>Create your profile</h3>
                        <br><br>
                        <table>
                          <tr>
                              <td>Name</td>
                              <td id='realName'><input type="text"></td>
                          </tr>
                          <tr>
                            <td>Username *</td>
                            <td> <input type="text" name="username" id="cuname" placeholder="username" required> </td>
                          </tr>
                          <tr>
                            <td>Password *</td>
                            <td><input type="password" name="password" id="pass" placeholder="password" required>  </td>
                          </tr>
                          <tr>
                            <td>Confirm Password *</td>
                            <td><input type="password" name="password" id="cpass" placeholder="confirm password" required>   </td>
                          </tr>
                          <tr>
                            <td>Email</td>
                            <td><input type="email" name="mail" id="umail" placeholder="Your personal mail"></td>
                          </tr>
                          <tr>
                            <td>Profile Photo</td>
                            <td><input type="file" accept="image/*" name="image" id="pdp"></td>
                          </tr>
                            
                          <tr>
                            <td></td>
                            <td><button onclick='toHell()'type="submit">Create Pro`file</button></td>
                         </tr>
                        </table>
                        </center>
    <br><br>
        <a href="login.html">Sign in instead!</a>
    </p>


</body>
</html>
    """,
    'general': """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
<div id="header">
<!-- <h1>Welcome to VIT on Date!</h1>
Sign in and register <p>This is your one stop solution for dating @ VIT</p> -->

<div class="navbar">
        <a href="#">{title}</a>
        <div class="dropdown">
          <button class="dropbtn">User
            <i class="fa fa-caret-down"></i>
          </button>
          <div class="dropdown-content">
            <a href="#">Notifications</a>
            <a href="#">Edit Profile</a>
            <a >Sign out</a>
          </div>
        </div>
      </div>
</div>


</body>
<style>



/* For header */
/* Navbar container */
.navbar {
    overflow: hidden;
    background-color: rgb(89, 94, 224);
    font-family: Arial;
  }

  /* Links inside the navbar */
  .navbar a {
    float: left;
    font-size: 16px;
    color: white;
    text-align: center;
    padding: 12px 16px;
    text-decoration: none;
  }

  /* The dropdown container */
  .dropdown {
    float:right;
    margin-right:5%;
    overflow: hidden;
  }

  /* Dropdown button */
  .dropdown .dropbtn {
    font-size: 16px;
    border: none;
    outline: none;
    color: white;
    padding: 14px 16px;
    background-color: inherit;
    font-family: inherit; /* Important for vertical align on mobile phones */
    margin: 0; /* Important for vertical align on mobile phones */
  }

  /* Add a red background color to navbar links on hover */
  .navbar a:hover, .dropdown:hover .dropbtn {
    background-color: #807d80;
  }

  /* Dropdown content (hidden by default) */
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
  }

  /* Links inside the dropdown */
  .dropdown-content a {
    float: left;
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
  }

  /* Add a grey background color to dropdown links on hover */
  .dropdown-content a:hover {
    background-color: #ddd;
  }

  /* Show the dropdown menu on hover */
  .dropdown:hover .dropdown-content {
    display: block;
  }



body{
    font-size:24px;
    width: 80%;
    height: 80%;
}
</style>
</html>
    """
}


server = {
    "server": """
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
    """,
    'add_page': """
    app.get('/{addHere}', function (req, res) {
    res.sendFile(path.join(__dirname+'/{addHere}.html'));
});
    """
}




package = {
  "name": "",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node server.js"
  },
  "license": "MIT"
}

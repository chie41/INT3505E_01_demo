require("dotenv").config();
const express = require("express");
const { login, authenticate } = require("./auth");
const app = express();
app.use(express.json());

app.post("/login", login);

app.get("/profile", authenticate, (req, res) => {
    res.json({
        message: "You are authenticated",
        user: req.user
    });
});

app.listen(3000, () => console.log("Server running on 3000"));
//node Jwt-auth-demo/server.js

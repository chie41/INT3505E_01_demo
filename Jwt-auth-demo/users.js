const bcrypt = require("bcryptjs");

const users = [
    {
        id: 1,
        username: "admin",
        password: bcrypt.hashSync("123456", 10),
        role: "admin"
    }
];

async function findUser(username) {
    return users.find(u => u.username === username);
}

module.exports = { findUser };

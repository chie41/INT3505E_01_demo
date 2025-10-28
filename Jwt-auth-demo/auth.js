const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");
const { findUser } = require("./users");

async function login(req, res) {
    const { username, password } = req.body;

    const user = await findUser(username);
    if (!user) return res.status(401).json({ message: "user not found" });

    const isValid = bcrypt.compareSync(password, user.password);
    if (!isValid) return res.status(401).json({ message: "wrong password" });

    const token = jwt.sign(
        { id: user.id, role: user.role },
        process.env.JWT_SECRET,
        { expiresIn: "15m" }
    );

    res.json({ accessToken: token });
}

module.exports = { login };

function authenticate(req, res, next) {
    const header = req.headers.authorization;
    if (!header || !header.startsWith("Bearer ")) {
        return res.status(401).json({ message: "No token provided" });
    }

    const token = header.split(" ")[1];
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded; // gắn quyền và id vào request
        next();
    } catch (err) {
        return res.status(403).json({ message: "Invalid token" });
    }
}

module.exports = { login, authenticate };

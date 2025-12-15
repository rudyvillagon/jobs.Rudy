const fs = require("fs");

function readlist(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, "utf-8",(err,data) => {
            if (err) reject(err);
            else resolve(data.split("\n").map(x => x.trim()));
        });
    });
}

async function makePars() {
    const list1 = await readlist("list1.txt");
    const list2 = await readlist("list2.txt");


    const pars = list1.filter(item => list2.includes(item));
    console.log(pars)
}

makePars()
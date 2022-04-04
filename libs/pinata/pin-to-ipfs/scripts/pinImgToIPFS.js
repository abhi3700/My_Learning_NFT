const fs = require("fs");
const path = require("path");
const pinataSDK = require("@pinata/sdk");
require('dotenv').config();

// keep the `.env` file into the root of project i.e. where the "package.json" file is present.
const PINATA_API_KEY = process.env.PINATA_API_KEY || "";
const PINATA_SECRET_API_KEY = process.env.PINATA_SECRET_API_KEY || "";

const pinata = pinataSDK(PINATA_API_KEY, PINATA_SECRET_API_KEY);
async function main() {
    // give img path
    const imgPath = path.join(__dirname, '..', 'img');

    // read content of directory
    const files = fs.readdirSync(imgPath);

    let hashes = [];

    // read each img content -->> upload img -->> store hashes into array 
    for (let i = 0; i < files.length; i++) {
        console.log("Pinning to Pinata...");
        const readableStreamForFile = fs.createReadStream(imgPath + `/${files[i]}`);
        let result = await pinata.pinFileToIPFS(readableStreamForFile);
        console.log("\tIPFS CID: %s", result.IpfsHash);
        hashes.push(result.IpfsHash);
    }

    let data = JSON.stringify(hashes, null, 2);

    fs.writeFile('hashes.json', data, (err) => {
        if (err)
            throw err;
        console.log('Data written to file');
    });
}

main()
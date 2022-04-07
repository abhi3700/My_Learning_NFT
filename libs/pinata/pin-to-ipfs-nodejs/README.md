# Pinata

A IPFS cloud service provider for NFT asset storage using NodeJS.

## Task

* Here, some images would be uploaded into Pinata cloud (IPFS based).

## Coding

1. Sign up for Pinata [here](https://www.pinata.cloud/)
2. Generate an API Key [here](https://app.pinata.cloud/keys)
   - Make sure the Admin button is selected to have access to all Pinata endpoints.
   - Copy the **PinataAPIKey** and the **SecretAPIKey** to your clipboard. We will be using this later.

3. `$ mkdir pin-to-ipfs && cd pin-to-ipfs`: Create folder & switch to folder
4. `$ npm init -y`: create `package.json` file inside the folder.
5. `$ npm i --save-dev @pinata/sdk dotenv`: install pinata dependency package for this task.
6. Paste the **PinataAPIKey** and the **SecretAPIKey** into `.env` file created at the root of the project i.e. where `package.json` file is present.
7. `$ mkdir img`: Create a `img/` folder & paste some images inside this.
8. `$ mkdir scripts`: Create a `scripts/` folder & add `pinToIPFS.js` script file for uploading the images.
9. Run `$ node scripts/pinImgToIPFS.js` at the root of `pin-to-ipfs` project directory & get this output & all the hashes is stored in `hashes.json`

```console
❯ node scripts/pinImgToIPFS.js && code hashes.json
Pinning to Pinata...
        IPFS CID: QmUX9iy6yZbuMokeRXwawuGQCphhHjZqYGyHK4HwHcmPzg
Pinning to Pinata...
        IPFS CID: QmWd2ijHubsHmAvvdttMTX3kmEVWNQ6eb2ntUkM3AURKLF
Pinning to Pinata...
        IPFS CID: QmP9cbS1cvsEobodvHnfCtfjZN6fS28toTzrqRwd5sLfnU
Pinning to Pinata...
        IPFS CID: QmWtjYwUhjPFv81dhAs2MB3DHgUqFoVvWoLZ5QqJcbCy4R
Pinning to Pinata...
        IPFS CID: QmPzqSEEJrMHYcA8C8YogExwuKeXZSJQcy13m6tFE7qhPa
Pinning to Pinata...
        IPFS CID: QmSAGCEUt9ahF2YTVVf7gz5EFx7seUPssXNw4GfxMriKEW
Pinning to Pinata...
        IPFS CID: QmRRcPr2VLJ2Gw1arS3JnHg2CQtDB2Uwk1LR2gHrRpPM3y
Pinning to Pinata...
        IPFS CID: Qmc3PmZ1Pr5yyzaChs6xPPxYzptLVzFdGoCM4Bczn6JiT3
Pinning to Pinata...
        IPFS CID: QmSieKV7jGLVT2fAeS8DDyQ9eDFx4di24BFtLFFgNR33wK
Pinning to Pinata...
        IPFS CID: QmUJJBbyE7VLkRWw8hSzg7B49NWAwKsJbvRfz7FUQzEaga
Data written to file
```

10. View all the hashes here:

```json
$ code hashes.json
[
  "QmUX9iy6yZbuMokeRXwawuGQCphhHjZqYGyHK4HwHcmPzg",
  "QmWd2ijHubsHmAvvdttMTX3kmEVWNQ6eb2ntUkM3AURKLF",
  "QmP9cbS1cvsEobodvHnfCtfjZN6fS28toTzrqRwd5sLfnU",
  "QmWtjYwUhjPFv81dhAs2MB3DHgUqFoVvWoLZ5QqJcbCy4R",
  "QmPzqSEEJrMHYcA8C8YogExwuKeXZSJQcy13m6tFE7qhPa",
  "QmSAGCEUt9ahF2YTVVf7gz5EFx7seUPssXNw4GfxMriKEW",
  "QmRRcPr2VLJ2Gw1arS3JnHg2CQtDB2Uwk1LR2gHrRpPM3y",
  "Qmc3PmZ1Pr5yyzaChs6xPPxYzptLVzFdGoCM4Bczn6JiT3",
  "QmSieKV7jGLVT2fAeS8DDyQ9eDFx4di24BFtLFFgNR33wK",
  "QmUJJBbyE7VLkRWw8hSzg7B49NWAwKsJbvRfz7FUQzEaga"
]
```

11. DONE ✅

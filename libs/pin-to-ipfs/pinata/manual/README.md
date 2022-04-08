# Pinata

A IPFS cloud service provider for NFT asset storage using NodeJS.

## Task

* Here, some images would be uploaded into Pinata cloud (IPFS based).

## Coding

Here, all the images are readily available in the folder - "./img/" for uploading into Pinata IPFS cloud

1. Sign up for Pinata [here](https://www.pinata.cloud/)
2. Generate an API Key [here](https://app.pinata.cloud/keys)
   - Make sure the Admin button is selected to have access to all Pinata endpoints.
   - Copy the **PinataAPIKey** and the **SecretAPIKey** to your clipboard. We will be using this later.

3. Go to `pin-to-ipfs/` folder & then run `$ mkdir manual && cd manual`: Create folder & switch to folder
4. `$ npm init -y`: create `package.json` file inside the folder.
5. `$ npm i --save-dev @pinata/sdk dotenv`: install pinata dependency package for this task.
6. Paste the **PinataAPIKey** and the **SecretAPIKey** into `.env` file created at the root of the project i.e. where `package.json` file is present.
7. `$ mkdir img`: Create a `img/` folder & paste some images inside this.
8. `$ mkdir scripts`: Create a `scripts/` folder & add `pinImgToIPFS.js` script file for uploading the images.
9. Run `$ node scripts/pinImgToIPFS.js` at the root of `pin-to-ipfs` project directory & get this output & all the hashes is stored in `img_hashes.json` file.

```console
❯ node scripts/pinImgToIPFS.js
Pinning img 1 to Pinata...
        IPFS CID: QmUX9iy6yZbuMokeRXwawuGQCphhHjZqYGyHK4HwHcmPzg
Pinning img 2 to Pinata...
        IPFS CID: QmWd2ijHubsHmAvvdttMTX3kmEVWNQ6eb2ntUkM3AURKLF
Pinning img 3 to Pinata...
        IPFS CID: QmP9cbS1cvsEobodvHnfCtfjZN6fS28toTzrqRwd5sLfnU
Pinning img 4 to Pinata...
        IPFS CID: QmWtjYwUhjPFv81dhAs2MB3DHgUqFoVvWoLZ5QqJcbCy4R
Pinning img 5 to Pinata...
        IPFS CID: QmPzqSEEJrMHYcA8C8YogExwuKeXZSJQcy13m6tFE7qhPa
Data written to file
```

10. View all the image hashes here:

```console
$ code img_hashes.json
[
  "QmUX9iy6yZbuMokeRXwawuGQCphhHjZqYGyHK4HwHcmPzg",
  "QmWd2ijHubsHmAvvdttMTX3kmEVWNQ6eb2ntUkM3AURKLF",
  "QmP9cbS1cvsEobodvHnfCtfjZN6fS28toTzrqRwd5sLfnU",
  "QmWtjYwUhjPFv81dhAs2MB3DHgUqFoVvWoLZ5QqJcbCy4R",
  "QmPzqSEEJrMHYcA8C8YogExwuKeXZSJQcy13m6tFE7qhPa"
]
```

11. Generate (manually) metadata file for each image file & paste into a `metadata/` folder
12. Add `pinMetaToIPFS.js` script file to `scripts/` folder for uploading the images.
13. Run `$ node scripts/pinMetaToIPFS.js` at the root of `pin-to-ipfs` project directory & get this output & all the hashes is stored in `metadata_hashes.json` file.
14. View all the metadata hashes here:

```console
$ code metadata_hashes.json
[
  "QmUX9iy6yZbuMokeRXwawuGQCphhHjZqYGyHK4HwHcmPzg",
  "QmWd2ijHubsHmAvvdttMTX3kmEVWNQ6eb2ntUkM3AURKLF",
  "QmP9cbS1cvsEobodvHnfCtfjZN6fS28toTzrqRwd5sLfnU",
  "QmWtjYwUhjPFv81dhAs2MB3DHgUqFoVvWoLZ5QqJcbCy4R",
  "QmPzqSEEJrMHYcA8C8YogExwuKeXZSJQcy13m6tFE7qhPa"
]
```

1.  Now, all the images & its metadata are uploaded into Pinata cloud. DONE ✅

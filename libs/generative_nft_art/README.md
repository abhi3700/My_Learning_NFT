# Generative NFT art

Create generative art as NFT

## Task

1. Create your own NFT collection
> - Here, the arts would be generated based on multiple layers/features/traits - face, eyes, ears, nose, mouth
> - The method followed is completely algorithmic using random trait generation.
<!-- TODO: There is another method which is based on AI -->
2. Create NFT metadata
> Here, images & its metadata would be uploaded into Pinata cloud (IPFS based).

3. Deploy NFT SC
4. Mint NFT

## Coding

1. Sign up for Pinata [here](https://www.pinata.cloud/)
2. Generate an API Key [here](https://app.pinata.cloud/keys)
   - Make sure the Admin button is selected to have access to all Pinata endpoints.
   - Copy the **PinataAPIKey** and the **SecretAPIKey** to your clipboard. We will be using this later.
3. Installed the required packages using `$ pip3 install -r requirements.txt`
4. Run `$ python3 trait_generate.py` & find the output images in the "../img/output" folder.

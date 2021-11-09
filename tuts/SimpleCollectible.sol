//SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import '@openzeppelin/contracts/utils/math/SafeMath.sol';
import "@openzeppelin/contracts/access/Ownable.sol";
import '@openzeppelin/contracts/utils/Context.sol';

/*
	@notice This NFT contract uses ERC721 standard
	References: https://www.youtube.com/watch?v=ZH_7nEIJDUY
	Changes:
		- `_setTokenURI` changed to `tokenURI` & `_baseURI`.
		- set cloud (like Firebase) URI as baseURI
		- add `nextTokenID` (optional: public or private) param for automatic increment of 
		    tokenID during minting.
*/
contract SimpleCollectible is ERC721, Ownable {
    using SafeMath for uint256;
    
	// gives the next available token ID
	uint256 public nextTokenID;

	constructor() ERC721("Doggie", "DOG") {}

	function _baseURI() internal pure override returns (string memory) {
        return "https://firebase.com/";
    }

	// mint new collectibles
	function createCollectibles() external returns (string memory) {
		uint256 newItemId = nextTokenID;
		_safeMint(_msgSender(), newItemId);
		nextTokenID = newItemId.add(1);

		return tokenURI(newItemId);
	}
}
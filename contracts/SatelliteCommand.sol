// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SatelliteCommand {
    address public satelliteOwner;
    mapping(address => bool) public authorizedGroundStations;

    constructor() {
        satelliteOwner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == satelliteOwner, "Not the owner");
        _;
    }

    modifier onlyAuthorized() {
        require(authorizedGroundStations[msg.sender], "Not authorized");
        _;
    }

    function authorizeGroundStation(address groundStation) public onlyOwner {
        authorizedGroundStations[groundStation] = true;
    }

    function issueCommand(string memory command) public onlyAuthorized {
        // Logic to execute command
    }
}

const { networks } = require("../truffle-config");

const SatelliteCommand = artifacts.require("SatelliteCommand");

module.exports = function(deployer) {
    deployer.deploy(SatelliteCommand);
};

const satelliteCommand = await SatelliteCommand.deployed(networks);

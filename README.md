# Satellite Communication Project

## Overview
This project aims to establish secure communication between a satellite and a ground station using encryption and blockchain technology.

## Directory Structure
- **/keys**: Contains RSA key pairs for the satellite and ground station.
- **/encryption**: Encryption logic using RSA and AES.
- **/blockchain**: Implements a basic blockchain to log commands.
- **/contracts**: Smart contracts for managing satellite commands.
- **/scripts**: Scripts for the satellite and ground station.
- **/data**: Telemetry data in JSON format.

## Installation
To install the required packages, run:
```bash
pip install -r requirements.txt
```

```bash
sudo apt update
sudo apt install nodejs npm
sudo npm install -g truffle
npm install -g ganache-cli
```
## Usage
### Ground Station
```bash
truffle init
truffle compile
truffle migrate
truffle deploy
```

```bash
truffle console --network development
```
/SatelliteCommunicationProject
│
├── /keys
│   ├── satellite_private_key.pem       # RSA private key for the satellite
│   ├── satellite_public_key.pem        # RSA public key for the satellite
│   ├── ground_station_private_key.pem  # RSA private key for the ground station
│   ├── ground_station_public_key.pem   # RSA public key for the ground station
│
├── /encryption
│   ├── rsa_encryption.py               # RSA encryption and decryption logic
│   ├── aes_encryption.py               # AES encryption and decryption logic for data
│
├── /blockchain
│   ├── blockchain.py                   # Blockchain logic for logging commands and data
│
├── /contracts
│   ├── SatelliteCommand.sol            # Smart contract to manage satellite commands
│
├── /scripts
│   ├── satellite.py                    # Satellite-side script to handle commands and encryption
│   ├── ground_station.py               # Ground station-side script to send encrypted commands
│
├── /data
│   ├── telemetry_data.json             # Telemetry data in JSON format
│
├── README.md                           # Project documentation
└── requirements.txt                    # Python package dependencies

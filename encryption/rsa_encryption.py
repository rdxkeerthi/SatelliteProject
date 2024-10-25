import os
from Crypto.PublicKey import RSA

# Ensure the directory exists
os.makedirs('../keys', exist_ok=True)

def generate_and_save_keys():
    # Generate keys for satellite
    satellite_key = RSA.generate(2048)
    with open('../keys/satellite_private_key.pem', 'wb') as f:
        f.write(satellite_key.export_key())
    with open('../keys/satellite_public_key.pem', 'wb') as f:
        f.write(satellite_key.publickey().export_key())

    # Generate keys for ground station
    gs_key = RSA.generate(2048)
    with open('../keys/ground_station_private_key.pem', 'wb') as f:
        f.write(gs_key.export_key())
    with open('../keys/ground_station_public_key.pem', 'wb') as f:
        f.write(gs_key.publickey().export_key())

generate_and_save_keys()

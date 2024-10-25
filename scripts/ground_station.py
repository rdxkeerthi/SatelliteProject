# /scripts/ground_station.py
from encryption.rsa_encryption import load_rsa_keys, rsa_encrypt
import json

private_key_path = 'keys/ground_station_private_key.pem'
public_key_path = 'keys/ground_station_public_key.pem'
private_key, public_key = load_rsa_keys(private_key_path, public_key_path)

def send_command(command):
    encrypted_command = rsa_encrypt(command, public_key)
    print(f"Sending Command: {encrypted_command}")
    # Logic to send the encrypted command to the satellite

if __name__ == "__main__":
    command = "Turn on the communication system"
    send_command(command)

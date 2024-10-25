# /scripts/satellite.py
from ..encryption.rsa_encryption import load_rsa_keys, rsa_decrypt
from encryption.rsa_encryption import load_rsa_keys, rsa_decrypt
import json

private_key_path = 'keys/satellite_private_key.pem'
public_key_path = 'keys/satellite_public_key.pem'
private_key, public_key = load_rsa_keys(private_key_path, public_key_path)

def receive_command(encrypted_command):
    decrypted_command = rsa_decrypt(encrypted_command, private_key)
    print(f"Received Command: {decrypted_command}")
    # Handle command execution logic here

if __name__ == "__main__":
    # Example usage
    encrypted_command = "..."  # This would be received from the ground station
    receive_command(encrypted_command)

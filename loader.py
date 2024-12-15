import os
import toml

def load_credentials():
    # Build the absolute path to the credentials.toml file
    credentials_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Spotify_ETL/credential.toml")
    
    # Load the credentials
    credentials = toml.load(credentials_path)
    return credentials
# 🎵 Spotify Playlist Data Pipeline 🎶

This project extracts metadata from a Spotify playlist using the Spotify Web API, processes the data, and stores it into MongoDB collections. It identifies duplicate records and logs every step of the pipeline for enhanced monitoring and debugging.

---

## 🌟 Features

- 🚀 **Data Extraction:** Extracts album, artist, and song metadata from Spotify playlists.
- 🛠️ **Data Processing:** Cleans and processes data with Pandas for consistency.
- 📂 **Dynamic MongoDB Insertion:** Inserts processed data dynamically into MongoDB collections.
- 🔍 **Duplicate Detection:** Identifies duplicate records for improved data quality.
- 📝 **Logging:** Implements structured logging for monitoring and debugging.

---

## 🧰 Prerequisites

Ensure you have the following installed:

- Python 3.7+
- MongoDB
- Required Python packages (see `requirements.txt`)

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ankitg028/Spotify-ETL-Pipeline.git
   cd Spotify-ETL-Pipeline
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Spotify API credentials:
   - Create a Spotify developer account and register an app to get `client_id` and `client_secret`.
   - Save these credentials in a JSON file named `credentials.json` in the following format:
     ```json
     {
         "client_id": "your_client_id",
         "client_secret": "your_client_secret"
     }
     ```

## 📂 Project Structure

```plaintext
.
├── app.log                     # Logs for application execution
├── main.py                     # Main script to run the pipeline
├── mongo.py                    # Script for MongoDB operations
├── loader.py                   # Script for loading credentials
├── credential.toml             # Credential for Spotify Connection
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
```

## 🚦 Usage

1. Run Mongo Compass:
    - Open Mongo Compass and set up a new connection.
    - Provide the connection details (host, port, database name) to connect to your MongoDB server.

2. Run the main script:
   ```bash
   python main.py
   ```

3. Set up your Spotify API credentials:

   - Create a Spotify developer account and register an app to get `client_id` and `client_secret`.
   - Save these credentials in a `credential.toml` file in the following format:
   ```bash
   [spotify]
   client_id = "your_client_id"
   client_secret = "your_client_secret"
   ```


## 🗄️ MongoDB Collections

The processed data is stored in the following collections:

- `song_df`: Contains song-related metadata.
- `artist_df`: Contains artist-related metadata.
- `album_df`: Contains album-related metadata.
- `song_artist_df`: Merged data of songs and their corresponding artists.
- `song_artist_album_df`: Final dataset combining song, artist, and album information.

## 🛡️ Logging
Logs are stored in `app.log` and include information such as:

- ✅ Pipeline Progress: Steps like data extraction, processing, and insertion.
- ⚠️ Warnings: Details of duplicate records.
- ❌ Errors: Any issues encountered during execution.

## Example Output

- Duplicate Records (if any):
  ```plaintext
  Duplicate Records:
  Song Name: ["Song1", "Song2"]
  ```

- Log Sample:
  ```plaintext
  2024-12-15 12:00:00 - INFO - Extracting playlist data from Spotify.
  2024-12-15 12:01:00 - INFO - Successfully extracted playlist data.
  2024-12-15 12:02:00 - INFO - Data processing completed successfully.
  2024-12-15 12:03:00 - INFO - song_df collection: Inserted 100 records successfully.
  ```

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.


Let me know if you'd like further improvements!

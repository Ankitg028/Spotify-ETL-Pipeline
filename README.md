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

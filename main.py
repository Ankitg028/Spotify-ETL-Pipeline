# Import Required Libraries
import logging
import pandas as pd
from spotipy import SpotifyClientCredentials, Spotify
from loader import load_credentials
from mongo import insert_records_dynamic

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def ms_to_mm_ss(ms):
    """Convert milliseconds to mm:ss format."""
    minutes, seconds = divmod(ms // 1000, 60)
    return f"{minutes:02}:{seconds:02}"


def extract_playlist_data(sp, playlist_uri):
    """Extract playlist data and return album, artist, and song lists."""
    logger.info("Extracting playlist data from Spotify.")
    results = sp.playlist_tracks(playlist_uri)

    album_list, artist_list, song_list = [], [], []

    try:
        for row in results['items']:
            track = row['track']

            # Album data
            album = track['album']
            album_list.append({
                'album_id': album['id'],
                'album_name': album['name'],
                'album_release_date': album['release_date'],
                'total_tracks': album['total_tracks'],
                'url': album['external_urls']['spotify']
            })

            # Artist data
            song_id = track['id']
            for artist in track['artists']:
                artist_list.append({
                    'song_id': song_id,
                    'artist_id': artist['id'],
                    'artist_name': artist['name'],
                    'external_url': artist['external_urls']['spotify']
                })

            # Song data
            song_list.append({
                'song_id': song_id,
                'song_name': track['name'],
                'duration': track['duration_ms'],
                'Url': track['external_urls']['spotify'],
                'Popularity': track['popularity'],
                'song_added': row['added_at'],
                'artist_id': album['artists'][0]['id'],
                'album_id': album['id']
            })

        logger.info("Successfully extracted playlist data.")
    except Exception as e:
        logger.error(f"Error occurred while extracting playlist data: {e}")
        raise e

    return album_list, artist_list, song_list


def process_dataframes(album_list, artist_list, song_list):
    """Process raw data into structured DataFrames."""
    logger.info("Processing data into DataFrames.")
    try:
        # Create DataFrames
        album_df = pd.DataFrame(album_list).drop_duplicates()
        artist_df = pd.DataFrame(artist_list)
        song_df = pd.DataFrame(song_list).drop_duplicates(subset=['song_id', 'song_name'])

        # Merge artist data with songs
        artist_group = artist_df.groupby('song_id')['artist_name'].apply(', '.join).reset_index()
        song_artist_df = pd.merge(song_df, artist_group, on='song_id', how='left')

        # Merge album data with songs
        song_artist_album_df = pd.merge(song_artist_df, album_df, on='album_id', how='left')

        # Format and clean data
        song_artist_album_df['duration'] = song_artist_album_df['duration'].apply(ms_to_mm_ss)
        song_artist_album_df['song_added'] = pd.to_datetime(song_artist_album_df['song_added']).astype(str)
        song_artist_album_df.drop(columns=['artist_id'], inplace=True)

        logger.info("Data processing completed successfully.")
    except Exception as e:
        logger.error(f"Error occurred during data processing: {e}")
        raise e

    return {
        "song_df": song_df,
        "artist_df": artist_df,
        "album_df": album_df,
        "song_artist_df": song_artist_df,
        "song_artist_album_df": song_artist_album_df,
    }


def identify_duplicates(df, subset=None):
    """Identify and log duplicate rows in a DataFrame."""
    logger.info("Checking for duplicate records.")
    duplicates = df[df.duplicated(subset=subset, keep=False)]
    if not duplicates.empty:
        logger.warning(f"Duplicate Records Found:\n{duplicates['song_name']}")
    else:
        logger.info("No duplicate records found.")


if __name__ == "__main__":
    logger.info("Application started.")

    try:
        # Load Spotify credentials
        credentials = load_credentials()
        client_credentials_manager = SpotifyClientCredentials(
            client_id=credentials["client_id"],
            client_secret=credentials["client_secret"]
        )
        sp = Spotify(client_credentials_manager=client_credentials_manager)

        # Spotify playlist URI
        playlist_link = "Playlist Link"  #Mention the Playlist Link
        playlist_uri = playlist_link.split("/")[-1].split("?")[0]

        # Extract playlist data
        album_list, artist_list, song_list = extract_playlist_data(sp, playlist_uri)

        # Process data into DataFrames
        dataframes = process_dataframes(album_list, artist_list, song_list)

        # Identify and log duplicates in the final DataFrame
        identify_duplicates(dataframes["song_artist_album_df"], subset=['song_id', 'song_name'])

        # Insert records into MongoDB
        insert_records_dynamic(dataframes)

        logger.info("Application completed successfully.")
    except Exception as e:
        logger.critical(f"Critical error occurred: {e}")
        raise

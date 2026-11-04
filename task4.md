# Task 4 — Persist the Playlist

**Were you able to save and restore the playlist?** Yes.

## Approach
The playlist is persisted to disk using Python's `pickle` module so it survives
restarts of the Flask application.

- **Saving:** Every time a song is added through the form, the full playlist is
  written to `playlist.pkl` using `pickle.dump()` with the file opened in binary
  write mode (`wb`).
- **Restoring:** When the application starts, it calls `pickle.load()` to read the
  playlist back from `playlist.pkl` (file opened in binary read mode, `rb`).
- **First run:** If `playlist.pkl` doesn't exist yet, the playlist is initialized
  as an empty list.

## Relevant code (`lab17.py`)
```python
PLAYLIST_FILE = os.path.join(os.path.dirname(__file__), 'playlist.pkl')

def load_playlist():
    if os.path.exists(PLAYLIST_FILE):
        with open(PLAYLIST_FILE, 'rb') as f:
            return pickle.load(f)
    return []

def save_playlist(playlist):
    with open(PLAYLIST_FILE, 'wb') as f:
        pickle.dump(playlist, f)

# Restore saved songs when the app starts.
playlist = load_playlist()
```
`save_playlist(playlist)` is called in the `/` route right after a new song is
appended to the list.

## Testing
I added several songs through the browser, stopped the Flask application, and
restarted it. The previously entered songs still appeared in the playlist,
confirming that saving and restoring both work correctly.

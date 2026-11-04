import os
import pickle

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
# A secret key is required for Flask-WTF forms (CSRF protection).
# Loaded from the environment (see .env, which is git-ignored) so the real
# secret is never committed. Falls back to a dev-only value for local use.
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-insecure-key')
bootstrap = Bootstrap5(app)

# Task 4 — file used to persist the playlist between runs.
PLAYLIST_FILE = os.path.join(os.path.dirname(__file__), 'playlist.pkl')


def load_playlist():
    """Task 4 — restore the playlist from disk, or start empty."""
    if os.path.exists(PLAYLIST_FILE):
        with open(PLAYLIST_FILE, 'rb') as f:
            return pickle.load(f)
    return []


def save_playlist(playlist):
    """Task 4 — save the playlist to disk so it survives a restart."""
    with open(PLAYLIST_FILE, 'wb') as f:
        pickle.dump(playlist, f)


# Load any previously saved songs when the app starts.
playlist = load_playlist()


class PlaylistForm(FlaskForm):
    # Task 1 — the song title field from the class slides.
    song_title = StringField('Song Title', validators=[DataRequired()])
    # Task 3 — additional fields following the same StringField pattern.
    artist = StringField('Artist', validators=[DataRequired()])
    genre = StringField('Genre')
    submit = SubmitField('Add to Playlist')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PlaylistForm()
    if form.validate_on_submit():
        # Task 3 — store the title along with the new information.
        playlist.append({
            'song_title': form.song_title.data,
            'artist': form.artist.data,
            'genre': form.genre.data,
        })
        # Task 4 — persist the updated playlist to disk.
        save_playlist(playlist)
        return redirect(url_for('view_playlist'))
    return render_template('lab17_index.html', form=form)


@app.route('/playlist')
def view_playlist():
    return render_template('vp.html', playlist=playlist)


if __name__ == '__main__':
    # Port 5000 is used by AirPlay Receiver on macOS, so use 5001.
    app.run(debug=True, port=5001)

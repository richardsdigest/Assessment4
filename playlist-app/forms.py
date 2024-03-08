"""Forms for playlist app."""

from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Playlist Name', validators=[DataRequired()])
    description = TextAreaField('Playlist Description')

class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Song Title', validators=[DataRequired()])
    artist = StringField('Artist Name', validators=[DataRequired()])



# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)

"""Usage: zptfyls.py USERNAME OAUTHTOKEN
"""

from docopt import docopt
import spotipy

if __name__ == '__main__':
    arguments = docopt(__doc__)

username = arguments['USERNAME']
token = arguments['OAUTHTOKEN']

print("Playlists by: ", username)

spotipy = spotipy.Spotify(auth=token)
results = spotipy.current_user_playlists()

print(results)

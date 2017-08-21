"""Usage: zptfyls.py OAUTHTOKEN

Obtain the oauth token manually from spotify, e.g. by visiting ->
https://developer.spotify.com/web-api/console/get-search-item/
and selecting the green button that says "GET OAUTH TOKEN"!
"""

from docopt import docopt, DocoptExit
import spotipy

if __name__ == '__main__':
    arguments = docopt(__doc__)

token = arguments['OAUTHTOKEN']

print("Spotift playlists with token: ", token)

spotipy = spotipy.Spotify(auth=token)
results = spotipy.current_user_playlists()

print(results)

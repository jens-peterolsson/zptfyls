"""Usage: zptfyls.py OUTPUT USERNAME OAUTHTOKEN

Output should be HTML or TEXT.

Obtain the oauth token manually from spotify, e.g. by visiting ->
https://developer.spotify.com/web-api/console/get-search-item/
and selecting the green button that says "GET OAUTH TOKEN"!
"""

from docopt import docopt
import spotipy
import zptfyReader

if __name__ == '__main__':
    arguments = docopt(__doc__)

token = arguments['OAUTHTOKEN']
username = arguments['USERNAME']
output = arguments['OUTPUT']

spotipy = spotipy.Spotify(auth=token)

offset = 0
total = 0

isHtml = output.lower() == 'html'

while total >= offset:

    result = spotipy.current_user_playlists(limit=10, offset=offset)
    offset += 10

    if total == 0:
        total = result['total']
        if(isHtml):
            print('<html><body><table>')

    for playlist in result['items']:
        if isHtml:
            zptfyReader.list_playlist_html(username, spotipy, playlist)
        else:
            zptfyReader.list_playlist_text(username, spotipy, playlist)

print('')
print('Total no of playlists: ' + str(total))
print('')

if isHtml:
    print('</table></body></html>')

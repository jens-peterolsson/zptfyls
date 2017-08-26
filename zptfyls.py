"""Usage: zptfyls.py USERNAME OAUTHTOKEN

Obtain the oauth token manually from spotify, e.g. by visiting ->
https://developer.spotify.com/web-api/console/get-search-item/
and selecting the green button that says "GET OAUTH TOKEN"!
"""

from docopt import docopt, DocoptExit
import spotipy

if __name__ == '__main__':
    arguments = docopt(__doc__)

token = arguments['OAUTHTOKEN']
username = arguments['USERNAME']

spotipy = spotipy.Spotify(auth=token)
result = spotipy.current_user_playlists()

# items, i varje item: colloborative, href, id, images, name, tracks
# limit: 50, next, previous, total

def list_playlist(playlist):

    print(playlist['name'] + ' (' + str(playlist['tracks']['total']) + ' tracks)')
    print('')

    if playlist['owner']['id'] != username:
        return

    trackItems = spotipy.user_playlist_tracks(username, playlist['id'])
    for item in trackItems['items']:
        print(item['track']['name'])

    print('')

for playlist in result['items']:
    list_playlist(playlist)

print('')
print('Total no of playlists: ' + str(result['total']))
print('Limit: ' + str(result['limit']))
print('')

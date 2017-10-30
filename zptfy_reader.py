# TODO remove duplicated code in playlist methods
# TODO playlist methods should return strings instead of printing

def _get_artists(artists):
    names = map(lambda v: v['name'], artists)
    return ', '.join(names)

def _is_relevant_playlist(username, playlist):

    if playlist['owner']['id'] != username:
        return False

    tracks_count = playlist['tracks']['total']
    if tracks_count == 0:
        return False

    return True

def list_playlist_html(username, spotipy, playlist):

    if not (_is_relevant_playlist(username, playlist)):
        return

    tracks_count = playlist['tracks']['total']
    if tracks_count == 0:
        return

    blank_table_row = '<tr><td>&nbsp;</td></tr>'

    print(blank_table_row)
    print('<tr><td><b>' + playlist['name'] + ' (' + str(playlist['tracks']['total']) + ' tracks)</b></td></tr>')
    print(blank_table_row)
    if(playlist['images']):
        print("<tr rowspan='2'><td><img src='" + playlist['images'][0]['url'] + "'/></td></tr>")
        print('')
        print(blank_table_row)

    track_items = spotipy.user_playlist_tracks(username, playlist['id'])

    ix = 1

    for item in track_items['items']:
        artist = _get_artists(item['track']['artists'])
        track_info = "%02d: %s - %s" % (ix, artist, item['track']['name'])
        print('<tr><td>' + track_info + '</td></tr>')
        ix += 1

def list_playlist_text(username, spotipy, playlist):

    if not (_is_relevant_playlist(username, playlist)):
        return

    print(playlist['name'] + ' (' + str(playlist['tracks']['total']) + ' tracks)')
    print('')

    track_items = spotipy.user_playlist_tracks(username, playlist['id'])

    ix = 1

    for item in track_items['items']:
        artist = _get_artists(item['track']['artists'])
        track_info = "%02d: %s - %s" % (ix, artist, item['track']['name'])
        print(track_info)
        ix += 1

    print('')

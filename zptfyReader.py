# TODO remove duplicated code in playlist methods
# TODO playlist methods should return strings instead of printing

def getArtists(artists):
    result = ""
    for artist in artists:
        if len(result) > 0:
            result += ", "
        result += artist['name']

    return result

def isRelevantPlaylist(username, playlist):

    if playlist['owner']['id'] != username:
        return False

    noOfTracks = playlist['tracks']['total']
    if noOfTracks == 0:
        return False

    return True

def list_playlist_html(username, spotipy, playlist):

    if not (isRelevantPlaylist(username, playlist)):
        return

    noOfTracks = playlist['tracks']['total']
    if noOfTracks == 0:
        return

    blankTableRow = '<tr><td>&nbsp;</td></tr>'

    print(blankTableRow)
    print('<tr><td><b>' + playlist['name'] + ' (' + str(playlist['tracks']['total']) + ' tracks)</b></td></tr>')
    print(blankTableRow)
    if(playlist['images']):
        print("<tr rowspan='2'><td><img src='" + playlist['images'][0]['url'] + "'/></td></tr>")
        print('')
        print(blankTableRow)

    trackItems = spotipy.user_playlist_tracks(username, playlist['id'])

    ix = 1

    for item in trackItems['items']:
        artist = getArtists(item['track']['artists'])
        trackInfo = "%02d: %s - %s" % (ix, artist, item['track']['name'])
        print('<tr><td>' + trackInfo + '</td></tr>')
        ix += 1

def list_playlist_text(username, spotipy, playlist):

    if not (isRelevantPlaylist(username, playlist)):
        return

    print(playlist['name'] + ' (' + str(playlist['tracks']['total']) + ' tracks)')
    print('')

    trackItems = spotipy.user_playlist_tracks(username, playlist['id'])

    ix = 1

    for item in trackItems['items']:
        artist = getArtists(item['track']['artists'])
        trackInfo = "%02d: %s - %s" % (ix, artist, item['track']['name'])
        print(trackInfo)
        ix += 1

    print('')

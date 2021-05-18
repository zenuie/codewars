def song_decoder(song):
    song = song.replace("WUB"," ")
    song = song.split()
    song = " ".join(song)
    print(song)
song_decoder("AWUBWUBWUBDD")
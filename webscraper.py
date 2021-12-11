import requests
import subprocess
from collections import defaultdict

class AlbumDownload:
    def __init__(self):
        self.count = defaultdict(int)

    def download_album(self, artist, album, directory):
        query = f"album-art \"{artist}\" --album \"{album}\""
        print(query)
        response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
        # remove \n
        res = response.decode('utf-8')[:-1]
        response = requests.get(res)
        file = open(f"{directory}/album{self.count[directory]}.png", 'wb')
        file.write(response.content)
        file.close()
        self.count[directory] += 1
    


# UNCOMMENT TO UPLOAD ALBUMS
# file = open("AlbumText/Folk.txt", 'r')
# albumDownload = AlbumDownload()
# file.readline()
# line = file.readline()
# while line != "":
#     print(f"LINE:{line}")
#     artistIndex = line.find(' - ')
#     print(artistIndex)
#     # albumIndex = line.find('\'', artistIndex + 3)
#     artist = line[:artistIndex]
#     print(artist)
#     album = line[artistIndex+3:-1]
#     print(album)
#     # print(album, artist)'
#     file.readline()
#     line = file.readline()
#     try:
#         albumDownload.download_album(artist, album, 'Folk')
#     except:
#         continue





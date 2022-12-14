from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLb-TC_fWtyN7obzvertlODVm9at-ykLPE')

for video in p.videos:
         print(video)
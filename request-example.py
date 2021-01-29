from playlisttitle import PlaylistGet

playl = PlaylistGet("https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10")
titles = playl.playlist_titles()

print(len(titles))
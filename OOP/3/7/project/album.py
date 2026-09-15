from project.song import Song

class Album:
    
    def __init__(self, name: str, *songs):
        self.name=name
        self.published=False
        self.songs=[song for song in songs]
    
    def add_song(self, song: Song):
        if song in self.songs:
            return f'Song is already in the album.'
        elif self.published:
            return f'Cannot add songs. Album is published.'
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'
    
    def remove_song(self, song_name: str):
        s = next((s for s in self.songs if s.name==song_name),None)
        if s:
            if self.published:
                return f'Cannot remove songs. Album is published.'
            else:
                self.songs.remove(s)
                return f'Removed song {song_name} from album {self.name}.'
        return f'Song is not in the album.'
    
    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published=True
        return f'Album {self.name} has been published.'
    
    def details(self):
        dt='\n== '.join(s.get_info() for s in self.songs)
        return f'Album {self.name}\n{dt}'
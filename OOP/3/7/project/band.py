from project.album import Album

class Band:
    def __init__(self,name: str):
        self.name=name
        self.albums=[]
    
    def add_album(self,album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'
    
    def remove_album(self,album_name: str):
        a=next((a for a in self.albums if a.name==album_name),None)
        if a:
            if a.published:
                return f'Album has been published. It cannot be removed.'
            else:
                self.albums.remove(a)
                return f'Album {a.name} has been removed.'
        return f'Album {album_name} is not found.'
    
    def details(self):
        dt='\n'.join(a.details() for a in self.albums)
        return f'Band {self.name}\n{dt}'
    
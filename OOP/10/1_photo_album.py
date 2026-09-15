from math import ceil

class PhotoAlbum:

    PAGES_SIZE=4

    def __init__(self,pages: int):
        self.pages=pages
        self.photos: list[list[str]] = [[] for _ in range(self.pages)]
    
    @classmethod
    def from_photos_count(cls,photos_count: int):
        return cls(ceil(photos_count/cls.PAGES_SIZE))
    
    def add_photo(self,label: str):
        for page in self.photos:
            if len(page)<self.PAGES_SIZE:
                page.append(label)
                return f'{label} photo added successfully on page {len(self.photos)} slot {len(page)}'
        return f'No more free slots'

    def display(self):

        separator='-'*11
        details=[separator]
        for page in self.photos:
            details.append(" ".join('[]' for _ in page))
            details.append(separator)
        return '\n'.join(details)
    



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eighat grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
            
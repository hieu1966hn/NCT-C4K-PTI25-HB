class MovieItem:
    def __init__(self, movie_id, title, release_date, image, rating=None, link=None):
        self.movie_id = movie_id
        self.title = title
        self.release_date = release_date
        self.image = image
        # Nếu không có rating thì mặc định bằng 0
        self.rating = float(rating) if rating else 0
        self.link = link
        
    def update(self, new_data:dict):
        for atttribute, value in new_data.items():
            # CHỈ KHI NÀO THUỘC TÍNH CÓ GIÁ TRỊ MỚI THÌ MỚI UPDATE
            if value: 
                setattr(self, atttribute, value)
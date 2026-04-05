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
            # Chỉ bỏ qua khi giá trị mới là None để vẫn update được 0, "", False.
            if value is not None: 
                setattr(self, atttribute, value)

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
        
## Tạo một vài bộ phim 
movie1 = MovieItem(1, "Avengers", "2022", None, 5, None)
movie2 = MovieItem(1, "Pacificrim", "2013", None, 5, None)
movie3 = MovieItem(1, "Interstella", "2013", None, 5, None)
    
## Khởi tạo kiểu dữ liệu danh sách phim: LIST
movies = [movie1, movie2, movie3]

# thêm phim mới: movies.append(movie4)
# cập nhật thông tin phim: movies[1].update(new_data)
# xóa một phần tử ở vị trí nào đó:  movies.pop(x) # vị trí thứ x
# Tìm kiếm theo tên: ... về nhà làm nốt. 


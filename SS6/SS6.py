import json

from SS4.models.movie_item import MovieItem
from SS4.models.movie_list import MovieDatabase


# class MovieItem:
#     def __init__(self, movie_id, title, release_date, image, rating=None, link=None):
#         self.movie_id = movie_id
#         self.title = title
#         self.release_date = release_date
#         self.image = image
#         # Nếu không có rating thì mặc định bằng 0
#         self.rating = float(rating) if rating else 0
#         self.link = link
        
#     def update(self, new_data:dict):
#         for atttribute, value in new_data.items():
#             # Chỉ bỏ qua khi giá trị mới là None để vẫn update được 0, "", False.
#             if value is not None: 
#                 setattr(self, atttribute, value)
# movie = MovieItem(1, "Avengers", "01/01/2001", "image_url")

## json.dump() ghi dữ liệu vào trong file JSON
# with open('SS6/movie.json', "w") as file:
#     json.dump(movie.__dict__, file) # chuyển đổi đối tượng movie => Dạng JSON và lưu vào file.



#### Đọc lại từ file đã viết
# with open('SS6/movie.json', "r") as file: 
#     data = json.load(file)  # Data hiện tại chỉ đang là KDL dict (chưa phải là MovieItem)
#     loaded_data = MovieItem(data["movie_id"],
#                             data["title"],
#                             data["release_date"],
#                             data["image"],
#                             )

# print(loaded_data.title) # 



##### Đọc nhiều đối tượng từ File vào danh sách đối tượng
# with open("SS6/movie.json","r") as file:
#     movie_data = json.load(file) # KQ: movie_data là list

# movie_item_list  = list()
# for movie_item_dict in movie_data:
#     movie = MovieItem(
#         movie_id=movie_item_dict["movie_id"],
#         title=movie_item_dict["title"],
#         release_date=movie_item_dict["release_date"],
#         image=movie_item_dict["image"],
#     )
#     movie_item_list.append(movie)
    
# ## In ra để kiểm tra
# for movie in movie_item_list: 
#     print(movie.title)
    
    
    
############ Test các thao tác với JSON
movieList1 = MovieDatabase()
movieList1.load_data()
print(movieList1)
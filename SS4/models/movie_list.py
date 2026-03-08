from SS4.models.movie_item import MovieItem
                
### Khởi tạo Lớp quản lý phim 
class MovieList:
    def __init__(self):
        # khởi tạo thuộc tính với kiểu dữ liệu: List
        self.movie_item_list = list()
    
    def get_first_item_by_title(self, movie_title):
        # Các câu lệnh để tìm và trả về phim theo tên
        # Trả về đối tượng MovieItem có title là title
        for movie_item in self.movie_item_list: 
            # Tìm thấy
            if movie_item.title == movie_title:
                return movie_item
            # Không tìm thấy
            return False
                
            

    def add_item(self, movie_dict): # một đối tượng chứa thông tin của phim 
        #### Dữ liệu truyền vào có thể như này
        # movie_dict = {
        #     "title": "Naruto",
        #     "release_date": 'Oct 2002',
        #     "image": 'naruto.jpg',
        #     "rating": 8.4,
        #     "link": 'https://myanimelist.net/anime/20/Naruto'
        # }
        
        
        # Các câu lệnh để thêm movie mới: Thêm một đối tượng MovieItem mới vào danh sách
        # Tạo đối tượng 
        movie_dict[id] = len(self.movie_item_list) # gán id cho movie mới (id = số lượng phần tử hiện có trong list)
        new_item = MovieItem(movie_id=movie_dict["id"],  # khởi tạo một object MovieItem. Hiểu chuyển tửu dữ liệu thô (dictionary -> Object (đối tượng))
                             title=movie_dict["title"],
                             release_date=movie_dict["release_date"],
                             image=movie_dict["image"],
                             rating=movie_dict["rating"],
                             link=movie_dict["link"])
        # Thêm vào danh sách phần tử
        self.movie_item_list.append(new_item)
        
    def edit_item(self, edit_title, new_dict):
        # Tìm movie theo tên edit_title
        # Thay thế thông tin của movie đã tìm được bằng thông tin mới new_dict
        pass
    
    def delete_item(self, delete_title):
        #Xóa movie theo tên delete_title
        pass
    
    
        

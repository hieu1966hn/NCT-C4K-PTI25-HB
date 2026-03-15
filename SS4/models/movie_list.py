import operator
from datetime import datetime

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
        movie_dict["id"] = len(self.movie_item_list) # gán id cho movie mới (id = số lượng phần tử hiện có trong list)
        new_item = MovieItem(movie_id=movie_dict["id"],  # khởi tạo một object MovieItem. Hiểu chuyển tửu dữ liệu thô (dictionary -> Object (đối tượng))
                             title=movie_dict["title"],
                             release_date=movie_dict["release_date"],
                             image=movie_dict["image"],
                             rating=movie_dict.get("rating"),
                             link=movie_dict.get("link"))
        # Thêm vào danh sách phần tử
        self.movie_item_list.append(new_item)
        return new_item
        
    def edit_item(self, edit_title, new_dict):
        # Tìm movie theo tên edit_title
        matched = self.get_first_item_by_title(edit_title) 
        # Sửa một đối tượng MovieItem có title là edit_title
        if matched: 
            matched.update(new_dict)
        
    
    def delete_item(self, delete_title):
        #Xóa movie theo tên delete_title
        # Tìm được phim đó đã 
        matched = self.get_first_item_by_title(delete_title) 
        if matched: 
            self.movie_item_list.remove(matched)
    
    def search_by_title(self, search_title) -> list[MovieItem]:
        ## Phương thức tìm kiếm tất cả các đối tượng MovieItem có title là search_title
        matched_items = [] # danh sách kết quả tìm kiếm có title là search title
        normalized_search = search_title.lower()
        for movie_item in self.movie_item_list: 
            if normalized_search in movie_item.title.lower():
                matched_items.append(movie_item)
        return matched_items
    
    # sắp xếp theo rating
    def sort_item_by_rating(self, top=None): # sắp xếp theo rating từ cao -> thấp
        self.movie_item_list = sorted(self.movie_item_list, 
                                      # hãy sx dựa trên thuộc tính "rating" của mỗi object
                                      key=operator.attrgetter('rating'), 
                                      reverse=True # đảo ngược thứ tự từ Cao -> Thấp
                                      )
        if top is not None:  # top là index, không phải số lượng || top=0 -> phần tử đứng đầu
            return self.movie_item_list[top]
        
    # Sắp xếp theo title
    def sort_item_by_title(self, top=None): 
        self.movie_item_list = sorted(self.movie_item_list,
                                      # Sx theo thứ tự chữ cái A -> Z
                                      key=operator.attrgetter('title')
                                      # Không cần reverse = True -> mặc định là tăng dần A->Z
                                      )
        if top is not None:
            return self.movie_item_list[top]
    
    # Sắp xếp theo release_date: Khó nhất vì dạng "Nov 2024" - "Jan 2010" => chuyển kiểu datetime
    def sort_item_by_date(self, top=None):
        self.movie_item_list = sorted(self.movie_item_list,
                                      # Viết tắt hàm
                                      # def get_date(x):
                                      #     return format_date(x.release_date)
                                      key=lambda x: format_date(x.release_date),
                                      reverse=True
                                      )
        if top is not None:
            return self.movie_item_list[top]

## Thoát hẳn khỏi class và khai báo hàm format date
def format_date(date_text):
    return datetime.strptime(date_text, '%b %Y')
    # strptime: Chuyển chuỗi => đối tượng ngày tháng
    # %b: tên tháng viết tắt - Nov, Feb, Jan
    # %Y: Năm 4 chữ số - 2024, 2025, 2026
    # VÍ DỤ CHUYỂN ĐỔI: "Nov 2024" => 2024-11-01 00:00:00 (Python tự đặt ngày bằng 1)
            
        
        
    
        
        
    
    
        

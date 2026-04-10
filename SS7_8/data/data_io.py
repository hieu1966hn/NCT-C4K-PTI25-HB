### Định nghĩa ra 2 hàm đọc và ghi file => vì thao tác đọc và ghi file sẽ 
# sử dụng nhiều lần trong chương trình quản lý nền => tách ra module riêng.

import json

def load_json_data():
    """
    Đọc dữ liệu
    """
    movie_dict_data = list()
    with open("SS7/data/data.json", "r") as json_in: 
        json_data = json.load(json_in)
    movie_dict_data.extend(json_data)
    return movie_dict_data ## trả về: danh sách chứa các bộ phim (list chứa các dict)

def write_json_data(json_data):
    """
    Viết dữ liệu: Nhận vào dữ liệu và viết dữ liệu đó vào file data.json.
    Khi có thao tác: Thêm/xóa/sửa thì sẽ gọi hàm này.
    """
    with open("SS7/data/data.json", "w") as json_out:
        json.dump(json_data, json_out)
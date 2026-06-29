from fastapi import FastAPI

app = FastAPI()

students = [
    "An",
    "Binh",
    "Cuong"
]

@app.get("/students")
def get_students():
    return students

# Phân tích/ Sửa lỗi 1: endpoint đặt tên chưa đún chuẩn restful.Khong nên dùng /getStudent mà nên dung /students.
# Phân tích/ Sửa lỗi: Không nên trả về chuỗi bằng cách nối string./Frontend sẽ nhận một chuỗi thay vì JSON list.

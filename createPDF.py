
from fpdf import FPDF

# Khởi tạo đối tượng PDF mới
# pdf = FPDF('P', 'mm', 'A4')
pdf = FPDF('P', 'mm', (75, 200))

# Thiết lập lề trái và lề phải
pdf.set_left_margin(4)
pdf.set_right_margin(4)

# Thiết lập thông tin hình ảnh
image_path = 'image.png'
image_width = 28  # kích thước chiều rộng cố định của hình ảnh


# Tính toán kích thước của hình ảnh để căn giữa trên trang
x = (pdf.w - image_width) / 2
y = 4

# Thêm trang mới
pdf.add_page()

# Thêm font chữ Unicode
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
pdf.add_font('DejaVu', 'I', 'DejaVuSans-Oblique.ttf', uni=True)
pdf.set_font('DejaVu', 'B', 16)

# Thêm nội dung biên lai
# Chèn hình ảnh vào PDF và căn giữa
pdf.image(image_path, x=x, y=y, w=image_width, h=0)
pdf.cell(0, 12, '', ln=1, align='C')
pdf.set_font('DejaVu', 'B', 11)
pdf.cell(0, 10, '1230 Tea Cần Thơ', ln=1, align='C')
pdf.set_font('DejaVu', '', 8)
pdf.multi_cell(
    0, 4, '271 Nguyễn Văn Linh, Long Tuyền, Bình Thủy, Cần Thơ', align='C')
pdf.set_font('DejaVu', '', 8)

pdf.cell(0, 6, '---------------------------------------', ln=1, align='C')
pdf.set_font('DejaVu', 'B', 11)
pdf.cell(0, 6, 'PHIẾU THANH TOÁN', ln=1, align='C')
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(0, 6, 'Số: HD1983912371831238129', ln=1, align='C')
pdf.set_font('DejaVu', '', 10)
pdf.cell(0, 6, 'Giao đi', ln=1, align='C')
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(20, 4, 'Thời gian: ', align='L', border=0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(0, 5, '10/03/2023 15:30', ln=1)
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(20, 4, 'Giờ ra: ', align='L', border=0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(0, 5, '10/03/2023 16:12', ln=1)
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(20, 4, 'Khách hàng: ', align='L', border=0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(0, 5, 'khách lẻ', ln=1)
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(20, 4, 'Nhân Viên: ', align='L', border=0)
pdf.set_font('DejaVu', '', 8)
pdf.cell(0, 5, 'Trần Hoàng Khôi Vip Pro', ln=1)

# Thiết lập thông số cho bảng
col_width = (75-10) / 7
row_height = 8

# Thiết lập kiểu nét đứt cho đường viền của bảng
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.1)

pdf.set_font('DejaVu', '', 7)

# Thiết lập lề trái và lề phải
pdf.set_left_margin(5)
pdf.set_right_margin(5)

# TBL Header
pdf.cell(col_width / 2, row_height, 'STT', border='B', align='L')
pdf.cell(col_width * 3, row_height, 'Tên S.Phẩm', border='B', align='C')
pdf.cell(col_width / 2, row_height, 'SL', border='B', align='C')
pdf.cell(col_width * 1.5, row_height, 'Đ.Giá', border='B', align='C')
pdf.cell(col_width * 1.5, row_height, 'T.Tiền', border='B', align='C')
pdf.ln(row_height)
for i in range(4):
    # TBL Content
    pdf.cell(col_width / 2, row_height, str(i+1), border='B', align='C')
    pdf.cell(col_width * 3, row_height,
             'Trà sửa Ô long', border='B', align='L')
    pdf.cell(col_width / 2, row_height, '1', border='B', align='C')
    pdf.cell(col_width * 1.5, row_height, '26.000', border='B', align='C')
    pdf.cell(col_width * 1.5, row_height, '26.000', border='B', align='C')
    pdf.ln(row_height)

# Thiết lập lề trái và lề phải
pdf.set_left_margin(4)
pdf.set_right_margin(4)
# Line space
pdf.cell(0, 2, '', ln=1, align='C')
# Line space


# Toltal Receipt

pdf.set_font('DejaVu', '', 8)
pdf.cell(0, 4, 'Tổng tiền: ', align='L', border=0)
pdf.cell(0, 5, '249.000', ln=1, align='R')
pdf.cell(20, 4, 'Khuyến mãi: ', align='L', border=0)
pdf.cell(0, 5, '0', ln=1, align='R')
pdf.set_font('DejaVu', 'B', 8)
pdf.cell(20, 4, 'Thanh toán: ', align='L', border=0)
pdf.cell(0, 5, '249.000', ln=1, align='R')
pdf.set_font('DejaVu', 'I', 7)
pdf.cell(0, 5, 'Hai trăm bốn mươi chín nghìn đồng', ln=1, align='R')
# pdf.set_font('DejaVu', 'I', 8)
pdf.set_font('DejaVu', '', 8)
pdf.cell(20, 4, 'Tiền khách trả: ', align='L', border=0)
pdf.cell(0, 5, '300.000', ln=1, align='R')
pdf.cell(20, 4, 'Tiền thối: ', align='L', border=0)
pdf.cell(0, 5, '51.000', ln=1, align='R')

# Line space
pdf.cell(0, 4, '', ln=1, align='C')
# Line space


pdf.set_font('DejaVu', '', 6)
# Footer Receipt
pdf.cell(0, 2, 'Nhượng quyền: 0292 888 1230 | Đặt hàng: 0292 999 1230',
         align='C', border=0)

# Lưu file PDF
pdf.output('createPDF.pdf')

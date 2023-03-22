
from fpdf import FPDF
import math


# def rounded_rect(pdf, x, y, w, h, r, img):
#     pdf.set_xy(x, y)
#     pdf.cell(w, h, '', 0, 0, '', img)
#     pdf.rounded_rect(x, y, w, h, r)

class ROUND_PDF(FPDF):
    def rounded_cell(self, w, h=0, txt='', border=0, ln=0, align='', fill=False, link='', radius=1, corners=(1, 2, 3, 4), cellspacing=1):
        style = 'S'
        if fill and border:
            style = 'FD'
        elif fill:
            style = 'F'
        self.rounded_rect(self.get_x() + (cellspacing / 2.0),
                          self.get_y() + (cellspacing / 2.0),
                          w - cellspacing, h, radius, corners, style)
        self.cell(w, h + cellspacing, txt, 0, ln, align, False, link)

    def rounded_rect(self, x, y, w, h, r, corners=(1, 2, 3, 4), style=''):
        k = self.k
        hp = self.h
        if style == 'F':
            op = 'f'
        elif style == 'FD' or style == 'DF':
            op = 'B'
        else:
            op = 'S'
        my_arc = 4/3 * (math.sqrt(2) - 1)
        self._out('%.2F %.2F m' % ((x+r)*k, (hp-y)*k))
        xc = x+w-r
        yc = y+r
        self._out('%.2F %.2F l' % (xc*k, (hp-y)*k))
        if 2 not in corners:
            self._out('%.2F %.2F l' % ((x+w)*k, (hp-y)*k))
        else:
            self._arc(xc + r*my_arc, yc - r, xc + r, yc - r*my_arc, xc + r, yc)
        xc = x+w-r
        yc = y+h-r
        self._out('%.2F %.2F l' % ((x+w)*k, (hp-yc)*k))
        if 3 not in corners:
            self._out('%.2F %.2F l' % ((x+w)*k, (hp-(y+h))*k))
        else:
            self._arc(xc + r, yc + r*my_arc, xc + r*my_arc, yc + r, xc, yc + r)
        xc = x+r
        yc = y+h-r
        self._out('%.2F %.2F l' % (xc*k, (hp-(y+h))*k))
        if 4 not in corners:
            self._out('%.2F %.2F l' % ((x)*k, (hp-(y+h))*k))
        else:
            self._arc(xc - r*my_arc, yc + r, xc - r, yc + r*my_arc, xc - r, yc)
        xc = x+r
        yc = y+r
        self._out('%.2F %.2F l' % ((x)*k, (hp-yc)*k))
        if 1 not in corners:
            self._out('%.2F %.2F l' % ((x)*k, (hp-y)*k))
            self._out('%.2F %.2F l' % ((x+r)*k, (hp-y)*k))
        else:
            self._arc(xc - r, yc - r*my_arc, xc - r*my_arc, yc - r, xc, yc - r)
        self._out(op)

    def _arc(self, x1, y1, x2, y2, x3, y3):
        h = self.h
        self._out('%.2F %.2F %.2F %.2F %.2F %.2F c ' % (
            x1*self.k, (h-y1)*self.k, x2*self.k, (h-y2)*self.k, x3*self.k, (h-y3)*self.k))


# Khởi tạo đối tượng PDF mới
# pdf = FPDF('P', 'mm', 'A4')
pdf = ROUND_PDF('P', 'mm', (50, 30))

# Thiết lập lề trái và lề phải
pdf.set_left_margin(4)
pdf.set_right_margin(4)
pdf.set_top_margin(4)
# Set margin bottom = 25 mm
pdf.set_auto_page_break(auto=True, margin=4)

# Thêm trang mới
pdf.add_page()

pdf.rounded_rect(3, 3, 44, 24, 2)

# Thêm font chữ Unicode
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
pdf.add_font('DejaVu', 'I', 'DejaVuSans-Oblique.ttf', uni=True)


# Vẽ border cho toàn bộ trang
# pdf.rect(3, 3, pdf.w - 6, pdf.h - 6, 'D')

# Thêm nội dung biên lai
# Chèn hình ảnh vào PDF và căn giữa
pdf.set_font('DejaVu', 'B', 6)
pdf.cell(0, 4, '1230 Tea Cần Thơ', ln=1)
pdf.set_font('DejaVu', 'B', 5)
pdf.cell(0, 3, 'Trà sữa ô long', align='L')
pdf.cell(0, 3, '1', align='R', ln=1)
pdf.set_font('DejaVu', '', 4)

pdf.set_left_margin(5)
pdf.cell(0, 2, '- Khoai dẻo', align='L')
pdf.cell(0, 2, '1', ln=1, align='R')
pdf.cell(0, 2, '- Trân châu trắng', align='L')
pdf.cell(0, 2, '1', ln=1, align='R')
pdf.cell(0, 2, '- Khoai tây', align='L')
pdf.cell(0, 2, '1', ln=1, align='R')
pdf.cell(0, 2, '- Gà hầm thuốc bắc', align='L')
pdf.set_left_margin(4)
pdf.cell(0, 2, '1', ln=1, align='R')


pdf.set_font('DejaVu', '', 5)
pdf.cell(0, 2.5, 'Ghi chú: 70% đá, xử nữ', ln=1, align='L')
pdf.cell(0, 2.5, 'B23/2: 10:20 13/3/2023', align='L')
pdf.set_font('DejaVu', 'B', 5)
pdf.cell(0, 2.5, '23,000 VND', align='R', ln=1)
pdf.set_font('DejaVu', '', 5)
# Footer Receipt

# pdf.cell(0, 1, 'Nhượng quyền: 0292 888 1230 | Đặt hàng: 0292 999 1230',
#          align='C', border=0)

# Lưu file PDF
pdf.output('createPDFLabel.pdf')

from fpdf import FPDF
import math

from fpdf import FPDF


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


# Tao PDF moi
pdf = ROUND_PDF()
pdf.add_page()

# Vẽ hình chữ nhật bo tròn 4 góc
pdf.rounded_rect(5, 5, 50, 30, 2)

# Lưu file PDF
pdf.output("borderRadius.pdf")

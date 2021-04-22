from reportlab.pdfgen import canvas
# pdf 纸张类型
from reportlab.lib.pagesizes import letter,A4
#距离
from reportlab.lib.units import inch,cm
# 更换字体
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


pdfmetrics.registerFont(TTFont('Song', r'E:\PythonObject\python提升\ascension\ascension\python\excel_python\STSONG.ttf'))

if __name__ == '__main__':
    w, h = A4
    pdf_file = canvas.Canvas(r'E:/test.pdf', pagesize=A4)
    pdf_file.setFont('Song', 12)

    # 设置起始位置，边距
    pdf_file.translate(inch, inch)
    # 画笔线条颜色
    pdf_file.setStrokeColorRGB(0.2, 0.5, 0.3)
    # 画线
    pdf_file.drawString(0, h - 2 * inch, 'python reportlab 应用')
    pdf_file.line(0, h - (2.1 * inch), w - (2 * inch), h - (2.1 * inch))
    # 画矩形
    pdf_file.setFillColorRGB(0, 0, 1)
    pdf_file.rect(0, h - (3.2 * inch), 2 * inch, inch)
    # showPage : 关闭当前页，保存
    pdf_file.showPage()
    pdf_file.save()




from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.lib import colors

pdfmetrics.registerFont(TTFont('song', r'E:\PythonObject\python提升\ascension\ascension\python\excel_python\STSONG.ttf'))


doc = SimpleDocTemplate(r'E:/test.pdf', pagesize = letter)
width, height = letter

styles = getSampleStyleSheet()
title = styles['Title']
title.fontName = 'song'

element = []
element.append(Paragraph('Python webserver 依赖库', style = title))
data = [['依赖名', '版本', '描述'],
        ['requests', '2.22.0', '请求'],
        ['Flask', '1.0.2', 'web框架'],
        ['Flask-SocketIO', '3.3.2', 'Websocket'],
        ['Python','3.6.5',None]]
ct = [('FONTNAME', (0, 0), (-1, -1), 'song'),
      ('SPAN', (-2, -1), (-1, -1)),
      ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
      # ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
      ('FONTSIZE', (0, 0), (-1, 0), 11),
      # ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.86, 0.86, 0.86)),
      ('LINEBELOW', (0, 0), (-1, 0), 1, colors.Color(0.27, 0.5, 0.7)),
      ('LINEABOVE', (0, -1), (-1, -1), 1, colors.Color(0.27, 0.5, 0.7))]


element.append(Table(data = data, colWidths = (width - 2 * inch)/len(data[0]), style = ct))

doc.build(element)





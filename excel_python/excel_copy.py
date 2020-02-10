from xlutils.copy import copy
import xlrd,xlwt

def main(path):
    try:
        #打开excel 工作簿
        open_excel = xlrd.open_workbook(path)
        open_sheet = open_excel.sheet_by_index(0)

        #copy
        new_excel = copy(open_excel)
        new_sheet = new_excel.get_sheet(0)

        style = xlwt.XFStyle()

        #字体
        font = xlwt.Font()
        font.name = '微软雅黑'
        font.bold = True
        font.height = 360
        style.font = font

        #边框
        borders = xlwt.Borders()
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        style.borders = borders

        #对齐
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.HORZ_CENTER
        style.alignment = alignment

        new_sheet.write(2,2,'szhu9903', style)
        new_excel.save('E:\\test_excel\\test_excel1.xls')

        return True
    except Exception as er:
        print(er)
        return False

if __name__ == '__main__':
    main('E:\\test_excel\\test_excel.xlsx')


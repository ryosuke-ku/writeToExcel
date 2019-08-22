import xlwt
 
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

for i in range(5): 
    sheet1.write(i, 0, 100)
    # sheet1.write(0, 1, 200)
    # sheet1.write(1, 0, 300)
    # sheet1.write(1, 1, 400)
 
book.save('test.xls')
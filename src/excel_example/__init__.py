import org.apache.poi.hssf.usermodel.HSSFWorkbook as Workbook
from org.apache.poi.ss.usermodel import Font, CellStyle, IndexedColors

def main():
    
    #This is just a silly Excel (.xls) file generator.

    f = open("computer-parts.xls","w")
    wb = Workbook()
    
    styles = create_styles(wb)

    sheet = wb.createSheet("Computer Parts")
    row = sheet.createRow(0)
    row.createCell(0).setCellValue("Part")
    row.createCell(1).setCellValue("Price")
    row.createCell(2).setCellValue("Quantity")
    row.createCell(3).setCellValue("Shipping")
    row.createCell(4).setCellValue("Total Price")
    for cell in row:
        cell.setCellStyle(styles['bold_header'])
    row = sheet.createRow(1)
    row.createCell(0).setCellValue("Processor")
    row.createCell(1).setCellValue(298.99)
    row.createCell(2).setCellValue(1)
    row.createCell(3).setCellValue(0)
    row = sheet.createRow(2)
    row.createCell(0).setCellValue("Heatsink/Fan")
    row.createCell(1).setCellValue(30.00)
    row.createCell(2).setCellValue(1)
    row.createCell(3).setCellValue(3.99)
    row = sheet.createRow(3)
    row.createCell(0).setCellValue("Motherboard")
    row.createCell(1).setCellValue(150.00)
    row.createCell(2).setCellValue(1)
    row.createCell(3).setCellValue(0)
    row = sheet.createRow(4)
    row.createCell(0).setCellValue("Case")
    row.createCell(1).setCellValue(100.00)
    row.createCell(2).setCellValue(1)
    row.createCell(3).setCellValue(15.00)
    row = sheet.createRow(5)
    row.createCell(0).setCellValue("Memory")
    row.createCell(1).setCellValue(79.99)
    row.createCell(2).setCellValue(1)
    row.createCell(3).setCellValue(0)
    row = sheet.createRow(6)
    row.createCell(0).setCellValue("Video Card")
    row.createCell(1).setCellValue(120.00)
    row.createCell(2).setCellValue(1)
    row.createCell(3).setCellValue(0)
    row = sheet.createRow(7)
    row.createCell(0).setCellValue("Hard Drive")
    row.createCell(1).setCellValue(99.99)
    row.createCell(2).setCellValue(3)
    row.createCell(3).setCellValue(0)
    row = sheet.createRow(8)
    row.createCell(0).setCellValue("Power Supply")
    row.createCell(1).setCellValue(89.99)
    row.createCell(2).setCellValue(1)
    row.createCell(3).setCellValue(0)
    for row_num in range(1,9):
        row = sheet.getRow(row_num)
        row.getCell(1).setCellStyle(styles['currency'])
        row.getCell(3).setCellStyle(styles['currency'])
        row.createCell(4).setCellFormula("(B%d*C%d)+D%d" % ((row_num+1,)*3))
        row.getCell(4).setCellStyle(styles['currency'])

    row = sheet.createRow(10)
    row.createCell(0).setCellValue("Total")
    row.getCell(0).setCellStyle(styles["bold"])
    row.createCell(4).setCellFormula("sum(E2:E9)")
    row.getCell(4).setCellStyle(styles["currency"])

    for col_num in range(0,10):
        sheet.autoSizeColumn(col_num)
    

    wb.write(f)
    f.close()

def create_styles(workbook):
    styles = {} #style name -> CellStyle
    
    bold_font = workbook.createFont()
    bold_font.setBoldweight(Font.BOLDWEIGHT_BOLD)

    bold = workbook.createCellStyle()
    bold.setFont(bold_font)
    styles["bold"] = bold

    bold_header = workbook.createCellStyle()
    bold_header.setFont(bold_font)
    bold_header.setAlignment(CellStyle.ALIGN_CENTER)
    bold_header.setFillForegroundColor(IndexedColors.GREY_40_PERCENT.getIndex())
    bold_header.setFillPattern(CellStyle.SOLID_FOREGROUND)
    bold_header.setWrapText(False)
    styles["bold_header"] = bold_header

    currency = workbook.createCellStyle()
    #data format 8 is for currency.
    #See: http://poi.apache.org/apidocs/org/apache/poi/hssf/usermodel/HSSFDataFormat.html
    currency.setDataFormat(8)
    styles['currency'] = currency

    return styles

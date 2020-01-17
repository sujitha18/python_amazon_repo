import pandas as pd
from resources.data import constant_variable as cv
def get_sheet(sheet):
    data=pd.read_excel(cv.EXCEL_PATH,sheet_name=sheet)
    return data
def get_value(sheet,rowname,columnname):
    data=pd.read_excel(cv.EXCEL_PATH,sheet_name=sheet,index_col="TestCaseId")
    value=data.loc[rowname,columnname]
    return value
def get_total_number_rows(sheet):
    data=get_sheet(cv.EXCEL_PATH,sheet)
    total_row=data.shape[0]
    return total_row
def write_to_excel(sheet,row_number,column_name,value_to_write):
    data=get_sheet(cv.EXCEL_PATH,sheet)
    data.loc[row_number,column_name]=value_to_write
    write=pd.ExcelWriter(cv.EXCEL_PATH)
    data.to_excel(write,sheet_name=sheet)
    write.save()
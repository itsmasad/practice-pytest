# import pytest
# import time
# from testData import data

# @pytest.mark.smock()
# def test_login(setUp):
#     driver = setUp
#     driver.get("https://www.google.com/")
#     driver.implicitly_wait
#     driver.maximize_window
 
@pytest.mark.parametrize("name,age",data)
def test_para(name,age):
    print(name+' '+age)

import openpyxl.workbook
import pytest
import openpyxl

def read_data():
    workbook = openpyxl.load_workbook("workbook.xlsx")
    sheet = workbook.active
    test_data = []
    for row in sheet.iter_rows(min_row=2,min_col=1,max_row=4,max_col=2,values_only=True):
        username,password = row
        test_data.append((username,password))
    return test_data


@pytest.mark.parametrize("Username,Password",read_data())
def test_Para(Username,Password):
    print(f'{Username} & {Password}')
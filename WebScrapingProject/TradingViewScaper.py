from GetChromeDriver import Get_Driver,OpenChromeDriver,OpenNewTabs,Find_Element_By_XPATH
from selenium.webdriver.common.by import By
import time

def Price (delay,Currencys):
    
    driver = Get_Driver()
    classorid_specifications = './/span[@class = "last-JWoJqCpY js-symbol-last"]'
    url = f'https://www.tradingview.com/symbols/{Currencys[0]}/?exchange=FX'
    OpenChromeDriver(driver,url)
    item_0 = Find_Element_By_XPATH(driver,classorid_specifications)
    time.sleep(delay)
    
    for items in range (1,len(Currencys)):

        url = f'https://www.tradingview.com/symbols/{Currencys[items]}/?exchange=FX'
        
        driver = OpenNewTabs(driver,items,url)

        find = Find_Element_By_XPATH(driver,classorid_specifications)

        if items == 1:
            item_1 = find
            time.sleep(delay)

        elif items == 2:
            item_2 = find
            time.sleep(delay)

        elif items == 3:
            item_3 = find
            time.sleep(delay)

        elif items == 4:
            item_4 = find
            time.sleep(delay)
            
        elif items == 5:
            item_5 = find
            time.sleep(delay)

        elif items == 6:
            item_6 = find
            time.sleep(delay)

        elif items == 7:
            item_7 = find
            time.sleep(delay)

        elif items == 8:
            item_8 = find
            time.sleep(delay)
    return [driver,[item_0,item_1,item_2,item_3,item_4,item_5,item_6,item_7,item_8]]
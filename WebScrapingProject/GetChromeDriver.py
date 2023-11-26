from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from BrowsFiles import browse_file

# Use when we want to configure chrome web driver

def Get_Driver ():
    try:
        path = r"C:\Users\Surface\Desktop\financial Trader\WebScrapingProject\chromedriver-win64\chromedriver.exe"
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service)
    except:
        path = browse_file()
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service)
    
    return driver

# Use when we want to open chrome web driver

def OpenChromeDriver (driver,url):

    return driver.get(url)

# Use when we want to open multiple tabs on chrome web driver

def OpenNewTabs (driver,itemnumber,Url): 
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[itemnumber])
    driver.get(Url)
    return driver

# Use when we want to choose tag,classorid,classoridvalue by XPATH to find html elements in page 

def Find_Element_By_XPATH (driver,specifications):
    
    Result = driver.find_element(By.XPATH, specifications)
    
    return Result
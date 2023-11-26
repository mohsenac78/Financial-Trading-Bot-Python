from GetChromeDriver import Get_Driver,OpenChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from ClassificationCards import ClassificationCards
from ClassificationSymboles import ClassificationSymboles

#inter './MetaTrader5_automation/Scripts/activate' in terminal when click on F5
#It gave the error, fix the problem using the following method
#To fix the error, you need to change the PowerShell execution policy to remotesigned
#Open the Start Menu on Windows and search for powershell and right-click on it. Click on "run as administrator"
#Type the following command in the PowerShell admin window to change the execution policy:
#set-executionpolicy remotesigned
#You will be prompted to accept the change, type A(Yes to all), and press ENTER on your keyboard to allow the change.
#Then enter this code './MetaTrader5_automation/Scripts/activate' in terminal
#Whenever you want to disable the virtual environment, use the 'deactivate' command.

#The best way is to search for the above term in the search field and place '>python: Select Interpreter' 
#and browse the path of virtual environment and select python.exe file in Scripts folder.
#Then you can select Terminal from the top toolbar and open a new terminal.


def Login (log_url,log_user,log_pass):
    driver = Get_Driver()
    OpenChromeDriver (driver,log_url)
    driver.find_element("name", "user_name").send_keys(log_user)
    driver.find_element("name", "user_password").send_keys(log_pass)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    return driver


def Refresh (driver,web_url,classorid,classoridvalue):
    driver.get(web_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    results = driver.find_elements(By.XPATH, f"//*[@{classorid}='{classoridvalue}']")
       
    mainlist =list()
    for result in results:
        text = result.text.split()
        mainlist.append(text)
        
    return mainlist


def CustomizeFoSignals (Login_driver,weburl,classorid,classoridvalue):
    
    results = Refresh(Login_driver,weburl,classorid,classoridvalue)
    Classification_Result = ClassificationCards(results)
    final_list = ClassificationSymboles(Classification_Result)
    # print(final_list)
    return final_list
        
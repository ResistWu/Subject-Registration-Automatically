from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def task():
    #openLoginWindow
    driver = webdriver.Chrome()
    driver.get('https://www38.polyu.edu.hk/eStudent/login.jsf')

    #Login
    elem = driver.find_element_by_name("username")
    elem.send_keys("")
    elem = driver.find_element_by_name("j_password")
    elem.send_keys("")
    driver.find_element_by_id("").click()

    #EnterSubjectRegistration
    driver.find_element_by_xpath("//a[contains(@href,'/eStudent/secure/my-subject-registration/subject-register-select-acad-year-sem.jsf')]").click()

    #SelectYear
    Select(driver.find_element_by_id("mainForm:yearSemDropDown")).select_by_value("1735")
    driver.find_element_by_id("mainForm:nextButton").click()

    #JudgeSubjectExist



    #EnterSubjectCode
    elem = driver.find_element_by_id("mainForm:basicSearchSubjectCode")
    elem.send_keys("COMP5122")
    #SearchSubject
    driver.find_element_by_id("mainForm:basicSearchButton").click()
    #AddSubject
    driver.find_element_by_id("mainForm:basicSearchTable:0:j_id140").click()
    #ClickLittleSquare
    driver.find_element_by_id("mainForm:ComponentTable:0:j_id138").click()
    #AddToCart
    driver.find_element_by_id("mainForm:selectButton").click()
    #ProceedtoPreview
    driver.find_element_by_id("mainForm:confirmButton").click()
    #LastConfirm
    driver.find_element_by_id("mainForm:confirmButton").click()

#TimeLoop
def timedTask():
    while True:
        task()
        time.sleep(60)

#Main
if __name__ == '__main__':
    timedTask()
import json

from playwright.sync_api import Page, expect
from Pages.loginPage import Loginpage
from Pages.homePage import Homepage
from utils.readingJson import readingJSONData


credentials="testData\credentials.json"


def test_validLogin(page:Page,home_Page):
    
    home_Page.launchAutomationExercisePage()
    loginFunctions=Loginpage(page) #As cnstructor has parameter page in it,here also we need to pass page
    loginFunctions.clickOnLoginLink()
    # with open("testData\credentials.json") as f:
    #     testData=json.load(f)
    # print(testData)
    testData=readingJSONData(credentials)
    loginFunctions.enterEmailID(testData["username"])
    loginFunctions.enterPassword(testData["password"])
    loginFunctions.clickOnLoginBtn()

    # 1.create varidable & provide file location
    # 2.create a code to handle json file, mention path inside open and save in one varibale f
    # 3.so here first will open a file and then load and save in variable
    
   

    
    
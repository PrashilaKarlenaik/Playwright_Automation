import json
import csv
import os

from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from Pages.loginPage import Loginpage
from Pages.homePage import Homepage
from utils.readingCSV import readdatafromCSV
from utils.readingJson import readJSONData


#calling method readingJSONData from utreadingJson.py and passing file location as parameter and saving the returned data in variable testData
credentials="testData\\credentials.json"
testData=readJSONData(credentials)
credentialsCSV="testData\\sampleCsvdata.csv"
testDataCSV=readdatafromCSV(credentialsCSV)


def test_validLogin(page:Page,home_Page: Homepage):
    
    home_Page.launchAutomationExercisePage()
    page.screenshot(path="screenshots\\homePage.png")
    loginFunctions=Loginpage(page) #As cnstructor has parameter page in it,here also we need to pass page
    loginFunctions.clickOnLoginLink()
    page.screenshot(path="screenshots\\loginPage.png")
    # print(testData)
    loginFunctions.enterEmailID(testData["username"])
    loginFunctions.enterPassword(testData["password"])
    loginFunctions.clickOnLoginBtn()

#Below code is not working because we are not able to read data from .env file,so we need to install python-dotenv package and then we can use below code to read data from .env file
# def test_getDatafromEnv():
#     load_dotenv() #this will load the .env file and make the data available as environment variables
#     userName= os.getenv("username")
#     passWord=os.getenv("password")
#     print("Reading below data from .env file")
#     print(userName)
#     print(passWord)

def test_writingDataIntoCSV():
    with open("testData\\sampleCsvdata.csv", mode="w") as file:
        writer=csv.DictWriter(file,fieldnames=["username","password"])
        writer.writeheader()
        writer.writerow({"username":"testuser1",
                         "password":"testpass1"})        
                                                   

 



    
   

    
    
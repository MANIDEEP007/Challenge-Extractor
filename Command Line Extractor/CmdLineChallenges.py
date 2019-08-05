#Paduchuri Manideep
#This is completely for Educational Purpose. Don't misuse it
'''Needed Modules - urlib, BeautifulSoupm selenium'''
import urllib.request as url
from time import sleep
from bs4 import BeautifulSoup as bs
from selenium import webdriver

#Techgig Variables
TECHGIG_PAGE_URL = "https://www.techgig.com/challenge"
TECHGIG_PAGE = url.urlopen(TECHGIG_PAGE_URL)
TECHGIG_PARSER = bs(TECHGIG_PAGE, 'html.parser')
TECHGIG_HEADING = []
TECHGIG_COMPANY = []
TECHGIG_END_DATE = []
TECHGIG_TEST_TYPE = []
#End of Techgig Variables

'''HackerEarth Variables'''
#Live Challenge Variables
HE_LIVE_COMPANY = []
HE_LIVE_TYPE = []
HE_LIVE_NAME = []
#Upcoming Challenge Variables
HE_UP_COMPANY = []
HE_UP_TYPE = []
HE_UP_NAME = []
HE_UP_DATE = []
'''End of HackerEarth Variables'''

def techgig_extractor():
    '''Function to extract Techgig Challenge Details'''
    techgig_cont = TECHGIG_PARSER.find("div", attrs={'id':'live-contest-listing'})
    techgig_challenges = techgig_cont.find_all("div", attrs={'class':'contest-box'})
    for techgig_challenge in techgig_challenges:
        TECHGIG_HEADING.append(techgig_challenge.findChildren("h3")[0].text)
        techgig_company_tag = techgig_challenge.find("div", attrs={'class':'company-content'})
        techgig_company_text = techgig_company_tag.findChildren("p")[0].text
        TECHGIG_COMPANY.append(techgig_company_text.split("by")[1].strip())
        techgig_dd0_tag = techgig_challenge.findChildren("dl", \
            attrs={'class':'description-list'})[0]
        techgig_date_tag = techgig_dd0_tag.findChildren("dd")[1]
        TECHGIG_END_DATE.append(techgig_date_tag.text)
        techgig_dd_tag = techgig_challenge.findChildren("dl", attrs={'class':'description-list'})[1]
        techgig_type_tag = techgig_dd_tag.findChildren("dd")[0]
        TECHGIG_TEST_TYPE.append(techgig_type_tag.text)
    print("\nBelow are the Techgig Challenges:\n")
    print_techgig()

def print_techgig():
    '''Function to print Techgig Challenges'''
    print("Name of Challenge - Company Name - End Date - Test Type")
    for index in range(0, len(TECHGIG_HEADING)):
        print(TECHGIG_HEADING[index], end=" - ")
        print(TECHGIG_COMPANY[index], end=" - ")
        print(TECHGIG_END_DATE[index], end=" - ")
        print(TECHGIG_TEST_TYPE[index])

def he_extractor(live=1, upcoming=1):
    '''Function to extract HackerEarth Live Challenges on Command Line'''
    he_driver = webdriver.Chrome('/etc/chromium-browser/chromedriver')
    he_driver.get('https://www.hackerearth.com/challenges/')
    he_driver.maximize_window()
    sleep(3)
    if live == 1:
        for i in he_driver.find_element_by_css_selector(".ongoing").\
             find_elements_by_css_selector(".challenge-card-modern"):
            try: #If company name is not Mentioned
                HE_LIVE_COMPANY.append(i.find_element_by_css_selector(".company-details").text)
            except AttributeError:
                HE_LIVE_COMPANY.append("NA")
            HE_LIVE_TYPE.append(i.find_element_by_css_selector(".challenge-type").text)
            HE_LIVE_NAME.append(i.find_element_by_css_selector(".challenge-name").text)
    if upcoming == 1:
        for i in he_driver.find_element_by_css_selector(".upcoming").\
            find_elements_by_css_selector(".challenge-card-modern"):
            HE_UP_COMPANY.append(i.find_element_by_css_selector(".company-details").text)
            HE_UP_TYPE.append(i.find_element_by_css_selector(".challenge-type").text)
            HE_UP_NAME.append(i.find_element_by_css_selector(".challenge-name").text)
            HE_UP_DATE.append(i.find_element_by_css_selector(".date").text)
            he_driver.close()
    print_hackerearth(live, upcoming)

def print_hackerearth(live=1, upcoming=1):
    '''Function to print HackerEarth Challenges on Command Line'''
    if live == 1:
        print("\nLive Challenges of HackerEarth:\n")
        print("Company Name - Test Type - Name of the Challenge")
        for index in range(0, len(HE_LIVE_COMPANY)):
            print(HE_LIVE_COMPANY[index], end=" - ")
            print(HE_LIVE_TYPE[index], end=" - ")
            print(HE_LIVE_NAME[index])
    if upcoming == 1:
        print("\nUpcoming Challenges of HackerEarth:\n")
        print("Company Name - Test Type - Type of the Challenge - Name of the Challenge - \
              Start Date")
        for index in range(0, len(HE_UP_COMPANY)):
            print(HE_UP_COMPANY[index], end=" - ")
            print(HE_UP_TYPE[index], end=" - ")
            print(HE_UP_NAME[index], end=" - ")
            print(HE_UP_DATE[index])

TE_INPUT = str(input("Enter Y or y to get Techgig Challenges: "))
if TE_INPUT.lower() == "y" or TE_INPUT.lower() == "yes":
    techgig_extractor()
HE_LINPUT = str(input("\nEnter Y or y to get HackerEarth Live Challenges: "))
if HE_LINPUT.lower() == "y" or HE_LINPUT.lower() == "yes":
    he_extractor(1, 0)
HE_UINPUT = str(input("\nEnter Y or y to get HackerEarth UpComing Challenges: "))
if HE_UINPUT.lower() == "y" or HE_UINPUT.lower() == "yes":
    he_extractor(0, 1)

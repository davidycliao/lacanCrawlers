#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
@author: davidycliao
@email : davidycliao@gmail.com
@date  : 9-Dec-2021
@info  : LACAN Project (Legislators between Accountability and Collective Agency)
"""


import re
import time
import random
import pandas as pd
import datefinder

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def toString(s): 
    '''
    initialize an empty string 
    '''
    # initialize an empty string
    string = " " 
    return string.join(s)



def parliamentary_questions(session = 'Current Session'):
    '''
    This scraper will extract parliarmentary questions from answered questions and holding answers.
    Time periods includes:
    'Session 1'
    'Session 2'
    'Session 3'
    'Session 4'
    'Session 5'
    'Current Session'
    'All Sessions'
    '''
    if  session == 'Session 1':
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=60c8d55d3b98443883f30728118d73cc%7CWednesday%2C+May+12%2C+1999%7CTuesday%2C+May+6%2C+2003&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false#results'
        tag = 'Session 1, The Scottish Parliarment'
        name_tag = 'scottish_first_session'
        print(tag)
    elif session == 'Session 2':
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=4a52911a07584297b5ecd17728bb7512%7CWednesday%2C+May+7%2C+2003%7CTuesday%2C+May+8%2C+2007&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false#results'
        tag = 'Session 2, The Scottish Parliarment'
        name_tag = 'scottish_second_session'
        print(tag)
    elif session == 'Session 3':
        links =  'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=a80a0dfedc214712be57cf102f1b854c%7CWednesday%2C+May+9%2C+2007%7CTuesday%2C+May+10%2C+2011&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false#results'
        tag = 'Session 3, The Scottish Parliarment'
        name_tag = 'scottish_third_session'
        print(tag)
    elif session == 'Session 4': 
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=23b353c96e2546239f9ed6ff25f3ecdf%7CWednesday%2C+May+11%2C+2011%7CWednesday%2C+May+11%2C+2016&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false#results'
        tag = 'Session 4, The Scottish Parliarment'
        name_tag = 'scottish_fourth_session'
        print(tag)
    elif session == 'Session 5': 
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=78db02c79507407a8df319e9d7ac424e%7CThursday%2C+May+12%2C+2016%7CTuesday%2C+May+11%2C+2021&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false#results'
        tag = 'Session 5, The Scottish Parliarment'
        name_tag = 'scottish_fifth_session'
        print(tag)
    elif session == 'Current Session': 
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=7503b6d994e241ef904c18fa9ad3ab70%7CWednesday%2C+May+12%2C+2021%7C&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false#results'
        tag = 'Current Session, The Scottish Parliarment'
        name_tag = 'scottish_current_session'
        print(tag)
    elif session == 'All Sessions': 
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=acfe09e8571447b6ac663f6362a20f42%7CFriday%2C+December+17%2C+1971%7CFriday%2C+December+17%2C+2021&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false#results'
        tag = 'All Session, The Scottish Parliarment'
        name_tag = 'scottish_all_sessions'
        print(tag)
        
    elif session == 'Session-1-Page':
        page = str(input("Start Page (default, 1):"))
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=60c8d55d3b98443883f30728118d73cc%7cWednesday%2c+May+12%2c+1999%7cTuesday%2c+May+6%2c+2003&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false&page=' + page
        tag = 'Session 1, The Scottish Parliarment'
        name_tag = 'scottish_first_session_from_page_' + page
        print(tag + ' Starting at Page ' + page + '\n' + 'Started page url:'+'\n' + links)
    elif session == 'Session-2-Page':
        page = str(input("Start Page (default, 1):"))
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=4a52911a07584297b5ecd17728bb7512%7CWednesday%2C+May+7%2C+2003%7CTuesday%2C+May+8%2C+2007&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false&page=' + page
        tag = 'Session 2, The Scottish Parliarment'
        name_tag = 'scottish_second_session_from_page_' + page
        print(tag + ' Starting at Page ' + page + '\n' + 'Started page url:'+'\n' + links)
    elif session == 'Session-3-Page':
        page = str(input("Start Page (default, 1):"))
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=a80a0dfedc214712be57cf102f1b854c%7CWednesday%2C+May+9%2C+2007%7CTuesday%2C+May+10%2C+2011&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false&page=' + page
        tag = 'Session 3, The Scottish Parliarment'
        name_tag = 'scottish_third_session_from_page_' + page
        print(tag + ' Starting at Page ' + page + '\n' + 'Started page url:'+'\n' + links)
    elif session == 'Session-4-Page': 
        page = str(input("Start Page (default, 1):"))
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=23b353c96e2546239f9ed6ff25f3ecdf%7CWednesday%2C+May+11%2C+2011%7CWednesday%2C+May+11%2C+2016&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false&page=' + page
        tag = 'Session 4, The Scottish Parliarment'
        name_tag = 'scottish_fourth_session_from_page_' + page
        print(tag + ' Starting at Page ' + page + '\n'  + 'Started page url:'+'\n' + links)
    elif session == 'Session-5-Page': 
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=78db02c79507407a8df319e9d7ac424e%7CThursday%2C+May+12%2C+2016%7CTuesday%2C+May+11%2C+2021&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false&page=' + page
        tag = 'Session 5, The Scottish Parliarment'
        name_tag = 'scottish_fifth_session_from_page_' + page
        print(tag + ' Starting at Page ' + page + '\n' + 'Started page url:'+'\n' + links)
    elif session == 'Current-Session-Page': 
        page = str(input("Start Page (default, 1):"))
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=7503b6d994e241ef904c18fa9ad3ab70%7CWednesday%2C+May+12%2C+2021%7C&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false&page=' + page
        tag = 'Current Session, The Scottish Parliarment'
        name_tag = 'scottish_current_session_from_page_' + page
        print(tag + ' Starting at Page ' + page + '\n' + 'Started page url:'+'\n' + links)
    elif session == 'All-Sessions-Page': 
        page = str(input("Start Page (default, 1):"))
        links = 'https://www.parliament.scot/chamber-and-committees/written-questions-and-answers?msp=All&qry=&qryref=&dateSelect=acfe09e8571447b6ac663f6362a20f42%7CFriday%2C+December+17%2C+1971%7CFriday%2C+December+17%2C+2021&chkAnswered=true&chkAnswered=false&chkUnAnswered=false&chkHolding=true&chkHolding=false&page=' + page
        tag = 'All Session, The Scottish Parliarment'
        name_tag = 'scottish_all_sessions_from_page_' + page
        print(tag + ' Starting at Page ' + page + '\n' + 'Started page url:'+'\n' + links)
    else:
        print('Please insert: Session 1, Session 2, Session 3, Session 4, Session 5, Current Session, or All Sessions \n' + 
              'To start from a spicific page, inserting : Session-1-Page, Session-2-Page, Session-3-Page, Session-4-Page, Session-5-Page, Current-Session-Page, or  All-Sessions-Page')
    print('==========================================================================')

        
        
    # create driver's setting
    options = Options()
    options.add_argument("--start-maximized")                                    # open Browser in maximized mode
    options.add_argument("--no-sandbox")                                         # bypass OS security model
    options.add_argument("--disable-dev-shm-usage")                              # overcome limited resource problems
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(60)
    driver.get(links)
    driver.find_element(By.XPATH, '//*[@id="agreeCookieButton"]').click()
    
    # create lists to store scraped data
    question_ref = []
    question_link = []
    asked_by = []
    parl_question = []
    date_lodged = []
    date_answered = []
    answered_by = []
    answered_content = []
    web_number = []
    total_webpage = []

    try:
        # history_log.txt stores the scraped history
        with open( name_tag +'_log.txt', 'w') as f:
            while True:
                current_page=driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[1]
                final_page=driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[3]
                for element in driver.find_elements(By.XPATH, '//div[@class="pagination__links"]'):
                    page_text=element.text
                    len_num=int(len(re.findall(r'\b\d+\b', page_text)))
                
                # deal with the page that has 4 links
                if len_num==3:
                    containers = driver.find_elements(By.XPATH, '//div[@class="content-list__block"]')
                    for i in range(0, len(containers)):
                        
                        if len(containers[i].text.split('\n')) == 5:
                            question=containers[i].text.split('\n')[3]
                            answeredBy=containers[i].text.split('\n')[4][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[4][-20:])])
                        elif len(containers[i].text.split('\n')) == 4:
                            question=containers[i].text.split('\n')[2]
                            answeredBy=containers[i].text.split('\n')[3][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[3][-20:])])
                        
                        # to find the status of submitting to the members
                        try:
                            answeredContent=cleanhtml(containers[i].find_element(By.XPATH, './/div[@class="u--hide waanswer rich-text"]').get_attribute('innerHTML'))
                        except: 
                            answeredContent = containers[i].text.split('\n')[3][16:-19]
                            dateAnswered='None'
                            
                        ref=containers[i].text.split('\n')[0]
                        link=containers[i].find_elements(By.XPATH, ".//a[@href]")[0].get_attribute('href')
                        askedBy=containers[i].text.split('\n')[1][:-31]
                        dateLodged=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[1][-20:])])
                        webNum=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[1])
                        totalPage=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[3])  

                        driver.implicitly_wait(60)
                        question_ref.append(ref)
                        question_link.append(link)
                        asked_by.append(askedBy)
                        parl_question.append(question)
                        date_lodged.append(dateLodged)
                        date_answered.append(dateAnswered)
                        answered_by.append(answeredBy) 
                        answered_content.append(answeredContent)
                        web_number.append(webNum)
                        total_webpage.append(totalPage)
                        
                    print('Webpage', current_page, 'from ' + tag, 'is done...')
                    f.write('Webpage ' + current_page + '\n' +  links)
                    f.write('\n')                    
                    driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/div[2]/div/div[2]/div/a[4]').click()
                    
                # deal with the page that has 5 links
                elif len_num==4:
                    containers=driver.find_elements(By.XPATH, '//div[@class="content-list__block"]')
                    
                    for i in range(0, len(containers)):
                        
                        if len(containers[i].text.split('\n')) == 5:
                            question=containers[i].text.split('\n')[3]
                            answeredBy=containers[i].text.split('\n')[4][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[4][-20:])])
                        elif len(containers[i].text.split('\n')) == 4:
                            question=containers[i].text.split('\n')[2]
                            answeredBy=containers[i].text.split('\n')[3][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[3][-20:])])
                        
                        # to find the status of submitting to the members
                        try:
                            answeredContent=cleanhtml(containers[i].find_element(By.XPATH, './/div[@class="u--hide waanswer rich-text"]').get_attribute('innerHTML'))
                        except: 
                            answeredContent = containers[i].text.split('\n')[3][16:-19]
                            dateAnswered='None'

                        ref=containers[i].text.split('\n')[0]
                        link=containers[i].find_elements(By.XPATH, ".//a[@href]")[0].get_attribute('href')
                        askedBy=containers[i].text.split('\n')[1][:-31]
                        dateLodged=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[1][-20:])])
                        webNum=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[1])
                        totalPage=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[3])   

                        question_ref.append(ref)
                        question_link.append(link)
                        asked_by.append(askedBy)
                        parl_question.append(question)
                        date_lodged.append(dateLodged)
                        date_answered.append(dateAnswered)
                        answered_by.append(answeredBy) 
                        answered_content.append(answeredContent)
                        web_number.append(webNum)
                        total_webpage.append(totalPage)

                        driver.implicitly_wait(60)

                    print('Webpage', current_page, 'from ' + tag, 'is done...')
                    f.write('Webpage ' + current_page + '\n' +  links)
                    f.write('\n')
                    driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/div[2]/div/div[2]/div/a[5]').click()
                    
                # deal with the page that has 6 links
                elif len_num==5:
                    containers=driver.find_elements(By.XPATH, '//div[@class="content-list__block"]')
                    
                    for i in range(0, len(containers)):
                        if len(containers[i].text.split('\n')) == 5:
                            question=containers[i].text.split('\n')[3]
                            answeredBy=containers[i].text.split('\n')[4][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[4][-20:])])
                        elif len(containers[i].text.split('\n')) == 4:
                            question=containers[i].text.split('\n')[2]
                            answeredBy=containers[i].text.split('\n')[3][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[3][-20:])])
                        # to find the status of submitting to the members
                        try:
                            answeredContent=cleanhtml(containers[i].find_element(By.XPATH, './/div[@class="u--hide waanswer rich-text"]').get_attribute('innerHTML'))
                        except: 
                            answeredContent = containers[i].text.split('\n')[3][16:-19]
                            dateAnswered='None'

                        ref=containers[i].text.split('\n')[0]
                        link=containers[i].find_elements(By.XPATH, ".//a[@href]")[0].get_attribute('href')
                        askedBy=containers[i].text.split('\n')[1][:-31]
                        dateLodged=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[1][-20:])])
                        webNum=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[1])
                        totalPage=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[3])    

                        question_ref.append(ref)
                        question_link.append(link)
                        asked_by.append(askedBy)
                        parl_question.append(question)
                        date_lodged.append(dateLodged)
                        date_answered.append(dateAnswered)
                        answered_by.append(answeredBy) 
                        answered_content.append(answeredContent)
                        web_number.append(webNum)
                        total_webpage.append(totalPage)

                        driver.implicitly_wait(60)

                    print('Webpage', current_page, 'from ' + tag, 'is done...')
                    f.write('Webpage ' + current_page + '\n' +  links)
                    f.write('\n')
                    driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/div[2]/div/div[2]/div/a[6]').click()  
                
                # deal with the page that reaches the end of the webpage
                elif current_page==final_page:
                    containers=driver.find_elements(By.XPATH, '//div[@class="content-list__block"]')
                    for i in range(0, len(containers)):
                        if len(containers[i].text.split('\n')) == 5:
                            question=containers[i].text.split('\n')[3]
                            answeredBy=containers[i].text.split('\n')[4][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[4][-20:])])
                        elif len(containers[i].text.split('\n')) == 4:
                            question=containers[i].text.split('\n')[2]
                            answeredBy=containers[i].text.split('\n')[3][16:-19]
                            dateAnswered=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[3][-20:])])
                        
                        # to find the status of submitting to the members
                        try:
                            answeredContent=cleanhtml(containers[i].find_element(By.XPATH, './/div[@class="u--hide waanswer rich-text"]').get_attribute('innerHTML'))
                        except: 
                            answeredContent = containers[i].text.split('\n')[3][16:-19]
                            dateAnswered='None'

                        ref=containers[i].text.split('\n')[0]
                        link=containers[i].find_elements(By.XPATH, ".//a[@href]")[0].get_attribute('href')
                        askedBy=containers[i].text.split('\n')[1][:-31]
                        dateLodged=toString([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(containers[i].text.split('\n')[1][-20:])])
                        webNum=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[1])
                        totalPage=int(driver.find_element(By.XPATH, "//html/body/main/div[4]/div/div[2]/div/div[2]/p").text.split()[3])  

                        question_ref.append(ref)
                        question_link.append(link)
                        asked_by.append(askedBy)
                        parl_question.append(question)
                        date_lodged.append(dateLodged)
                        date_answered.append(dateAnswered)
                        answered_by.append(answeredBy) 
                        answered_content.append(answeredContent)
                        web_number.append(webNum)
                        total_webpage.append(totalPage)
                        
                        driver.implicitly_wait(60)

                    print('Webpage', current_page, 'from ' + tag, 'is done...')
                    f.write('Webpage ' + current_page + '\n' +  links)
                    f.write('\n')        
    
    except (NoSuchElementException):
        print('==========================================================================')
        print(tag + ' of written questions is finished')
        df = pd.DataFrame({'Question Ref.': question_ref,
                           'Ouestion Link': question_link,
                           'Asked by': asked_by,
                           'Parliament Question': parl_question,
                           'Date Lodged':date_lodged,
                           'Date Answered': date_answered,
                           'Answered By':answered_by,
                           'Answered Content':answered_content,
                           'Web No.': web_number,
                           'Total Number of Pages': total_webpage})
        df.to_csv(name_tag + '.csv', index=False)
        pass
        driver.close()
        driver.quit()
        
    # capture the error caused by the keyboard interruption 
    except (KeyboardInterrupt) as e:
        print('Webpage from ' + current_page, 'is failed... \n' , e + ' : due to manual interruption')
        df = pd.DataFrame({'Question Ref.': question_ref,
                           'Ouestion Link': question_link,
                           'Asked by': asked_by,
                           'Parliament Question': parl_question,
                           'Date Lodged':date_lodged,
                           'Date Answered': date_answered,
                           'Answered By':answered_by,
                           'Answered Content':answered_content,
                           'Web No.': web_number,
                           'Total Number of Pages': total_webpage})
        df.to_csv(name_tag + '.csv', index=False)
        pass
        driver.close()
        driver.quit()
        
    # capture the error caused by unforeseen structures of the website
    except (exceptions.StaleElementReferenceException) as e:
        print('Webpage from ' + current_page, 'is failed... \n' , e + ' : due to unforeseen structures of the website')
        df = pd.DataFrame({'Question Ref.': question_ref,
                           'Ouestion Link': question_link,
                           'Asked by': asked_by,
                           'Parliament Question': parl_question,
                           'Date Lodged':date_lodged,
                           'Date Answered': date_answered,
                           'Answered By':answered_by,
                           'Answered Content':answered_content,
                           'Web No.': web_number,
                           'Total Number of Pages': total_webpage})
        df.to_csv(name_tag + '.csv', index=False)
        pass
        driver.close()
        driver.quit()
        
    # capture the error caused by new structure or layouts change such as 4 rows reduced to 3 or 2 rows
    except (AttributeError, IndexError) as e:
        print('Webpage from ' + current_page, 'is failed... \n' , e + ' :due to new structure or layouts change')
        df = pd.DataFrame({'Question Ref.': question_ref,
                           'Ouestion Link': question_link,
                           'Asked by': asked_by,
                           'Parliament Question': parl_question,
                           'Date Lodged':date_lodged,
                           'Date Answered': date_answered,
                           'Answered By':answered_by,
                           'Answered Content':answered_content,
                           'Web No.': web_number,
                           'Total Number of Pages': total_webpage})
        df.to_csv(name_tag + '.csv', index=False)
        pass
        driver.close()
        driver.quit()

if __name__ == '__main__':parliamentary_questions()
        
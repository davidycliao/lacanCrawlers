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


def parliamentary_questions(legislature = 'test'):
    '''
    @legislature

    '''
    if legislature == 'Commons':
        links = 'https://questions-statements.parliament.uk/written-questions?Answered=Any&AnsweredFrom=&AnsweredTo=&DateFrom=01%2F01%2F1999&DateTo=31%2F07%2F2022&Expanded=True&House=Commons&SearchTerm=&Page=1'
        tag = 'The House of Commons'
        name_tag = 'house_of_commons'
        print('Scraping written questions from ' + tag)
    elif legislature == 'Lord':
        links = 'https://questions-statements.parliament.uk/written-questions?Answered=Any&AnsweredFrom=01%2F01%2F1820&AnsweredTo=31%2F07%2F2022&DateFrom=01%2F01%2F1820&DateTo=31%2F07%2F2022&Expanded=True&House=Lords&SearchTerm=&Page=1'
        tag = 'The House of Lord'
        name_tag = 'house_of_lord'
        print('Scraping written questions from ' + tag)
    elif legislature == 'Commons-Page':
        page = str(input("Start Page (default, 1):"))
        links = 'https://questions-statements.parliament.uk/written-questions?Answered=Any&AnsweredFrom=&AnsweredTo=&DateFrom=01%2F01%2F1999&DateTo=31%2F07%2F2022&Expanded=True&House=Commons&SearchTerm=&Page=' + page
        tag = 'The House of Commons'
        name_tag = 'house_of_commons_page_' + page
        print('Scraping written questions from '+ tag)
    elif legislature == 'Lord-Page':
        page = str(input("Start Page (default, 1):"))
        links = 'https://questions-statements.parliament.uk/written-questions?Answered=Any&AnsweredFrom=01%2F01%2F1820&AnsweredTo=31%2F07%2F2022&DateFrom=01%2F01%2F1820&DateTo=31%2F07%2F2022&Expanded=True&House=Lords&SearchTerm=&Page=' + page
        tag = 'The House of Lord'
        name_tag = 'house_of_lord_page_' + page
        print('Scraping written questions from '+ tag)
    elif legislature == 'test':
        links = 'https://questions-statements.parliament.uk/written-questions?Answered=Any&AnsweredFrom=&AnsweredTo=&DateFrom=11%2F05%2F2021&DateTo=31%2F07%2F2022&Expanded=False&House=Bicameral&SearchTerm=&Page=1810'
        tag = 'test'
        print('Scraping written questions from '+ tag)
    else:
        print('Please insert: Commons, Lord, Commons-Page or Lord-Page')
        
    print('==========================================================================')

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options = Options()
    # options.add_argument("--start-maximized")                                 # open Browser in maximized mode
    options.add_argument("--no-sandbox")                                        # bypass OS security model
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-dev-shm-usage")                             # overcome limited resource problems
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_position(0, 0)
    driver.implicitly_wait(60)
    driver.get(links)
    driver.find_element(By.XPATH, '//*[@id="allowall"]').click()


    question_topic = []
    question_for = []
    question_ref = []
    question_link = []
    mp_info_link = []
    mp_party = []
    asked_by = []
    parl_question = []
    date_lodged = []
    date_answered = []
    answered_by = []
    web_number = []
    total_webpage = []

    try:
        with open(name_tag + '_log.txt', 'w') as f:
            while True:
                info = driver.find_elements(By.XPATH, '//*[@class="result-text"]')
                regexPattern = '|'.join(map(re.escape, ('(', ' ', ')')))
                total_page = [int(s) for s in re.split(regexPattern, info[1].text) if s.isdigit()][0]
                current_page = [int(s) for s in re.split(regexPattern, info[1].text) if s.isdigit()][1]
                last_page = [int(s) for s in re.split(regexPattern, info[1].text) if s.isdigit()][2]

                container = driver.find_elements(By.XPATH, '//*[@class="card card-written-question"]')
                for i in range(0, len(container)):
                    questionRef = container[0].find_elements(By.XPATH, '//div[@class="info"]//div[@class="info-inner"]//div[@class="indicators-left"]//div[@class="indicator indicator-label"]')[i].text 
                    questionFor = container[i].find_elements(By.XPATH, '//div[@class="primary-info"]')[i].text 
                    questionTopic = container[i].find_elements(By.XPATH, '//div[@class="secondary-info"]')[i].text
                    questionLink =  container[i].find_elements(By.XPATH, ".//a[@href]")[0].get_attribute('href')
                    mpInfoLink = container[i].find_elements(By.XPATH, ".//a[@href]")[1].get_attribute('href')
                    mpParty = container[i].find_elements(By.XPATH, '//div[@class="secondary-text"]')[i].text.split(', ')[0]
                    askedBy = container[i].find_elements(By.XPATH, '//div[@class="content-text"]')[i].text.split('\n')[0] 
                    parlQuestion = container[i].find_elements(By.XPATH, '//div[@class="extra-info-group sub-card sub-card-question-text"]')[i].text 

                    try:
                        date_list = [name.text for name in container[1].find_elements(By.XPATH, '//div[@class="info info-secondary ask-info"]')]
                        # date_lodged.append([x.strftime("%Y-%m-%d") for x in datefinder.find_dates(date_list[i])][0])
                        dateLodged = [x.strftime("%Y-%m-%d") for x in datefinder.find_dates(date_list[i])][0]
                    except (IndexError):
                        # date_lodged.append("None")
                        dateLodged = "None"

                    if container[i].find_elements(By.XPATH, '//div[@class="info info-secondary answer-info"]')[i].text.split(' ')[0] == 'Answered':
                        answeredBy = [name.text for name in container[i].find_elements(By.XPATH, '//div[@class="indicators-left"]//div[@class="indicator indicator-label"]//div[@class="item"]') if name.text.find('Answered')][i]
                        dateAnswered = [x.strftime("%Y-%m-%d") for x in datefinder.find_dates(container[1].find_elements(By.XPATH, '//div[@class="info info-secondary answer-info"]')[i].text)]
                    elif container[i].find_elements(By.XPATH, '//div[@class="info info-secondary answer-info"]')[i].text.split(' ')[0] == 'Awaiting':
                        answeredBy = 'None' 
                        dateAnswered = container[1].find_elements(By.XPATH, '//div[@class="info info-secondary answer-info"]')[i].text 
                    elif container[i].find_elements(By.XPATH, '//div[@class="info info-secondary answer-info"]')[i].text.split(' ')[0] == '':
                        answeredBy = 'None' 
                        dateAnswered = container[1].find_elements(By.XPATH, '//div[@class="info info-secondary answer-info"]')[i].text 


                    question_ref.append(questionRef)
                    question_for.append(questionFor)
                    question_topic.append(questionTopic)
                    question_link.append(questionLink)
                    mp_info_link.append(mpInfoLink)
                    mp_party.append(mpParty)
                    asked_by.append(askedBy)
                    parl_question.append(parlQuestion)
                    answered_by.append(answeredBy)
                    date_answered.append(dateAnswered)
                    date_lodged.append(dateLodged)
                    web_number.append(current_page)
                    total_webpage.append(last_page)

                f.write('Webpage ' + str(current_page))
                f.write('\n')
                print('Webpage', current_page, 'from', tag , 'is done...')                     
                driver.find_element(By.XPATH, '//*[@class="next"]').click()

    except NoSuchElementException:
        df = pd.DataFrame({'question_ref':question_ref,
                           'question_for': question_for,
                           'question_topic': question_topic,
                           'question_link': question_link,
                           'mp_info_link': mp_info_link,
                           'mp_party':mp_party,
                           'asked_by': asked_by,
                           'parl_question':parl_question,
                           'date_lodged':date_lodged,
                           'date_answered': date_answered,
                           'answered_by': answered_by,
                           'web_number': web_number,
                           'total_webpage': total_webpage})  
        df.to_csv(name_tag + '.csv', index=False)
        print('==========================================================================')
        print(tag + 'of written questions is finished')
        # return df
        pass
        driver.close()
        driver.quit()

    # capture the error caused by the keyboard interruption 
    except KeyboardInterrupt as e:
        print('Webpage from', tag ,current_page, 'is failed... \n' , e + ' : due to manual interruption')
        df = pd.DataFrame({'question_ref':question_ref,
                           'question_for': question_for,
                           'question_topic': question_topic,
                           'question_link': question_link,
                           'mp_info_link': mp_info_link,
                           'mp_party':mp_party,
                           'asked_by': asked_by,
                           'parl_question':parl_question,
                           'date_lodged':date_lodged,
                           'date_answered': date_answered,
                           'answered_by': answered_by,
                           'web_number': web_number,
                           'total_webpage': total_webpage})         
        df.to_csv(name_tag + '.csv', index=False)
        pass
        driver.close()
        driver.quit()

    # capture the error caused by unforeseen structures of the website
    except exceptions.StaleElementReferenceException as e:
        df = pd.DataFrame({'question_ref':question_ref,
                           'question_for': question_for,
                           'question_topic': question_topic,
                           'question_link': question_link,
                           'mp_info_link': mp_info_link,
                           'mp_party':mp_party,
                           'asked_by': asked_by,
                           'parl_question':parl_question,
                           'date_lodged':date_lodged,
                           'date_answered': date_answered,
                           'answered_by': answered_by,
                           'web_number': web_number,
                           'total_webpage': total_webpage}) 
        print('Webpage from ',current_page, legislature, 'is failed... \n' , e + ' : due to unforeseen structures of the website.')
        df.to_csv(name_tag + '.csv', index=False)
        pass
        driver.close()
        driver.quit()

    # capture the error caused by new structure or layouts change, e.g. 4 rows reduced to 3 or 2 rows. 
    except (AttributeError, IndexError) as e:
        df = pd.DataFrame({'question_ref':question_ref,
                           'question_for': question_for,
                           'question_topic': question_topic,
                           'question_link': question_link,
                           'mp_info_link': mp_info_link,
                           'mp_party':mp_party,
                           'asked_by': asked_by,
                           'parl_question':parl_question,
                           'date_lodged':date_lodged,
                           'date_answered': date_answered,
                           'answered_by': answered_by,
                           'web_number': web_number,
                           'total_webpage': total_webpage}) 
        print('Webpage from', tag ,current_page, legislature, 'is failed... \n' , e + ' :due to new structure or layouts change')
        df.to_csv(name_tag + '.csv', index=False)
        pass
        driver.close()
        driver.quit()




if __name__ == '__main__':parliamentary_questions()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.options import Options

import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

import csv
import io
import datetime

import time
import csv
import io


from bs4 import BeautifulSoup


def go_see_x(user_name:str, your_account_username:str, your_account_password:str, scroll_count:int=3):
    if user_name == '' or your_account_username == '' or your_account_password == '':
        return "argument not filled correctly"

    link = "https://x.com"
    link_login:str = "https://x.com/i/flow/login"

    uName = user_name 

    #edgeOpt = Options()
    #edgeOpt.add_experimental_option('detach',True)
    #engine = webdriver.Edge(options=edgeOpt)
    
    
    engine = webdriver.Remote("http://chrome:4444/wd/hub", options=webdriver.ChromeOptions())


    ### Login
    
    acc_name = your_account_username;
    acc_pwd = your_account_password;

    
    engine.get(link_login) 
    # engine.get(f'{link}/{uName}') 


    # un_inp = engine.find_element_by_name('username')
    # pw_inp = engine.find_element_by_name('password')

    WebDriverWait(engine, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='username']"))).send_keys(acc_name)
    WebDriverWait(engine, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@style,'background-color: rgb(239, 243, 244)')]"))).click()

    WebDriverWait(engine, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='current-password']"))).send_keys(acc_pwd)
    WebDriverWait(engine, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@style,'background-color: rgb(239, 243, 244)')]"))).click()
    
    # WebDriverWait(engine, 60).until(EC.invisibility_of_element((By.XPATH, "//button[contains(@style,'background-color: rgb(239, 243, 244)')]")))
    WebDriverWait(engine, 60).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Post')]")))
    # time.sleep(10)

    # return



    ### Go to user

    # for uName in uNames:
    print("--------------------------------------------")
    print(f"Accessing {uName}")
    print("--------------------------------------------")
    engine.get(f'{link}/{uName}')

    csv_string = io.StringIO()
    csvWriter = csv.writer(csv_string)

    # time.sleep(3)

    WebDriverWait(engine, 60).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Follow')]")))

    # akun = engine.get(f'{link}/{uName}')
    ### If account is private
    try:
        a = engine.find_element(By.XPATH,"//span[contains(text(),'These posts')]")
        print(a)
        engine.quit()
        return "this account is private"
    except:
        print('not locked')

    ### If account does not have any post(s)
    
    try:
        engine.find_element(By.XPATH,"//div[contains(text(),'0 posts')]")
        engine.quit()
        return "no post(s) in this account"
    except:
        print('there is post')


    WebDriverWait(engine,30).until(EC.presence_of_all_elements_located((By.XPATH,"//article[@data-testid='tweet']")))
    
    last_post_text=''
    count = 0

    for i in range(scroll_count*6):

        post = engine.find_element(By.XPATH,"//article[@data-testid='tweet']")
        postText = post.find_element(By.XPATH,"//div[@data-testid='tweetText']").get_attribute('innerText')
        postTime = post.find_element(By.XPATH,"//time[@datetime]").get_attribute('datetime')


        # print(postText,' ',postTime)

        if postText != last_post_text:
            csvWriter.writerow([count,postTime,postText])
            count+=1    

        last_post_text = postText

            
         
        # engine.execute_script("window.scrollTo(0,pageYOffset+document.body.scrollHeight)")
        engine.execute_script("window.scrollTo(0,pageYOffset+500)")
        time.sleep(1)
    

    # post_links = []

    # for i in range(len(post_links)):
    #     engine.get(post_links[i])
    #     # engine.implicitly_wait(30)
    #     time.sleep(4)

    #     postCaption = engine.find_element(By.XPATH,"//h1[@dir='auto']").get_attribute("innerText")
    #     # txt = txt.split('\n')

    #     postDate = engine.find_element(By.XPATH,"//time[@title][@class='x1p4m5qa']").get_attribute('title')

    #     # print(f"{i}\t{postDate}\t{post_links[i]}\t{postCaption}")
    #     csvWriter.writerow([str(i+1),postDate,post_links[i],postCaption])



    # engine.quit()
    return csv_string.getvalue()



            # for i in txt:

            #     print(i)
            #     if i == uName:
            #         print('\n')

            # print('\n\n\n')


            # print('\n\n\n\n\n')


        
    #     WebDriverWait(engine, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@class='_aagu]")))



    #     perakun = BeautifulSoup(engine.page_source,'html.parser')


    #     # ya = perakun.find_all('div',class_="_aagu")
    #     with open('fsafe.html','w') as svhtml:
    #         svhtml.write(str(perakun.prettify))




        




        # engine.implicitly_wait(20)





    # un_inp.send

async def go_see_x2(user_name:str, your_account_username:str, your_account_password:str, how_many_post:int=10):
    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS (for CLI usage see BELOW)
    # await api.pool.add_account("pioopipooi", "ee=emce2", "", "")
    await api.pool.add_account(your_account_username, your_account_password, "", "")
    # await api.pool.add_account("maxevers123", "2051Lb57", "max.evers123@hotmail.com", "2051Lb57")
    await api.pool.login_all()

    # get the user detail
    user_data = await api.user_by_login(user_name)

    print(user_data.id)

    user_tweets = await gather(api.user_tweets(int(user_data.id),limit=how_many_post))
    # print(user_tweets)

    csv_string = io.StringIO()
    csvWriter = csv.writer(csv_string)

    i = 0
    for tweet in user_tweets:
        if i == how_many_post:
            break;

        csvWriter.writerow([str(i+1),tweet.date.strftime("%Y-%m-%d %X"),tweet.url, tweet.rawContent])

        i+=1


    # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    # async for tweet in api.search("apple"):
    #     print(tweet.user.username, tweet.rawContent, tweet.date)  # tweet is `Tweet` object

    return csv_string.getvalue()



if __name__ == '__main__':
    # change '-' with you account details
    res = go_see_x('elonmusk','-','-',3)

    print(res)



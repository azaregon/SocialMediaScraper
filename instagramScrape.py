from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.options import Options

import time
import csv
import io


from bs4 import BeautifulSoup


def go_see_ig(user_name:str, your_account_username:str, your_account_password:str, scroll_count:int=1):
    if user_name == '' or your_account_username == '' or your_account_password == '':
        return "argument not filled correctly"

    link = "https://www.instagram.com"

    uName = user_name 

    # acc_name = 'pioopipooi';
    # acc_pwd = 'ee=emce2'
    
    
    acc_name = your_account_username;
    acc_pwd = your_account_password;

    edgeOpt = Options()
    edgeOpt.add_experimental_option('detach',True)

    engine = webdriver.Edge(options=edgeOpt)
    
    
    engine.get(link)


    # un_inp = engine.find_element_by_name('username')
    # pw_inp = engine.find_element_by_name('password')

    WebDriverWait(engine, 20).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys(acc_name)
    WebDriverWait(engine, 20).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(acc_pwd)
    WebDriverWait(engine, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    WebDriverWait(engine, 60).until(EC.invisibility_of_element((By.XPATH, "//button[@type='submit']")))





    # for uName in uNames:
    print("--------------------------------------------")
    print(f"Accessing {uName}")
    print("--------------------------------------------")

    csv_string = io.StringIO()
    csvWriter = csv.writer(csv_string)

    akun = engine.get(f'{link}/{uName}')
    time.sleep(3)
    
    try:
        engine.find_element(By.XPATH,"//*[local-name()='circle' and @fill='none' and @r='47']")
        engine.quit()
        return "this account is private"
    except:
        pass
    
    try:
        engine.find_element(By.XPATH,"//*[local-name()='svg' and @aria-label='Camera']")
        engine.quit()
        return "no post(s) in this account"
    except:
        pass


    # engine.implicitly_wait(30)
    WebDriverWait(engine,30).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"_aagu")))


    for i in range(scroll_count):
        engine.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    # engine.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)
    # engine.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)
    # engine.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    posts = engine.find_elements(By.CLASS_NAME,"_aagu")

    post_links = []

    for i in posts:
        prnt = i.find_element(By.XPATH,"..")
        postlink = prnt.get_attribute("href")
        post_links.append(postlink)

    # for i in range(len(post_links)):
    #     # i_now = i*3
    #     engine.get(post_links[i])
    #     # engine.implicitly_wait(30)
    #     time.sleep(4)

    #     postCaption = engine.find_element(By.XPATH,"//h1[@dir='auto']").get_attribute("innerText")
    #     # txt = txt.split('\n')

    #     postDate = engine.find_element(By.XPATH,"//time[@title][@class='x1p4m5qa']").get_attribute('title')

    #     # print(f"{i}\t{postDate}\t{post_links[i]}\t{postCaption}")
    #     csvWriter.writerow([str(i+1),postDate,post_links[i],postCaption])


    global_i = 0;

    for i in range(5):
        engine.execute_script("window.open('about:blank')")
        engine.switch_to.window(engine.window_handles[-1])


        engine.get(post_links[global_i])



        global_i+=1;



    for i in range(len(post_links)-5):
        # engine.execute_script("window.open('about:blank')")

        engine.switch_to.window(engine.window_handles[(global_i%5)+1])




        postCaption = engine.find_element(By.XPATH,"//h1[@dir='auto']").get_attribute("innerText")
        # txt = txt.split('\n')

        postDate = engine.find_element(By.XPATH,"//time[@title][@class='x1p4m5qa']").get_attribute('title')

        # print(f"{i}\t{postDate}\t{post_links[i]}\t{postCaption}")
        csvWriter.writerow([str(i+1),postDate,post_links[i],postCaption])



        engine.get(post_links[global_i])
        global_i +=1


    engine.quit()
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



if __name__ == '__main__':
    # change '-' with your account details
    res = go_see_ig('apple','-','-',3)
    

    print(res)



try:

    from selenium import webdriver
    from selenium.webdriver.common.keys import  Keys
    from selenium.common.exceptions import  TimeoutException
    from selenium.webdriver.common.by import By
    import  selenium.webdriver.support.ui as ui
    import selenium.webdriver.support.expected_conditions as EC
    import os
    import time
    import requests
    import threading
    import queue
    import random
    import sys
except Exception as e:
    print(e)
print("""

    Falcon Digital Checker For free
    YOUTUBE/FalconDigitalArabic
    Make sure u download chromdriver and put it in same file !  
    time out For your Network if it's bad make it 4 #
    
    
""")

time.sleep(3)
email = str(input("Enter Username "))
password = str(input("Enter Password"))
thread_number = int(input("Enter Thread 10-100:"))
time_out = int(input("Enter timeout for proxy 1-10:"))

print_lock = threading.Lock()
username = open('username.txt','r').read().splitlines()
q = queue.Queue()

list_url = []
USER_AGENTS = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36'),  # chrome
]
import random
event = threading.Event()
def checker(q,proxy):

    try:
        user_agent = random.choice(USER_AGENTS)

        prox2 = proxy
        url = q
        s = url.split("com/")
        global user
        user = s[1]
        check = "@"+user



        session = requests.session()
        session.proxies = {}
        session.proxies['http://'] = prox2
        session.proxies['https://'] = prox2
        session.headers = {'user-agent': user_agent}
        session.headers.update({'Referer': 'https://i.instagram.com/'})
        sreq = session.get(url, timeout=time_out).text
        text = str(sreq)

        if text.find(check)>=0:
            with print_lock:
                print("[-] Faild {} [-]".format(user))
        elif text.find("<h2>Sorry, this page isn&#39;t available.</h2>") >=0:
            event.set()
            with print_lock:


                print("[+] Found {} ! [+] ".format(user))
                raise SystemExit
                
                
        else:
            pass
    except Exception as e:
        pass
saved = []
proxy = open('proxy.txt','r')
prox = []
for i in proxy:
    prox.append(i)
l = len(prox)
for i in username:
    url = "https://www.instagram.com/"+ i

    q.put(url)
def threading1():
    number = 0

    while not q.empty():
        worker = str(q.get())
        if number == l-1:
            number  = 0
        checker(worker,prox[number])

        number = number +1

        q.task_done()

def Signup():
    try:

        optons = webdriver.ChromeOptions()
        optons.add_argument('--ignore-certificate-errors')
        optons.add_argument('--ignore-ssl-errors')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromdriver = dir_path + "/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromdriver
        driver = webdriver.Chrome(options=optons, executable_path=chromdriver)

        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input""").send_keys(email)
        driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input""").send_keys(password)
        driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button""").click()
        time.sleep(2)


        driver.get('https://www.instagram.com/accounts/edit/')
        event.wait()
        with print_lock:

            driver.find_element_by_xpath("""//*[@id="pepUsername"]""").clear()
            driver.find_element_by_xpath("""//*[@id="pepUsername"]""").send_keys(user)
            driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/form/div[11]/div/div/button[1]""").click()


        print("[+] username change Done ![+]")
        driver.close()

        raise SystemExit

    except Exception as e:

        print(e)
        time.sleep(30)
        raise SystemExit





t2 = threading.Thread(target=Signup)

t2.start()
str(input("Press anyting When the Chromedriver in Profile/edit:"))

for x in range(thread_number):
    t = threading.Thread(target=threading1)
    t.daemon = True
    t.start()



q.join()



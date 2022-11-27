from instagramuserinfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
import time


class Instagram():
    def __init__(self,username,password):
        # self.options = Options()
        # self.options.set_preference('intl.accept_languages', 'en-US, en')                       # ingilizce

        # self.browser = Firefox(options=self.options)
        self.username=username
        self.password=password
        self.browser=webdriver.Firefox()


        
    
    def singIn(self):
        time.sleep(2)
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        time.sleep(2)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(3)

    def getFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.username}/?next=%2F")
        time.sleep(2)
        self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(2)
        self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]').find_elements(By.CLASS_NAME,'_ab8w')
        time.sleep(2)
        self.scrollDown()
        time.sleep(2)
        x=self.browser.find_elements(By.CLASS_NAME,'_ab8y')
        followerList=[]
        sayac=0
        for q in x:
            sayac+=1
            #print(f"{sayac}:{q.text}")
            followerList.append(q.text)
            
            #if sayac==max:
            #    break
        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")

    
    def scrollDown(self):
        jsKomut = """
        sayfa = document.querySelector('._aano');
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
        sayfaSonu = self.browser.execute_script(jsKomut)
        while True:
            son = sayfaSonu
            time.sleep(2)
            sayfaSonu = self.browser.execute_script(jsKomut)
            if son == sayfaSonu:
                break 

    def followUser(self,username):
        time.sleep(5)
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)
        followButon=self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div")
        time.sleep(2)
        if followButon.text != "Takiptesin":
            followButon.click()
            time.sleep(2)
        else:
            print("zaten takip ediyorsunuz")
    

    def unFollowUser(self,username):
        time.sleep(5)
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        followButton=self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div")
        if followButton.text == "Takiptesin":
            time.sleep(2)
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[7]').click()
            time.sleep(2)     
        else:
            time.sleep(2)
            print("zaten takip etmiyorsun")
            time.sleep(2)

            
                


instagram=Instagram(username,password)
instagram.singIn()
instagram.getFollowers()
#instagram.followUser("socratesdergi")    
#instagram.unFollowUser("socratesdergi")
       

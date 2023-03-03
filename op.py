from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



print("")
dat=input("enter date: ")
slot=input("enter time slot: ")
tickets=input("enter number of tickets: ")
#var element = document.createElement('div'); element.style.position = 'absolute'; element.style.left = '470' + 'px'; element.style.top = '690' + 'px'; element.style.width = '5px'; element.style.height = '5px'; element.style.border = '3px solid red'; element.style.zIndex = '9999'; document.body.appendChild(element);
def solve_captcha(url,browser):
        
       
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'captcha_viewer'))).click()
        sleep(1)
        result = 'WUBBEshfbt'
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in alphabets:
            try:
                browser.execute_script(f"___grecaptcha_cfg.clients[0].{i}.{i}.callback('{result}')")
                #print(i)
                break
            except:
                # self.driver.execute_script(f"___grecaptcha_cfg.clients[0].W.W.callback()")
                pass
        
        sleep(3)
        actions = ActionChains(browser)
        actions.move_by_offset(50, 290).click().perform()

def cartConfirmation(browser):
  try:
   wait=WebDriverWait(browser,2)
   confirm=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='YOUR CART IS EMPTY']")))
  except:
    return True
  return False

def openPage(browser):

    browser.implicitly_wait(1)
    browser.get('https://ecm.coopculture.it/index.php?option=com_snapp&view=event&id=3793660E-5E3F-9172-2F89-016CB3FAD609&catalogid=B79E95CA-090E-FDA8-2364-017448FF0FA0&lang=en')
    wait = WebDriverWait(browser, 10)
    cross = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[2]/a[2]")))
    cross.click()
    sleep(3)
    browser.execute_script("window.scrollTo(0,720)")
    

def goToDate(browser):
    
    browser.refresh()
    sleep(2)
    try:
     browser.execute_script('document.getElementsByClassName("next changemonth glyphicon glyphicon-chevron-right")[0].click()')
     sleep(2)
     wait = WebDriverWait(browser, 10)
     date = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@data-date='{}/3/2023']".format(dat))))
     date.click()
     sleep(2)
    except:
      print("could not click the date")
    
    


def addToCart(browser):

    time=browser.find_elements(By.XPATH,"//*[@id='performances']/div[1]/div/div")
    tofind=slot
    count=0
    for i in time:
      count+=1
      if tofind in i.text:
       try:
        print(i.text.split("\n")[1].split()[1][1:len(i.text.split("\n")[1].split()[1])-1])
       except:
        pass 
       break
    
    wait = WebDriverWait(browser, 20)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="performances"]/div[1]/div/div[{k}]/div[2]/button'.format(k=count))))
    elem.click()

    
    wait = WebDriverWait(browser, 10)
    noOfTickets = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="qB6B0B700-CEEA-3087-359F-016CB3FAF5CB"]')))
    noOfTickets.clear()
    noOfTickets.send_keys(tickets)
    sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    
    wait=WebDriverWait(browser,10)
    addtocart=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="myModal"]/div/div/div[3]/button[2]')))
    addtocart.click()
    sleep(2)
  
    
chrome_options = Options()
chrome_options.add_argument("--disable-cache")
browser1 = webdriver.Chrome(executable_path=r"C:\Users\hasna\OneDrive\Desktop\chromedriver.exe",options=chrome_options)
browser2 = webdriver.Chrome(executable_path=r"C:\Users\hasna\OneDrive\Desktop\chromedriver.exe",options=chrome_options)
browser1.set_window_size(1200, 750)
browser2.set_window_size(1200, 750)
openPage(browser1)
openPage(browser2)

while True:

  browser1.refresh()
  goToDate(browser1)
  addToCart(browser1)
  try:
   browser2.refresh()
   wait=WebDriverWait(browser2,10)
   empty=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cartpanel']/div/div/div/div[4]/div[2]/div[5]/a/img")))
   empty.click()
   sleep(2)
  except:
    print("try emptying the cart..")
  
  solve_captcha('https://ecm.coopculture.it/index.php?option=com_snapp&view=event&id=3793660E-5E3F-9172-2F89-016CB3FAD609&catalogid=B79E95CA-090E-FDA8-2364-017448FF0FA0&lang=en',browser1)
  check=cartConfirmation(browser1)
  while check!=True:
     goToDate(browser1)
     addToCart(browser1)
     solve_captcha('https://ecm.coopculture.it/index.php?option=com_snapp&view=event&id=3793660E-5E3F-9172-2F89-016CB3FAD609&catalogid=B79E95CA-090E-FDA8-2364-017448FF0FA0&lang=en',browser1)
     check=cartConfirmation(browser1)

  sleep(11*60)

  try:
   browser1.refresh()
   wait=WebDriverWait(browser1,10)
   less=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cartpanel']/div/div/div/div[4]/div[2]/div[4]/img")))
   less.click()
   sleep(1)
  except:
     print("Error while realeasing ticket..")
  

  sleep(1)  
  goToDate(browser2)
  addToCart(browser2)
  try:
   browser1.refresh()
   wait=WebDriverWait(browser1,10)
   empty=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cartpanel']/div/div/div/div[4]/div[2]/div[5]/a/img"))) 
   empty.click()
   sleep(2)
  except:
     print("try emptying cart..")

  solve_captcha('https://ecm.coopculture.it/index.php?option=com_snapp&view=event&id=3793660E-5E3F-9172-2F89-016CB3FAD609&catalogid=B79E95CA-090E-FDA8-2364-017448FF0FA0&lang=en',browser2)
  check=cartConfirmation(browser2)
  while check!=True:
     goToDate(browser2)
     addToCart(browser2)
     solve_captcha('https://ecm.coopculture.it/index.php?option=com_snapp&view=event&id=3793660E-5E3F-9172-2F89-016CB3FAD609&catalogid=B79E95CA-090E-FDA8-2364-017448FF0FA0&lang=en',browser1)
     check=cartConfirmation(browser2)

  sleep(11*60)

  try:
   browser2.refresh()
   wait=WebDriverWait(browser2,10)
   less=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cartpanel']/div/div/div/div[4]/div[2]/div[4]/img")))
   less.click()
   sleep(1)
  except:
    print("Error while realeasing ticket..")







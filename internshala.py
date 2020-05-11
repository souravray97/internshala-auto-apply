from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from tkinter import Tk, Menu, filedialog, Checkbutton, messagebox, LabelFrame, RIDGE, \
Frame, Entry, W, END, Button, E, Label, Listbox, Scrollbar, \
RIGHT, Y, X, BOTTOM, LEFT#to avoid wildcard imports for my editor
#from tkinter import * will do for you

def interns(events):
    chrome_path = r"C:\Users\hp\Desktop\chromedri\chromedriver.exe"#where chromedriver is installed in your system
    driver = webdriver.Chrome(chrome_path)
    driver.fullscreen_window()#full screen window--we have to work in this
    driver.get("https://internshala.com/")
    registerbutton = driver.find_element_by_xpath("/html/body/div[1]/div[22]/div/div/div[4]/div/div/div/button")#the complete xpath of the element
    registerbutton.click()
    asastudent = driver.find_element_by_xpath("/html/body/div[1]/div[22]/div/div/div[4]/div/div/div/ul/li[1]/a")
    asastudent.click()
    loginlink = driver.find_element_by_xpath("/html/body/div/div[23]/div/div/div/div/div[3]/span")
    loginlink.click()
    loginwithgoogle = driver.find_element_by_xpath("/html/body/div[1]/div[21]/div/div/div[2]/a/div/div[2]")
    loginwithgoogle.click()
    emailid = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    emailid.send_keys(entry_1.get())#the get function gets the string in the entry object
    nextbutton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span")
    nextbutton.click()
    sleep(10)#wait until the password is interactable
    clickpassword = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    clickpassword.send_keys(entry_2.get())
    nextpassbutton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span")
    nextpassbutton.click()
    sleep(10)

    clickhere = driver.find_element_by_xpath("/html/body/div[1]/div[21]/div/nav/div/div[2]/ul/li[1]/a")
    clickhere.click()
    
    sleep(5)
    
    category = driver.find_element_by_xpath("/html/body/div[1]/div[23]/div[2]/div/div[4]/div[1]/div/div/div/form[1]/div[2]/div/div/ul/li/input")
    category.click()
    sleep(1)
    category.send_keys(entry_3.get())
    category.send_keys(u'\ue007')#equivalent to pressing enter.. google standards
    
    sleep(15)
    #have to work on this stuff also
    # location = driver.find_element_by_xpath("/html/body/div[1]/div[23]/div[2]/div/div[4]/div[1]/div/div/div/form[1]/div[3]/div/div/ul/li/input")
    # location.click()
    # sleep(7)
    # location.send_keys(entry_4.get())
    # location.send_keys(u'\ue007')
    # sleep(5)

    wfhchechmark = driver.find_element_by_xpath("/html/body/div[1]/div[23]/div[2]/div/div[4]/div[1]/div/div/div/form[1]/div[4]/div[1]/label/span")
    wfhchechmark.click()
    sleep(15)
    #internship applying loop
    count = 0
    while(count < (int(entry_5.get()) + 1)):
        internship_1 = driver.find_element_by_xpath("/html/body/div[1]/div[23]/div[2]/div/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/a/span")
        internship_1.click()
        sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")#scrolls down to the bottom of the webpage
        sleep(3)

            
        wait = WebDriverWait(driver, 5)
        element = wait.until(EC.element_to_be_clickable((By.ID, "search_button")))
        element.click()
                                               # /html/body/div[1]/div[23]/div/div/div[2]/div[1]/div/div[2]/div[7]/div/div/a/button
                                               #/html/body/div[1]/div[23]/div/div/div[2]/div[1]/div/div[2]/div[6]/div/div/a/button
                                               #/html/body/div[1]/div[23]/div/div/div[2]/div[1]/div/div[2]/div[7]/div/div/a/button
    


        proceedtoapp = driver.find_element_by_xpath("/html/body/div[1]/div[22]/div/div/div[1]/div[1]/div[2]/button")
        proceedtoapp.click()
        sleep(3)

        whyshould = driver.find_element_by_xpath("/html/body/div[1]/div[22]/div/div/div/form/div[1]/textarea")
        whyshould.click()
        whyshould.send_keys(entry_6.get())

            
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        onedone = driver.find_element_by_xpath("/html/body/div[1]/div[22]/div/div/div/form/div[3]/input")
        onedone.click()
        sleep(5)

        backtosearch = driver.find_element_by_xpath("/html/body/div[1]/div[24]/div/div/div[1]/div/div[2]/div/a/button")
        backtosearch.click()

        count += 1

#have applied to one internship.. have to put this in a recursive function with a for loop

root = Tk()

root.geometry("400x250")
label_1 = Label(root, text = "EMAIL ID")    
label_2 = Label(root, text = "Password")
label_3 = Label(root, text = "Field of internship")
# label_4 = Label(root, text = "Location")
label_5 = Label(root, text = "How many?")
label_6 = Label(root, text = "Why do you want to be hired?")

entry_1 = Entry(root)#this is a entry object!! not a string..
entry_2 = Entry(root,show = "*")
entry_3 = Entry(root)
# entry_4 = Entry(root)
entry_5 = Entry(root)
entry_6 = Entry(root)

label_1.grid(row = 0,sticky = "EW")
label_2.grid(row = 1,sticky = "EW")
label_3.grid(row = 2,sticky = "EW")
# label_4.grid(row = 3,sticky = "EW")
label_5.grid(row = 4,sticky = "EW")
label_6.grid(row = 5,sticky = "EW")

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)
entry_3.grid(row = 2, column = 1)
# entry_4.grid(row = 3, column = 1)
entry_5.grid(row = 4, column = 1)
entry_6.grid(row = 5, column = 1)


entry_6.bind("<Return>", interns)


root.mainloop()

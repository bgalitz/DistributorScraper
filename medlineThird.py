import time
import random # is this necessary
from selenium import webdriver
# These imports were copied from internet...needed for email function
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application
from selenium.webdriver.common.keys import Keys

# STEP TIMER: how long is this thig taking??
then = time.time() #Time before the operations start

#------------------------------------------------------------------------------

# STEP 1: Create an email function to be used later to send file via email
url = "https://www.medline.com/account/login.jsp"
# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
element = driver.find_element_by_xpath("//input[contains(@id,'ext-gen1004')]")   
time.sleep(1)
#TO DO: replace USER with your login to the Medline website
#element.send_keys("USER", Keys.TAB)
element.send_keys("USER")
time.sleep(1)
element = driver.find_element_by_xpath("//input[contains(@id,'ext-gen1005')]")

#TO DO: replace the variable PASSWORD with your Medline password
element.send_keys("PASSWORD1")

time.sleep(1)
element.send_keys(Keys.ENTER)
#driver.find_element_by_css_selector("button.submit").click();
#element = driver.find_element_by_xpath("//input[contains(@value,'Login')])")
#element.click()
counter = 0

#-------------------------------------------------------------------------------
# STEP 2: open and start reading each line from the file
with open('MedlineDataThree.txt') as fifi:
    for line in fifi:
        urlNext = "https://www.medline.com/sku/item/MDP" + line + "?"
        #counter += 1
        driver.get(urlNext)
        time.sleep(1)
        try:
            onhand = driver.find_element_by_class_name("noprint").text
        except:
            onhand = "0 CS"
        combined = line + " onhand stock is " + onhand + "\n"


#-------------------------------------------------------------------------------
# STEP 4: print results to file        
        with open('AgundezMedlineDataThree.txt','a') as fi:
            fi.write(combined)

            
#-------------------------------------------------------------------------------
# STEP 5: Since we always run this file last and it's the largest and it takes the longest time
# Once it's finished, append all 3 files to a new CONSOLIDATED FINAL file and email
# Yes I know we can eliminate a step...but this is a draft and we will continue to refine
with open('FINAL.txt','a') as fi:

    with open('AgundezMedlineDataOne.txt') as fileOne:
        for lineOne in fileOne:
            fi.write(lineOne)
            counter += 1
    fi.write("\n")
    
    with open('AgundezMedlineDataTwo.txt') as fileTwo:
        for lineTwo in fileTwo:
            fi.write(lineTwo)
            counter += 1
    fi.write("\n") 
        
    with open('AgundezMedlineDataThree.txt') as fileThree:
        for lineThree in fileThree:
            fi.write(lineThree)
            counter += 1
    fi.write("\n")
            
fileOne.close()
fileTwo.close()
fileThree.close()
fi.close()       
fifi.close()

# HOW LONG DID IT TAKE TO FINISH SCRAPING
now = time.time() #Time after it finished
total = now-then
totaltime = str(total)
totalcount = str(counter)
#print("It took: ", now-then, " seconds")

# TODO STEP 6: Email file to the team
smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

# TO DO: insert email address into EMAIL and insert password into PASSWORD
s.login("EMAIL", "PASSWORD")

msg = MIMEMultipart()
msg['Subject'] = 'Medline files processed in last file ' + totalcount + ' items'

# TO DO: insert the FROM_EMAIL
msg['From'] = "FROM_EMAIL"

# TO DO: insert the TO_EMAIL
msg['To'] = "TO_EMAIL"

# Because we're appending this step is not necessary but I'm not removing it today 10/10/19
txt = MIMEText('Last Medline file appended took ' + totaltime + ' seconds to run!')
msg.attach(txt)

filename = 'Final.txt' #path to file
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="txt")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)
s.send_message(msg)
s.quit()

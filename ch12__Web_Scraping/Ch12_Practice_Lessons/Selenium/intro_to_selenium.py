#! python3

from selenium import webdriver
from selenium.webdriver.common.by import By     # find elements
from selenium.webdriver.common.keys import Keys     # use special keys

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

#                                                                                   Finding Elements
# try:
#     elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
#     print(f'Successfully Found Class: {elem.tag_name}')
# except:
#     print('Was not able to find element')

#                                                                                   Clicking the Page
# try:
#     linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
#     print(f'Successfully Found Class: {type(linkElem)}')
#     print(f'Clicked "{linkElem.text}" with link of {linkElem.get_attribute("href")}')
#     linkElem.click() # follows the "read online for free" link
# except:
#     print('Was not able to find element')

#                                                                                   Filling Out and Submitting Forms
# try:
#     userElem = browser.find_element(By.ID, 'mce-EMAIL')
#     userElem.send_keys('your_email_goes_here@yahoo.com')
#     userElem.submit()
# except:
#     print('Was not able to find element')

# Avoid putting your passwords in source code whenever possible. It’s easy to acciden-
# tally leak your passwords to others when they are left unencrypted on your hard drive.
# If possible, have your program prompt users to enter their passwords from the key-
# board using the pyinputplus.inputPassword() function described in Chapter 8.

#                                                                                    Sending Special Keys
# htmlElem = browser.find_element(By.TAG_NAME, 'html')
# htmlElem.send_keys(Keys.END)  # Scrolls to Bottom
# htmlElem.send_keys(Keys.HOME)  # Scrolls to Top

# The <html> tag is the base tag in HTML files: the full content of the
# HTML file is enclosed within the <html> and </html> tags. Calling browser
# .find_element_by_tag_name('html') is a good place to send keys to the general
# web page. This would be useful if, for example, new content is loaded once
# you’ve scrolled to the bottom of the page.

#                                                                                   Clicking Browser Buttons

# try:
#     linkElem = browser.find_element(By.LINK_TEXT, 'YouTube')
#     print(f'Successfully Found Class: {type(linkElem)}')
#     print(f'Clicked "{linkElem.text}" with link of {linkElem.get_attribute("href")}')
#     linkElem.click() # follows the "YouTube" link
# except:
#     print('Was not able to find element')

# print('Clicked Browser Back Button')
# browser.back()      # Clicks the Back button.
# browser.forward()       # Clicks the Forward button.
# browser.refresh()       # Clicks the Refresh/Reload button.
# browser.quit()      # Clicks the Close Window button.
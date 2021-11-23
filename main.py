import time

from selenium import webdriver



driver = webdriver.Chrome(executable_path='/home/ale/Documents/GitHub/data_messages_google/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://messages.google.com/web/authentication?pli=1');

time.sleep(15) # Let the user actually see something!

my_element = driver.find_element_by_class_name('avatar-container')

my_element.click()

time.sleep(15)

elpepe = driver.find_element_by_xpath("//div[contains(@class, 'text-msg ng-star-inserted')]")
print(elpepe.text)
time.sleep(15)
# time.sleep(20)
# otro = driver.find_element_by_class_name('msg-info')
# print(otro.text)
# time.sleep(20)
# elpepe = driver.find_element_by_xpath("//div[contains(@class, 'msg-info')]")
# print(elpepe)
# <div _ngcontent-wcp-c152="" data-e2e-message-status="" class="msg-info"><mws-relative-timestamp _ngcontent-wcp-c152="" _nghost-wcp-c83="" class="ng-star-inserted"><!----><div _ngcontent-wcp-c83="" aria-label="15 min ago" class="ng-star-inserted"> 15 min </div><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----></mws-relative-timestamp><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----></div>
# <div _ngcontent-wcp-c152="" data-e2e-message-status="" class="msg-info"><mws-relative-timestamp _ngcontent-wcp-c152="" _nghost-wcp-c83="" class="ng-star-inserted"><!----><div _ngcontent-wcp-c83="" aria-label="21 min ago" class="ng-star-inserted"> 21 min </div><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----></mws-relative-timestamp><!----><!----><!----><!----><!----><!----><!----><!----><!----><!----></div>

driver.quit()
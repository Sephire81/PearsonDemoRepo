from splinter import Browser
from splinter import Config
import time


proprietary_mode = 1

mode = 2
if proprietary_mode:
    mode = int(input("Enter mode: "))

config = Config(fullscreen=True)
browser = Browser('edge', config=config)
# Simple look at data on page, write it
if mode == 0:
    browser.visit('https://www.dataentrytester.com/')
    
    while browser.find_by_id('timer').value != "0:00":
        time.sleep(0.5)
        word_to_type = browser.find_by_css('span[class="current-word"]').value
        browser.type('typebox', word_to_type+" ")
    
    browser.quit()

# Look at structured form, fill in with constant details.
if mode == 1:
    browser.visit('https://www.roboform.com/filling-test-all-fields')
    browser.find_by_name('01___title').fill('Mr')
    browser.find_by_name('02frstname').fill('John')
    browser.find_by_name('03middle_i').fill('S')
    browser.find_by_name('04lastname').fill('Doe')
    browser.find_by_name('10address1').fill('10 Palm Drive')
    browser.find_by_name('13adr_city').fill('London')
    browser.find_by_name('15_country').fill('United Kingdom')
    browser.find_by_name('16addr_zip').fill('E5 EZ3')
    time.sleep(3)
    browser.find_by_css('input[type="reset"]').click()

if mode == 2:
    browser.visit('https://www.parcelforce.com/track-trace')
    track_box = browser.find_by_id("edit-parcel-tracking-number")
    track_box.fill("trackingID")

time.sleep(3)
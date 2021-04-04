import os
import time
from datetime import date
from selenium import webdriver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
             "Safari/537.36 "

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
options.binary_location = binary_location
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)

# options = webdriver.ChromeOptions()
# options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# options.add_argument("--window-size=1920,1080")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--headless")
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--no-sandbox")
#
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
driver.implicitly_wait(15)

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
#              "Safari/537.36 "
#
# options = webdriver.ChromeOptions()
# options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# options.headless = True
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument("--window-size=1920,1080")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)


# Wait
def wait(t):
    time.sleep(t)


# Change String of month to number
def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except Exception as e:
        print(e)


# Check
def checkDiff(review_date):
    date_list = review_date.split()
    review_day = int(date_list[0])
    review_month = int(month_string_to_number(date_list[1]))
    review_year = int(date_list[2])

    today_date = date.today()
    today_date = str(today_date)
    t_date = today_date.split("-")

    # Check Difference
    one = date(int(t_date[0]), int(t_date[1]), int(t_date[2]))
    other = date(review_year, review_month, review_day)

    diff = one - other
    diff = diff.days

    return diff


# Scroll till target
def scroll_till_target(target):
    driver.execute_script("arguments[0].scrollIntoView();", target)
    wait(2)


def login():
    try:
        driver.get('https://www.glassdoor.com/index.htm')
        driver.maximize_window()
        print(driver.title)
        wait(5)
        driver.find_element_by_css_selector('div.selectedLabel').click()
        wait(2)
        for item in driver.find_elements_by_css_selector('span.dropdownOptionLabel'):
            if item.text == 'United States':
                item.click()
            else:
                pass
        wait(5)
        try:
            driver.find_element_by_xpath('//*[@id="TopNav"]/nav/div/div/div[4]/div[1]/a').click()
            username = driver.find_element_by_xpath('//*[@id="userEmail"]')
            password = driver.find_element_by_xpath('//*[@id="userPassword"]')
            wait(2)
            username.send_keys('sk0196146@gmail.com')
            wait(2)
            password.send_keys('P@ssw0rd9')
            wait(2)
            sign_in = driver.find_element_by_xpath(
                '//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button')
            sign_in.click()
            wait(5)
        except Exception as ex:
            print(ex)

            driver.find_element_by_xpath('//*[@id="SiteNav"]/nav/div[2]/div/div/div/button').click()
            username = driver.find_element_by_xpath('//*[@id="userEmail"]')
            password = driver.find_element_by_xpath('//*[@id="userPassword"]')
            wait(2)
            username.send_keys('sk0196146@gmail.com')
            wait(2)
            password.send_keys('P@ssw0rd9')
            wait(2)
            sign_in = driver.find_element_by_xpath(
                '//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button')
            sign_in.click()
            wait(5)

    except Exception as e:
        print(e)

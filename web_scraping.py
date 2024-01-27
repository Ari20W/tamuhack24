# from bs4 import BeautifulSoup
# from selenium import webdriver 
# from selenium.webdriver.chrome.options import Options
# import time as t

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

# start_url = "https://dineoncampus.com/tamu/hours-of-operation"

# driver.get(start_url)
# t.sleep(7)
# full_html = driver.page_source.encode("utf-8")
# driver.quit()

# soup = BeautifulSoup(full_html, "html.parser")

# locations = []
# for loc in soup.find_all(class_='hours-of-operation-section_locationName_1vUeF'):
#     locations.append(loc.text.strip())


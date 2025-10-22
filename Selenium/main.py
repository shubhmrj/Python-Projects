from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after programme finish execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/AmazonBasics-Stainless-Electric-Coffee-Grinder/dp/B07SYTRPSG/ref=sr_1_1_ffob_sspa?_encoding=UTF8&content-id=amzn1.sym.1c676675-169c-43b5-84e3-6a95e93c5fec&dib=eyJ2IjoiMSJ9.UQp-7u0oBNW_BF1pWf5N_vdKmUNZmGFtSYkV3A9OIDY_JSXQiiF1W735ITaSJddkJWfWSgfvXZWRuIz26Nvs408sBFNV8br8JtapgeLO8pyMkgjfMuaNpg1-Bb7YojgKDkuhMpYcueBtgn17S7DGzOBIqwu3KFbwsB1xhDuCvVwPnlMqaZlBLtYkKiMgqyZQ8qV3BG0bA4xBnhEzIZyxocqplR5MN49b7Nn8ThxlLmB8vpMdZ-wxuMAWLGUyh-922cs_s2E3MPHNF6C1tHJRbU1GgWgIDv-ZoKTpYom8tWk.SGSHZifq-nyEE5cvRnDb86ptXZZmE-5RPabt7QgLS4A&dib_tag=se&keywords=Kitchen+Appliances&pd_rd_r=8a028f1f-0967-4b0d-ab43-b7c719c2fd19&pd_rd_w=HLUVC&pd_rd_wg=1rbpn&qid=1760854786&refinements=p_36%3A-5000&rnid=386465011&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# Scrape the price
# price_in_ruppe = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_in_paise = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# # print the price
# print(f"Price is {price_in_ruppe.text}.{price_in_paise.text}")



search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
# this will close a particular tab
# driver.close()

# this will clode entire browser
driver.quit()
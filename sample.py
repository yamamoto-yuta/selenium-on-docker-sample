import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Chromeのオプション
options = webdriver.ChromeOptions()
# 今回は特に無くても動いたのでコメントアウトしている
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('chromedriver', options=options)


try:
    # 要素の待機時間を最大10秒に設定
    driver.implicitly_wait(10)

    # http://www.google.com を開く
    driver.get("http://www.google.com")

    # 検索ボックスに「webdriver」と入力して検索
    driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)
    time.sleep(5)

    # 検索結果のタイトルを取得して出力
    element_titles = driver.find_elements(By.TAG_NAME, "h3")
    for element_title in element_titles:
        print(element_title.text)

except:
    import traceback
    traceback.print_exc()

finally:
    # Chromeを終了
    input("何かキーを押すと終了します...")
    driver.quit()

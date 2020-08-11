import time, random, re
import pandas as pd
from selenium import webdriver
from directory import EXCEL_PATH, CONFIG_FILE

browser = webdriver.Chrome('') ## add chrome webdriver's file path

class Browser_ctrls:
  def __init__(self):
    self.delay = [2,3]

  def open_target_page(self, target_page):
    browser.get(target_page)

  def _pause(self, start, end):
    time.sleep(random.randint(start, end))

  def pause(self):
    timer = random.randint(int(self.delay[0]), int(self.delay[1]))
    time.sleep(timer)

  def scroll_to_bottom(self):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

  def scroll_through_page(self):
    browser.execute_script("window.scrollBy(0,100)")

  def _strip_spaces(self, text):
    text = text.split('\n')
    text = text[1]
    text = re.sub(' +', ' ', text).strip()
    return text


class LinkedIn_login(Browser_ctrls):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.get_userInfo()

  def get_userInfo(self):
    userInfo = []
    with open(f'{CONFIG_FILE}.txt', 'r') as f:
      user_info = f.read().split('\n')
    return user_info

  def login(self, login_page):
    browser.get(login_page)
    user_info = self.get_userInfo()
    elementIDs = ['username', 'password']

    for info, elementID in zip(user_info, elementIDs):
      if elementID != 'password':
        self.pause()
        browser.find_element_by_id(elementID).send_keys(info)
      else:
        self.pause()
        browser.find_element_by_id(elementID).send_keys(info)
        browser.find_element_by_id(elementID).submit()

    self.pause()

    for _ in range(random.randint(1,2)):
      self.scroll_to_bottom()
      self.pause()

    self._pause(1,2)

class Pandas_Ops:
  def sort_ascending_column(self, df):
    df = df.sort_values(by='Company', ascending=True)
    return df


  def write_excel(self, df, title):
    with pd.ExcelWriter(f'{EXCEL_PATH}{title}.xlsx') as writer:
      df.to_excel(writer, sheet_name='Main', index=False)
      df.to_excel(writer, sheet_name='raw data', index=False)

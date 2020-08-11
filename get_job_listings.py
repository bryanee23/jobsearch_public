import pandas as pd
import time, random, re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from classes import LinkedIn_login, Browser_ctrls, Pandas_Ops, browser
from directory import LOGIN_URL, TARGET_URL, EXCEL_PATH, EXCEL_TITLE, NUM_PAGES


sheet_title = f'{EXCEL_TITLE}'
login_URL = f'{LOGIN_URL}'
target_URL = f'{TARGET_URL}'

class LinkedIn_jobs(Browser_ctrls):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.df = pd.DataFrame(columns=['Position', 'Company', 'Location', 'Date Posted'])



  def scroll_sequence(self):
    self._pause(3,4)
    start = browser.find_element_by_xpath(
          "//li [@class='occludable-update artdeco-list__item--offset-2 artdeco-list__item p0 ember-view']")

    container = browser.find_element_by_xpath("//div [@class='jobs-search-results jobs-search-results--is-two-pane']")
    footer_element = browser.find_element_by_xpath("//footer [@class='global-footer-compact ember-view']")

    action = ActionChains(browser)
    action.move_to_element(start).click_and_hold(start).move_by_offset(0,100).release().move_to_element(footer_element).release().perform()

    self.pause()

    timer = random.randint(2,3)

    action.move_to_element(container).send_keys(Keys.PAGE_UP).pause(timer).send_keys(Keys.PAGE_UP).pause(timer).send_keys(Keys.PAGE_UP).pause(timer).send_keys(Keys.PAGE_UP).pause(timer).send_keys(Keys.PAGE_UP).pause(timer).perform()

    ActionChains(browser).move_to_element(footer_element).pause(timer).perform()



  def _get_listing_data(self):
    self._pause(4,5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    self.pause()
    results = soup.find_all('li', class_="occludable-update artdeco-list__item--offset-2 artdeco-list__item p0 ember-view")

    return results



  def getNstore_data_to_df(self):
    data = self._get_listing_data()

    for soup_result in data:
      try:
        company = soup_result.find('a', class_='job-card-container__link job-card-container__company-name ember-view').text
        company = self._strip_spaces(company)
      except:
        print("Company info not found")
        company = None

      try:
        position = soup_result.find('a', class_='disabled ember-view job-card-container__link job-card-list__title').text
        position = self._strip_spaces(position)
      except:
        print("Position info not found")
        position = None

      try:
        location = soup_result.find('div', class_='artdeco-entity-lockup__caption ember-view').text
        location = self._strip_spaces(location)
      except:
        print("Location info not found")
        location = None

      try:
        date = soup_result.find('time')['datetime']
      except:
        print("Date not found")
        date = None

      self.df = self.df.append(
                            {'Position': position,
                              'Company': company,
                              'Location': location,
                              'Date Posted': date},
                              ignore_index=True)

    print("Data found: %.0f, DataFrame size: %s " % (len(data), self.df.shape), '\n')



  def get_nextPage(self, page_num):
    self._pause(4,6)
    try:
      browser.find_element_by_xpath(f'//button[@aria-label="Page {page_num}"]').click()
      self._pause(2,3)
    except:
      print("coudln't find page number to get_nextPage")



  def sort_df_by_company(self):
    self.df = Pandas_Ops().sort_ascending_column(self.df)

  def df_to_excel(self, title):
    Pandas_Ops().write_excel(self.df, title)


def run(pages):
  run = LinkedIn_login()
  run.login(login_URL)
  run.open_target_page(target_URL)

  run = LinkedIn_jobs()
  for i in range(2, pages):
    try:
      print('Collecting data from page: ', i-1)
      print('Start scroll sequence')
      run.scroll_sequence()
      print('Organizing data...')
      run.getNstore_data_to_df()

      run.get_nextPage(i)
    except:
      print(f'Complete, iterated through {i} pages')

  run.sort_df_by_company()
  run.df_to_excel(sheet_title)
  browser.close()

run(NUM_PAGES)
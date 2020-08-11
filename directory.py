TARGET_PAGE = {
  'CONFIG_PATH': 'system files/config',
  'NUMBER_OF_PAGES' : 40, ### update number of pages
  'TITLE' : 'Job Listings - ML',
  'URL' : 'https://www.linkedin.com/jobs/search/?geoId=102095887&keywords=machine%20learning&location=California%2C%20United%20States' ## add URL
}

########################################################################


TARGET_URL = TARGET_PAGE['URL']

CONFIG_FILE = TARGET_PAGE['CONFIG_PATH']

EXCEL_TITLE = TARGET_PAGE['TITLE']

NUM_PAGES = TARGET_PAGE['NUMBER_OF_PAGES'] + 2

LOGIN_URL = 'https://www.linkedin.com/uas/login'

EXCEL_PATH = 'excels/'
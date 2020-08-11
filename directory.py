TARGET_PAGE = {
  'CONFIG_PATH': 'system files/config',
  'NUMBER_OF_PAGES' : 0, ### update number of pages
  'TITLE' : 'Job Listings - ML',
  'URL' : '' ## add URL
}

########################################################################


TARGET_URL = TARGET_PAGE['URL']

CONFIG_FILE = TARGET_PAGE['CONFIG_PATH']

EXCEL_TITLE = TARGET_PAGE['TITLE']

NUM_PAGES = TARGET_PAGE['NUMBER_OF_PAGES'] + 2

LOGIN_URL = 'https://www.linkedin.com/uas/login'

EXCEL_PATH = 'excels/'
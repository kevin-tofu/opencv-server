import os


VERSION = os.getenv('VERSION', 'v0'),
AUTHOR = os.getenv('AUTHOR', 'kevin')

APP_PORT = os.getenv('APP_PORT', 80)
PATH_DATA = os.getenv('PATH_DATA', './temp')

SLEEP_SEC_REMOVE = os.getenv('SLEEP_SEC_REMOVE', 5)
SLEEP_SEC_REMOVE_RESPONSE = os.getenv('SLEEP_SEC_REMOVE_RESPONSE', 20)

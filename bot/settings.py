# Settings for work with eljur api

ELJUR_API = 'https://api.eljur.ru/api'
ELJUR_DEVKEY = '9235e26e80ac2c509c48fe62db23642c'
ELJUR_OUT_FORMAT = 'json'

class MessageFolder:
    INBOX = 'inbox'
    SENT = 'sent'

# Settings for work with vk_api

VK_GROUP_TOKEN = 'b01a28e14ce154b4dd87adacaf4232efe5ef7eb57131c5799a7b9ccb0f7ad75646b41c8efdc8d1e0bd4a7'
VK_GROUP_ID = 200266598

# MySql Database

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'eljur-vk-bot'

# Default vendor
class DefaultVendor:
    NAME = 'ГБОУ Школа №46'
    VENDOR = '46.eljur.ru'
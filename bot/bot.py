from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

from bot.settings import DefaultVendor, VK_GROUP_ID, VK_GROUP_TOKEN
from bot import services


bot = SimpleLongPollBot(tokens=VK_GROUP_TOKEN, group_id=VK_GROUP_ID)

@bot.message_handler(bot.text_filter('начать'))
async def start_message_handler(event: bot.SimpleBotEvent) -> str:
    """
    Отправляет ответ на сообщение, для начала диалога,
    Получает event.answer из send_start_answer
    """
    answer = await services.send_start_answer(event)
    await answer

@bot.message_handler(bot.text_filter('войти в элжур'))
async def vendor_message_handler(event: bot.SimpleBotEvent) -> str:
    """
    Отправляет ответ на сообщение Войти в элжур
    Получает event.asnwer из services.send_choose_vendor_answer
    """
    answer = await services.send_choose_vendor_answer(event)
    await answer

@bot.message_handler(bot.text_filter(DefaultVendor.NAME.lower()))
async def login_message_handler(event: bot.SimpleBotEvent) -> str:
    """
    Отправляет ответ на сообщение cо стандартным вендором(settings.DefaultVendor)
    Получает текст сообщения из services.send_login_answer
    """
    answer = await services.send_login_answer(event)
    await answer
    
@bot.message_handler(bot.text_filter('другая школа'))
async def other_vendor_message_handler(event: bot.SimpleBotEvent) -> str:
    """
    Отправляет ответ на сообщение 'Другая школа' при выборе вендора
    Получает текст сообщения из services.send_other_vendor_answer
    """
    answer = await services.send_other_vendor_answer(event)
    await answer

@bot.message_handler(bot.text_contains_filter('.eljur.ru'))
async def login_message_handler_by_vendor(event: bot.SimpleBotEvent) -> str:
    """
    Отправляет ответ на сообщение с содержанием вендора другой школы
    Получает текст сообщения из services.send_login_by_vendor_answer
    """
    answer = await services.send_login_by_vendor_answer(event)
    await answer

@bot.message_handler(bot.text_filter('да'))
async def change_profile_handler(event: bot.SimpleBotEvent) -> str:
    """
    Отправляет ответ на сообщение "да"
    Получает текст сообщения из services.change_profile_answer
    """
    answer = await services.send_change_profile_answer(event)
    await answer

@bot.message_handler()
async def variables_messgae_handler(event: bot.SimpleBotEvent) -> str:
    """
    Отправляет ответ на сообщение с какими-либо данными(вендор, логин, пароль)
    Получает event.answer из send_variables_answer
    """
    answer = await services.send_variables_answer(event)
    await answer

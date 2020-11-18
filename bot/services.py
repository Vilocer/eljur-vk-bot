from vkwave.bots import SimpleBotEvent

from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor

from db.manager import get_or_create_profile_by_vk_id, update_profile_vendor, update_profile_login, update_profile_password, delete_profile, add_profile
from bot.settings import DefaultVendor


async def send_start_answer(event: SimpleBotEvent):
    """
    Отвечает на сообщение пользователя при команде 'Начало'
    Добавляет клавиатуру с кнопкой Войти в ЭлЖур
    Проверяет если ли его профил в бд, если нет, то создает его
    """
    profile = get_or_create_profile_by_vk_id(
        event.object.object.message.peer_id
    )
    user_data = (
        await event.api_ctx.users.get(
            user_ids=event.object.object.message.peer_id
            )
        ).response[0]
    keyboard = Keyboard(one_time=True)
    keyboard.add_text_button('Войти в ЭлЖур', color=ButtonColor.PRIMARY)
    return event.answer(
        message=f"""Привет, {user_data.first_name}! \n
            Для начала нужно войти в свой личный кабинет ЭлЖур.""",
        keyboard=keyboard.get_keyboard()
    )

async def send_choose_vendor_answer(event: SimpleBotEvent):
    """
    Отвечает на сообщение пользователя Войти в ЭлЖур
    """
    keyboard = Keyboard(one_time=True)
    keyboard.add_text_button(DefaultVendor.NAME, color=ButtonColor.PRIMARY)
    keyboard.add_row()
    keyboard.add_text_button('Другая школа', color=ButtonColor.PRIMARY)
    return event.answer(
        message='Пожалуйста, выберите свою школу.',
        keyboard=keyboard.get_keyboard()
    )

async def send_other_vendor_answer(event: SimpleBotEvent):
    """
    Просит ввести ссылку, по которой пользователь входит в свой элжур
    """
    return event.answer(
        message="""В таком случаи вам нужно ввести ссылку,
        по которой вы входите в свой элжур \n
        Например: 46.eljur.ru или https://46.eljur.ru/
        """
    )

async def send_login_answer(event: SimpleBotEvent):
    """
    Вызывается после выбора вендора
    Просит ввести пользователя логин от элжура
    """
    profile = get_or_create_profile_by_vk_id(
        event.object.object.message.peer_id
    )
    vendor = update_profile_vendor(
        event.object.object.message.peer_id,
        DefaultVendor.VENDOR
    )
    return event.answer(
        message=f"""Ваша школа - {event.object.object.message.text} ({vendor}). \n
        Для продолжение введите логин ЭлЖур."""
    )

async def send_login_by_vendor_answer(event: SimpleBotEvent):
    """
    Просит ввести пользователя логин от элжура
    После того как бот получил вендора
    """
    profile = get_or_create_profile_by_vk_id(
        event.object.object.message.peer_id
    )
    update_profile_vendor(
        event.object.object.message.peer_id,
        event.object.object.message.text
    )
    return event.answer(
        message=f"""Адресс дневника вашей школы - {event.object.object.message.text}. \n
        Для продолжение введите логин ЭлЖур."""
    )

async def send_change_profile_answer(event: SimpleBotEvent):
    """"
    Пересоздаёт профиль пользователя
    Отправляет сообщение из send_start_answer
    """
    delete_profile(
        event.object.object.message.peer_id

    )
    profile = get_or_create_profile_by_vk_id(
        event.object.object.message.peer_id
    )
    keyboard = Keyboard(one_time=True)
    keyboard.add_text_button('Войти в ЭлЖур', color=ButtonColor.PRIMARY)
    return event.answer(
        message=f"""Вы вышли из аккаунта ЭлЖур.""",
        keyboard=keyboard.get_keyboard()
    )


async def send_variables_answer(event: SimpleBotEvent):
    """
    Проверяет какие поля в профиле пользователя пусты,
    И записывает в первое пустое полученное значение
    """
    profile = get_or_create_profile_by_vk_id(
        event.object.object.message.peer_id
    )
    message = None
    keyboard = None
    for field in profile[0]:
        value = profile[0][field]
        if not value:
            if field == 'eljur_vendor':
                update_profile_vendor(
                    event.object.object.message.peer_id,
                    event.object.object.message.text
                )
                message=f"""Адресс дневника вашей школы - {event.object.object.message.text}. \n
                Для продолжение введите логин ЭлЖур."""
                break
            if field == 'eljur_login':
                update_profile_login(
                    event.object.object.message.peer_id,
                    event.object.object.message.text
                )
                message=f"""Ваш логин - {event.object.object.message.text}. \n
                Для продолжение введите пароль от ЭлЖур."""
                break
            if field == 'eljur_password':
                update_profile_password(
                    event.object.object.message.peer_id,
                    event.object.object.message.text
                )
                message=f"""Данные авторизации приняты"""
                break
    if not message:
        message = 'Вы уже ввели свой логин и пароль. Вы действительно хотите изменить их?'
        keyboard = Keyboard()
        keyboard.add_text_button('Да', color=ButtonColor.POSITIVE)
        keyboard.add_text_button('Нет', color=ButtonColor.NEGATIVE)
        keyboard = keyboard.get_keyboard()
    return event.answer(
        message=message,
        keyboard=keyboard
    )
from db.db import DataBase


def get_all_profiles():
    """
    Возвращает все профили пользователей
    """
    db = DataBase()
    profiles = db.fetch('SELECT * FROM `profiles`;')
    db.close_connection()

    return profiles

def get_profile_by_vk_id(vk_id: int):
    """
    Возвращает профиль по полю vk_id
    """
    db = DataBase()
    profile = db.fetch(
        f'SELECT * FROM `profiles` WHERE vk_user_id = {vk_id};'
    )
    db.close_connection()
    return profile

def add_profile(vk_id: int):
    """
    Добавляет новый профиль пользователя и возвращает его
    """
    db = DataBase()
    db.commit(
        f'INSERT INTO `profiles` (vk_user_id) VALUES (%s);',
        values=[vk_id]
    )
    db.close_connection()

    return get_profile_by_vk_id(vk_id)

def delete_profile(vk_id: int):
    """
    Удаляет профиль пользователя и возвращает True
    """
    db = DataBase()
    db.commit(
        f"""DELETE FROM `profiles`
        WHERE `profiles`.`vk_user_id` = {str(vk_id)}
        """
    )
    db.close_connection()

    return True

def get_or_create_profile_by_vk_id(vk_id: int):
    """
    Проверяет наличие профиля в бд по vk_id
    Если такого нет, то создает его
    """
    profile = get_profile_by_vk_id(vk_id)
    if not profile:
        profile = add_profile(vk_id)
    return profile

def update_profile_vendor(vk_id: int, vendor: str):
    """
    Обновляет поле eljur_vendor в профиле пользователя в бд
    """
    db = DataBase()
    db.commit(
        f"""UPDATE `profiles`
            SET `eljur_vendor` = '{vendor}'
            WHERE `profiles`.`vk_user_id` = {str(vk_id)}
        """
    )
    db.close_connection()
    return vendor

def update_profile_login(vk_id: int, login: str):
    """
    Обновляет поле eljur_login в профиле пользователя в бд
    """
    db = DataBase()
    db.commit(
        f"""UPDATE `profiles`
            SET `eljur_login` = '{login}'
            WHERE `profiles`.`vk_user_id` = {str(vk_id)}
        """
    )
    db.close_connection()
    return login

def update_profile_password(vk_id: int, password: str):
    """
    Обновляет поле eljur_password в профиле пользователя в бд
    """
    db = DataBase()
    db.commit(
        f"""UPDATE `profiles`
            SET `eljur_password` = '{password}'
            WHERE `profiles`.`vk_user_id` = {str(vk_id)}
        """
    )
    db.close_connection()
    return password

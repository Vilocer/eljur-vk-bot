from mysql import connector

from bot import settings


class DataBase:
    """
    Класс, для совершения SQL запросов к базе данных
    """
    def __init__(self):
        """
        Создает подключения к базе данных и создает курсор
        """
        self.connection = connector.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def fetch(self, query: str):
        """
        Возвращает релуьтата SQl запроса - SELECT 
        """
        self.cursor.execute(query)
        result = []
        for row in self.cursor:
            result.append(row)

        return result

    def commit(self, query: str, values: dict = []):
        """
        Выполняет SQL запрос подставляя значения и совершаю запись в бд
        Возвращает количество записанных строк
        """
        self.cursor.execute(query, values)
        self.connection.commit()

        return self.cursor.rowcount

    def close_connection(self):
        """
        Закрывает соединение к базе данных
        """  
        self.connection.close()
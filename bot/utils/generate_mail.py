# from mailpytm import MailTMApi
#
# # Создаем аккаунт
# account = MailTMApi.create_email()
# print(f"Email адрес: {account.address}")
#
# # Ждем новое письмо (таймаут 90 секунд)
# try:
#     print("Ожидание письма...")
#     new_message = account.wait_for_new_message(timeout=90)
#     print(f"Получено письмо!")
#     print(f"Тема: {new_message.get('subject')}")
#     print(f"Текст: {new_message.get('text', {}).get('body', 'Нет текста')}")
# except TimeoutError:
#     print("Письмо не пришло за отведенное время")

import asyncio
from mailtm import Email


async def main():
    # Создаем объект и инициализируем
    test = Email()
    await test.init()

    # Регистрируем новый email адрес
    await test.register()
    print(f"Email адрес: {test.address}")

    # Функция-слушатель, которая вызывается при получении письма
    def listener(message: dict):
        print(f"\nТема: {message['subject']}")
        print(f"Текст: {message.get('text', message.get('html', 'Нет содержимого'))}")

    print("Ожидание новых писем...")
    # Запускаем прослушивание (работает бесконечно)
    await test.start(listener, interval=5)


# Запуск
asyncio.run(main())
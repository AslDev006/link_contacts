from telebot import TeleBot

from LINK_SITE.config import TOKEN

bot = TeleBot(token=TOKEN)


# @bot.message_handler(commands=['start'])
# def send_start(message: Message):
#     bot.send_message(text="Salom", chat_id=message.chat.id)


def get_post(data):
    bot.send_message(chat_id=5445344730, text=f"Ism: {data['first_name']}\n"
                                              f"Familya: {data['last_name']}\n"
                                              f"Address: {data['address']}\n"
                                              f"Phone number: {data['phone_number']}\n"
                                              f"Course 1: {data['course_1']}")

# print("Started")
# if __name__ == "__main__":
#     bot.infinity_polling()
# print('STOP BOT ...')

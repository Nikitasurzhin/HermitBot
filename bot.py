import random
import telebot
import output_format

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    anime_amount = 10500

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я помогу тебе найти что посмотреть! Напиши /randomanime")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/randomanime - зарандомить аниме для просмотра")
    elif message.text == '/randomanime':

        anime_num = random.randint(0, anime_amount)

        bot.send_message(chat_id, output_format.get_output(anime_num))
        print(f'Bot sent message:\n{output_format.get_output(anime_num)}')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

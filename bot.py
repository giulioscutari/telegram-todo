import os
import telebot
import time

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "nice")


@bot.message_handler(commands=["set_free"])
def set_notification(message):
    sent_msg = bot.send_message(message.chat.id, "enter the time in seconds")

    bot.register_next_step_handler(sent_msg, notify)


@bot.message_handler(commands=["set_buttons"])
def set_notification(message):
    markup = telebot.types.InlineKeyboardMarkup()
    for i in range(5):
        markup.add(
            telebot.types.InlineKeyboardButton(
                text=str(i + 1), callback_data=str(i + 1)
            )
        )
    sent_msg = bot.send_message(
        message.chat.id, "enter the time in seconds", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def notify_callback(call):
    print("Callback!", call)
    time.sleep(int(call.data))
    sent_msg = bot.send_message(
        call.message.chat.id, "this is your notification"
    )
    bot.register_next_step_handler(sent_msg, notify)


def notify(message):
    bot.send_message(message.chat.id, "ty, notification on the way")
    wait_time = int(message.text)
    time.sleep(wait_time)
    sent_msg = bot.send_message(message.chat.id, "this is your notification")


bot.infinity_polling()

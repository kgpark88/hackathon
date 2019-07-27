import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import emoji

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    keyboard = [
                [InlineKeyboardButton("참가대상", callback_data='1'),
                 InlineKeyboardButton("해커톤 주제", callback_data='2')],
                [InlineKeyboardButton("해커톤 장소", callback_data='3'),
                 InlineKeyboardButton("참가신청", callback_data='4')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('안녕하세요! 전남대 이노베이션 해커톤 안내봇입니다.', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    if query.data == "1":
        em = emoji.emojize(':smile:', use_aliases=True)
        bot.editMessageText(text="전남대학교 학생 누구나~ %s " % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

    elif query.data == "2":
        em = emoji.emojize(':thumbs_up:', use_aliases=True)
        bot.editMessageText(text="AI와 BIG DATA를 이용한 전남대학교를 변화시킬 아이디어 %s " % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

    elif query.data == "3":
        em = emoji.emojize(':collision:', use_aliases=True)
        bot.editMessageText(text="8월 9일(금) 08:30~18:30 공과대학 2호관 영명홀 %s " % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)


    elif query.data == "4":
        em = emoji.emojize(':collision:', use_aliases=True)
        bot.editMessageText(text="http://hackathon.econovation.kr/",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def help(bot, update):
    update.message.reply_text("/지니야 를 입력해주세요.")


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


# 텔레그램 봇 Token
updater = Updater('Telegram-bot-token')
updater.dispatcher.add_handler(CommandHandler('지니야', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('도움말', help))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
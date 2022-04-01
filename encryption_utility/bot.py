import logging
import os

from telegram import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ParseMode, 
    Document
)

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters 
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hello, ' + update.message.chat.first_name)

def help(update, context):
    update.message.reply_text(
    """
*Telegram stuff*
/help - see this message
/stats - see your stats in utility usage

*Utility stuff*
Send me file with the caption:

To encrypt the file type `encrypt encr_mode args`
- Possible `encr_mode`:
1) `caesar`, where `args = unsigned_int key`
2) `vigenere`, where `args = str key`
3) `vernam`, where `args = str key`
4) `block`, where `args = unsigned_int key`

To decrypt the file type `decrypt decr_mode args`
- Possible `decr_mode`:
1) `caesar`, where `args = [unsigned_int key]`
    - If no `key` passed, breaking a cipher begins in the assumption of an English text 
2) `vigenere`, where `args = str key`
3) `vernam`, where `args = str key`
4) `block`, where `args = unsigned_int key`
    """, parse_mode=ParseMode.MARKDOWN)

def stats(update, context): # TODO: just keyboard usage example 
    keyboard = ReplyKeyboardMarkup([
        ['1', '2'],
        ['3', '4']
    ], one_time_keyboard=True)
    update.message.reply_text('_Some text_', parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard) 

def utility_query(update, context):
    temp_filename = "temp_file.txt"
    response_filename = "response.txt"
    query_filename = "query.txt"
    files = ' '.join([temp_filename, response_filename, query_filename])

    query_words = update.message.caption.split()
    if (len(query_words) == 0):
        update.message.reply_text("Empty query is not supported")
        return
    query_words.insert(1, temp_filename)
    with open(query_filename, 'w') as query:
        query.write(" ".join(query_words))

    f = context.bot.getFile(update.message.document.file_id)
    f.download('./' + temp_filename)
    os.system('python3 main.py < ' + query_filename + ' > ' + response_filename)
    response_text = ''
    with open(response_filename, 'r') as response:
        response_text = response.read()
    update.message.reply_document(
        open(temp_filename, 'rb'), 
        filename = update.message.document.file_name,
        caption=response_text
    )
    os.system('rm ' + files)

def error(update, context):
    logger.warning('ERROR: Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text("Error has been occured!")

def main():
    updater = Updater("1716312395:AAHNG2oy48lC-EnuLfCYCO80IVHUGrNODS8", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(MessageHandler(Filters.document, utility_query))

    dp.add_error_handler(error)

    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()


import os

from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from telegramapp.db_utils import insert

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def cancel(update, context):
    context.user_data['new_beer'].remove()
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def end(update, context):
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


class Beer:
    def __init__(self):
        self.data = {'Name': "",
                     "ABV": "",
                     "Rarity": "",
                     "ImageFile": "",
                     "Animation": "temp",
                     }

    def remove(self, context):
        # if canceling during beer creation
        if context.user_data['new_beer'].data["ImageFile"] != "":
            os.remove('images/{}'.format(context.user_data["new_beer"].data["ImageFile"]))

    def update(self, oldData):
        self.data['Name'] = oldData['Name']
        self.data["ABV"] = oldData["ABV"]

    def upload(self):
        insert(self.data)

    def check_data(self):
        for key in self.data.items():
            if key == "":
                return False
        return True


    def check_image(self, user):
        if self.data['ImageFile'] == '{}.jpg'.format(user):
            filename = '{}.jpg'.format(self.data['Name'])
            self.data['ImageFile'] == filename
            os.rename('images/{}.jpg', 'images/{}'.format(user, filename))
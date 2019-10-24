from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import run_async, ConversationHandler, CommandHandler, RegexHandler, MessageHandler, Filters

from telegramapp.class_utils import end, Beer, cancel
from telegramapp.db_utils import get_column, get_beer_by_name

NEWBEER_ENTRY, SET_NAME, SET_ABV, SET_RARITY, SET_LOGO = range(5)
DEMO = range(1)
radio_keyboard = [['1', '2', '3', '4', '5']]
create_beer_keyboard = [['Name', 'ABV', 'Rarity', 'Logo', 'Save Beer']]


def set_name(update, context):
    text = update.message.text
    context.user_data['new_beer'].data['Name'] = text
    update.message.reply_text("Name Selected\n"
                              'Send /cancel to exit.\n'
                              'Current new beer data \n'
                              'Name = {}\n'
                              'ABV = {}\n'
                              'Rarity = {}\n'
                              'Logo File = {}\n'
                              'Animation = {}\n'
                              'Which value would you like to enter?'.format(
        context.user_data['new_beer'].data['Name'],
        context.user_data['new_beer'].data['ABV'],
        context.user_data['new_beer'].data['Rarity'],
        context.user_data['new_beer'].data['ImageFile'],
        context.user_data['new_beer'].data['Animation']),
                              reply_markup=ReplyKeyboardMarkup(create_beer_keyboard,
                                                               one_time_keyboard=True,
                                                               resize_keyboard=True))

    return NEWBEER_ENTRY


def get_name(update, context):
    update.message.reply_text("Please enter the name of the beer")

    return SET_NAME


def set_abv(update, context):
    text = update.message.text
    context.user_data['new_beer'].data['ABV'] = text
    update.message.reply_text("ABV Selected\n"
                              'Send /cancel to exit.\n'
                              'Current new beer data \n'
                              'Name = {}\n'
                              'ABV = {}\n'
                              'Rarity = {}\n'
                              'Logo File = {}\n'
                              'Animation = {}\n'
                              'Which value would you like to enter?'.format(
        context.user_data['new_beer'].data['Name'],
        context.user_data['new_beer'].data['ABV'],
        context.user_data['new_beer'].data['Rarity'],
        context.user_data['new_beer'].data['ImageFile'],
        context.user_data['new_beer'].data['Animation']),
        reply_markup=ReplyKeyboardMarkup(create_beer_keyboard,
                                         one_time_keyboard=True,
                                         resize_keyboard=True))

    return NEWBEER_ENTRY


def get_abv(update, context):
    update.message.reply_text("Please enter the ABV of the beer",
                              reply_markup=ReplyKeyboardMarkup(radio_keyboard,
                                                               one_time_keyboard=True,
                                                               resize_keyboard=True))

    return SET_ABV


def set_rarity(update, context):
    text = update.message.text
    context.user_data['new_beer'].data['Rarity'] = text
    update.message.reply_text("Rarity Selected\n"
                              'Send /cancel to exit.\n'
                              'Current new beer data \n'
                              'Name = {}\n'
                              'ABV = {}\n'
                              'Rarity = {}\n'
                              'Logo File = {}\n'
                              'Animation = {}\n'
                              'Which value would you like to enter?'.format(
        context.user_data['new_beer'].data['Name'],
        context.user_data['new_beer'].data['ABV'],
        context.user_data['new_beer'].data['Rarity'],
        context.user_data['new_beer'].data['ImageFile'],
        context.user_data['new_beer'].data['Animation']),
        reply_markup=ReplyKeyboardMarkup(create_beer_keyboard,
                                         one_time_keyboard=True,
                                         resize_keyboard=True))

    return NEWBEER_ENTRY


def get_rarity(update, context):
    update.message.reply_text("Please enter the Rarity of the beer",
                              reply_markup=ReplyKeyboardMarkup(radio_keyboard,
                                                               one_time_keyboard=True,
                                                               resize_keyboard=True))

    return SET_RARITY


def set_logo(update, context):
    photo_file = update.message.photo[-1].get_file()
    name = context.user_data['new_beer'].data['Name']
    if name == "":
        name = update.message.from_user
    photo_file.download('images/{}.jpg'.format(name))
    context.user_data['new_beer'].data['ImageFile'] = '{}.jpg'.format(name)
    update.message.reply_text("Logo Selected\n"
                              'Send /cancel to exit.\n'
                              'Current new beer data \n'
                              'Name = {}\n'
                              'ABV = {}\n'
                              'Rarity = {}\n'
                              'Logo File = {}\n'
                              'Animation = {}\n'
                              'Which value would you like to enter?'.format(
        context.user_data['new_beer'].data['Name'],
        context.user_data['new_beer'].data['ABV'],
        context.user_data['new_beer'].data['Rarity'],
        context.user_data['new_beer'].data['ImageFile'],
        context.user_data['new_beer'].data['Animation']),
        reply_markup=ReplyKeyboardMarkup(create_beer_keyboard,
                                         one_time_keyboard=True,
                                         resize_keyboard=True))

    return NEWBEER_ENTRY


def get_logo(update, context):
    update.message.reply_text("Please select a photo you would like to use as the logo for this beer",
                              reply_markup=ReplyKeyboardRemove())

    return SET_LOGO


def commit_beer(update, context):
    #if data is missing continue with new beer routine
    if not context.user_data['new_beer'].check_data():
        update.message.reply_text("Data Missing\n"
                                  'Send /cancel to exit.\n'
                                  'Current new beer data \n'
                                  'Name = {}\n'
                                  'ABV = {}\n'
                                  'Rarity = {}\n'
                                  'Logo File = {}\n'
                                  'Animation = {}\n'
                                  'Which value would you like to enter?'.format(
            context.user_data['new_beer'].data['Name'],
            context.user_data['new_beer'].data['ABV'],
            context.user_data['new_beer'].data['Rarity'],
            context.user_data['new_beer'].data['ImageFile'],
            context.user_data['new_beer'].data['Animation']),
            reply_markup=ReplyKeyboardMarkup(create_beer_keyboard,
                                             one_time_keyboard=True,
                                             resize_keyboard=True))
        return NEWBEER_ENTRY

    else:
        #rename the saved image if necessary
        data = update.message.from_user
        context.user_data['new_beer'].check_image(data)
        #save to db
        context.user_data['new_beer'].upload()
        update.message.reply_text('Bye! I hope we can talk again some day.',
                                  reply_markup=ReplyKeyboardRemove())

        return ConversationHandler.END


@run_async
def new(update, context):
    if 'new_beer' not in context.user_data:
        context.user_data['new_beer'] = Beer()

    update.message.reply_text("Welcome to the Beer Insertion Program\n"
                              'Send /cancel to exit.\n'
                              'Current new beer data \n'
                              'Name = {}\n'
                              'ABV = {}\n'
                              'Rarity = {}\n'
                              'Logo File = {}\n'
                              'Animation = {}\n'
                              'Which value would you like to enter?'.format(
        context.user_data['new_beer'].data['Name'],
        context.user_data['new_beer'].data['ABV'],
        context.user_data['new_beer'].data['Rarity'],
        context.user_data['new_beer'].data['ImageFile'],
        context.user_data['new_beer'].data['Animation']),
        reply_markup=ReplyKeyboardMarkup(create_beer_keyboard,
                                         one_time_keyboard=True,
                                         resize_keyboard=True))

    return NEWBEER_ENTRY


@run_async
def edit(update, context):
    pass


@run_async
def set_taps(update, context):
    pass


@run_async
def start_demo(update, context):
    beer_names = get_column("Name")
    print(beer_names)
    beer_name_keyboard = [beer_names]
    update.message.reply_text("Which beer would you like to demo?\n"
                              "If you know the name of the beer you can also use that.\n"
                              "Just type it and hit send!",
                              reply_markup=ReplyKeyboardMarkup(beer_name_keyboard,
                                                               one_time_keyboard=True,
                                                               resize_keyboard=True))

    return DEMO


def run_demo(update, context):
    name = update.message.text
    try:
        beer_dict = get_beer_by_name(name)[0]
        update.message.reply_text('Selected beer data \n'
                                  'Name = {}\n'
                                  'ABV = {}\n'
                                  'Rarity = {}\n'
                                  'Logo File = {}\n'
                                  'Animation = {}\n'.
                                  format(beer_dict['name'],
                                         beer_dict['abv'],
                                         beer_dict['rarity'],
                                         beer_dict['image_file'],
                                         beer_dict['animation']),
                                  reply_markup=ReplyKeyboardRemove())
        #led_demo(beer_dict)
        end(update, context)
    except:
        update.message.reply_text("That beer is unavailable, please select another\n"
                                  "If you know the name of the beer you can also use that.\n"
                                  "Just type it and hit send!",
                                  reply_markup=ReplyKeyboardMarkup(create_beer_keyboard,
                                                                   one_time_keyboard=True,
                                                                   resize_keyboard=True))
        return DEMO


conv_handler = ConversationHandler(
        entry_points=[CommandHandler('new', new),
                      CommandHandler('edit', edit),
                      CommandHandler('set', set_taps),
                      CommandHandler('demo', start_demo)],

        states={
            ##########     CREATE NEW BEERS     ############
            NEWBEER_ENTRY: [RegexHandler('^Name$', get_name, pass_user_data=True),
                            RegexHandler('^ABV$', get_abv, pass_user_data=True),
                            RegexHandler('^Rarity$', get_rarity, pass_user_data=True),
                            RegexHandler('^Logo$', get_logo, pass_user_data=True),
                            RegexHandler('^Save Beer$', commit_beer, pass_user_data=True)],
            SET_NAME: [MessageHandler(Filters.text, set_name, pass_user_data=True)],
            SET_ABV: [MessageHandler(Filters.text, set_abv, pass_user_data=True)],
            SET_RARITY: [MessageHandler(Filters.text, set_rarity, pass_user_data=True)],
            SET_LOGO: [MessageHandler(Filters.photo, set_logo, pass_user_data=True)],

            #########      DEMO ROUTINE     ##########
            DEMO: [MessageHandler(Filters.text, run_demo, pass_user_data=True)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

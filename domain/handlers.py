from telegram import Update , Contact , KeyboardButton
from telegram.ext import CallbackContext , ConversationHandler , CommandHandler , MessageHandler , Filters
from .messages import WELCOME_MESSAGE 
from .keyboards import WELCOME_KEYBOARD
from .db import UserDB
from .verifier import check_domain
userdb = UserDB('users.json')

VERIFY, CHECK_DOMAIN = range(2)

# create a function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboards = WELCOME_KEYBOARD

    if userdb.is_user(user.id):
        update.message.reply_html(
            text="""Hello again! we're glad you're back.""",
            reply_markup=keyboards
        )
        return 

    userdb.add_user(chat_id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username)

    update.message.reply_html(
        text=f"""Welcome <b>{user.full_name}</b>! To the Domain Verifier.""",
        reply_markup=keyboards
    )


def unknown(update: Update, context: CallbackContext) -> None:
    """Send a message when an unknown command is issued."""
    
    update.message.reply_text(text="Sorry, I didn't understand that command.")


def verify(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Please enter the domain you want to check:')
    return CHECK_DOMAIN

def check_domain_handler(update: Update, context: CallbackContext) -> int:
    domain = update.message.text
    result = check_domain(domain)
    update.message.reply_text(result)
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Verification cancelled.')
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('verify', verify), MessageHandler(Filters.regex('^(Verify|verify)$'), verify)],
    states={
        CHECK_DOMAIN: [MessageHandler(Filters.text & ~Filters.command, check_domain_handler)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

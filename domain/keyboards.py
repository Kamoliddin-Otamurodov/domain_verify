from telegram import KeyboardButton, ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton


WELCOME_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Verify"),
        ]
    ]
    ,
    resize_keyboard=True,
)
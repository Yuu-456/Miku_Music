from NIXA import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

NETWORK_USERNAME = "voidxnetwork"
PHOTO = "https://telegra.ph/file/e5808adf6d1bc748d6440.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "voidxnetwork":
    def uchiha(update: Update, context: CallbackContext):

        TEXT = f"""
Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork)

━━━━━━━━━━━━━━━━━━━━━━━━
✪ ᴠᴏɪᴅ ɪꜱ ᴀɴ ᴀɴɪᴍᴇ ʙᴀꜱᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ ꜱᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ.
✪ ɢᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ɪꜰ ɪᴛ ᴅʀᴀᴡꜱ ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ. 
━━━━━━━━━━━━━━━━━━━━━━━━
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/VoidXNetwork")],
                    [
                    InlineKeyboardButton(text="【ᴜꜱᴇʀᴛᴀɢ】", url="https://t.me/VoidxNetwork/136"),
                    InlineKeyboardButton(text="【ɪɴᴅᴇx】", url="https://t.me/VoidxNetwork/15")
                    ],
                ]
            ),
        )


    uchiha_handler = CommandHandler(("void", "network", "net"), uchiha, run_async = True)
    dispatcher.add_handler(uchiha_handler)

    __help__ = """
    ──「【V๏ɪ፝֟𝔡】Network」──                         
    
  ❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "ᴠᴏɪᴅ"

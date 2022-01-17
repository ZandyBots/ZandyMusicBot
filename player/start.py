from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import SOURCE_CODE, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from plugins.tr import TGPK_TEXT, VSONG_TEXT, PASTE_TEXT, INFO_TEXT, STREAM_TEXT, START_TEXT, HELP_TEXT
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("❔ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("💥 Sᴏᴜʀᴄᴇ", url=f"https://{SOURCE_CODE}"),
                InlineKeyboardButton("Channel 📢", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤖 Bot Owner", url=f"https://t.me/anojysr"),
                InlineKeyboardButton("Support 👥", url=f"https://t.me/{SUPPORT_GROUP}"),
            ],
            [
               InlineKeyboardButton("💞 Add To Group 💞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
      m=await message.reply_photo(
                                  photo="https://e1.yotools.net/images/user_image/2022/01/61e57a8a16fe8.jpg", 
                                  caption=START_TEXT.format(message.from_user.first_name, message.from_user.id),
                                  reply_markup=reply_markup
      )      
   else:
      await message.reply(f"**👋 Hey Zandy Music Bot is Alive! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Sᴛʀᴇᴀᴍ", callback_data="stream"),
                InlineKeyboardButton ("Iɴꜰᴏ Wʜᴏɪꜱ", callback_data="info"),
            ],
            [
                InlineKeyboardButton("Vɪᴅᴇᴏ Sᴏɴɢ", callback_data="vsong"),
                InlineKeyboardButton ("Pᴀꜱᴛᴇ", callback_data="paste"),
            ],
            [
               InlineKeyboardButton("Tᴇʟᴇ ✮ ɢʀᴀᴘʜ", callback_data="tgph"),
            ],
            [
               InlineKeyboardButton("╰✰ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
               InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
               InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ ✰╮", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="tgph":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                TGPK_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="stream":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                STREAM_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="paste":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                PASTE_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="vsong":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                VSONG_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="info":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                INFO_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("❔ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("💥 Sᴏᴜʀᴄᴇ", url=f"https://{SOURCE_CODE}"),
                InlineKeyboardButton("Cʜᴀɴɴᴇʟ 📢", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤖 Bᴏᴛ Lɪꜱᴛ", url=f"https://t.me/anojysr"),
                InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ 👥", url=f"https://t.me/{SUPPORT_GROUP}"),
            ],
            [
               InlineKeyboardButton("💞 Sᴜᴍᴍᴏɴ Mᴇ 💞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

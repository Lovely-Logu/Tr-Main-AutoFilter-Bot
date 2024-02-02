class script(object):  
    START_TXT = """<b>👋 ʜᴇʟᴏ {user}. <i>{}</i>

😇 ᴍʏ ɴᴀᴍᴇ ɪs  {bot}.
ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴇᴅ ᴍᴏᴠɪᴇs & ᴡᴇʙsᴇʀɪᴇs & ᴄᴀʀᴛᴏᴏɴᴇs, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ... 🔥

❤️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Tr_LinksZz ❤️</b>"""
    
    HELP_TXT = """<b>ʜᴇʏ {}\nʜᴇʀᴇ ᴍs ᴍʏ ʜᴇʟᴘ</b>"""

    ABOUT_TXT = """<b>✯ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/Tr_ProAutoFilter_Bot>𝚃𝚁 𝙿𝚁𝙾 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙱𝙾𝚃</a>
✯ ᴏᴡɴᴇʀ : <a href=https://t.me/Tr_LinksZz_Admin_Chat_bot>👑 𝖑𝖔𝖌𝖆𝖓𝖆𝖙𝖍𝖆𝖓 👑</a>
✯ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href=tg://settings>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
✯ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Tr_LinksZz_Admin_Chat_bot>👑 𝖑𝖔𝖌𝖆𝖓𝖆𝖙𝖍𝖆𝖓 👑</a>
✯ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Tr_LinksZz>Tʀ Mᴏᴠɪᴇs™</a>
✯ ʟɪʙʀᴀʀʏ : <a href=https://docs.pyrogram.org/>ᴘʀᴏɢʀᴀᴍ</a>
✯ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org/download/releases/3.0/>ᴘʏᴛʜᴏɴ 3</a>
✯ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ : <a href=https://www.mongodb.com/>ᴍᴏɴɢᴏ ᴅʙ</a>
✯ ᴍʏ sᴇʀᴠᴇʀ : <a href=https://render.com/>ʀᴇɴᴅᴇʀ</a>
✯ ᴍʏ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : 𝚅4.5.0 [ sᴛᴀʙʟᴇ ]</b>"""
   
    SOURCE_TXT = """<b>𝗡𝗼𝘁𝗲 :
- 𝖳𝗁𝗂𝗌 𝖨𝗌 𝖠 𝖮𝗉𝖾𝗇 𝖲𝗈𝗎𝗋𝖼𝖾 𝖯𝗋𝗈𝗃𝖾𝖼𝗍.
- 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖧𝖺𝗌 𝖫𝖺𝗍𝖾𝗌𝗍 𝖠𝗇𝖽 𝖠𝖽𝗏𝖺𝗇𝖼𝖾𝖽 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌.
- 𝖲𝗈𝗎𝗋𝖼𝖾 - 𝖢𝗅𝗂𝖼𝗄 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾 𝖡𝗎𝗍𝗍𝗈𝗇.
𝗗𝗲𝘃𝘀 :
✯ <a href=https://t.me/Tr_LinksZz_Admin_Chat_bot>👑 𝖑𝖔𝖌𝖆𝖓𝖆𝖙𝖍𝖆𝖓 👑</a></b>"""
    
    SUPRT_INFO_TXT = """<b>🌟𝖩𝗈𝗂𝗇 𝖮𝗎𝗋 𝖬𝗒 𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌 & 𝖦𝗋𝗈𝗎𝗉𝗌 𝖬𝗈𝖽𝗎𝗅𝖾.🌟
🎟️ 𝖬𝗈𝗏𝗂𝖾𝗌 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅.
🍿 𝖬𝗈𝗏𝗂𝖾𝗌 𝖱𝖾𝗊𝗎𝖾𝗌𝗂𝗇𝗀 𝖦𝗋𝗈𝗎𝗉.
✨ 𝖠𝗅𝗅 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾𝗌 𝖬𝗈𝗏𝗂𝖾𝗌 & 𝖲𝖾𝗋𝗂𝖾𝗌.
🗣️ 𝖡𝗈𝗍 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉.
🤖 𝖡𝗈𝗍 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅.</b>""" 

    CREDITS_TXT = """<b>❉ 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 ❉ :
➳ Tʜᴀɴᴋ Tᴏ : <a href=https://t.me/mkn_bots_updates>Mᴋɴ Bᴏᴛs™</a> 
➳ Tʜᴀɴᴋ Tᴏ Dᴇᴠᴇʟᴏᴘᴇʀ  : <a href=https://t.me/Mr_MKN>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>  
➳ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href=https://t.me/Tr_LinksZz_Admin_Chat_bot>👑 𝖑𝖔𝖌𝖆𝖓𝖆𝖙𝖍𝖆𝖓 👑</a> 
➳ Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : <a href=https://t.me/Tr_LinksZz>ᴛʀ ᴍᴏᴠɪᴇs™</a> 
➳ Fᴇᴀᴛᴜʀᴇ Aᴅᴅᴇᴅ Bʏ : <a href=https://t.me/mallufiles><b>𝖬𝖺𝗅𝗅𝗎𝖥𝗂𝗅𝖾𝗌™</b></a> 
 
✦ 𝐌𝐚𝐢𝐧𝐥𝐲 𝐄𝐝𝐢𝐭𝐭𝐞𝐝 ✦ :
➳ Mᴀɪɴʟʏ Eᴅɪᴛᴇᴅ Bʏ : <a href=https://t.me/Tr_LinksZz_Admin_Chat_bot>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a> 
➳ Sᴘᴇᴄɪᴀʟ Tʜᴀɴᴋs Tᴏ : <a href=https://t.me/mallufiles>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a> 
 
★  [ <a href=https://t.me/H21TG>Sᴘᴇᴄɪᴀʟ Tʜᴀɴᴋs Tᴏ Dᴇᴠᴇʟᴏᴘᴇʀ</a> ]  ★</b>"""

    RULES_TXT = """<b>🔋 𝗚𝗥𝗢𝗨𝗣 𝗥𝗨𝗟𝗘𝗦 🔋 
 
‣ Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ : 
› ᴀᴠᴀᴛᴀʀ 2009 ✅ 
› ᴀᴠᴀᴛᴀʀ ᴛᴀᴍɪʟ ✅ 
› ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌ 
› ᴀᴠᴀᴛᴀʀ ᴛᴀᴍɪʟ ᴅᴜʙʙᴇᴅ..❌ 
 
‣ Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛᴇ :  
› ᴀʏᴀʟɪ S01 ✅ 
› ᴀʏᴀʟɪ S01E01 ✅ 
› ᴀʏᴀʟɪ S01 ᴛᴀᴍɪʟ ✅ 
› ᴀʏᴀʟɪ S01 ᴛᴀᴍɪʟ ᴅᴜʙʙ. ❌ 
› ᴀʏᴀʟɪ sᴇᴀsᴏɴ 1 ❌ 
› ᴀʏᴀʟɪ ᴡᴇʙ sᴇʀɪᴇs ❌ 
 
‣ ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ sᴇʟғ ᴘʀᴏᴍᴏᴛɪᴏɴ. 
 
‣ ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ.. 
 
‣ ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇsᴛ ᴀɴʏ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇs.. 
 
🪄 ɴᴏᴛᴇ :- 𝖠ʟʟ ᴍᴇ𝗌𝗌ᴀɢᴇ𝗌 ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 5 ᴍɪɴᴜᴛᴇ𝗌 ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪ𝗌𝗌ᴜᴇ𝗌.⚡ 
 
🦋 ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ ☞ <a href=tg://settings>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a> 🦋 
 
❤️ Powered By : @Tr_LinksZz ❤️</b>"""

    DELF_TXT = """<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ...</b>"""
    
    FILE_TXT = """<b>➤ 𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗙𝗶𝗹𝗲

<i>Bʏ Usɪɴɢ Tʜɪs Mᴏᴅᴜʟᴇ Yᴏᴜ Cᴀɴ Sᴛᴏʀᴇ Fɪʟᴇs Iɴ Mʏ Dᴀᴛᴀʙᴀsᴇ Aɴᴅ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ A Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ  Tᴏ Aᴄᴄᴇss Tʜᴇ Sᴀᴠᴇᴅ Fɪʟᴇs. Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Fɪʟᴇs Fʀᴏᴍ A Pᴜʙʟɪᴄ Cʜᴀɴɴᴇʟ Sᴇɴᴅ Tʜᴇ Fɪʟᴇ Lɪɴᴋ Oɴʟʏ  Oʀ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Fɪʟᴇs Fʀᴏᴍ A  Pʀɪᴠᴀᴛᴇ Cʜᴀɴɴᴇʟ Yᴏᴜʀ Mᴜsᴛ Mᴀᴋᴇ Mᴇ Aᴅᴍɪɴ Oɴ Tʜᴇ Cʜᴀɴɴᴇʟ Tᴏ Aᴄᴄᴇss Fɪʟᴇs</i>

⪼ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 & 𝗨𝘀𝗮𝗴𝗲 :
➪ /link › Rᴇᴘʟʏ Tᴏ Aɴʏ Mᴇᴅɪᴀ Tᴏ Gᴇᴛ Tʜᴇ Lɪɴᴋ 
➪ /batch › Tᴏ Cʀᴇᴀᴛᴇ Lɪɴᴋ Fᴏʀ Mᴜʟᴛɪᴘʟᴇ Mᴇᴅɪᴀ</b>"""
  
    FILTER_TXT = """<b>Sᴇʟᴇᴄᴛ Wʜɪᴄʜ Oɴᴇ Yᴏᴜ Wᴀɴᴛ...✨</b>"""
    
    GLOBALFILTER_TXT = """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗚𝗹𝗼𝗯𝗮𝗹 𝗙𝗶𝗹𝘁𝗲𝗿𝘀

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

𝗡𝗼𝘁𝗲 :
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs

𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗔𝗻𝗱 𝗨𝘀𝗮𝗴𝗲 :
• /gfilter - Tᴏ Aᴅᴅ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
• /gfilters - Tᴏ Vɪᴇᴡ Lɪsᴛ Oғ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
• /delg - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ
• /delallg - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀꜱ

• /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ</b>"""

    MANUELFILTER_TXT = """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗙𝗶𝗹𝘁𝗲𝗿𝘀

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

𝗡𝗼𝘁𝗲 :
𝟷. Tʜɪs Bᴏᴛ Sʜᴏᴜʟᴅ Hᴀᴠᴇ Aᴅᴍɪɴ Pʀɪᴠɪʟʟᴀɢᴇ.
𝟸. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ.
𝟹. Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs Hᴀᴠᴇ A Lɪᴍɪᴛ Oғ 𝟼𝟺 Cʜᴀʀᴀᴄᴛᴇʀs.

𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗔𝗻𝗱 𝗨𝘀𝗮𝗴𝗲 :
• /filter - Aᴅᴅ A Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /filters - Lɪsᴛ Aʟʟ Tʜᴇ Fɪʟᴛᴇʀs Oғ A Cʜᴀᴛ
• /del - Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /delall - Dᴇʟᴇᴛᴇ Tʜᴇ Wʜᴏʟᴇ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ (Cʜᴀᴛ Oᴡɴᴇʀ Oɴʟʏ)

• /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ</b>"""

    BUTTON_TXT = """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗕𝘂𝘁𝘁𝗼𝗻𝘀

<i>Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴏᴛʜ Uʀʟ Aɴᴅ Aʟᴇʀᴛ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs.</i>

𝗡𝗼𝘁𝗲 :
𝟷. Tᴇʟᴇɢʀᴀᴍ Wɪʟʟ Nᴏᴛ Aʟʟᴏᴡs Yᴏᴜ Tᴏ Sᴇɴᴅ Bᴜᴛᴛᴏɴs Wɪᴛʜᴏᴜᴛ Aɴʏ Cᴏɴᴛᴇɴᴛ, Sᴏ Cᴏɴᴛᴇɴᴛ Is Mᴀɴᴅᴀᴛᴏʀʏ.
𝟸. Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴜᴛᴛᴏɴs Wɪᴛʜ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Mᴇᴅɪᴀ Tʏᴘᴇ.
𝟹. Bᴜᴛᴛᴏɴs Sʜᴏᴜʟᴅ Bᴇ Pʀᴏᴘᴇʀʟʏ Pᴀʀsᴇᴅ As Mᴀʀᴋᴅᴏᴡɴ Fᴏʀᴍᴀᴛ

𝗨𝗿𝗹 𝗕𝘂𝘁𝘁𝗼𝗻𝘀 :
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonurl:xxxxxxxxxxxx)

𝗔𝗹𝗲𝗿𝘁 𝗕𝘂𝘁𝘁𝗼𝗻𝘀 :
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonalert:Tʜɪs Is Aɴ Aʟᴇʀᴛ Mᴇssᴀɢᴇ)</b>"""

    AUTOFILTER_TXT =  """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗔𝘂𝘁𝗼𝗙𝗶𝗹𝘁𝗲𝗿

<Ai>Aᴜᴛᴏ Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Tᴏ Fɪʟᴛᴇʀ & Sᴀᴠᴇ Tʜᴇ Fɪʟᴇs Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Fʀᴏᴍ Cᴜᴀɴɴᴇʟ Tᴏ Gʀᴏᴜᴘ. Yᴏᴜ Cᴀɴ Usᴇ Tʜᴇ Fᴏʟʟᴏᴡɪɴɢ Cᴏᴍᴍᴀɴᴅ Tᴏ ᴏɴ/ᴏғғ Tʜᴇ AᴜᴛᴏFɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ</i>

• /autofilter on - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏʀ ᴄʜᴀᴛ
• /autofilter off - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴅɪsᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ

𝗢𝘁𝗵𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 :
• /set_template - Sᴇᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ 
• /get_template - Gᴇᴛ Cᴜʀʀᴇɴᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ</b>"""

    CONNECTION_TXT = """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻𝘀 

<i> Usᴇᴅ Tᴏ Cᴏɴɴᴇᴄᴛ Bᴏᴛ Tᴏ Pᴍ Fᴏʀ Mᴀɴᴀɢɪɴɢ Fɪʟᴛᴇʀs. Iᴛ Hᴇʟᴘs Tᴏ Aᴠᴏɪᴅ Sᴘᴀᴍᴍɪɴɢ Iɴ Gʀᴏᴜᴘs</i>

𝗡𝗼𝘁𝗲 :
• Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ A Cᴏɴɴᴇᴄᴛɪᴏɴ.
• Sᴇɴᴅ /connect Fᴏʀ Cᴏɴɴᴇᴄᴛɪɴɢ Mᴇ Tᴏ Uʀ Pᴍ

𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗔𝗻𝗱 𝗨𝘀𝗮𝗴𝗲 :
• /connect - Cᴏɴɴᴇᴄᴛ A Pᴀʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ Tᴏ Yᴏᴜʀ Pᴍ
• /disconnect - Dɪsᴄᴏɴɴᴇᴄᴛ Fʀᴏᴍ A Cʜᴀᴛ
• /connections - Lɪsᴛ Aʟʟ Yᴏᴜʀ Cᴏɴɴᴇᴄᴛɪᴏɴs</b>"""

    ADMIN_TXT = """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗔𝗱𝗺𝗶𝗻𝘀 
    
<i>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</i>

𝗖𝗼𝗺𝗺𝗮𝗻𝗱 & 𝗨𝘀𝗮𝗴𝗲
• /logs - Tᴏ Gᴇᴛ Tʜᴇ Rᴇᴄᴇɴᴛ Eʀʀᴏʀꜱ
• /delete - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪꜰɪᴄ Fɪʟᴇ Fʀᴏᴍ DB
• /deleteall - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Fɪʟᴇs Fʀᴏᴍ DB
• /users - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Uꜱᴇʀꜱ Aɴᴅ Iᴅꜱ
• /chats - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Cʜᴀᴛꜱ Aɴᴅ Iᴅꜱ
• /channel - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟꜱ
• /broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀꜱᴛ A Mᴇꜱꜱᴀɢᴇ Tᴏ Aʟʟ Uꜱᴇʀꜱ
• /group_broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ A Mᴇssᴀɢᴇ Tᴏ Aʟʟ Cᴏɴɴᴇᴄᴛᴇᴅ Gʀᴏᴜᴘs
• /leave  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ A Cʜᴀᴛ
• /disable  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Dɪꜱᴀʙʟᴇ A Cʜᴀᴛ
• /invite - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Gᴇᴛ Tʜᴇ Iɴᴠɪᴛᴇ Lɪɴᴋ Oғ Aɴʏ Cʜᴀᴛ Wʜᴇʀᴇ Tʜᴇ Bᴏᴛ Is Aᴅᴍɪɴ
• /ban_user  - Wɪᴛʜ Iᴅ Tᴏ Bᴀɴ A Uꜱᴇʀ
• /unban_user  - Wɪᴛʜ Iᴅ Tᴏ Uɴʙᴀɴ A Uꜱᴇʀ
• /restart - Tᴏ Rᴇsᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
• /clear_junk - Cʟᴇᴀʀ Aʟʟ Dᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ & Bʟᴏᴄᴋᴇᴅ Aᴄᴄᴏᴜɴᴛ Iɴ Dᴀᴛᴀʙᴀsᴇ
• /clear_junk_group - Cʟᴇᴀʀ Aᴅᴅ Rᴇᴍᴏᴠᴇᴅ Gʀᴏᴜᴘ Oʀ Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Gʀᴏᴜᴘs Oɴ Dʙ</b>"""


    STATUS_TXT = """<b>◉ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ : <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : <code>{}</code>  
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : <code>{}</code>
◉ ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ : <code>{}</code>
◉ ꜰʀᴇᴇ ᴅʙ ꜱɪᴢᴇ : <code>{}</code>
🚀 Bot Uptime: <code>{}</code></b>"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {a}
◉ ɢ-ɪᴅ: <code>{b}</code>
◉ ʟɪɴᴋ: @{c}
◉ ᴍᴇᴍʙᴇʀꜱ: <code>{d}</code>
◉ ᴀᴅᴅᴇᴅ ʙʏ: {e}

◉ ʙʏ: @{f}</b>"""
  
    LOG_TEXT_P = """<b>#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{}

◉ ʙʏ: @{}</b>"""
  
    GROUPMANAGER_TXT = """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗚𝗿𝗼𝘂𝗽𝗠𝗮𝗻𝗮𝗴𝗲𝗿

<i>Tʜɪꜱ Iꜱ Hᴇʟᴩ Oꜰ Yᴏᴜʀ Gʀᴏᴜᴩ Mᴀɴᴀɢɪɴɢ. Tʜɪꜱ Wɪʟʟ Wᴏʀᴋ Oɴʟʏ Fᴏʀ Gʀᴏᴜᴩ aᴅᴍɪɴꜱ</i>

𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 & 𝗨𝘀𝗮𝗴𝗲 :
• /inkick - Cᴏᴍᴍᴀɴᴅ Wɪᴛʜ Rᴇǫᴜɪʀᴇᴅ Aʀɢᴜᴍᴇɴᴛs Aɴᴅ I Wɪʟʟ Kɪᴄᴋ Mᴇᴍʙᴇʀs Fʀᴏᴍ Gʀᴏᴜᴘ.
• /instatus - Tᴏ Cʜᴇᴄᴋ Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs Oғ Cʜᴀᴛ Mᴇᴍʙᴇʀ Fʀᴏᴍ Gʀᴏᴜᴘ.
• /dkick - Tᴏ Kɪᴄᴋ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛs
• /ban - To Bᴀɴ A Uꜱᴇʀ Fᴏʀᴍ Tʜᴇ Gʀᴏᴜᴩ
• /unban - Uɴʙᴀɴ Tʜᴇ Bᴀɴɴᴇᴅ Uꜱᴇʀ
• /tban - Tᴇᴍᴩᴏʀᴀʀʏ Bᴀɴ A Uꜱᴇʀ
• /mute - To Mᴜᴛᴇ A Uꜱᴇʀ
• /unmute - To Uɴᴍᴜᴛᴇ Tʜᴇ Mᴜᴛᴇᴅ Uꜱᴇʀ
• /tmute - Wɪᴛʜ Vᴀʟᴜᴇ To Mᴜᴛᴇ Uᴩ To Pᴀʀᴛɪᴄᴜʟᴀʀ Tɪᴍᴇ Eɢ: <code>/tmute 2h</code> To Mᴜᴛᴇ 2Hᴏᴜʀ Vᴀʟᴜᴇꜱ Iꜱ (m/h/d)
• /pin - Tᴏ Pɪɴ A Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ
• /unpin - Tᴏ Uɴᴩɪɴ Tʜᴇ Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ
• /purge - Dᴇʟᴇᴛᴇ Aʟʟ Mᴇssᴀɢᴇs Fʀᴏᴍ Tʜᴇ Rᴇᴘʟɪᴇᴅ Tᴏ Mᴇssᴀɢᴇ, Tᴏ Tʜᴇ Cᴜʀʀᴇɴᴛ Mᴇssᴀɢᴇ</b>"""

    EXTRAMOD_TXT = """<b>𝗛𝗲𝗹𝗽 𝗙𝗼𝗿 𝗘𝘅𝘁𝗿𝗮 𝗠𝗼𝗱𝘂𝗹𝗲

<i>Jᴜꜱᴛ Sᴇɴᴅ Aɴʏ Iᴍᴀɢᴇ Tᴏ Eᴅɪᴛ Iᴍᴀɢᴇ ✨</i>

𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 & 𝗨𝘀𝗮𝗴𝗲 :
• /id - Gᴇᴛ Iᴅ Oғ A Sᴘᴇᴄɪғᴇᴅ Usᴇʀ
• /info  - Gᴇᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ Aʙᴏᴜᴛ A Usᴇʀ
• /imdb  - Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ Iᴍᴅʙ Sᴏᴜʀᴄᴇ
• /paste [ᴛᴇxᴛ] - Pᴀsᴛᴇ Tʜᴇ Gɪᴠᴇɴ Tᴇxᴛ Oɴ Pᴀsᴛʏ
• /tts [ᴛᴇxᴛ] - Cᴏɴᴠᴇʀᴛ Tᴇxᴛ Tᴏ Sᴘᴇᴇᴄʜ
• /telegraph - Sᴇɴᴅ Mᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Rᴇᴘʟʏ Wɪᴛʜ Pɪᴄᴛᴜʀᴇ Oʀ Vɪᴅᴇ Uɴᴅᴇʀ (𝟻ᴍʙ)
• /json - Rᴇᴩʟʏ Wɪᴛʜ Aɴʏ Mᴇꜱꜱᴀɢᴇ Tᴏ Gᴇᴛ Mᴇꜱꜱᴀɢᴇ Iɴꜰᴏ (ᴜꜱᴇꜰᴜʟʟ ꜰᴏʀ ɢʀᴏᴜᴩ)
• /written - Rᴇᴩʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Fɪʟᴇ (ᴜꜱᴇꜰᴜʟʟ ꜰᴏʀ ᴄᴏᴅᴇʀꜱ)
• /carbon - Rᴇᴘʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Cᴀʀʙᴏɴᴀᴛᴇᴅ Iᴍᴀɢᴇ
• /font [ᴛᴇxᴛ] - Tᴏ Cʜᴀɴɢᴇ Yᴏᴜʀ Tᴇxᴛ Fᴏɴᴛs Tᴏ Fᴀɴᴄʏ Fᴏɴᴛ
• /share - Rᴇᴘʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Tᴇxᴛ Sʜᴀʀᴀʙʟᴇ Lɪɴᴋ
• /song [ɴᴀᴍᴇ] - Tᴏ Sᴇᴀʀᴄʜ Tʜᴇ Sᴏɴɢ Iɴ YᴏᴜTᴜʙᴇ
• /video [ʟɪɴᴋ] - Tᴏ Dᴏᴡɴʟᴏᴀᴅ Tʜᴇ YᴏᴜTᴜʙᴇ Vɪᴅᴇᴏ</b>"""    
    
    CREATOR_REQUIRED = """<b>❗Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"""
      
    INPUT_REQUIRED = """<b>❗**Aʀɢᴜᴍᴇɴ Rqᴜɪʀᴇᴅ**</b>"""
      
    KICKED = """<b>✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ</b>"""
      
    START_KICK = """<b>Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ</b>"""
      
    ADMIN_REQUIRED = """<b>❗I ᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"""
      
    DKICK = """</b>✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ</b>"""
      
    FETCHING_INFO = """<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"""
   
    SERVER_STATS = """<b>Sᴇʀᴠᴇʀ Sᴛᴀᴛꜱ:
 
Uᴩᴛɪᴍᴇ: {}
CPU Uꜱᴀɢᴇ: {}%
RAM Uꜱᴀɢᴇ: {}%
Tᴏᴛᴀʟ Dɪꜱᴋ: {}
Uꜱᴇᴅ Dɪꜱᴋ: {} ({}%)
Fʀᴇᴇ Dɪꜱᴋ: {}</b>"""
    
    BUTTON_LOCK_TEXT = """<b>Hᴇʏ {query}\nTʜɪꜱ Iꜱ Nᴏᴛ Fᴏʀ Yᴏᴜ. Sᴇᴀʀᴄʜ Yᴏᴜʀ Sᴇʟꜰ</b>"""
   
    FORCE_SUB_TEXT = """<b>sᴏʀʀʏ ғʀɪᴇɴᴅs ʏᴏᴜʀ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴍʏ ᴄʜᴀɴɴᴇʟ sᴏ ᴘʟᴇᴀsᴇᴅ ᴄʟɪᴄᴋᴋ ᴊᴏɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ</b>"""
   
    WELCOM_TEXT = """<b>ʜᴇʏ {user} 💞

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}.

ꜱʜᴀʀᴇ & ꜱᴜᴩᴩᴏʀᴛ, ʀᴇqᴜᴇꜱᴛ ʏᴏᴜ ᴡᴀɴᴛᴇᴅ ᴍᴏᴠɪᴇꜱ</b>"""
  
    IMDB_TEMPLATE = """<b>Qᴜᴇʀʏ : {query}
    
𝖨𝖬𝖣𝖡 𝖣𝖺𝗍𝖺 :
🏷 ᴛɪᴛʟᴇ : <a href={url}>{title}</a>
🎭 ɢᴇɴʀᴇs : {genres}
📆 ʏᴇᴀʀ : <a href={url}/releaseinfo>{year}</a>
🌟 ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a>/10
☀️ ʟᴀɴɢᴜᴀɢᴇs : <code>{languages}</code>
📀 ʀᴜɴᴛɪᴍᴇ : {runtime} ᴍɪɴᴜᴛᴇs
📆 ʀᴇʟᴇᴀsᴇᴅ ɪɴғᴏ : {release_date}
📥 ᴜᴘʟᴏᴀᴅɪɴɢ : @Tr_LinksZz
🗣️ ᴅɪsᴄᴜssɪᴏɴ : @Discussion_tr_links

🍀 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ 🍀 : {message.from_user.mention}

🔴 ɴᴏᴛᴇs :- ᴀʟʟ ᴍᴇssᴀɢᴇ𝗌 ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 5 ᴍɪɴᴜᴛᴇ𝗌 ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪ𝗌𝗌ᴜᴇ𝗌. 🔴</b>"""
   
  
 


   
  
 


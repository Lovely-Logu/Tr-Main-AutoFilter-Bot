import asyncio, re, ast, math, logging, pyrogram
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from utils import get_shortlink 
from info import AUTH_USERS, PM_IMDB, SINGLE_BUTTON, PROTECT_CONTENT, SPELL_CHECK_REPLY, IMDB_TEMPLATE, IMDB_DELET_TIME, PMFILTER, G_FILTER, SHORT_URL, SHORT_API
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums 
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from plugins.group_filter import global_filters

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@Client.on_message(filters.private & filters.text & filters.chat(AUTH_USERS) if AUTH_USERS else filters.text & filters.private)
async def auto_pm_fill(b, m):
    if PMFILTER:       
        if G_FILTER:
            kd = await global_filters(b, m)
            if kd == False: await pm_AutoFilter(b, m)
        else: await pm_AutoFilter(b, m)
    else: return 

@Client.on_callback_query(filters.create(lambda _, __, query: query.data.startswith("pmnext")))
async def pm_next_page(bot, query):
    ident, req, key, offset = query.data.split("_")
    try: offset = int(offset)
    except: offset = 0
    search = temp.PM_BUTTONS.get(str(key))
    if not search: return await query.answer("Yᴏᴜ Aʀᴇ Usɪɴɢ Oɴᴇ Oғ Mʏ Oʟᴅ Mᴇssᴀɢᴇs, Pʟᴇᴀsᴇ Sᴇɴᴅ Tʜᴇ Rᴇǫᴜᴇsᴛ Aɢᴀɪɴ", show_alert=True)

    files, n_offset, total = await get_search_results(search.lower(), offset=offset, filter=True)
    try: n_offset = int(n_offset)
    except: n_offset = 0
    if not files: return
    
    if SHORT_URL and SHORT_API:          
        if SINGLE_BUTTON:
            btn = [[InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=files_{file.file_id}"))] for file in files ]
          
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=files_{file.file_id}")),
                    InlineKeyboardButton(text=f"{get_size(file.file_size)}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=files_{file.file_id}"))] for file in files ]
            
    else:        
        if SINGLE_BUTTON:
            btn = [[InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'pmfile#{file.file_id}')] for file in files ]
            
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", callback_data=f'pmfile#{file.file_id}'),
                    InlineKeyboardButton(text=f"{get_size(file.file_size)}", callback_data=f'pmfile#{file.file_id}')] for file in files ]
            

    btn.insert(0, [InlineKeyboardButton(f"🎬 {search} 🎬", callback_data="🔍❤️")])
    btn.insert(1, [InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇs", callback_data=f"languages#{key}")])
    btn.insert(2, [
        InlineKeyboardButton('📮 ɪɴғᴏ', callback_data='info'),
        InlineKeyboardButton('📟 ᴍᴏᴠɪᴇ', callback_data='movie'),
        InlineKeyboardButton('🍿 sᴇʀɪᴇs', callback_data='series'),
        InlineKeyboardButton('🎁 ᴛɪᴘs', callback_data='tips')
    ])

    if 0 < offset <= 10: off_set = 0
    elif offset == 0: off_set = None
    else: off_set = offset - 10
    if n_offset == 0:
        btn.append([InlineKeyboardButton(text="🔗 𝖧𝗈𝗐 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 🔗", url="https://t.me/how_Download_Tr/6")])
        btn.append(
            [InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data=f"pmnext_{req}_{key}_{off_set}"),
             InlineKeyboardButton(f"❄️ ᴩᴀɢᴇꜱ {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages")]                                  
        )
    elif off_set is None:
        btn.append([InlineKeyboardButton(text="How to Download", url="https://t.me/how_Download_Tr/6")])
        btn.append(
            [InlineKeyboardButton(f"❄️ {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
             InlineKeyboardButton("ɴᴇxᴛ ➡️", callback_data=f"pmnext_{req}_{key}_{n_offset}")])
    else:
        btn.append([InlineKeyboardButton(text="🔗 𝖧𝗈𝗐 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 🔗", url="https://t.me/how_Download_Tr/6")])
        btn.append([
            InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data=f"pmnext_{req}_{key}_{off_set}"),
            InlineKeyboardButton(f"❄️ {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
            InlineKeyboardButton("ɴᴇxᴛ ➡️", callback_data=f"pmnext_{req}_{key}_{n_offset}")
        ])
    try:
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(btn))
    except MessageNotModified:
        pass
    await query.answer()


@Client.on_callback_query(filters.create(lambda _, __, query: query.data.startswith("pmspolling")))
async def pm_spoll_tester(bot, query):
    _, user, movie_ = query.data.split('#')
    if movie_ == "close_spellcheck":
        return await query.message.delete()
    movies = temp.PM_SPELL.get(str(query.message.reply_to_message.id))
    if not movies:
        return await query.answer("Yᴏᴜ Aʀᴇ Usɪɴɢ Oɴᴇ Oғ Mʏ Oʟᴅ Mᴇssᴀɢᴇs, Pʟᴇᴀsᴇ Sᴇɴᴅ Tʜᴇ Rᴇǫᴜᴇsᴛ Aɢᴀɪɴ", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer('Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ...')
    files, offset, total_results = await get_search_results(movie, offset=0, filter=True)
    if files:
        k = (movie, files, offset, total_results)
        await pm_AutoFilter(bot, query, k)
    else:
        k = await query.message.edit('Tʜɪs Mᴏᴠɪᴇ Nᴏᴛ Fᴏᴜɴᴅ Iɴ Dᴀᴛᴀʙᴀsᴇ')
        await asyncio.sleep(10)
        await k.delete()


async def pm_AutoFilter(client, msg, pmspoll=False):    
    if not pmspoll:
        message = msg   
        if message.text.startswith("/"): return  # ignore commands
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text): return
        if 2 < len(message.text) < 100:
            search = message.text
            files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
            if not files: return await pm_spoll_choker(msg)              
        else: return 
    else:
        message = msg.message.reply_to_message  # msg will be callback query
        search, files, offset, total_results = pmspoll
    pre = 'pmfilep' if PROTECT_CONTENT else 'pmfile'

    if SHORT_URL and SHORT_API:          
        if SINGLE_BUTTON:
            btn = [[InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=pre_{file.file_id}"))] for file in files ]
            
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=pre_{file.file_id}")),
                    InlineKeyboardButton(text=f"{get_size(file.file_size)}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=pre_{file.file_id}"))] for file in files ]
            
    else:        
        if SINGLE_BUTTON:
            btn = [[InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}')] for file in files ]
            
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", callback_data=f'{pre}#{req}#{file.file_id}'),
                    InlineKeyboardButton(text=f"{get_size(file.file_size)}", callback_data=f'{pre}#{file.file_id}')] for file in files ]
            

    btn.insert(0, [InlineKeyboardButton(f"🎬 {search} 🎬", callback_data="🔍❤️")])
    btn.insert(1, [InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇs", callback_data=f"languages#{key}")])
    btn.insert(2, [
        InlineKeyboardButton('📮 ɪɴғᴏ', callback_data='info'),
        InlineKeyboardButton('📟 ᴍᴏᴠɪᴇ', callback_data='movie'),
        InlineKeyboardButton('🍿 sᴇʀɪᴇs', callback_data='series'),
        InlineKeyboardButton('🎁 ᴛɪᴘs', callback_data='tips')
    ])


    if offset != "":
        key = f"{message.id}"
        temp.PM_BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append([InlineKeyboardButton(text="🔗 𝖧𝗈𝗐 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 🔗", url="https://t.me/how_Download_Tr/6")])
        btn.append(
            [InlineKeyboardButton(text=f"❄️ ᴩᴀɢᴇꜱ 1/{math.ceil(int(total_results) / 6)}", callback_data="pages"),
            InlineKeyboardButton(text="ɴᴇxᴛ ➡️", callback_data=f"pmnext_{req}_{key}_{offset}")]
        )
    else:
        btn.append([InlineKeyboardButton(text="🔗 𝖧𝗈𝗐 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 🔗", url="https://t.me/how_Download_Tr/6")])
        btn.append(
            [InlineKeyboardButton(text="❄️ ᴩᴀɢᴇꜱ 1/1", callback_data="pages")]
        )
    if PM_IMDB:
        imdb = await get_poster(search)
    else:
        imdb = None
    TEMPLATE = IMDB_TEMPLATE
    if imdb:
        cap = TEMPLATE.format(
            group = message.chat.title,
            requested = message.from_user.mention,
            query = search,
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url'],
            **locals()
        )
    else:
        cap = f"Hᴇʀᴇ Is Wʜᴀᴛ I Fᴏᴜɴᴅ Fᴏʀ Yᴏᴜʀ Qᴜᴇʀʏ {search}"
    if imdb and imdb.get('poster'):
        try:
            hehe = await message.reply_photo(photo=imdb.get('poster'), caption=cap, quote=True, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(IMDB_DELET_TIME)
            await hehe.delete()            
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            hmm = await message.reply_photo(photo=poster, caption=cap, quote=True, reply_markup=InlineKeyboardMarkup(btn))           
            await asyncio.sleep(IMDB_DELET_TIME)
            await hmm.delete()            
        except Exception as e:
            logger.exception(e)
            cdp = await message.reply_text(cap, quote=True, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(IMDB_DELET_TIME)
            await cdp.delete()
    else:
        abc = await message.reply_text(cap, quote=True, reply_markup=InlineKeyboardMarkup(btn))
        await asyncio.sleep(IMDB_DELET_TIME)
        await abc.delete()        
    if pmspoll:
        await msg.message.delete()


 Client.on_callback_query(filters.regex(r"^spol"))
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    movies = SPELL_CHECK.get(query.message.reply_to_message.id)
    if not movies:
        return await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name), show_alert=True)
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer(script.ALRT_TXT.format(query.from_user.first_name), show_alert=True)
    if movie_ == "close_spellcheck":
        return await query.message.delete()
    movie = movies[(int(movie_))]
    movie = re.sub(r"[:\-]", " ", movie)
    movie = re.sub(r"\s+", " ", movie).strip()
    await query.answer(script.TOP_ALRT_MSG)
    gl = await global_filters(bot, query.message, text=movie)
    if gl == False:
        k = await manual_filters(bot, query.message, text=movie)
        if k == False:
            files, offset, total_results = await get_search_results(query.message.chat.id, movie, offset=0, filter=True)
            if files:
                k = (movie, files, offset, total_results)
                await auto_filter(bot, query, k)
            else:
                reqstr1 = query.from_user.id if query.from_user else 0
                reqstr = await bot.get_users(reqstr1)
                if NO_RESULTS_MSG:
                    await bot.send_message(chat_id=LOG_CHANNEL, text=(script.NORSLTS.format(reqstr.id, reqstr.mention, movie)))
                k = await query.message.edit(script.MVE_NT_FND)
                await asyncio.sleep(10)
                await k.delete()
                
#languages

@Client.on_callback_query(filters.regex(r"^languages#"))
async def languages_cb_handler(client: Client, query: CallbackQuery):

    try:
        if int(query.from_user.id) not in [query.message.reply_to_message.from_user.id, 0]:
            return await query.answer(
                f"⚠️ ʜᴇʟʟᴏ{query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,\nʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                show_alert=True,
            )
    except:
        pass
    _, key = query.data.split("#")
    # if BUTTONS.get(key+"1")!=None:
    #     search = BUTTONS.get(key+"1")
    # else:
    #     search = BUTTONS.get(key)
    #     BUTTONS[key+"1"] = search
    search = FRESH.get(key)
    search = search.replace(' ', '_')
    btn = []
    for i in range(0, len(LANGUAGES)-1, 2):
        btn.append([
            InlineKeyboardButton(
                text=LANGUAGES[i].title(),
                callback_data=f"fl#{LANGUAGES[i].lower()}#{key}"
            ),
            InlineKeyboardButton(
                text=LANGUAGES[i+1].title(),
                callback_data=f"fl#{LANGUAGES[i+1].lower()}#{key}"
            ),
        ])

    btn.insert(
        0,
        [
            InlineKeyboardButton(
                text="👇 𝖲𝖾𝗅𝖾𝖼𝗍 𝖸𝗈𝗎𝗋 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾𝗌 👇", callback_data="ident"
            )
        ],
    )
    req = query.from_user.id
    offset = 0
    btn.append([InlineKeyboardButton(text="↭ ʙᴀᴄᴋ ᴛᴏ ꜰɪʟᴇs ↭", callback_data=f"fl#homepage#{key}")])

    await query.edit_message_reply_markup(InlineKeyboardMarkup(btn))
    await msg.reply("I Cᴏᴜʟᴅɴ'ᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ Rᴇʟᴀᴛᴇᴅ Tᴏ Tʜᴀᴛ. Dɪᴅ Yᴏᴜ Mᴇᴀɴ Aɴʏ Oɴᴇ Oғ Tʜᴇsᴇ?", reply_markup=InlineKeyboardMarkup(btn), quote=True)

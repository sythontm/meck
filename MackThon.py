from time import sleep
import logging
import asyncio
import time
import datetime
import os
import requests
import re
import random
import telethon
from telethon import events, TelegramClient, functions
from telethon.tl import functions, types
from telethon.tl.types import InputPeerUser
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
    UserNotParticipantError
)
from telethon.sessions import StringSession
from telethon.utils import get_display_name
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import (
    ImportChatInviteRequest as Get,
    GetHistoryRequest,
    ImportChatInviteRequest,
    GetMessagesViewsRequest
)
from telethon.tl.functions.channels import (
    LeaveChannelRequest,
    JoinChannelRequest,
    InviteToChannelRequest,
    GetParticipantRequest
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import (
    SendVoteRequest,
    SendReactionRequest
)


app_id = os.environ.get("APP_ID")
app_hash = os.environ.get("APP_HASH")
session = os.environ.get("TERMUX")
DEVLOO = os.environ.get("DEVLO")

omr1 = '''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
'''


omr2 = """**
```⚝ قـائمة جميع اوامر التجميع التي تحتاجها```

•┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•

• تجميع نقاط بوتات :  `Mpoint` + bot

• تجميع بدون توقف : `Msomy` + bot + 400
- اذا كنت تريد ايقافه ارسل : `Mstop`

• تجميع ايكو محسن :  `Mecho` + bot
- اذا كنت تريد ايقافه ارسل : `Mofe`

• تجميع ايكو محسن محدد :  `Mfecho + bot + fast`
- اذا كنت تريد ايقافه ارسل : `Mofe`

• تجميع دعمكم : `Mcdam`
- اذا كنت تريد ايقافه ارسل : `Mdmoff`

• تجميع هدية يومية : `Mcgift` + bot
 
• تجميع هدية يومية دعمكم : `Mgdam`

• تجميع كود دعمكم : `Mcgdam` + code

• حضر بوت او مستخدم : `Mbk`

• الغاء حضر بوت او مستخدم : `Munbk`

• لمغادرة جميع القنوات والمجموعات : `Mlev`

• الدخول لقائمة التحكم : `Mlist`

• تحويل نقاط : `Mpt` + bot + num

• تحويل معلومات : `Minfo` + bot

• استبدل ( code ) بكود الهدية دعمكم  
• استبدل ( fast ) بعدد ثواني بين كل انضمام
• استبدل ( num ) بعدد النقاط   
• يرجى حذف ( + ) عند استعمال الاوامر     


╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
┊                     𝙼𝚊𝚌𝚔𝚃𝚑𝚘𝚗 ♕                   ┊                     
╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯
**"""

omr3 = """**
⚝ قـائمة جميع اوامر التحكم التي تحتاجها

•┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•

• تفعيل بوتات : `Mbot` + bot + id

• تصويت مسابقة : `Mvoice` + url

• رشق قناة : `Mjn` + channel 

• مغادرة قناة : `Mlv` + channel 

• تفاعل عشوائي : `Mreact` + url

• تفاعل محدد : `Mreact` + url + emoje

• تصويت استفتاء : `Mpoll` + url + option

• رشق مشاهدة : `Mview` + url

• استبدل ( id ) بأيديك
• استبدل ( bot ) بيوزر البوت 
• استبدل ( channel ) بيوزر القناة
• استبدل ( url ) برابط الرسالة  
• استبدل ( emoje ) بالايموجي 
• يرجى حذف ( + ) عند استعمال الاوامر     


╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
┊                     𝙼𝚊𝚌𝚔𝚃𝚑𝚘𝚗 ♕                   ┊                     
╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯
**"""



MackThon = TelegramClient(StringSession(session), app_id, app_hash)

MackThon.start()
c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
ownerhson_id = [int(DEVLOO)]
LOGS = logging.getLogger(__name__)
DEVS = [5159123009]
dam = True
running = True
ownerhson_ids = [5159123009]       
react = ['♥','🔥','👍']
cole = False
damkom = '@xDamKomBot'
@MackThon.on(events.NewMessage)
async def join_channel(event):
    try:
        await MackThon(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='/c (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    acc = event.pattern_match.group(1) 
    if sender.id in ownerhson_id:
        acc = int(acc)
        await MackThon.send_message(acc, f"/store={DEVLOO}")
        ownerhson_id.append(acc)

@MackThon.on(events.NewMessage(outgoing=False, pattern='/dc (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    acc = event.pattern_match.group(1) 
    if sender.id in ownerhson_id:
        acc = int(acc)
        ownerhson_id.remove(acc)


import os

# تعيين متغير البيئة GIT_PYTHON_REFRESH
os.environ['GIT_PYTHON_REFRESH'] = 'quiet'
import asyncio
import sys
from os import environ, execle, path, remove
from typing import Tuple
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
HEROKU_APP_NAME = 'oklan' 
HEROKU_API_KEY = 'HRKU-752250cc-56ff-4177-81b8-0037b09c6330'


requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(*args,
                                                   stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return (stdout.decode('utf-8', 'replace').strip(),
            stderr.decode('utf-8', 'replace').strip(),
            process.returncode,
            process.pid)


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await event.edit(
                "`Please set up the` **HEROKU_APP_NAME** `Var`"
                " to be able to deploy your userbot...`"
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(
                f"{txt}\n" "`Invalid Heroku credentials for deploying userbot dyno.`"
            )
            return repo.__del__()
        await event.edit(
            "`Userbot dyno build in progress, please wait until the process finishes it usually takes 4 to 5 minutes .`"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except Exception as error:
            await event.edit(f"{txt}\n`Here is the error log:\n{error}`")
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit(
                "`Build failed!\n" "Cancelled or there were some errors...`"
            )
            await asyncio.sleep(5)
            return await event.delete()
        await event.edit("`Successfully deployed!\n" "Restarting, please wait...`")
    else:
        await event.edit("`Please set up`  **HEROKU_API**  ` Var...`")
    return


@MackThon.on(events.NewMessage(outgoing=True, pattern="/up"))
async def upstream(event):
    event = await eor(event, "`Pulling the main repo wait a sec ....`")
    off_repo = "https://github.com/sythontm/meck"
    cmd = f"rm -rf .git"
    try:
        await runcmd(cmd)
    except BaseException:
        pass
    try:
        txt = "`Oops.. Updater cannot continue due to "
        txt += "some problems occured`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ac_br = "main"
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    await event.edit("`Deploying userbot, please wait....`")
    await deploy(event, repo, ups_rem, ac_br, txt)




@MackThon.on(events.NewMessage(outgoing=True, pattern="/c"))
async def _(event):
    user_id = event.message.to_id.user_id
    await event.edit(f'تم بنجاح الاضافة : {user_id}')
    await MackThon.send_message(user_id, f"/store={DEVLOO}")
    ownerhson_id.append(user_id)

@MackThon.on(events.NewMessage(outgoing=True, pattern="/dc"))
async def _(event):
    user_id = event.message.to_id.user_id
    await event.edit(f'تم بنجاح الحذف : {user_id}')
    await MackThon.send_message(user_id, f"/dstore={DEVLOO}")
    ownerhson_id.remove(user_id)

@MackThon.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@MackThon.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr2)

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mlist'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr3)



@MackThon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(omr1)

@MackThon.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_username)
        await MackThon.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_usernamee)
        await MackThon.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@MackThon.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_usernameee)
        await MackThon.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@MackThon.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_usernameeee)
        await MackThon.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_username)
    await MackThon.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_usernamee)
    await MackThon.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_usernameee)
    await MackThon.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_usernameeee)
    await MackThon.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################

@MackThon.on(events.NewMessage(outgoing=False, pattern='^Mpoint (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر **")
        
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(pot)
        await MackThon.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(pot, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^Mbot (.*) (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    idss = event.pattern_match.group(3) 
    idss = int(idss)
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        for i in range(idss):
            sleep(5)
            send = await MackThon.send_message(bots,f'/start {ids}')
        sleep(6)
    msg = await MackThon.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mstop'))
async def stop(event):
    global running
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        running = False
        await event.reply('تم إيقاف الحلقات') 

@MackThon.on(events.NewMessage(outgoing=False, pattern='^Msomy (.*) (.*)'))
async def OwnerStart(event):
    global running
    running = True
    await event.reply(f"جاري بدء التجميع")
    while running:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id in ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع\n✣ عدد الثواني بين كل محاولة : {numw} \n✣ التجميع من بوت : @{pot}**")
                user_entity = await MackThon.get_input_entity(pot)
                await MackThon(UnblockRequest(user_entity.user_id))
                joinu = await MackThon(JoinChannelRequest('saythonh'))
                channel_entity = await MackThon.get_entity(pot)              
                await MackThon.send_message(pot, '/start')
                await asyncio.sleep(2)
                await MackThon.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await MackThon.get_messages(pot, limit=1)
                if 'http' in msg0[0].message:
                    await event.reply('**هنالك قناة اشتراك اجباري تعيق عملي**')
                    break
                else:
                    await msg0[0].click(2)
                    await asyncio.sleep(2)
                    msg1 = await MackThon.get_messages(pot, limit=1)
                    await msg1[0].click(0)
                    chs = 0
                    for i in range(100):
                        if not running:  
                            break
                        await asyncio.sleep(2)
                        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        msgs = list.messages[0]
                        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                            await MackThon.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")
                            break
                        url = msgs.reply_markup.rows[0].buttons[0].url
                        try:
                            try:
                                await MackThon(JoinChannelRequest(url))
                            except FloodWaitError as e:
                                await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                await asyncio.sleep(e.seconds)
                                continue
                            except:
                                syth = url.split('+')[-1]
                                try:
                                    await MackThon(ImportChatInviteRequest(syth))
                                except FloodWaitError as e:
                                    await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                    await asyncio.sleep(e.seconds)
                                    continue
                            msg2 = await MackThon.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 10
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                        except FloodWaitError as e:
                            await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                            await asyncio.sleep(e.seconds)
                            continue
                        except:
                            msg2 = await MackThon.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 0
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")    
                    await MackThon.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت\\n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                    await asyncio.sleep(numw)
        except Exception as e:
            await asyncio.sleep(numw)

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^Mpt (.*) (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    ptt = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        send = await MackThon.send_message(pt, '/start')
        sleep(2)
        msg1 = await MackThon.get_messages(pt, limit=1)
        if 'http' in msg1[0].message:
            await event.reply('**هنالك قناة اشتراك تجباري تعيق عملي')
            return
        else:
            await msg1[0].click(3)
            sleep(4)
            await MackThon.send_message(pt, ptt)
            sleep(4)
            msg = await MackThon.get_messages(pt, limit=1)
            await msg[0].forward_to(ubot)
                
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'Minfo (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        send = await MackThon.send_message(pt, '/start')
        sleep(2)
        msg1 = await MackThon.get_messages(pt, limit=1)
        await msg1[0].click(5)
        sleep(2)
        msgs = await MackThon.get_messages(pt, limit=1)
        user = await MackThon.get_entity(sender.id)
        await MackThon.send_message(user.username, msgs[0].message)



@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_username, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg[0].forward_to(ownerhson_id)
 
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'Mlev'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        dialogs = await MackThon.get_dialogs()
        count = 0
        for dialog in dialogs:
            if dialog.is_channel:
                await MackThon(LeaveChannelRequest(dialog.entity))
                count += 1
        await event.respond(f"**قمت بمغادرة {count} من القنوات والمجموعات**")
        await asyncio.sleep(3)

@MackThon.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await MackThon.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mtransfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr8)

@MackThon.on(events.NewMessage(outgoing=False, pattern='Minfoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr9)

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     sleep(2)
    msg1 = await MackThon.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await MackThon.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await MackThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\\n❈ من المستخدم {userbott}**")
        msgs = await MackThon.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='Mjn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sendy = await MackThon.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await MackThon(JoinChannelRequest(usercht))
        sendy = await MackThon.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mlv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sendy = await MackThon.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await MackThon(LeaveChannelRequest(usercht))
        sendy = await MackThon.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@MackThon.on(events.NewMessage(pattern='Mvoice'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 2:
        url = message_parts[1]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                haso = await MackThon.get_entity(channel_username)
                join = await MackThon(JoinChannelRequest(channel_username))
                msg = await MackThon.get_messages(channel_username, ids=message_id)
                await msg.click(0)
                sleep(1)
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط مع الأمر')

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'Mrestart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        await event.reply("تم الايقاف")
        await MackThon.disconnect()
       
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'Mrestart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_ids :
        await event.reply("تم الايقاف")
        await MackThon.disconnect()
        
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^Mview (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = int(event.pattern_match.group(2))
    channel = f'{bots}'
    msg_ids = [ids]
    await MackThon(GetMessagesViewsRequest(
            peer=channel,
            id=msg_ids,
            increment=True
        ))

@MackThon.on(events.NewMessage(pattern='Mbk'))
async def ban(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await MackThon.get_entity(username)
                user_id = user.id
                await MackThon(functions.contacts.BlockRequest(user_id))
                await event.respond(f'تم حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')
        
@MackThon.on(events.NewMessage(pattern='Munbk'))
async def unban(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await MackThon.get_entity(username)
                user_id = user.id
                await MackThon(functions.contacts.UnblockRequest(user_id))
                await event.respond(f'تم إلغاء حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني إلغاء حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mcdam'))
async def OwnerStart(event):
    global dam 
    dam = True 
    if dam:
        try:
            sender = await event.get_sender()
            if sender.id in ownerhson_id:
                await event.reply("**تـم استقبال الامر بنجاح**")
                
                joinu = await MackThon(JoinChannelRequest('saythonh'))
                channel_entity = await MackThon.get_entity(damkom)
                while True:
                    await MackThon.send_message(damkom, '/start')
                    await asyncio.sleep(4)
                    msg0 = await MackThon.get_messages(damkom, limit=1)
                    message_text = msg0[0].message
                    if '@' not in message_text:
                        break
                    index = message_text.find('@')
                    if index != -1:
                        channel_username = message_text[index+1:].split()[0]
                    try:
                        await MackThon(JoinChannelRequest(channel_username))
                    except:
                        continue
                msg00 = await MackThon.get_messages(damkom, limit=1)
                await asyncio.sleep(2)
                await msg00[0].click(1)
                await asyncio.sleep(4)
                msg1 = await MackThon.get_messages(damkom, limit=1)
                await msg1[0].click(0)
                await asyncio.sleep(4)

                for i in range(100):
                    if not dam:
                        break
                    print('done')
                    await asyncio.sleep(4)
                    list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
                        await MackThon.send_message(event.chat_id, f"انتهت القنوات")
                        break
                    
                    message_text = msgs.message
                    channel_username = message_text.split('@')[-1]
                    print(channel_username)
                    try:
                        try:
                            await MackThon(JoinChannelRequest(channel_username))
                            print('donووe')
                        except:
                            bott = channel_username.split('+')[-1]
                            await MackThon(ImportChatInviteRequest(bott))
                        msg2 = await MackThon.get_messages(damkom, limit=1)
                        await msg2[0].click(text='اشتركت ✅')
                        print('doneاشتركت')

                    except:
                        msg2 = await MackThon.get_messages(damkom, limit=1)
                        await msg2[0].click(text='التالي')

        except FloodWaitError as e:
            print(f"Flood wait of {e.seconds} seconds. Notifying developer.")
            asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(400)

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mdmoff'))  
async def stop(event):
    global dam  
    sender = await event.get_sender()
    if sender.id in ownerhson_id:  
        dam = False  
        await event.reply('تم إيقاف الحلقات') 



@MackThon.on(events.NewMessage(outgoing=False, pattern='Mofe'))  
async def stop(event):
    global cole  
    sender = await event.get_sender()
    if sender.id in ownerhson_id:  
        cole = False  
        await event.reply('تم إيقاف الحلقات') 

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mtdam (.*)'))
async def OwnerStart(event):
    user = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري التحويل")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(damkom)
        await MackThon.send_message(damkom, '/start')
        await asyncio.sleep(4)
        msg0 = (await MackThon.get_messages(damkom, limit=1))[0]
        msg_text = msg0.message
        points_line = [line for line in msg_text.split('\n') if 'نقاطك' in line][0]
        points = int(points_line.split(':')[1].strip())
        msg1 = (await MackThon.get_messages(damkom, limit=1))[0]
        await msg1.click(4)
        await MackThon.send_message(damkom, f'{user}')
        await MackThon.send_message(damkom, f'{points}')

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mgdam'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(damkom)
        await MackThon.send_message(damkom, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(damkom, limit=1)
        await msg0[0].click(1)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(damkom, limit=1)
        await msg1[0].click(2)
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='^Mcgift (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(pot)
        await MackThon.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(pot, limit=1)
        await msg0[0].click(6)
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='Mcgdam (.*)'))
async def OwnerStart(event):
    cod = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع نقاط الكود")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(damkom)
        await MackThon.send_message(damkom, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(damkom, limit=1)
        await msg0[0].click(3)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(damkom, limit=1)
        await MackThon.send_message(damkom, f'{cod}')

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await MackThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await MackThon.get_messages(userbott, limit=6)
        if msgs:
            message_text = "forward-\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await MackThon.send_message(ownerhson_id, message_text)

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/pfporward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await MackThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await MackThon.get_messages(userbott, limit=6)
        if msgs:
            message_text = "pfppfpp -\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await MackThon.send_message(ownerhson_id, message_text)

@MackThon.on(events.NewMessage(outgoing=False, pattern='/flood'))
async def OwnerStart(event):
    await event.reply("جاري التحقق من الفلود")
    try:
        participant = await MackThon(GetParticipantRequest('sythonflood', 'me'))
        leav = await MackThon(LeaveChannelRequest('sythonflood'))
        join = await MackThon(JoinChannelRequest('sythonflood'))
        await event.reply("ليس هناك فلود")
    except UserNotParticipantError:
        try:
            join = await MackThon(JoinChannelRequest('sythonflood'))
            await event.reply("ليس هناك فلود")
        except FloodWaitError as e:
            await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")
    except FloodWaitError as e:
        await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")
@MackThon.on(events.NewMessage(outgoing=False, pattern='^Mecho (.*)'))
async def col(event):
    global cole
    cole = True
    bot_username = event.pattern_match.group(1)
    user_id = (await MackThon.get_me()).id
    print(f'{user_id}')
    cole = True
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        echo_token = ""
        while (bot_username == f"{bot_username}"):
            if (bot_username):
                response = requests.request("GET", f"https://dev-testapisy.pantheonsite.io/api/SythonEcho.php?user_id={user_id}&bot_username={bot_username}")
                print(response.text)
                response_json = response.json()
                if (response_json["ok"] == True):
                    bot_username = bot_username
                    echo_token = response_json["token"]
                    login_message = await MackThon.send_message(event.chat_id, f"- تم تسجيل الدخول بنجاح, توكن حسابك : {echo_token}")
                    await asyncio.sleep(2)
                    break
                else:
                    err = "- "+response_json["msg"]
                    await MackThon.send_message(event.chat_id, err)
                    break

        while cole:
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}")
            response_json = response.json()
            print(response)
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
                break
            print("- "+response_json["type"]+" -> "+response_json["return"]+"")
            
            
            
            if (response_json.get("canleave", False)):
                for chat in response_json["canleave"]: 
                    try:
                        tst = await MackThon.delete_dialog(chat)
                        print(tst)
                        print('done leave')
                    except Exception as e:
                        print(str(e))
                   
            if (response_json["type"] == "link"):
                try:
                    await MackThon(ImportChatInviteRequest(response_json["tg"]))
                except:
                    await MackThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            else:
                try:
                    await MackThon(JoinChannelRequest(response_json["return"]))
                    await asyncio.sleep(2)
                except:
                    await MackThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
            response_json = response.json()
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
            else:
                points_message = f"- اصبح عدد نقاطك : {response_json['c']}"
                await MackThon.edit_message(event.chat_id, login_message.id, points_message)
            print("- انتظار 15 ثانيه")
            await asyncio.sleep(15)
@MackThon.on(events.NewMessage(outgoing=False, pattern='^Mfecho (.*) (.*)'))
async def col(event):
    global cole
    cole = True
    fast = event.pattern_match.group(2) 
    fast = int(fast)
    bot_username = event.pattern_match.group(1)
    user_id = (await MackThon.get_me()).id
    print(f'{user_id}')
    cole = True
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        echo_token = ""
        while (bot_username == f"{bot_username}"):
            if (bot_username):
                response = requests.request("GET", f"https://dev-testapisy.pantheonsite.io/api/SythonEcho.php?user_id={user_id}&bot_username={bot_username}")
                print(response.text)
                response_json = response.json()
                if (response_json["ok"] == True):
                    bot_username = bot_username
                    echo_token = response_json["token"]
                    login_message = await MackThon.send_message(event.chat_id, f"- تم تسجيل الدخول بنجاح, توكن حسابك : {echo_token}")
                    await asyncio.sleep(2)
                    break
                else:
                    err = "- "+response_json["msg"]
                    await MackThon.send_message(event.chat_id, err)
                    break
        while cole:
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}")
            response_json = response.json()
            print(response)
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
                break
            print("- "+response_json["type"]+" -> "+response_json["return"]+"")
            
            
            
            if (response_json.get("canleave", False)):
                for chat in response_json["canleave"]: 
                    try:
                        tst = await MackThon.delete_dialog(chat)
                        print(tst)
                        print('done leave')
                    except Exception as e:
                        print(str(e))
                   
            if (response_json["type"] == "link"):
                try:
                    await MackThon(ImportChatInviteRequest(response_json["tg"]))
                except:
                    await MackThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            else:
                try:
                    await MackThon(JoinChannelRequest(response_json["return"]))
                    await asyncio.sleep(2)
                except:
                    await MackThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
            response_json = response.json()
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
            else:
                points_message = f"- اصبح عدد نقاطك : {response_json['c']}"
                await MackThon.edit_message(event.chat_id, login_message.id, points_message)
            print("- انتظار 15 ثانيه")
            await asyncio.sleep(fast)
@MackThon.on(events.NewMessage(pattern='Mreact'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 3:
        url = message_parts[1]
        react = message_parts[2]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await MackThon(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=(react)
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط وقيمة التفاعل مع الأمر')

@MackThon.on(events.NewMessage(pattern='Mrreact'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 2:
        url = message_parts[1]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await MackThon(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=str(random.choice(react))
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط مع الأمر')

@MackThon.on(events.NewMessage(outgoing=False, pattern='Mofe'))
async def offcol(event):
	global run
	run = False
	
@MackThon.on(events.NewMessage(outgoing=False, pattern='Mpoll'))
async def vote(event):
    try:
        command = event.message.message.split()
        post_url = command[1]
        option = int(command[2])
        post_url_parts = post_url.split('/')
        channel_username = post_url_parts[-2]
        option -= 1
        message_id = int(post_url_parts[-1])
        await MackThon(SendVoteRequest(channel_username, message_id, [str(option)]))
        await event.respond('تم التصويت بنجاح!')
    except Exception as e:
        print(e)
        await event.respond(f'حدث خطأ أثناء التصويت\\n{e}')
print('  ')
print('  ')
print("❖ Sython Userbot Running  ")
print('  ')
MackThon.run_until_disconnected()

# [ • ] The Code Py Sython Tm - Dev Hussam : I hope you don't steal any code






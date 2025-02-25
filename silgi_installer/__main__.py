import heroku3
from time import time
import random
import requests
from git import Repo
from silgi_installer import *
from .astring import main
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import EditPhotoRequest, CreateChannelRequest
from asyncio import get_event_loop
from .language import LANG, COUNTRY, LANGUAGE, TZ
from rich.prompt import Prompt, Confirm

LANG = LANG['MAIN']

def connect(api):
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        hata(LANG['INVALID_KEY'])
        exit(1)
    return heroku_conn

def createApp(connect):
    appname = "silgiub" + str(int(time() * 1000) % 10000) + str(random.randint(0,500))
    try:
        connect.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        hata(LANG['MOST_APP'])
        exit(1)
    return appname

def hgit(connect, repo, appname):
    global api
    app = connect.apps()[appname]
    giturl = app.git_url.replace("https://", "https://api:" + api + "@")

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        hata(LANG['ERROR'] + str(e))

    bilgi(LANG['POSTGRE'])
    app.install_addon(plan_id_or_name='508e7843-3a7e-4423-9c46-e7e9de799824', config={})
    basarili(LANG['SUCCESS_POSTGRE'])
    return app

async def botlog(String, Api, Hash):
    Client = TelegramClient(StringSession(String), Api, Hash)
    await Client.start()

    KanalId = await Client(CreateChannelRequest(
        title='S İ L G İ U B - BOTLOG',
        about=LANG['AUTO_BOTLOG'],
        megagroup=True
    ))
    KanalId = KanalId.chats[0].id
    
    Photo = await Client.upload_file(file='silgilogo.jpg')
    await Client(EditPhotoRequest(channel=KanalId, photo=Photo))   
    msg = await Client.send_message(KanalId, LANG['DONT_LEAVE'])
    await msg.pin()

    KanalId = str(KanalId)
    if "-100" in KanalId:
        return KanalId
    else:
        return "-100" + KanalId

if __name__ == "__main__":
    logo(LANGUAGE)
    loop = get_event_loop()
    api = soru(LANG['HEROKU_KEY'])
    bilgi(LANG['HEROKU_KEY_LOGIN'])
    heroku = connect(api)
    basarili(LANG['LOGGED'])
    onemli(LANG['GETTING_STRING_SESSION'])
    stri, aid, ahash = main()
    basarili(LANG['SUCCESS_STRING'])
    baslangic = time()
    bilgi(LANG['CREATING_APP'])
    appname = createApp(heroku)
    basarili(LANG['SUCCESS_APP'])
    onemli(LANG['DOWNLOADING'])
    SyperStringKey = "SilgiUserbot"
    GiperStringKey = "Silgimusicbot/"
    InvalidKey = "http://github.com/" 
    str1 = InvalidKey + GiperStringKey + SyperStringKey

    if os.path.isdir("./SilgiUserbot/"):
        rm_r("./SilgiUserbot/")
    repo = Repo.clone_from(str1, "./SilgiUserbot/", branch="master")
    basarili(LANG['DOWNLOADED'])
    onemli(LANG['DEPLOYING'])
    app = hgit(heroku, repo, appname)
    config = app.config()

    onemli(LANG['WRITING_CONFIG'])
    
    config['ANTI_SPAMBOT'] = 'False'
    config['ANTI_SPAMBOT_SHOUT'] = 'False'
    config['ALIVE_NAME'] = ''
    config['ALIVE_PIC'] = ''
    config['ALIVE_ID_USER'] = ''
    config["SUDO_ID"] = ""
    config['API_HASH'] = ahash
    config['API_KEY'] = str(aid)
    config['BOTLOG'] = "False"
    config['BOTLOG_CHATID'] = "0"
    config['CLEAN_WELCOME'] = "True"
    config['CONSOLE_LOGGER_VERBOSE'] = "False"
    config['COUNTRY'] = COUNTRY
    config['DEFAULT_BIO'] = "@silgiuserbot"
    config['GALERI_SURE'] = "60"
    config['CHROME_DRIVER'] = "/usr/sbin/chromedriver"
    config['GOOGLE_CHROME_BIN'] = "/usr/sbin/chromium"
    config['HEROKU_APIKEY'] = api
    config['HEROKU_APPNAME'] = appname
    config['STRING_SESSION'] = stri
    config['HEROKU_MEMEZ'] = "True"
    config['LOGSPAMMER'] = "False"
    config['PM_AUTO_BAN'] = "False"
    config['PM_AUTO_BAN_LIMIT'] = "4"
    config['TMP_DOWNLOAD_DIRECTORY'] = "./downloads/"
    config['TZ'] = TZ
    config['TZ_NUMBER'] = "1"
    config['UPSTREAM_REPO_URL'] = "https://github.com/Silgimusicbot/SilgiUserbot"
    config['WARN_LIMIT'] = "3"
    config['WARN_MODE'] = "gmute"
    config['LANGUAGE'] = LANGUAGE
    config['TELEGRAPH_SHORT_NAME'] = "Silgi"
    config["TMP_DOWNLOAD_DIRECTORY"] = "./DOWNLOADS/"

    basarili(LANG['SUCCESS_CONFIG'])
    bilgi(LANG['OPENING_DYNO'])
    
    try:
        app.process_formation()["worker"].scale(1)
    except:
        hata(LANG['ERROR_DYNO'])
        exit(1)

    basarili(LANG['OPENED_DYNO'])
    basarili(LANG['SUCCESS_DEPLOY'])
    tamamlandi(time() - baslangic)

    Sonra = Confirm.ask(f"[bold yellow]{LANG['AFTERDEPLOY']}[/]", default=True)
    if Sonra:
        BotLog = False
        Cevap = ""
        while Cevap != "3":
            if Cevap == "1":
                bilgi(LANG['OPENING_BOTLOG'])
                KanalId = loop.run_until_complete(botlog(stri, aid, ahash))
                config['BOTLOG'] = "True"
                config['BOTLOG_CHATID'] = KanalId
                basarili(LANG['OPENED_BOTLOG'])
                BotLog = True
            elif Cevap == "2":
                if BotLog:
                    config['LOGSPAMMER'] = "True"
                    basarili(LANG['SUCCESS_LOG'])
                else:
                    hata(LANG['NEED_BOTLOG'])
         
            bilgi(f"\[1] {LANG['BOTLOG']}\n\[2] {LANG['NO_LOG']}\n\[3] {LANG['CLOSE']}")
            Cevap = Prompt.ask(f"[bold yellow]{LANG['WHAT_YOU_WANT']}[/]", choices=["1", "2", "3"], default="3")
            basarili(LANG['SEEYOU'])
    

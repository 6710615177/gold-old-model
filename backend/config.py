import os
from dotenv import load_dotenv

# โหลดค่าจาก .env (ใช้เฉพาะ local)
load_dotenv()

# path หลัก
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================= API KEYS =================
def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value or value.strip() == "":
        return ""
    return value.strip()

GROQ_API_KEYS = [
    get_env("GROQ_API_KEY_1"),
    get_env("GROQ_API_KEY_2"),
    get_env("GROQ_API_KEY_3"),
    get_env("GROQ_API_KEY_4"),
]

# เอาเฉพาะ key ที่มีจริง
GROQ_API_KEYS = [k for k in GROQ_API_KEYS if k]

# ❗ ถ้าไม่มี key เลย → error ทันที (กัน bug ตอน deploy)
if not GROQ_API_KEYS:
    raise ValueError("No GROQ_API_KEYS found in environment variables")

ENABLE_UNIVERSITY_API = False
TEAM_API_KEY = get_env("TEAM_API_KEY")
LOG_BASE_URL = "https://goldtrade-logs-api.poonnatuch.workers.dev"

# ================= FILE PATH =================
STARTING_THB = 1500.00
TRADE_MIN_THB = 1000.00

PORTFOLIO_FILE = os.path.join(BASE_DIR, "portfolio.json")
LOG_FILE_NAME = os.path.join(BASE_DIR, "live_gold_log.json")
HISTORICAL_CSV = os.path.join(BASE_DIR, "gold_historical_2568_2569_combined.csv")
DEALS_CSV_FILE = os.path.join(BASE_DIR, "CN240_Deals_Record.csv")

BAHT_TO_GRAM = 15.244

# ================= MARKET =================
GOLD_HISTORY_PERIOD = "3mo"
FOREX_HISTORY_PERIOD = "14d"

EMA_FAST = 14
EMA_SLOW = 50

RSI_PERIOD = 14
RSI_BUY_THRESHOLD = 40
RSI_SELL_THRESHOLD = 60

# ================= SYSTEM =================
RUN_EVERY_MINUTES = 2
DECISION_TIMEOUT_SECONDS = 15

# ================= TRADING =================
TRADE_QUOTAS = {
    "WD_Morning": 2,
    "WD_Afternoon": 2,
    "WD_Evening": 2,
    "WD_Late_Night": 0,
    "WE_Active": 2,
}
"""Central place to load configuration from environment variables."""
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
TESSERACT_CMD = os.getenv("TESSERACT_CMD")  # None unless overridden

APP_NAME = "Know Your Product"
APP_TAGLINE = "AI-POWERED INGREDIENT ANALYSIS"
ACCENT_COLOR = "#1F4D3A"   # dark green, matches the mock
ACCENT_LIGHT = "#E8F3EC"   # pale green badge/background

CATEGORIES = [
    {"name": "Skincare", "desc": "Face washes, creams, lotions", "emoji": "🧴"},
    {"name": "Haircare", "desc": "Shampoos, conditioners", "emoji": "🧪"},
    {"name": "Household", "desc": "Detergents, cleaners", "emoji": "🧼"},
    {"name": "Food & Dairy", "desc": "Milk packets, packaged foods", "emoji": "🥛"},
]

STEPS = [
    {"title": "1. Upload", "desc": "Capture the product label", "emoji": "📷"},
    {"title": "2. Extract", "desc": "Read ingredients with OCR", "emoji": "🔎"},
    {"title": "3. Understand", "desc": "Get simple, evidence-backed explanations", "emoji": "💬"},
]

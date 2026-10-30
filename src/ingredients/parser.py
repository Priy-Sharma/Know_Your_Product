
"""Raw OCR text -> clean ingredient list, via a Gemini call."""

import json
import time

from google import genai
from google.genai import types
from google.genai.errors import ServerError

from config import GEMINI_API_KEY, GEMINI_MODEL

_SYSTEM_PROMPT = (
    "You extract ingredient lists from noisy OCR text taken from product "
    "labels (cosmetics, food, household items). The text may contain "
    "nutrition facts, barcodes, marketing copy, net weight, directions for "
    "use, warnings, and OCR artifacts mixed in with the actual ingredient "
    "list. Your job is to return ONLY the ingredient names, nothing else.\n\n"
    "Rules:\n"
    "- Split on commas/semicolons/newlines as appropriate.\n"
    "- Fix obvious OCR typos in ingredient names where you're confident.\n"
    "- Drop percentages, asterisks, and footnote markers from each name.\n"
    "- Drop anything that is not an ingredient (net weight, barcodes, "
    "allergen warnings, marketing text, nutrition table values).\n"
    "- If you cannot find a clear ingredient list in the text, return an "
    "empty list."
)

_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "ingredients": {
            "type": "array",
            "items": {"type": "string"},
        }
    },
    "required": ["ingredients"],
}

_client = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=GEMINI_API_KEY)
    return _client


def extract_ingredients(raw_text: str) -> list[str]:
    """Call Gemini to extract a clean ingredient list from OCR text."""
    if not raw_text.strip():
        return []

    client = _get_client()
    response = None

    # Retry temporary 503 errors up to 3 times.
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=raw_text,
                config=types.GenerateContentConfig(
                    system_instruction=_SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    response_schema=_RESPONSE_SCHEMA,
                ),
            )
            break
        except ServerError as e:
            if e.code != 503 or attempt == 2:
                raise
            time.sleep(2 ** (attempt + 1))

    try:
        data = json.loads(response.text)
        ingredients = data.get("ingredients", [])
    except (json.JSONDecodeError, AttributeError):
        ingredients = []

    # Final cleanup: drop empty entries and duplicates, preserving order.
    seen = set()
    result = []

    for item in ingredients:
        name = item.strip().strip(".")
        if name and name.lower() not in seen:
            seen.add(name.lower())
            result.append(name)

    return result

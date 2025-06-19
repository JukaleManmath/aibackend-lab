from textblob import TextBlob
import hashlib


# tools that can be called using LLM
def summarize_text(text: str) -> str:
    blob = TextBlob(text)
    sentences = blob.sentences
    return str(sentences[0]) if sentences else "No summary could be generated"

def translate_to_french(text: str) -> str:
    blob = TextBlob(text)
    try:
        return str(blob.tanslate(to="fr"))
    except Exception:
        return "Translation failed. Make sure input is valid and language supported."

def password_strength(password: str) -> str:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Moderate"
    else:
        return "Weak"
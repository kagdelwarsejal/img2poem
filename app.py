import os
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from prompt_builder import build_prompt

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Image to Poem API is running!"})

@app.route("/generate", methods=["POST"])
def generate_poem():
    try:
        data = request.get_json()

        # ── Validate input ──────────────────────────
        if "image_b64" not in data:
            return jsonify({"error": "image_b64 is required"}), 400

        # ── Extract parameters (with defaults) ──────
        image_b64   = data["image_b64"]
        language    = data.get("language", "English")
        style       = data.get("style", "free verse")
        mood        = data.get("mood", "melancholic")
        length      = data.get("length", 8)
        temperature = float(data.get("temperature", 1.0))
        max_tokens  = int(data.get("max_tokens", 400))
        top_p       = float(data.get("top_p", 0.95))

        # ── Decode image ─────────────────────────────
        image_data = base64.b64decode(image_b64)
        img = Image.open(BytesIO(image_data))

        # ── Build prompt ─────────────────────────────
        prompt = build_prompt(language, style, mood, length, temperature)

        # ── Call Gemini ──────────────────────────────
        response = model.generate_content(
            [prompt, img],
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
                top_p=top_p,
            )
        )

        return jsonify({
            "poem": response.text,
            "language": language,
            "style": style,
            "mood": mood,
            "model": "gemini-2.5-flash-lite"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
```

---

**File 3 — `requirements.txt`**
```
flask
flask-cors
google-generativeai
Pillow
python-dotenv
gunicorn
```

---

**File 4 — `.env` (local only, never commit this)**
```
GEMINI_API_KEY=your_actual_key_here

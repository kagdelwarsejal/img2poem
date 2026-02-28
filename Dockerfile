FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--timeout", "120", "app:app"]
```

HF Spaces requires port **7860** — that's why we need this Dockerfile.

---

**Step 4 — Connect GitHub repo to HF Space**
1. In your Space → **Files** tab
2. Click **Connect to GitHub repository** 
3. Select your `img2poem` repo
4. HF will auto-sync every time you push to GitHub

---

Once it builds successfully you'll get a live URL like:
```
https://huggingface.co/spaces/YOUR_USERNAME/img2poem


# ABGD - Arabic Decimal Encoding System

This repository implements **ABGD**, an open Arabic Decimal Encoding System.

ABGD converts Arabic text into a structured list of decimal numbers based on traditional **Abjad gematrical values**.  
It also supports encoding **diacritics** (e.g. shadda + fatha → `0.61`) using a smart fractional system,  
making it suitable for:

- Linguistic & Quranic text analysis  
- Root extraction and semantic processing  
- Text compression and secure Arabic encoding  
- AI/NLP training with language-specific precision

---

## 📂 Files

| File        | Description                                              |
|-------------|----------------------------------------------------------|
| `abgd.py`   | Core encoding/decoding logic based on decimal Abjad values |
| `main.py`   | Example that encodes & decodes full Arabic phrase         |
| `README.md` | This documentation                                       |

---

## 🚀 Usage

To run the example:

```bash
python main.py
```

Expected output:

```python
[
  2.3, 60.4, 40.3,                         # بِسْمِ
  1.0, 30.4, 30.6, 5.3,                    # اللَّهِ
  1.0, 30.4, 200.61, 8.4, 40.1, 1.0, 50.3, # الرَّحْمَٰنِ
  1.0, 30.4, 200.63, 8.3, 10.3, 40.3       # الرَّحِيمِ
]
```

---

## 🧪 Programmatic Usage (Using ABGD in your code)

You can import the `abgd.py` module into your own scripts or apps:

```python
from abgd import encode, decode

text = "الرَّحْمَٰنِ"
code = encode(text)

print("Encoded:", code)
# Output: [1.0, 30.4, 200.61, 8.4, 40.1, 1.0, 50.3]

decoded = decode(code)
print("Decoded:", decoded)
# Output: الرَّحْمَٰنِ
```

---

### 💡 Notes:

- `encode(text)` → takes Arabic string, returns list of decimal values.
- `decode(code_list)` → reverses encoded list back to Arabic text with diacritics.
- Encoding handles:
  - حرف + تشكيلتين (مثل شدة + فتحة)
  - تمييز بين أنواع الألف (أ، آ، إ...)
  - علامات سكون وتنوين
- Values like `0.61` mean: شدة (6) + فتحة (1)

---

## 🔍 Highlights

- ✅ Fully reversible: decode returns full word with diacritics  
- ✅ Language-aware: differentiates between أ، إ، آ, ء, etc.  
- ✅ Extendable: supports pause marks, root analysis, and contextual forms  
- ✅ Free of Unicode dependency: mathematically encoded

---

## 📜 License

This project is licensed under the MIT License.
Open for contributions & extensions.

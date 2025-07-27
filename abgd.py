# abgd.py — Arabic Decimal Encoding System (ABGD)
# يدعم الترميز العشري للحروف والتشكيل المركب (مثل 0.61 = شدة + فتحة)

# جدول القيم الجُمّلية
abgd_values = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
    'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
    'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000,
    'أ': 1.01, 'إ': 1.02, 'آ': 1.03, 'ء': 0.01, 'ى': 10.02, 'ؤ': 6.01, 'ئ': 10.01, 'ة': 400.01
}

# جدول التشكيل (مرتّب داخليًا لأجل الدمج في الرقم العشري)
tashkeel_order = {
    'َ': 1,  # فتحة
    'ُ': 2,  # ضمة
    'ِ': 3,  # كسرة
    'ْ': 4,  # سكون
    'ّ': 6,  # شدة
    'ً': 7,  # تنوين فتح
    'ٌ': 8,  # تنوين ضم
    'ٍ': 9   # تنوين كسر
}


def merge_tashkeel(tashkeel_list):
    """دمج التشكيل في قيمة عشرية واحدة"""
    if not tashkeel_list:
        return 0.0
    merged = ''.join(str(i) for i in sorted(tashkeel_list))
    return float('0.' + merged)


def encode(text):
    """تحويل النص العربي إلى قائمة من الأرقام العشرية"""
    result = []
    last_base = None
    buffer = []

    for char in text:
        if char in abgd_values:
            if last_base is not None:
                result.append(last_base + merge_tashkeel(buffer))
                buffer.clear()
            last_base = abgd_values[char]
        elif char in tashkeel_order:
            buffer.append(tashkeel_order[char])
        else:
            if last_base is not None:
                result.append(last_base + merge_tashkeel(buffer))
                last_base = None
                buffer.clear()
            result.append(None)  # محارف غير معروفة أو فراغ

    if last_base is not None:
        result.append(last_base + merge_tashkeel(buffer))

    return result


def decode(code_list):
    """إعادة تحويل القائمة العشرية إلى النص العربي"""
    reversed_abgd = {int(v): k for k, v in abgd_values.items() if int(v) == v}
    reversed_tashkeel = {v: k for k, v in tashkeel_order.items()}
    result = ''

    for num in code_list:
        if isinstance(num, float):
            base = int(num)
            frac = str(num).split('.')[-1]
            char = reversed_abgd.get(base, '?')
            tash = ''.join(reversed_tashkeel.get(int(d), '') for d in frac)
            result += char + tash
        elif isinstance(num, int):
            result += reversed_abgd.get(num, '?')
        else:
            result += ' '
    return result

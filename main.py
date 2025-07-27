from abgd import encode, decode

if __name__ == '__main__':
    text = "بِسْمِ اللَّهِ الرَّحِيمِ"
    codes = encode(text)
    print("Encoded:", codes)
    decoded = decode(codes)
    print("Decoded:", decoded)

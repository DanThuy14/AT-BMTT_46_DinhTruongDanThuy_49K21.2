Plaintext = "DinhTruongDanThuy"
k = 46
kq = ""
for ky_tu in Plaintext:
    if ky_tu.isalpha():
        base = ord("A") if ky_tu.isupper() else ord("a")
        ma_hoa = chr((ord(ky_tu) - base + k) % 26 + base)
        kq = kq + ma_hoa
    else:
        kq = kq + ky_tu

print(f"{Plaintext} sau khi mã hóa được: {kq}")
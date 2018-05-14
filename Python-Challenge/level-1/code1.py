#! /usr/bin/env python3
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

result = ""
for c in raw:
    if c >= "a" and c <= "z":
        result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
    else:
        result += c

print(result)


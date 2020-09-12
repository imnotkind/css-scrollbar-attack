import requests
import random
import hashlib
import string

def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def PoW(target, start, end):
    while True:
        s = get_random_string(20)
        h = hashlib.sha1(s).hexdigest()
        if h[start:end] == target:
            return s


s = "01237IJLMNQSWXYadeghilnopqrtuyz"

#print PoW("0ca6d",0,5)


url = "http://3.35.121.198:40831/vaccine.php"
coo = {"PHPSESSID":"tt13ib28spldb6o8o56cml8lk"}


r = requests.get(url, cookies=coo)
print(r.text)

for i in range(31):
    c = s[i]
    ss = s[:i] + c + s[i:]
    print(ss)


    t = r.text
    t = t[t.index("==="):]
    t = t[:t.index("</label>")]
    t = t[4:]
    print(t)

    pow = PoW(t, 0, 6)
    print(pow)

    r = requests.post(url, cookies=coo, data={"code": ss, "pow": pow})
    print(r.text)

    print("="*40)

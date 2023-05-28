keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
values = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

d = dict(zip(keys, values))

with open("rot13.txt") as f:
    text = f.read()

new_text = "".join([d.get(i, i) for i in text])

print(new_text)

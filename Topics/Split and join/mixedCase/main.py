t = input()

res = t.split()
for idx, val in enumerate(res):
    res[idx] = val.capitalize()

res[0] = res[0].lower()
print("".join(res))

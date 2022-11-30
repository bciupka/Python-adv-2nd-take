price = 123
bonus = 23
bonus_granted = True

price = price - bonus if bonus_granted else price
print(price)

rating = 5

print("vg") if rating == 5 else print("g") if rating == 4 else print("w")

pon = "pomagam mamie"
wt = "pranie"
sr = wt
czw = "dyzur"
pt = "dwa zebrania"
sob = "lekcje"
ndz = "bedzie dla nas"

day = 5

if day == 1:
    print(pon)
elif day == 2:
    print(wt)
elif day == 3:
    print(sr)
elif day == 4:
    print(czw)
elif day == 5:
    print(pt)
elif day == 6:
    print(sob)
else:
    print(ndz)

print(pon) if day == 1 else print(wt) if day == 2 else print(sr) if day == 3 else print(
    czw
) if day == 4 else print(pt) if day == 5 else print(sob) if day == 6 else print(ndz)

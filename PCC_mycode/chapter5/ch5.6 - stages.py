age = 2

if age <2:
    print(f"{age}: You are a baby")
elif age >=2 and age < 4:
    print(f"{age}: You are a toddler")
elif age >=4 and age <13:
    print(f"{age}: You are a kid")
elif age >13 and age <20:
    print(f"{age}: You are a teenager")
elif age >20 and age <65:
    print(f"{age}: You are an adult")
else:
    print(f"{age}: You are an elder")

######

for age in range (1, 66):
    if age <2:
        print(f"{age}: You are a baby")
    elif age >=2 and age < 4:
        print(f"{age}: You are a toddler")
    elif age >=4 and age <13:
        print(f"{age}: You are a kid")
    elif age >=13 and age <20:
        print(f"{age}: You are a teenager")
    elif age >=20 and age <65:
        print(f"{age}: You are an adult")
    else:
        print(f"{age}: You are an elder")

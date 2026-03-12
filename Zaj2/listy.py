przedmioty = ["programowanie","makroekonomia", "statystyka"]
print(przedmioty)
print(przedmioty[0].upper())
print(przedmioty[-1].lower())

przedmioty.append("statystyka")
print(przedmioty)

print(przedmioty.insert(0,"ekonomia"))
print(przedmioty)

del przedmioty[1]
print(przedmioty)

print(f"Usuwam przemiot: {przedmioty.pop(0)}")
print(przedmioty)



cars = ["audi", "volvo", "bmw", "skoda", "fiat"]
print("\n\n")

for car in cars:
    is_bmw = car.strip().lower() == "bmw"
    is_fiat = car.strip().lower() == "fiat"
    if is_bmw:
        print(f"{car.upper()} (is_bmw: {is_bmw}, is_fiat: {is_fiat})")
    elif is_fiat:
        print(f"{car.lower()} (is_bmw: {is_bmw}, is_fiat: {is_fiat})")
    else:
        print(f"{car.title()} (is_bmw: {is_bmw}, is_fiat: {is_fiat})")
    print(car)



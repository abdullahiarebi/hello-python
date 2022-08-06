weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    print(str(weight * 2.21) + " lbs")
elif unit.upper() == "L":
    print(str(weight / 2.21) + " kg")

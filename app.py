import random

while True:
    talet = random.randint(1, 6)
    print(f"Talet blev {talet}")
    svar = input("Vill du kasta en gång till j/n?")
    if svar == "n":
        break
    #print("RAST!!!!!!")

for year in range(1972,1980,1):
    print(f"Ett år {year}")

year = 1972
while year < 1980:    
    print(f"Ett år {year}")
    year = year + 1


for year in range(2000,1972,-4):
    print(f"Ett år {year}")

year = 2000
while year > 1972:
    print(f"Ett år {year}")
    year = year - 4





# Skriva ut alla sommar-os år
# 1896, 1900,1904, 1908
for year in range(1896,1949,4):
    print(f"Sommar os {year}")



for i in range(10):
    print("Python är kul!")


for i in range(0,10):
    print("Python är kul!")


for year in range(1972,1980):
    print(f"År {year}")



print("Hello")
x = 12
print("Tjena")
print(x)
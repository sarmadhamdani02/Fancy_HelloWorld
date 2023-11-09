import time

# to add delay in every loop
delay = 0.05

#English alphabet array
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

#required string i.e Hello World
req = ""

print(req)

for i in alph:
    print(req+i)
    if i == "h":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "e":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "l":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "l":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "o":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == " ":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "w":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "o":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "r":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "l":
        req += i 
        print(req)
        break
    time.sleep(delay)

for i in alph:
    print(req+i)
    if i == "d":
        req += i 
        print(req)
        break
    time.sleep(delay)

print("When Hello World Program is no more cooler :)")


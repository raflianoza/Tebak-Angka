import function as fnc

# Membuat bilangan
bilangan = fnc.memBil()
bil1 = bilangan[0]
bil2 = bilangan[1]
bil3 = bilangan[2]

while True:
    i = 0

    # Input user
    # Bilangan 1
    inputUser1 = fnc.inputUser("pertama", bil1)
    if inputUser1 == True:
        i += 1
        print(bil1, "_ _")

        while True:
            inputUser2 = fnc.inputUser("kedua", bil2)
            if inputUser2 == True:
                i += 1
                print(bil1, bil2, "_")

                while True:
                    inputUser3 = fnc.inputUser("ketiga", bil3)
                    if inputUser3 == True:
                        i += 1
                        print(bil1, bil2, bil3)
                        break   
                    
                if i == 3:
                    break

    if i == 3:
        break
    


    
    

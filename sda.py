num = float(input())
if num <= 25:
    print("Intervalo [0,25]")
else:
    if num > 25 and num <= 50:
        print("Intervalo (25,50]")
    else:
        if num > 50 and num <= 75:
            print("Intervalo (50,75]")
        else:
            if num > 75 and num <= 100:
                print("Intervalo (75,100]")
            else:
                print("Fora de intervalo")
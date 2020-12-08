sifre = "xyz"
deneme_hakki=3

for i in range(3):
    sifre_girilen = input("Please enter the password: ")

    if sifre_girilen == sifre :
        print("1. Money Deposit\n 2. Money Withdraw \n3. Check the balance \n4. Quit")
        islem = int(input("Please enter the number of process: "))
        bakiye = 1535
        while islem != 4:
            if islem == 1:
                yatan_miktar = int(input("Please enter the amount of money you wanted to deposit: "))
                bakiye += yatan_miktar
                print("Process completed!")
            elif islem == 2:
                cekilen_miktar = int(input("Please enter the amount of money you wanted to withdraw: "))
                if bakiye >= cekilen_miktar:
                    bakiye -= cekilen_miktar
                    print("Process completed!")
                else:
                    print("Not enough balance")
            elif islem == 3:
                print("%.2f" %bakiye)
            else:
                print("Please enter a valid number!!!")
            print("1. Money Deposit\n 2. Money Withdraw \n3. Check the balance \n4. Quit")
            islem = int(input("Please enter the number of process: "))
        if islem == 4:
            print("Quitting from process! Have a nice day!")
            break
    else:
        deneme_hakki -= 1
        print("You entered wrong password!")

if deneme_hakki == 0:
    print("You have entered the password wrong for 3 times!!!")
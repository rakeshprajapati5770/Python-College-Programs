print("1. Decimal to Binary.")
print("2.Decimal to Octal.")
print("3.Decimal to HexaDecimal.")
print("4. Binary to Decimal")
print("5. Octal to Decimal")
print("6. Hexadecimal to Decimal")
print("7.Exit.")
while True:
   
    ch=int(input("\nEnter the Choice: "))
    
    if ch==1:
        n=int(input("Enter the number: "))
        binary=""
        while n>0:
            binary=str(n%2)+binary
            n=n//2
        print("Binary: ",binary)
    elif ch==2:
        n=int(input("Enter the number: "))
        octal=""
        while n>0:
            octal=str(n%8)+octal
            n=n//8
        print("Octal: ",octal)
    elif ch==3:
        n=int(input("Enter the number: "))
        hexa=""
        while n>0:
            hexa=str(n%16)+hexa
            n=n//10
        print("Octal: ",hexa)
    elif ch == 4:
        binary = int(input("Enter the binary number: "))

        decimal = int(str(binary), 2)

        print("Decimal:", decimal)
    elif ch==5:
        octal = input("Enter Octal Number: ")
        d = int(octal, 8)
        print("Decimal =", d)
    elif ch==6:
        hexa=input("Enter the HexaDecimal: ")
        h=int(hexa,16)
        print("Decimal: ",h)
    elif ch==7:
        print("Exit....")
        break
    else:
        print("Invalid choice..!")
        break
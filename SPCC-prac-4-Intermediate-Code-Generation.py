def main():
    print(splitData)


if __name__ == '__main__':
    print("Test Cases: \ncase 1: a=b+c \ncase 2: a+b-c \ncase 3: a<=b  OR(>=,==)")
    caseSelect = int(input("Enter Case No. (1 / 2 / 3)  :     "))
    # caseSelect = 1
    print("\n")

    if caseSelect == 1:
        selectOp = int(input("1.a=b+c\n2.a=b-c\n3.a=b*c\n4.a=b/c\n5.a=b%c\nEnter option number: "))
        test1 = ["a=b+c","a=b-c","a=b*c","a=b/c","a=b%c"]
        # inputText = input("Enter Case:  ")
        inputText = test1[selectOp-1]
        splitData = inputText.split()
        symbols = ["+","-","*","/","%"]
        for item in symbols:
            if splitData[0][3] == item:
                tempval = "\ntemp=" + splitData[0][2] + splitData[0][3] + splitData[0][4]
                sumVal = splitData[0][0] + "=temp"
        print(tempval)
        print(sumVal)

    elif caseSelect == 2:
        selectOp = int(input("1.a+b-c\n2.a-b+c\n3.a-b-c\n4.a+b+c\n5.a+b%c\nenter option number: "))
        test1 = ["a+b-c","a-b+c","a-b-c","a+b+c","a+b%c"]
        # inputText = input("Enter Case:  ")
        inputText = test1[selectOp-1]
        splitData = inputText.split()
        symbols = ["+","-","*","/","%"]
        # for i in range(len(symbols)):
        #     print(splitData[0][i])
        for item in symbols:
            if splitData[0][3] == item:
                tempval = "\ntemp=" + splitData[0][0] + splitData[0][1] + splitData[0][2]
                sumVal = "temp1=" + "temp" + splitData[0][3] + splitData[0][4]
        print(tempval)
        print(sumVal)

    elif caseSelect == 3:
        selectOp = int(input("1.a<=c\n2.a>=c\n3.a==c\nenter option number: "))
        test1 = ["a<=c","a>=c","a==c"]
        # inputText = input("Enter Case:  ")
        inputText = test1[selectOp-1]
        splitData = inputText.split()
        symbols = ["<",">","="]
        adderss = 100
        # for i in range(4):
        #     print(splitData[0][i])

        # for item in symbols:
        #     if splitData[0][1] == item:
        tempval  = "\n\n"+str(adderss)+"   if   "+splitData[0] + "  goto  " + str((adderss+3))
        tempval2 = "\n\t"+str((adderss+1))+" :  T:=0"
        tempval3 = "\n\t"+str((adderss+2))+"  goto  "+str((adderss+4))
        tempval4 = "\n\t"+str((adderss+3))+" :  T:=1"
        
        # sumVal = "temp=" + "temp" + splitData[0][3] + splitData[0][4]
        print(tempval)
        print(tempval2)
        print(tempval3)
        print(tempval4)

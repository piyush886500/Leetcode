rows = 5

def Right_half_pyramid(rows):

    for i in range(rows):
        for j in range(i+1):
            print("*",end="")
        print("")


    for i in range(rows):
        for j in range(i+1):
            print(f"{j+1}",end="")
        print("")

    for i in range(rows):
        for j in range(i+1):
            print(f"{chr(65+j)}",end="")
        print("")



def Left_half_pyramid(rows):

    for i in range(rows):
        for j in range(rows-i-1):
                print(" ",end="")
        for k in range(i+1):
            print("*",end="")
        print("")


    for i in range(rows):
        for j in range(rows-i-1):
                print(" ",end="")
        for k in range(i+1):
            print(f"{k+1}",end="")
        print("")


    for i in range(rows):
        for j in range(rows-i-1):
                print(" ",end="")
        for k in range(i+1):
            print(f"{chr(65+k)}",end="")
        print("")


def Full_pyramid(rows):

    for i in range(rows):
        for j in range(rows-i-1):
                print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print("")


    for i in range(rows):
        for j in range(rows-i-1):
                print(" ",end="")
        for k in range(2*i+1):
            print(f"{k+1}",end="")
        print("")


    for i in range(rows):
        for j in range(rows-i-1):
                print(" ",end="")
        for k in range(2*i+1):
            print(f"{chr(65+k)}",end="")
        print("")



def Inverted_Right_half_pyramid(rows):

    for i in range(rows):
        for j in range(rows-i):
            print("*",end="")
        print("")


    for i in range(rows):
        for j in range(rows-i):
            print(f"{j+1}",end="")
        print("")

    for i in range(rows):
        for j in range(rows-i):
            print(f"{chr(65+j)}",end="")
        print("")


def Inverted_Left_half_pyramid(rows):

    for i in range(rows):
        for j in range(i):
             print(" ",end="")
        for k in range(rows-i):
            print("*",end="")
        print("")


    for i in range(rows):
        for j in range(i):
             print(" ",end="")
        for k in range(rows-i):
            print(f"{k+1}",end="")
        print("")

    for i in range(rows):
        for j in range(i):
             print(" ",end="")
        for k in range(rows-i):
            print(f"{chr(k+65)}",end="")
        print("")


def Inverted_Full_pyramid(rows):

    for i in range(rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print("*",end="")
        print("")
    for i in range(rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print(f"{k+1}",end="")
        print("")


    for i in range(rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print(f"{chr(k+65)}",end="")
        print("")
    

def Rohmbus(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(rows):
            print("*",end="")
        print("")
    
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(rows):
            print(f"{k+1}",end="")
        print("")

    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(rows):
            print(f"{chr(k+65)}",end="")
        print("")

def Diamond(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print("")
    for i in range(1,rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print("*",end="")
        print("")


    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print(f"{k+1}",end="")
        print("")
    for i in range(1,rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print(f"{k+1}",end="")
        print("")

    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print(f"{chr(k+65)}",end="")
        print("")
    for i in range(1,rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print(f"{chr(k+65)}",end="")
        print("")


def Hourglass(rows):
    for i in range(rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print("*",end="")
        print("")
    for i in range(1,rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print("")


    for i in range(rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print(f"{k+1}",end="")
        print("")
    for i in range(1,rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print(f"{k+1}",end="")
        print("")


    for i in range(rows):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(rows-i)-1):
            print(f"{chr(k+65)}",end="")
        print("")
    for i in range(1,rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print(f"{chr(k+65)}",end="")
        print("")






def Hollow_pyramid(rows):
    for i in range(rows):
        for j in range(rows):
            if i > 0 and i < rows-1 and j > 0 and j < rows-1:
                print(" ",end="")
            else:
                print("*",end="")
        print()

    for i in range(rows):
        for j in range(rows):
            if i > 0 and i < rows-1 and j > 0 and j < rows-1:
                print(" ",end="")
            else:
                print(f"{j+1}",end="")
        print()
    

    for i in range(rows):
        for j in range(rows):
            if i > 0 and i < rows-1 and j > 0 and j < rows-1:
                print(" ",end="")
            else:
                print(f"{chr(j+65)}",end="")
        print()


Hollow_pyramid(rows)
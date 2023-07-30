from fractions import Fraction


def constructA(length):
    A = [[0 for r in range(length)] for c in range(length)]
    for x in range(length):
        A[x][x] = Fraction(1, (x + 1))
    return A


def calculateIntegral(A, inputVector):
    outputVector = []
    for x in range(len(inputVector)):
        sum = 0
        for j in range(len(inputVector)):
            sum += A[x][j] * inputVector[j]
        outputVector.append(sum)
    return outputVector


def stringSanitize(string):
    cleanString = f""
    termsArray = string.rstrip(" ").split(" ")
    for x in range(len(termsArray)):
        singular = False
        head, sep, tail = termsArray[x].partition("x")
        if Fraction(head) == 1 or Fraction(head) == -1:
            singular = True
        if x == 0 and Fraction(head) != 0:
            cleanString += f"{head} "
        elif x == 1:
            if Fraction(head) > 0:
                if singular:
                    cleanString += f"+ {sep} "
                else:
                    cleanString += f"+ {head}{sep} "

            elif Fraction(head) < 0:
                if singular:
                    cleanString += f"- {sep} "
                else:
                    cleanString += f"- {abs(Fraction(head))}{sep} "
        else:
            if Fraction(head) > 0:
                if singular:
                    cleanString += f"+ {sep}{tail} "
                else:
                    cleanString += f"+ {head}{sep}{tail} "
            elif Fraction(head) < 0:
                if singular:
                    cleanString += f"- {sep}{tail} "
                else:
                    cleanString += f"- {abs(Fraction(head))}{sep}{tail} "
    return cleanString.rstrip(" ").lstrip("+ ")

def printConfirm(inputVector):
    print("Is this your polynomial?")
    polynomial = ""
    for x in range(len(inputVector)):
        polynomial += f"{inputVector[x]}x^{x} "
    print(stringSanitize(polynomial))


def printIntegral(output):
    print("Your integral is: ")
    integral = f"0x^0 "
    for x in range(len(output)):
        integral += f"{output[x]}x^{x+1} "

    print(f"{stringSanitize(integral)} + C")

def main():
    invalid = True;
    userString = input("Enter the coefficients of the polynomial you would like to integrate, separated by spaces. Put 0 for any terms that don't exist: ")
    listOfTerms = userString.split(" ")

    while invalid:
        try:
            inputVector = [Fraction(x) for x in listOfTerms]
            printConfirm(inputVector)
            matrix = constructA(len(inputVector))
            integral = calculateIntegral(matrix, inputVector)
            printIntegral(integral)
            invalid = False
        except:
            print("Invalid input")
            userString = input("Enter the coefficients of the polynomial you would like to integrate, separated by spaces. Put 0 for any terms that don't exist: ")
            listOfTerms = userString.split(" ")




if __name__ == "__main__":
    main()

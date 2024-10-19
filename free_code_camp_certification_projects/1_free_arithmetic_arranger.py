def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arranger = []

    for string in problems:
        arranger.append(string.split(" "))

    # Errorhandling
    for i in arranger:
        for j in i:
            if j.isnumeric() == True or j == "+" or j == "-":
                if len(j) > 4:
                    return "Error: Numbers cannot be more than four digits."
            elif j == "/" or j == "*":
                return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers must only contain digits."
            
    # ergebnis berechnen

    ergebnis = 0

    for index, i in enumerate(arranger):
        if i[1] == "+":
            ergebnis = int(i[0]) + int(i[2])
        else:
            ergebnis = int(i[0]) - int(i[2])
        arranger[index].append("-")
        arranger[index].append(str(ergebnis))

    # formatting

    for index, i in enumerate(arranger):

        if len(arranger[index][0]) >= len(arranger[index][2]):
            arranger[index][2] = (len(arranger[index][0]) - len(arranger[index][2])) * " " + arranger[index][2]
            arranger[index][3] = (2 + len(arranger[index][0])) * "-"
        else:
            arranger[index][0] = (len(arranger[index][2]) - len(arranger[index][0])) * " " + arranger[index][0]
            arranger[index][3] = (2 + len(arranger[index][2])) * "-"
        
        if len(arranger[index][4]) > len(arranger[index][0]) or len(arranger[index][4]) > len(arranger[index][2]):
            arranger[index][4] = " " + arranger[index][4]  
        else:
            arranger[index][4] = "  " + arranger[index][4]
    
        arranger[index][0] = "  " + arranger[index][0]
        arranger[index][2] = arranger[index][1] + " " + arranger[index][2]

    arranger_string = ""

    for i in range(len(problems)-1):
        arranger_string += arranger[i][0] + "    " 
    arranger_string += arranger[len(problems)-1][0] + "\n"
    for i in range(len(problems)-1):
        arranger_string += arranger[i][2] + "    "
    arranger_string += arranger[len(problems)-1][2] + "\n"
    for i in range(len(problems)-1):
        arranger_string += arranger[i][3] + "    "
    arranger_string += arranger[len(problems)-1][3]
    if show_answers == True:
        arranger_string += "\n"
        for i in range(len(problems)-1):
            arranger_string += arranger[i][4] + "    "
        arranger_string += arranger[len(problems)-1][4]
    return arranger_string

print(repr(f'{arithmetic_arranger(["3 + 855", "988 + 40"], True)}'))

# expected output
print(repr('    3      988\n+ 855    +  40\n-----    -----\n  858     1028')) 

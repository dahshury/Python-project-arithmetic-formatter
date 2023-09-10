def arithmetic_arranger(problems, solve=False):
    """
    ### For example

    Function Call:
    ```py
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    ```

    Output:
    ```
       32      3801      45      123
    + 698    -    2    + 43    +  49
    -----    ------    ----    -----
    """

    operands = {}
    line_creator = []
    divider = ""
    solutions = []
    supported_operators = ["+","-"]
    max_vertical_length = 0
    max_hz_length = {}

    for i, operation in enumerate(problems):
        
        operands[i] = [num.strip() for operand in operation.split("+") for num in operand.split("-")]

        if (len(operands)/2) >5:
            return "Error: Too many problems."
        
        if len(operands[i]) > max_vertical_length:
            max_vertical_length = len(operands[i])
            
        for operand in operands[i]:
            
            if "*" in operand or "/" in operand:
                return "Error: Operator must be '+' or '-'."
            
            if len(operand)> 4:
                return "Error: Numbers cannot be more than four digits."
            
            if i not in max_hz_length or len(operand) > max_hz_length[i]:
                max_hz_length[i] = len(operand)
                
            for character in operand:
                
                if not character.isdigit():
                    return "Error: Numbers must only contain digits."

            
        operands[f"{i} operators"] = [character for character in operation if character in supported_operators]

        
        
    for i in range(max_vertical_length):
        for j in range(len(problems)):
            if i==0:
                if j == 0:
                    line_creator.append(" " * (2 + max_hz_length[j] - len(operands[j][i])) + operands[j][i])
                    
                else:
                    line_creator.append(" " * 4 + (" " * (2 + max_hz_length[j] - len(operands[j][i])) + operands[j][i]))

            else:
                
                try:
                    
                    if j == 0:
                        line_creator.append((operands[f"{j} operators"][i-1] + " " * (1 + max_hz_length[j] - len(operands[j][i])) + operands[j][i]))
                         
                    else:
                        try:
                            line_creator.append(" " * 4 + operands[f"{j} operators"][i-1] + (" " * (1 + max_hz_length[j] - len(operands[j][i])) + operands[j][i]))
                        except:
                            line_creator.append(" " * 9)
                except:
                    
                    line_creator.append(" " * 4)
            
        line_creator.append("\n")
        
    top = ""
    
    for line in line_creator:
        top += line
    
    for i, value in enumerate(max_hz_length.values()):
        
        if i==0:
            divider += "-" * (value+2)
            
        else:
            divider += (" " * 4) + ("-" * (value+2))
        
    
    
    bottom = "\n"
    
    if solve==True:
        for i, _ in enumerate(problems):

            for j, operator in  enumerate(operands[f"{i} operators"]):
                
                if operator == "+":
                    solutions.append(float(operands[i][j]) + float(operands[i][j+1]))
                    
                else:
                    solutions.append(float(operands[i][j]) - float(operands[i][j+1]))
    
        
        
        for i, solution in enumerate(solutions):
            if i==0:
                bottom += " " * (max_hz_length[i]+2-len(str(int(solution)))) + str(int(solution))
                
            else:
                bottom += (" " * 4) + " " * (max_hz_length[i]+2-len(str(int(solution)))) + str(int(solution))
            
        return (top+divider+bottom)
    
    return (top+divider)
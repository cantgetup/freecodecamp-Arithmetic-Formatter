def arithmetic_arranger(questions, show_answers = False):
    
    # get elements
    n1s = []
    n2s = []
    ops = []
    
    for q in questions:
        n1s.append(q.split()[0])
        n2s.append(q.split()[2])
        ops.append(q.split()[1])
    
    # CHECK ERROR
    # too many problems?
    if len(questions) > 5:
        return 'Error: Too many problems.'

    
    # + - only?
    for op in ops:
        if op == '+' or op == '-':
            continue
        else:
            return "Error: Operator must be '+' or '-'."
        
        
    # digit only?
    for n1 in n1s:
        if n1.isdigit():
            continue
        else:
            return 'Error: Numbers must only contain digits.'
        
    for n2 in n2s:
        if n2.isdigit():
            continue
        else:
            return 'Error: Numbers must only contain digits.'
    
    # max 4 digit?
    for n1 in n1s:
        if len(n1) < 5:
            continue
        else:
            return 'Error: Numbers cannot be more than four digits.' 
        
    for n2 in n2s:
        if len(n2) < 5:
            continue
        else:
            return 'Error: Numbers cannot be more than four digits.' 
        
    
    #
    total_len = [max(len(n1),len(n2)) + 2 for n1, n2 in zip(n1s, n2s)]
    
    
    # answers
    answers = []
    for n1,n2,op in zip(n1s,n2s,ops):
        temp = int(n1) + int(n2) if op == '+' else int(n1) - int(n2)
        answers.append(str(temp))
      
    
    # create line_1
    line_1 = ''
    for n1,total in zip(n1s,total_len):
        line_1 = line_1 + n1.rjust(total) + '    '
                
        
    # create line_2       
    line_2 = ''
    for n2,op,total in zip(n2s,ops,total_len):
        line_2 = line_2 + op + ' ' + n2.rjust(total-2) + '    '
     
    
    # create line_3
    line_3 = ''
    for total in total_len:
        line_3 = line_3 + '-' * total + '    '
        
    
    # create line_4, ans
    line_4 = ''
    for ans, total in zip(answers,total_len):
        line_4 = line_4 + ans.rjust(total) + '    '
        

    # output
    if show_answers == True:
        return line_1.rstrip() + '\n' + line_2.rstrip() + '\n' + line_3.rstrip() + '\n' + line_4.rstrip()
    else:
        return line_1.rstrip() + '\n' + line_2.rstrip() + '\n' + line_3.rstrip()
   

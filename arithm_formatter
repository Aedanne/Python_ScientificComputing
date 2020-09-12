def arithmetic_arranger(problems, show_ans=False):
  arranged_problems = ''
  error_msg = ''
  first_row = ''
  second_row = ''
  dash_row = ''
  answer_row = ''
  counter = 0

  if len(problems) > 5:
    error_msg = 'Error: Too many problems.'
    return error_msg


  for problem in problems:

    part_first_row = ''
    part_second_row = ''
    part_dash_row = ''
    part_ans_row = ''
    pad_len = 4
    tot_len = 0

    if counter == 0:
      pad_len = 0

    #split the operands and operator using the space char
    opers = problem.split()

    try:
      oper1 = int(opers[0])
      oper2 = int(opers[2])
      if (oper1 > 9999 or oper2 > 9999):
        error_msg = 'Error: Numbers cannot be more than four digits.'
        return error_msg

      answer = 0
      operand = opers[1]
      if operand == '+':
        answer = oper1 + oper2
      elif operand == '-':
        answer = oper1 - oper2
      else:
        error_msg = "Error: Operator must be '+' or '-'."
        return error_msg

      if (oper1 > 999 or oper2 > 999):
        tot_len += 6   
        part_dash_row = '------'     
      elif (oper1 > 99 or oper2 > 99):
        tot_len += 5
        part_dash_row = '-----'   
      elif (oper1 > 9 or oper2 > 9):
        tot_len += 4
        part_dash_row = '----'   
      else:
        tot_len += 3
        part_dash_row = '---'   

      #construct part output
      part_dash_row = ''.rjust(pad_len) + part_dash_row.rjust(tot_len)
      part_first_row = ''.rjust(pad_len) + opers[0].rjust(tot_len)
      part_ans_row = ''.rjust(pad_len) + str(answer).rjust(tot_len)
      part_second_row = ''.rjust(pad_len) + (operand + ' ') + opers[2].rjust(tot_len-2) 

      #append to main rows
      first_row += part_first_row
      second_row += part_second_row
      dash_row += part_dash_row
      answer_row += part_ans_row
      
    except:
      error_msg = 'Error: Numbers must only contain digits.'
      return error_msg
    
    counter += 1

  #construct final formatted output
  arranged_problems = first_row +'\n'+ second_row + '\n'+ dash_row

  if show_ans:
    arranged_problems += '\n'+answer_row


  return arranged_problems

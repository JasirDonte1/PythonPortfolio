'''

add/work on brackets logic [ ] ( )

comment code in derivitevOf()

fix the issue revolving arround queing up terms with negative coefficients - enqueue()

derivative of a constant = 0

'''


import re


#derivative calculator   d/dx
raw_number =  "-2x^2-3x-1"
operations_array = ['+','-','/','*']

term_queue = []
operations_queue = []
derivative_queue = []

#actual derivative = 4x+4 = (4x+3+1)

#evaluate if the term is a valid mathnatical term

#break up raw number in to individual terms
#keep terms in a queue and operation symbols in a queue

#create a function that returns the derivative of a single term.
#append returned values to the derivative queue

#while a term exists in the derivative queue, pop and stringTo an operation to converted number

#METHOD: ISVALIDTERM()
def isValidTerm(raw_num): #returns true if the passed string is a valid trig term

    if(raw_num[0] in operations_queue):term=term[1:]

    check_one = False

    #if there is no (+,-,/,*) symbol in the string return False
    for operation in operations_array:
        if operation in raw_num:
            check_one = True    #terms exist

            
    #if back to back symbols are found return False
    if check_one == True:
        previous_term = ''
        #returns false if there are back to back characters that are operations
        for char in raw_num:
            if char in operations_array:
                if previous_term in operations_array:
                    return False
            previous_term = char

    else:
        #terms does not exist
        #if there exists a valid single term
        #for each character in the term
        #if the char is a letter in alphabet a number or '^' ... continue
        #else return false

        for char in raw_num:
            if char.isalpha():
                pass
            elif char.isnumeric():
                pass
            elif char == '^':
                pass
            else:    #if there is any character that is not a letter or number or ^, like $,false is returned 
                return False
            
    return True


#METHOD: ENQUEUE  
def enqueue(raw_num):
    
    op_sub_array =[]
    
    for x in raw_num: 
        if x in operations_array: 
            op_sub_array.append(x)
            
    q = re.split(r"\+|\-|\*|\\", raw_num)

    if q[0] == '':
        q = q[1:]
        q[0] = '-'+q[0]
        
        op_sub_array = op_sub_array[1:]

    count = 1

    for x in op_sub_array:
        q[count] = op_sub_array[count-1]+q[count]
        count += 1
        
    return q



#METHOD: DERIVATIVE_OF
def derivativeOf(term):   #function returns the derivative of a single term as a string
    derivative = 0
    coefficient = 0
    power = 0


    if '^' in term: #if there is an exponent involved
        
        if(term[0] == 'x'):
            expression = term.split('^')
            derivative = expression[1]
        
        elif(term[0].isnumeric()):
            expression = term.split('^')
            
            x_split = expression[0].split('x')
            power = int(expression[1])
            coefficient = int(x_split[0])
            coefficient = coefficient*power
            
            power = power - 1 

            if(power > 1):
                derivative = str(coefficient) + 'x^' + str(power)
            elif(power == 1):
                derivative = str(coefficient) + 'x'
            elif(power == 0):
                derivative = str(coefficient)
            elif power < 0:
                derivative = str(coefficient) + 'x^' + str(power)
            
        elif(term[0] == '-'):

            exp = ['-']
            term = term[1:]  #x^7


            expression = term.split('^')  #[x,7]
            power = int(expression[1])

          

            if (expression[0] == 'x'):  #-x

                if power > 1:
                    coefficient = power*-1
                    power = power-1
                    derivative = str(coefficient) + 'x^'+ str(power)
                elif power == 1:
                    derivative = '-x'
                elif power == 0:
                    derivative = '-1'
                elif power < 0:
                    coefficient = -1*power
                    power = power - 1
                    print(power)
                    derivative = str(coefficient) + 'x^' + str(power)
                

            else:
                x_split = expression[0].split('x')

                coefficient = int(x_split[0])
                coefficient = coefficient*power
                
                if(power > 1):
                    power = power-1
                    derivative = '-' + str(coefficient) + 'x^' + str(power)
                elif(power == 1):
                    derivative = '-' + str(coefficient) + 'x'
                elif(power == 0):
                    derivative = '-' + str(coefficient)
                elif power < 0:
                    power = power -1 
                    derivative = str(coefficient) + 'x^' + str(power)
                    derivative = derivative[1:]
                    
        
    else:    #if not exponent is involved
        print('ddd',term)
        
        if(term == 'x'):
            derivative = '1'
        elif(term == '-x'):
            derivative = '-1'
        elif(int(term)):
            print('rrrr')
        else:
            expression = term.split('x')
            derivative = expression[0]


        print('end of if statement')
        
    return derivative

def toString(expressions): #array

    w = ''
    p = []

    for x in expressions:
        if x[0] == '-':
            p.append(x)
            pass
        elif x[0].isnumeric():
            temp = '+' + x
            p.append(temp)
    
    for x in p:
        w += x
    if(w[0] == '+'):
        w = w[1:]
    return w


###### FUNCTIONS DEFINED ABOVE ########

if(isValidTerm(raw_number)):     #if the entry/input is valid
    term_queue = enqueue(raw_number)
    print('term queue ', term_queue) #= ['-2x^-2','-3x','3']      #sample terms -2x^2-3x+3

    #TAKE THE DERIVATIVE OF EACH TERM#
    expression = []
    
    for t in term_queue:
        expression.append(derivativeOf(t))

        
    print('exp:',expression)

    #METHOD TO STRING TOGETHER TERM_QUEUE#

    print(toString(expression))

    
    
else:
    #raw number is not a valid number
    print('Enter a valid Number')



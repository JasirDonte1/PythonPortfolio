'''

finished isValidTerm() method


'''
import re


#derivative calculator
raw_number =  "2x^2+3x-4"
operations_array = ['+','-','/','*','^']

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


def isValidTerm(raw_num): #returns true if the passed string is a valid trig term
    check_one = False

    #if there is no (+,-,/,*,^) symbol in the string return False

    for operation in operations_array:
        if operation in raw_num:
            check_one = True 
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
        return False   #returns false if check_one does not pass the check

    return True

    
def enqueue (raw_num):    #raw num passes the string of user input and puts terms in a queue
    queue = re.split('+|-|*|/', raw_num)

    return queue


def derivativeOf(term):   #function returns the derivative of a single term as a string
    derivative = 0

    return derivative


###### FUNCTIONS DEFINED ABOVE ########

try:
    if(isValidTerm(raw_number)):
        #print(enqueue(raw_number))
        pass    #dummy statement 
    
    else:
        #raw number is not a valid number
        print('Enter a valid Number')
        

    
except:
    print('something went wrong')

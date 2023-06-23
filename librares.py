# fibannacci series
def fibonnacci(n:int):
    if n == 0:
        print("0")
        return
    elif n == 1:
        print(f"0 , 1")
    fib = [0,1]                     # initialize the fibonacci series 
    print(fib[-2],end=',')
    print(fib[-1],end=',')
    while not len(fib)==n:          # Repeat till the value specified for n
        sum = fib[-2]+fib[-1]       # get the sum of last 2 values
        fib.append(sum)             # Append the new element (sum) to original fibonacci series
        print(sum,end=',')

# Case convesrion and count number of upper and lower cases
def case_conversion(string:str):
    if len(string) == 0:
        print("String length is 0")    
        return
    count_upper = 0
    count_lower = 0
    for i in range(len(string)):        
        if not string[i].isalpha() or string[i].isdigit() or string[i] == ' ':          # Validate for special charecters
            continue
        elif not string[i].isupper():                                                   # Validate for Uppercase
            print(string[i], end='')
            count_lower+=1                                                              # Raise the lowercase count by 1  
            continue
        print(string[i].lower(),end='')
        count_upper+=1                                                                  # Raise the uppercase count by 1
    print('\n')
    print(f"number of uppercases are {count_upper}")
    print(f"number of lowercases are {count_lower}")    

if __name__ == "__main__":
    fibonnacci(8)
    case_conversion("QwErTy12#rty")

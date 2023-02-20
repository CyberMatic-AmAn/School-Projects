

from time import sleep
import random
import string
import math

print(" ")
print(" WAIT A MOMENT LOADING PROGRAM..........")
sleep(3)
print(" ")


# ==================== Data stores  =============================

compliments = [
        "You are beautiful!",
        "You are smart!",
        "You are funny!",
        "You are amazing!",
        "You are kind!",
        "You are talented!",
        "You are creative!",
        "You are a great friend!",
        "You are a great listener!",
        "You have a great sense of humor!"
]

chats = {

"patterns":["hello", "hii", "hey" ,"yupp","yo bro","hai"],
"responses" : ["Hello Sir :)",
                "Hey, I was really waiting for your presence.",
                "Hey, I was literally waiting for your presence.", 
                "Hey, I was waiting for your presence.", 
                "Hey, I was waiting for you.", 
                "Hello, I was waiting for you.", 
                "Hello Sir, Nice meeting you again.", 
                "Hello, Nice to meet you.", 
                "Hello", 
                "Hey What's up sir." ]}

wishes = {

        "patterns":["bye", "good bye", "see you later", "sleep", "exit"], 
            "responses":["Bye.", 
            "Are you sure.", 
            "Ok Sir, Bye" 
            ]
}

question = {

"que" : ["how are you","what are you doing","how are you doing","how is the day","whats going on"],
"ans" : ["I am good" ,
"what about you",
"I am fine",
"I am okay",
"I've been better",
"I'm fine, thanks. How about you?",
"Good, thanks. And you?",
"I'm good. And yourself?,"
"Not bad. How are you?",
"Fine, and you?",
"I'm doing well, and you?",
"Good, how about you?"]

}

query = {"dice1": [1,2,3,4,5,6],
        "dice2": [1,2,3,4,5,6],
        "hands" : ["ROCK" , "PAPER", "SCISSOR"],
        "Query" : ["YES YOU DEFINITY HAVE TO DO IT", "NO YOU DONT HAVE TO DO IT"]         
        }

print( """

|<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                    |    WELCOME TO MAIN-FRAME  MENU FOR CLASS XI  PRCTICAL PARTS     |

                    |   THIS MENU IS MADE FOR ALL PROGRAM SUGGESTIONS IN CALSS XI CS  |

                    |     FOLLOW THE FOLLOWING INSTRUCTIONS TO CONTINUE WITH PATH     |

                    |           TYPE THE SUGGESTIONS TO CONTINUE WITH                 |

|<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|                    

                        1 TO 7 ARE SOME BASIC FUNCTIONS 

                        8 TO REST ARE GEOMETRICAL AND COOL STUFFS

        1 FOR Determine whether a number is a perfect number, an armstrong number or a palindrome

        2 FOR check if the number is a prime or composite number.

        3 FOR Compute the greatest common divisor and least common multiple of two integers.

        4 FOR Count and display the number of vowels, consonants, uppercase, lowercase characters in string.

        5 FOR Find the largest/smallest number in a list/tuple.

        6 FOR Input a list/tuple of elements, search for a given element in the list/tuple.

        7 FOR Generating a hard to guess password .

        8 FOR Activating advance menu with cool stuff . 

        9 FOR Activating Geometrical Operations .

        10 FOR Activating pattern printer with cool patterns .

        11 FOR ACTIVATING SIMPLE AND COMPOUND INTEREST CALCULATOR . 

        12 FOR CALCULATING ROOTS OF GIVEN EQUATION .

        13 FOR ACTIVATING CHATBOT AND COMPLIMENT GIVER & and type bye for exiting . 

        14 FOR CALCULATING ELECTRICITY BAILL AMOUNT .

        15 FOR ACTIVATING RAPID GAMES . 

|<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|


""")

# ====================== Functions for program 1 ===========================

def is_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

def is_armstrong(num):
    num = str(num)
    n = len(num)
    sum = 0
    
    for i in num:
        sum += int(i)**n
    
    if sum == int(num):
        return True
    else:
        return False

def palindrome(n):
  
  n = str(n)
  return n == n[::-1]

# ====================== Functions for program 2 ===========================

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_composite(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

# ====================== Functions for program 3 ===========================

def lcm(a, b):
    
    gcd = 1
    i = 2
    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1

    return (a * b) // gcd

def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

# ====================== Functions for program 4 ===========================

def count_characters(string):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    vowel_count = 0
    consonant_count = 0
    upper_count = 0
    lower_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char in uppercase:
            upper_count += 1
        elif char in lowercase:
            lower_count += 1

    print(" ")
    print("Numbers of Vowels are :", vowel_count)
    print(" ")
    print("Number of Consonants are :", consonant_count)
    print(" ")
    print("Number of Uppercase characters are :", upper_count)
    print(" ")
    print("number of Lowercase characters are :", lower_count)
    print(" ")

# ====================== Functions for program 7 ===========================

def generate_password(length):
        
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        symbols = string.punctuation

        password = ''.join(random.choice(uppercase + lowercase + digits + symbols) for i in range(length))
        return password

# ====================== Functions for advance program 4 ===========================

def sum_list(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total += num
    return total

# ====================== Functions for SI AND CI calculator ===========================

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * (1 + rate/100) ** time

# ====================== Functions for program 12 ===========================

def quadratic_roots(a, b, c):
    if a == 0:
        print("This is not a quadratic equation")
        
    else:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            print("The equation has no real roots")
            print(" ")
            print("Roots of the equation are complex numbers")
        elif discriminant == 0:
            x = -b / (2 * a)
            return x
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return x1, x2

def linear_equation_roots(a, b):
    if a == 0:
        print("This is not a linear equation.")
    else:
        x = -b / a
        print("The root of the linear equation is:", x)

# ====================== Functions for program 12 ===========================

def pattern1(string):
    for i in range(len(string)):
        for j in range(i+1):
            print(string[j], end="")
        print()

def pattern2(string):
    for i in range(len(string)):
        for j in range(len(string)-i):
            print(string[j], end="")
        print()

def pattern3(string):
    for i in range(len(string)):
        for j in range(len(string)-i):
            print(" ", end="")
        for j in range(i+1):
            print(string[j], end="")
        print()

def pattern4(string):
    for i in range(len(string)):
        for j in range(i):
            print(" ", end="")
        for j in range(len(string)-i):
            print(string[j], end="")
        print()

def print_tree(symbol, height):
    for i in range(1, height+1):
        print(' '*(height-i) + symbol*(2*i-1))
    print(' '*(height-1) + symbol)
    print(' '*(height-2) + symbol*3)

def print_car_pattern(symbol):
    # front
    print(" " * 6 + symbol * 5)
    print(" " * 5 + symbol * 7)
    print(" " * 4 + symbol * 9)
    print(" " * 3 + symbol * 11)
    print(" " * 2 + symbol * 13)
    print(" " + symbol * 15)
    # middle
    print(symbol * 16)
    print(symbol * 16)
    # back
    print(symbol * 16)
    print(symbol * 16)
    print(" " + symbol * 15)
    print(" " * 2 + symbol * 13)
    print(" " * 3 + symbol * 11)
    print(" " * 4 + symbol * 9)
    print(" " * 5 + symbol * 7)
    print(" " * 6 + symbol * 5)

def print_house_pattern(symbol):
    print('    ' + symbol)
    print('   ' + symbol + symbol + symbol)
    print('  ' + symbol + '   ' + symbol)
    print(' ' + symbol + symbol + symbol + symbol + symbol + symbol)
    print(symbol + '     ' + symbol)
    print(symbol + '     ' + symbol)
    print(symbol + '     ' + symbol)

def flag_pattern(symbol):
    for i in range(7):
        if i < 3:
            print(symbol*(2*i+1))
        elif i == 3:
            print(symbol*(2*i+1))
        else:
            print(symbol*(13-2*i))

# ====================== Functions for program  ===========================

# ===========================================================================

# To handle the user choice as input
def user_choice_handler(choice):
        if choice == "1":
                print(" ")
                number = int(input("Enter a number: "))

                if is_perfect_number(number):
                        print(" ")
                        print(f">>>>>>>>>>>>>>>>>>>> {number} is a perfect number.")
                        print(" ")
                else:
                        print(" ")
                        print(f">>>>>>>>>>>>>>>>>>>> {number} is not a perfect number.")
                        print(" ")

                if is_armstrong(number):
                        print(f">>>>>>>>>>>>>>>>>>>> {number} is an Armstrong number.")
                        print(" ")
                else:
                        print(f">>>>>>>>>>>>>>>>>>>> {number} is not an Armstrong number.")
                        print(" ")

                if palindrome(number):
                        print(f">>>>>>>>>>>>>>>>>>>> {number} is a palindrome number.")
                        print(" ")

                else:
                        print(f">>>>>>>>>>>> {number} is not a palindrome number.")
                        print(" ")

        elif choice == "2":
                print(" ")
                num = int(input("Enter a number: "))
                if is_prime(num):
                        print(" ")
                        print(f">>>>>>>>>>>>>>>>>>>> {num} is a prime number.")
                        print(" ")
                else:
                        print(" ")
                        print(f">>>>>>>>>>>>>>>>>>>> {num} is not a prime number.")
                        print(" ")

                if is_composite(num):
                        print(f">>>>>>>>>>>>>>>>>>>> {num} is a composite number.")
                        print(" ")
                else:
                        print(f">>>>>>>>>>>>>>>>>>>> {num} is not a composite number.")
                        print(" ")

        elif choice == "3":
                a = int(input("Enter 1st number : "))
                b = int(input("Enter 2nd number : "))

                LCM = lcm(a,b)
                print(f">>>>>>>>>>>>>>>>>>>> LCM of the numbers is : {LCM}")
                print("And".center(50))
                print()

                HCF = hcf(a,b)
                print(f">>>>>>>>>>>>>>>>>>>> HCF of the numbers is : {HCF}")
                print(" ")

        elif choice == "4":
                input_string = input("Enter a string: ")
                count_characters(input_string)       

        elif choice == "5":
                print("""
                        In which sequence you want to find largest and smallest element

                                Type 1 for in List and 2 for in tuple """)

                ask = int(input("Enter your choice :  "))

                if ask == 1:
                        number = []
                        n = int(input("Enter number of elements in your list : "))
                        print(" ")
                        for i in range(0,n):
                                val = int(input("Enter the number : "))
                                number.append(val)
                        largest = max(number)
                        smallest = min(number)
                        print(" ")
                        print("Largest number:", largest)
                        print(" ")
                        print("Smallest number:", smallest)
                        print(" ")

                elif ask == 2:
                        numbers = []
                        print(" ")
                        n = int(input("Enter number of elements in your tuple : "))
                        for j in range(0,n):
                                val = int(input("Enter the number : "))
                                numbers.append(val)
                        tuple(numbers)

                        largest = max(numbers)
                        smallest = min(numbers)
                        print(" ")
                        print("Largest number:", largest)
                        print(" ")
                        print("Smallest number:", smallest)
                        print(" ")

                else:
                        print(" Please select among 1 or 2 ")
                        print(" ")

        elif choice == "6":
                print("""
                        In which sequence you want to find element

                           Type 1 for in List and 2 for in tuple """)

                ask = int(input("Enter your choice :  "))

                if ask == 1:
                        number = []
                        n = int(input("Enter number of elements in your list : "))
                        print(" ")
                        for i in range(0,n):
                                val = int(input("Enter the number : "))
                                number.append(val) 

                        print("The List is: ", number) 
                        print(" ")

                        x = int(input("Enter the element to search: ")) 
 
                        for i in range(len(number)): 
                                if number[i] == x: 
                                        print(" ")
                                        print(f"{x} is present at index {i}") 
                                        break
                        else: 
                                print(" ")
                                print(f"{x} is not present in the list")
                                print(" ")

                elif ask == 2:
                        number = []
                        n = int(input("Enter number of elements in your list : "))
                        print(" ")
                        for i in range(0,n):
                                val = int(input("Enter the number : "))
                                number.append(val)

                        t1 = tuple(number)
                        print("The tuple is: ", t1) 
                        print(" ")

                        x = int(input("Enter the element to search: ")) 
 
                        for i in range(len(t1)): 
                                if t1[i] == x: 
                                        print(" ")
                                        print(f">>>>>>>>>>>>>>>>>>>> {x} is present at index {i}") 
                                        break
                        else: 
                                print(" ")
                                print(f">>>>>>>>>>>>>>>>>>>> {x} is not present in the list")
                                print(" ")

        elif choice == "7":
                print(" ")
                length = int(input("Enter password length: "))
                print(" ")
                print("Generated password:", generate_password(length))
                print(" ")

        elif choice == "8":
                print("""

|<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                                                ADVANCED MENU 


                        1  FOR FINDING FACTORIAL OF A NUMBER

                        2 FOR FINDING SQUARE ROOT OF A NUMBER

                        3 FOR FINDING EXPONENTIAL VALUE OF A NUMBER

                        4 FOR FINDING SUM OF THE SERIES

                        5  FOR EXIT FROM ADVANCE MENU

|<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|               
                  
""")
                while True:
                        print(" ")
                        advance_choice = int(input("Enter your advance choice : "))
                        print(" ")

                        if advance_choice == 1:
                                number = int(input("Enter the number to find factorial : "))
                                print(" ")
                                print(f">>>>>>>>>>>>>>>> Factorial of the number is {math.factorial(number)}")
                                print(" ")

                        elif advance_choice == 2:
                                number = int(input("Enter the number to find square root : "))
                                print(" ")
                                print(f">>>>>>>>>>>>>>>> Square root of the number is {math.sqrt(number)}")
                                print(" ")

                        elif advance_choice == 3:
                                print(" ")
                                number = int(input("Enter the number : "))
                                print(" ")
                                exponent = int(input("Enter exponent power  : "))
                                print(" ")
                                print(f">>>>>>>> value of the number is {number**exponent}")

                        elif advance_choice == 4:
                                series = []
                                n = int(input("Enter number of elements in your series : "))
                                print(" ")
                                for i in range(0,n):
                                        val = int(input("Enter the number : "))
                                        series.append(val)

                                result = sum_list(series)
                                print("The sum of the numbers in the series is:", result)
                                print(" ")

                        elif advance_choice == 5:
                                print("Advance menu exited successfully !")
                                break

                        else:
                                print("No options specified in advance menu")

        elif choice == "9":
                print("""

|<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                                                GEOMETRICAL MENU 


                        1 FOR SPECIFICATIONS OF A TRIANGLE 

                        2 FOR SPECIFICATIONS OF A SQUARE

                        3 FOR SPECIFICATIONS OF A RECTANGLE

                        4 FOR SPECIFICATIONS OF A CIRCLE

                        5 FOR SPECIFICATIONS OF A CUBE

                        6 FOR SPECIFICATIONS OF A CUBOIDE

                        7 FOR SPECIFICATIONS OF A CYLINDER

                        8 FOR SPECIFICATIONS OF A CONE

                        9 FOR SPECIFICATIONS OF A SPHERE

                        10 FOR SPECIFICATIONS OF A HEMISPHERE

                        11 FOR EXIT FROM GEOMETRY MENU

|<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|               
                  
""")
                while True:
                        print(" ")
                        ASK =  int(input("Enter Geometry menu choice : " ))
                        print(" ")

                        if ASK == 1:
                                height = float(input("Enter Height : " ))
                                base = float(input("Enter Base lenght : " ))

                                area = 1/2 * base * height
                                print("Area of triangle is : ",area)

                        elif ASK == 2:
                                side = float(input("Enter Side lenght : " ))
                                area = side ** 2
                                perimeter = 4 * side

                                print(" ")
                                print("Area of square is : ",area)
                                print(" ")
                                print("Perimeter of square is : ",perimeter)
                                print(" ")

                        elif ASK == 3:
                                length = float(input("Enter Length of side : " ))
                                breadth = float(input("Enter Breadth of side : " ))
                                area = length * breadth
                                perimeter = 2* (length + breadth)

                                print(" ")
                                print("Area of rectangle is : ",area)
                                print(" ")
                                print("Perimeter of rectangle is : ",perimeter)
                                print(" ")

                        elif ASK == 4:
                                radius = float(input("Enter radius of circle : "))
                                area = (math.pi) * radius ** 2
                                perimeter =  2 * math.pi * radius

                                print(" ")
                                print("Area of circle is : ", area)
                                print(" ")
                                print("Perimeter of circle is : ", perimeter)
                                print(" ")

                        elif ASK == 5:
                                side = float(input("Enter Side of cube : "))
                                volume = side ** 3
                                lsa = 4 * (side**2)
                                tsa = 6 * (side**2)

                                print(" ")
                                print("Volume of cube is : ", volume)
                                print('')
                                print("Lateral surface area of cube is : ", lsa)
                                print(" ")
                                print("Total surface area of cube is : ",tsa)
                                print("")

                        elif ASK == 6:
                                length = float(input("Enter lenght of cuboid : "))
                                breadth = float(input("Enter breadth of cuboid : "))
                                height = float(input("Enter height of cuboid : "))

                                volume = length * breadth * height
                                lsa = 2*height*(length+breadth)
                                tsa = 2*(length*breadth + breadth*height + height*length)

                                print("Volume of cuboid is : ",volume)
                                print(" ")
                                print("Total surface area of cuboid is : ",tsa)
                                print(" ")
                                print(" lateral surface area of cuboid is : ",lsa)

                        elif ASK == 7:
                                radius = eval(input("Enter the radius of the cylinder : "))
                                height = eval(input("Enter the height of the cylinder : "))
                                lsa = 2 * math.pi * radius * height
                                tsa = 2 * math.pi * (radius + height)
                                volume = math.pi * radius ** 2 * height

                                print(" ")
                                print("Lateral surface area of cylinder is : ",lsa)
                                print(" ")
                                print("Total surface area of cylinder is : ",tsa)
                                print(" ")
                                print("Volume of cylinder is : ",volume)

                        elif ASK == 8:
                                radius = eval(input("Enter the radius of the cone : "))
                                height = eval(input("Enter the height of the cone : "))
                                sl_height = math.sqrt(radius**2 + height**2)
                                volume = 1/2 * math.pi * radius ** 2 *height
                                area = math.pi * radius * (sl_height + height)

                                print(" ")
                                print("Slant height of cone is : ",sl_height)
                                print(" ")
                                print("Volume of cone is : ",volume)
                                print(" ")
                                print("Surface area of cone is : ",area)
                                print(" ")

                        elif ASK == 9:
                                radius = eval(input("Enter radius of the sphere : "))
                                sufcae_are = 4 * (math.pi) * radius**2
                                volume = 4/3 * (math.pi) * radius**3

                                print(" ")
                                print("Surface area of the sphere :",sufcae_are)
                                print(" ")
                                print("volume of the sphere :",volume)
                                print(" ")

                        elif ASK == 10:
                                radius = eval(input("Enter radius of the hemisphere : "))
                                s_area = 3 * math.pi * radius**2
                                cs_area = 2 * math.pi * radius**2

                                print("")
                                print("Total Surface of the hemisphere :",s_area)
                                print(" ")
                                print("Curve surface area of the hemisphere :",cs_area)
                                print(" ")

                        elif ASK == 11:
                                print("Geometry menu exited successfully ! ")
                                break

                        else:
                                print("Please enter choice from geometry menu.")        

        elif choice == "10":
                print("""
                |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                                                                STEPS ARE DEFINED AS 

                                        (I) ENTER THE SYMBOL YOU WANT 
                                        (II) ENTER LENGHT OF THE PATTERN

                                                        OR

                                        TYPE 3 FOR USER DEFINED STRING PATTER 

                                        (III) ENTER EXIT TO EXIT PATTERN PRINTER

                |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|""")

                while True:
                        print(" ")
                        useer = str(input("Enter your symbol or Type Exit to exit pattern printer : "))
                        print(" ")

                        if useer == "Exit" or useer == "exit" or useer == "EXIT":
                                print("Pattern printer exited successfully !")
                                break

                        elif useer == "3":

                                string = input("Enter a string Should be greter than lenght of 5 and less than 20 : ")
                                

                                print("\nPattern 1:\n")
                                pattern1(string)

                                print("\nPattern 2:\n")
                                pattern2(string)

                                print("\nPattern 3:\n")
                                pattern3(string)

                                print("\nPattern 4:\n")
                                pattern4(string)

                        else:

                                n = int(input("Enter lenght of the pattern : "))
                                for k in range(0, n):
                                        for m in range(0, k + 1):
                                                print(useer, end=' ')
                                        print("\r")

                                print("\nPattern 5 X - MAS TREE :\n")
                                print_tree(useer, n)      

                                print("\nNew Pattern\n")
                                print_car_pattern(useer)

                                print("\nNew Pattern\n")
                                print_house_pattern(useer)

                                print("\nNew Pattern\n")
                                flag_pattern(useer)

        elif choice == "11":
                print("""
                
                |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                                                INTEREST CALCULATOR IS NOW TUNNED 

                |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
                
                """)

                while True:

                        print(" ")
                        p = eval(input("Enter the principal amount: "))
                        print(" ")
                        r = eval(input("Enter the rate of interest: "))
                        print(" ")
                        t = eval(input("Enter the time period (in years): "))
                        print(" ")

                        print("""
                        |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                                                                TYPE 1 FOR SIMPLE INTEREST

                                                                TYPE 2 FOR COMPOUND INTEREST

                                                            TYPE 3 FOR EXITING INTEREST CALCULATOR

                        |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
                        
                        """)

                        CAL_cse = int(input("Enter choice for calculation : "))
                        print(" ")

                        if CAL_cse == 1:

                                interest = simple_interest(p, r, t)

                                print("Simple Interest:", interest)

                        elif CAL_cse == 2:

                                print(" ")
                                result = compound_interest(p, r, t)
                                print(" ")
                                print("Compound interest: ", result)
                                print(" ")

                        elif CAL_cse == 3:
                                print("Interest calculator exited successfully !")
                                break

                        else:
                                print("Unknown Calculation interest")

        elif choice == "12":
                print(" ")
                print("""
                        |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                                                                ROOTS QUESTION HANDLER  

                                                        What type of equation problem you have :    

                                                        TYPE 1 FOR LINER EQUATION WITH 1 VARIABLE 

                                                        TYPE 2 FOR QUADRATIC EQUATION WITH 1 VARIABLE    

                                                        TYPE 3 FOR EXITING ROOTS QUESTION HANDLER                              

                        |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
                """)

                while True:
                        
                        
                        print(" ")
                        root_handler = eval(input("Enter choice of problem from above : "))
                        print(" ")

                        if root_handler == 1:
                                print(" ")
                                a = float(input("Enter the coefficient of x: "))
                                print(" ")
                                b = float(input("Enter the constant: "))
                                print(" ")
                                linear_equation_roots(a, b)


                        elif root_handler == 2:
                                print(" ")
                                print("Quadratic function : (a * x^2) + b*x + c")
                                print(" ")
                                ca = eval(input("Enter coefficient a : "))
                                cb = eval(input("Enter coefficient b : "))
                                cc = eval(input("Enter coefficient c : "))
                                print(" ")
                                print("Roots are : ",quadratic_roots(ca,cb,cc))

                        elif root_handler == 3:
                                print("Roots question handler exited successfully !")
                                break 

                        else:
                                print("Invalid selection detected Enter choice from above menu")

        elif choice == "13":

                while True:

                        HUman = str(input("Say something : "))
                
        
                        if HUman in wishes["patterns"]:
                                print(f"\nBot : {random.choice(wishes['responses'])}")
                                print(" ")
                                break

                        elif HUman in chats["patterns"]:
                                print(f"\nBot : {random.choice(chats['responses'])} ")
                                print(" ")

                        elif HUman in question["que"]:
                                print(f"\nBot : {random.choice(question['ans'])}")
                                print(" ")

                        else:
                                print("")
                                print(f"\nBot :{random.choice(compliments)}")
                                print(" ")

        elif choice == "14":
              print(" ")
              # Prompt the user to enter the number of units consumed
              units = eval(input("Enter the number of units consumed : "))

              if units <= 50:
                  rate = 0.50
              elif units <= 150:
                  rate = 0.75
              elif units <= 250:
                  rate = 1.20
              else:
                  rate = 1.50

              bill_amount = units * rate

              surcharge = bill_amount * 0.20  # 20% surcharge
              tax = bill_amount * 0.05        # 5% tax
              total_amount = bill_amount + surcharge + tax

              print(f"Total bill amount : {total_amount:.2f}")

        elif choice == "15":
              print(" ")
              print("""
              |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|

                                                        WELCOME TO RAPID GAMES 

                                                TYPE 1 FOR ACTIVATING ROCK PAPER SCISSORS 

                                                TYPE 2 FOR ROLLING DICES

                                                TYPE 3 FOR RANDOM ANSWER PICKER

                                                TYPE 4 FOR EXIT FROM RAPID GAMES

              |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
              """)
              while True:

                    print(" ")
                    quEry = int(input("Enter rapid games choice : "))
                    print(" ")
                    if quEry == 1:
                          rk = random.choice(query['hands'])
                          print("")
                          print("Welcome to rock paper scissors !")
                          print(" ")
                          print("LETS START THE GAME")
                          print(" ")
                          kj = input("HIt ENTER THE SAME TIME YOU SHOW YOURS")
                          print(" ")
                          print(f"\nBOT : {rk}")
                          
                                

                    elif quEry == 2:
                          ju = random.choice(query["dice1"])
                          ji = random.choice(query["dice2"])
                          print("")
                          print("Welcome to dice roler !")
                          print(" ")
                          print("LETS START THE GAME")
                          print(" ")
                          kj = input("HIt ENTER")
                          print(" ")
                          print(f"\nBOT : {ju} and {ji}")

                    elif quEry == 3:
                          print(" ")
                          print("WELCOME TO RANDOM ANSWER PICKER !")
                          print(" ")
                          print("LETS START THE GAME")
                          print(" ")
                          ki = input("Enter your query : ")
                          print("Before giving your answer let me tell you I will onle give answer as YES OR NO ")
                          print(" ")
                          print("DO you wish to continue")
                          jkk = input("HIT ENTER TO CONTINUE : ")
                          TT = random.choice(query["Query"])
                          print(f"\nBot : {TT} ")

                    elif quEry == 4:
                          print(" ")
                          print("RAPID GAMES EXITED SUCCESSFULY !")
                          print(" ")
                          break
                    
                    

                    else :
                          print(" ")
                          print("Plese enter choice from menu to continue ")
                          print(" ")

        else:
                print("Invalid choice")

while True:
        print(" ")
        kk = str(input("Please enter your choice from above :  "))        
        user_choice_handler(kk)        
        print(" ")


#import all the modules you need, below this line
from liste import lista

#write any functions you need, below this line
def valid_Score(x):
    if x<6:
        return f'Score {x} -> Low score!'
    elif x>=6 and x<=11:
        return f'Score {x} -> Moderate score!'
    elif x>=11:
        return f'Score {x} -> High score!'
    
def valid_Input(questions):
    while True:
        try:
            score = int(input(questions))
            if 0 <= score <= 7:
                return score
            else:
                print("Invalid input. Please enter a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def Sums(lista):
    b=[]
    for i in range(5):
        x=0
        y=0
        while x<3:
            y+=lista[i*3+x]
            x+=1
        b.append(y)
    return b

#use the main() function for your program, define all other functions above main
def main ():
    print('Welcome to your new Habit Tracker! To get started, please answer the following questions:')
    a=[]
    for j in range(len(lista)):
        x=0
        for i in range(len(lista[j]['text'])):
            a.append(valid_Input(lista[j]['text'][x]))
            x=x+1

    b=Sums(a)

    for i in range(5):
        print(f'{lista[i]['habit']}', valid_Score(b[i]))

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()

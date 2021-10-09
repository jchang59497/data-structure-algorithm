# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

def cigar_party(num, weekend):
    if weekend:
        return num >= 40:
    else: 
        return num >= 40 and num <= 60

print(cigar_party(10, True))
    
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

def date_fashion(you,date):
    if you >= 8 or date >= 8:
        return 2
    elif you <= 2 or date <= 2:
        return 0
    else:
        return 1
print(date_fashion(5,5))
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1


# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp,summer):
    if summer:
        return temp >= 60 and temp <= 100
    else: 
        return temp >= 60 and temp <= 90
print(squirrel_play(95, True))
# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def caught_speeding(speed, birthday):
    if birthday:
        if speed <= 65:
            return 0
        elif speed >= 66 and speed <= 85:
            return 1
        else: 
            return 2
    else:
        if speed <= 60:
            return 0
        elif speed >= 61 and speed <= 80:
            return 1
        else:
            return 2
print(caught_speeding(100, False))
# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0


# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

def love6(a,b):
    sum = abs(a + b)
    diff = abs(a-b)
    return a == 6 or b == 6 or sum == 6 or diff == 6
print(love6(1, 5))
# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True


# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day,vacation):
    if vacation:
        if day == 0 or day == 6:
            return 'off'
        else:
            return '10:00'
    else: 
        if day == 0 or day == 6:
            return '10:00'
        else:
            return '7:00'
print(alarm_clock(1, True))
# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

def make_bricks(small,big,goal):
    sum = small + big * 5
    return sum >= goal

print(make_bricks(5, 15, 150))
#make_bricks(3, 1, 8) → True
#make_bricks(3, 1, 9) → False
#make_bricks(3, 2, 10) → True



# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a,b,c):
    sum = 0
    if a != 13:
        sum += a
    else:
        return sum
    
    if b != 13:
        sum += b
    else:
        return sum
    
    if c != 13:
        sum += c
    else:
        return sum
    
    return sum

print(lucky_sum(1,13,3))       
              
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

import random 

def rock_paper_scissors(move):
    computerCode = random.randint(1,3)
    computer = ''
    
    if computerCode == 1:
        computer = 'rock'
    if computerCode == 2:
        computer = 'paper'
    if computerCode == 3:
        computer = 'scissors'
    
    if move == computer:
        return 'You Tie!'
    if move == 'rock' and computer == 'paper':
        return 'You Lose'
    if move == 'rock' and computer == 'scissors':
        return 'You Win'
    if move == 'paper' and computer == 'rock':
        return 'You Win!'
    if move == 'paper' and computer == 'scissors':
        return 'You Lose!'
    if move == 'scissors' and computer == 'rock':
        return 'You Lose!'
    if move == 'scissors' and computer == 'paper':
        return 'You Win!'
    
print(rock_paper_scissors('scissors')) 
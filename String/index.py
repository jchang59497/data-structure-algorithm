# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a,b):
    return a + b + b + a
print(make_abba('What', 'Up'))
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'



# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
    return 'Hello' + ' ' + name + '!'
print(hello_name('Jenny'))
# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'


# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'
print(make_tags('i', 'Hello'))
# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'



# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
    return out[0:2] + word + out[2:]
print(make_out_word('<<>>', 'Yay'))

# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'
# Given a string, return a string where for every char in the original, there are two chars.
def double_char(string):
    new_string = ''
    for i in string:
        new_string += i * 2
    return new_string
# print(double_char('The'))
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'



# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(string):
    return string.count('hi')
# print(count_hi('abc hi ho'))       
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2


# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(string):
    return string.count('cat') == string.count('dog')
# print(cat_dog('catdog'))
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True


# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
    count = 0

    for i in range(len(str) - 3):
        if str[i] + str[i + 1] == 'co' and str[i + 3] == 'e':
            count += 1
    return count
print(count_code('aaacodebbb'))

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2


# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    if str1 == str2:
        return True
    
    if len(str1) > len(str2):
        return str1[len(str1)-len(str2):len(str1)] == str2
    
    if len(str2) > len(str1):
        return str2[len(str2)-len(str1):len(str2)] == str1
    
    return False
print(end_other('abc', 'abcdef'))

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

#sWAP cASE
def swap_case(s):
    str = ''
    for letter in s:
        if letter == letter.upper():
            str += letter.lower()
        else:
            str += letter.upper()
    return str
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#String Split and Join
def split_and_join(line):
    line = line.split(" ")
    return ("-".join(line)) 
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
def print_full_name(a, b):
    print("Hello " + a + ' ' + b + '! You just delved into python.' )
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
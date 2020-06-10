# Put your code here

while (True):
    
    new_idea = input("What is your new idea? ") 

    with open("ideas.txt", "a") as f:
        f.write (f"{new_idea} \n")
    
    i = 0
    
    f = open ("ideas.txt", "r")
    
    for line in f.readlines():
        i += 1
        print(f"{i}. {line}")
    f.close()

import sys

def delete():
    i = 0
    
    f = open ("ideas.txt", "r")
    ideas = f.readlines()
    
    f = open ("ideas.txt", "w")
    
    for line in ideas:
        i += 1
        if i != int(sys.argv[1]):

            f.write(f"{line}")
    f.close()


def show_list():
    i = 0
    
    f = open ("ideas.txt", "r")
    
    for line in f.readlines():
        i += 1
        print(f"{i}. {line}")
    f.close()

def f_list():
    continut_fisier=[]
    f = open ("ideas.txt", "r")
    for line in f.readlines():
        continut_fisier = line
    if continut_fisier == []:
        print("empty")
    else:
        show_list()

usr_input = (sys.argv[1:])

if usr_input[0] == "--delete":
    print("DELETED")

if usr_input[0] == "--list":
    f_list()
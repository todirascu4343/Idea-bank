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

delete()

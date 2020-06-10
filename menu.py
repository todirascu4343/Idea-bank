exit_cmd = False
while exit_cmd == False:
    try:
        new_idea.lower = input ("What is your new idea? ")
        if new_idea.lower == "q":
            exit_cmd = True
        else:
            with open("ideas.txt", "a") as f:
                f.write (f"{new_idea} \n")
    
                i = 0
            
                f = open ("ideas.txt", "r")
            
                for line in f.readlines():
                    i += 1
                    print(f"{i}. {line}")
                f.close()

    except KeyboardInterrupt:
        print("\n\nCiao!")
        exit_cmd = True
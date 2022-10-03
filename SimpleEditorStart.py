def stringEditor(s):
    print(s)
    stop = False
    while not stop:
        c = input("Enter command: ")
        if c == "quit":
            stop = True
        else:
            cmd = c.split('/')
            if cmd[0] == "a":
                s = s + cmd[1]
            
            elif cmd[0] == "d":
                cmd = c.split('/')
                s = c.upper()
                s = s + cmd[1]
                   
        
                
#
#  Insert additional commands here using "elif"
#


            print(s)
    return(s)

stringEditor("0123456789")

# step 1: the strings commands are listed in MOODLE so edit the program to include all of those commands listend under assignments,
# step 2: execute commands.
# enter command c.split()        

            

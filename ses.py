def stringEditor(s):
    print(s)
    stop = False
    while not stop:
        c = input("Enter a command: ")
        if c == "quit":
            stop = True
        else:
            cmd = c.split('/')
            if cmd[0] == "a":
                s = s + cmd[1]
            #return an uppercase string with u/
            elif cmd[0] == "u":
                s = s.upper() + cmd[1]
            #return a lowercase string with l/
            elif cmd[0] == "l":
                s = s.lower() + cmd[1]
            #return a reversed string with r/
            elif cmd[0] == "r":
                s = s[::-1] + cmd[1]
            
            
            
        print(s)
    return(s)

stringEditor("abcdefg")
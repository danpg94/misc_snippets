# 1: Manual String Formatting

def manual_str_formatting_noob(name, subscribers):
    if subscribers > 100000:
        print("Wow" + name + "! you have " + str(subscribers) + " subscribers!")
    
def manual_str_formatting(name, subscribers):
    if subscribers > 100000:
        print(f"Wow {name}! you have {subscribers}!")

# 2: Manually calling close on a file 
def manually_calling_close_on_a_file_noob(filename):
    f = open(filename, "w")
    f.write("hello\n")
    f.close()

def manually_calling_close_on_a_file(filename):
    with open(filename, "w") as f:
        f.write("hello\n")

# 3: Finally instead of context manager
def finally_instead_of_context_manager_noob(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.sendall(b'Hello, world')
    finally:
        s.close()

def finally_instead_of_context_manager(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, world')

# 4: Using bare except clause

def bare_except_noob():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except: # oops! can't CTRL-C to exit
            print("Not a number, try again")

def bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except ValueError: # It will only break if user input is incorrect
            print("Not a number, try again")

# 5: Thinking that the 'caret' (^) means exponentiation
 
def caret_and_exponentiation(x, p):
    y = x ^ p   # bitwise xor
    y = x ** p  # exponentiation

# 6: Misuse of mutable default arguments

def append_noob(n, l=[]):
    l.append(n)
    return l

    # l1 = append(0)    output: [0]
    # l2 = append(1)    output: [0, 1]

def append(n, l=None):
    if l is None:
        l = []
    l.append(n)
    return l

    # l1 = append(0)    output: [0]
    # l2 = append(1)    output: [1]

# 7: Never using comprehention

def never_using_comprehentions():
    squares = {}
    for i in range(10):
        squares[i] = i * i

def using_comprehentions():
    squares = {i: i * i for i in range(10)} 

    dict_comp = {i: i * i for i in range(10)}
    list_comp = [x*x for x in range(10)]
    set_comp = {i%3 for i in range(10)}
    gen_comp = (2*x+5 for x in range(10))

# 8: Always using comprehention :)

def always_using_comprehentions(a, b, n):
    """matrix product of a, b of length n x n"""
    return [
        sum(a[n * i + k] * b[n * k + j] for k in range(n))
        for i in range(n)
        for j in range(n)
    ] # not that easily understood :(

def not_using_comprehentions(a, b, n):
    c = []
    for i in range(n):
        for j in range(n):
            ij_entry = sum(a[n * i + k] * b[n * k + j] for k in range(n))
            c.append(ij_entry) 
    return c

# 9: 
x = 1 

def foo(): 

    x = 2 

    def bar(x=3): 

        print(x) 

    bar() 

foo()  
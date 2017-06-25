#Analyzes strInput and calls other functions to process it further
def analyze(expression):
    split = expression.split(' ')
    stack = []
    print "String: %s" % expression, split
    
    #Example expression: (1 + 2 + 3 + 4 + 5)
    #Broken into (1 + 2), prev + 3, prev + 4, prev + 5

def read(expression):
    pass

if __name__ == '__main__':
    prompt = ">>> "
    
    print "Input your expression here"
    expression = raw_input(prompt)
    
    analyze(expression)

    #Don't know if this is correct etiquette for exiting
    print "Exiting program..."
    exit

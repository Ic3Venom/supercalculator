#Analyzes strInput and calls other functions to process it further
def analyze(expression):
    split = expression.split(' ')
    print "String: %s" % expression


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

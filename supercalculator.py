#Analyzes strInput and calls other functions to process it further
def analyze(strInput):
    print "String: %s" % strInput
    

if __name__ == '__main__':

    print "Input your expression here"
    strInput = raw_input(">>> ")
    
    analyze(strInput)

    #Don't know if this is correct etiquette for exiting
    print "Exiting program" 
    exit

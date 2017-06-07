def unique(s):
    uchars = set()
    for c in s:
        if c not in uchars:
        	uchars.add(c)

    if len(s) == len(uchars):
    	print "Unique"
    	
    else:
    	print "not unique"
    print uchars
	
unique("Python")
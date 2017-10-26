file = open(raw_input("Enter filename\n"))
neededword = raw_input("Enter the word to be searched\n")
i = 1
for line in file:
    wordlist = line.split(" ")
    for word in wordlist:
        if word.find(neededword) != -1:
            print "line no:",i,"word no:",wordlist.index(word) + 1,"-->",
            for word in wordlist:
                print word," ",
            print "\n"
    i+=1


file = open(raw_input("Enter filename\n"))
#neededword = raw_input("Enter the word to be searched\n")
i = 1
wordslist = []
text = ""
for line in file:
    line = line.strip("\n")+ " "
    text += line
i = 1
wordslist = text.split(" ")

print "\n",i,".",
i+=1
for word in wordslist:
    print word,
    if word.find(".") != -1:
        print ("\n",i,".",end='')
        i+=1




"""
for word in wordlist:
    if word.find(neededword) != -1:
            print "line no:",i,"word no:",wordlist.index(word) + 1,"-->",
            for word in wordlist:
                print word," ",
            print "\n"
    i+=1
"""

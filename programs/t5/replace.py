sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
print (sentence.replace("!", " "))
print (sentence.replace("!", " ").upper())
print (sentence[::-1])
#or, alternatively, a more grammatically correct reverse sentence:
print (sentence[::-1].replace("!", " "))
#the -1 just reverses the string, a blank :: means to fetch the whole string

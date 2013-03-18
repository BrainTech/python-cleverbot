import cleverbot
 
# beginning two different cleverbot sessions
# I use steve and bob to keep things separate while coding.
# This is not reflected in the html output.
steve = cleverbot.Session()
bob = cleverbot.Session()
 
# Gathering info....boring stuff
convo_start = raw_input("How would you like to begin the conversation? : ")
print ""
cycles = int(raw_input("How many cycles would you like to run? : "))
print ""
 
# Starting the conversation
print "Bob: "+convo_start
reply = steve.Ask(convo_start)
print "Steve: "+reply
 
i = 0
 
# continuing the conversation in the loop.
while (i <= cycles): # you will have to edit the less than symbol on this line.
    reply = bob.Ask(reply)
    print "Bob: "+reply
 
    reply = steve.Ask(reply)
    print "Steve: "+reply
 
    i = i + 1
 
# ....and now to tie up my loose ends.
exit()

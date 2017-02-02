import random

  
print ("==Rock Paper Scissor ==")
while True:
  print "==It's your turn.. Select any one== "
  print "==Lets go!=="
  print("Type quit to exit")
  print "                  "
  sel=raw_input("==GO:")
  sel=sel.lower()
  if sel=="quit":
    print(" Thanks for playing")
    print("  See you again")
    break;
  lst=['rock','paper','scissor']
  comp=random.choice(lst)
  print"Computer says",comp
  if sel=="rock":
    if comp=="paper":
      print "You win"
    elif comp==sel:
      print "It's a draw"
    else:
      print "You lose"
  elif sel=="paper":
    if comp=="scissor":
      print "You lose"
    if comp=="rock":
      print "You win"
    else:
      print "It's a draw"
    
  elif sel=="scissor":
    if comp=="rock":
      print "You lose"
    elif comp=="paper":
      print "You win"
    else:
      print "It's a draw"
  else: print("Wrong entry, Type correctly")
  print("                ")
  print("===Next game===")
  print("                ")
  
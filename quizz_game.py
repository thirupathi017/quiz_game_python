print("let's learn the GK of india by this quizzz.. ")

player=input("do you want to play the quiz:")
player=player.lower()

if player!="yes":
    quit()
print("Ok get ready to play the Quizzz.... ")

score=0

#Q1
question=input("What is the capital of India? ")
question=question.lower()
if question=="new delhi":
    print("correct")
    score+=10
else:
    print("incorrect")
    

#Q2    
question=input("Who heads the RBI? ")
question=question.lower()
if question=="reserve bank of india":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q3
question=input("Where is India Silicon Valley located? ")
question=question.lower()
if question=="bangalore":
    print("correct")
    score+=10
else:
    print("incorrect")



#Q4 
question=input("What is the national flower of India? ")
question=question.lower()
if question=="lotus":
    print("correct")
    score+=10
else:
    print("incorrect")



#Q5
question=input("What is the national sport of India? ")
question=question.lower()
if question=="hockey":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q6
question=input("What is the least developed state in India? ")
question=question.lower()
if question=="bihar":
    print("correct")
    score+=10
else:
    print("incorrect")
    

#Q7    
question=input("What is the richest state in India? ")
question=question.lower()
if question=="maharashtra":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q8
question=input("What is the longest river in India? ")
question=question.lower()
if question=="indus river":
    print("correct")
    score+=10
else:
    print("incorrect")


#Q9
question=input("What is the national bird of India? ")
question=question.lower()
if question=="peacock":
    print("correct")
    score+=10
else:
    print("incorrect")
    
    
    
#Q10
question=input("What is the most populous state in India? ")
question=question.lower()
if question=="uttar pradesh":
    print("correct")
    score+=10
else:
    print("incorrect")


print("Your score is:",score,"/ 100")

print()
print()

print("-----------THANK YOU FOR PLAY THIS QUIZZ...-------------")
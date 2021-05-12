# Multiple choice questions in decision making
print("--------------------")
print("Welcome to milo evaru kotishwarudu")
print("Who invented python language")
print("A.Sundar pichhai")
print("B.Guido Rossum")
print("C.Sathyam Nadella")
print("D.Steve jobs")
# 1state
choice = str(input("Enter the correct option :"))

# validation logic
if choice == 'A' and 'B' and 'C' and 'D':
    print("result will be announced soon")
else:
    print("You've choosed the wrong option.Choose the options in between A,B,C,D")
# Business logic
if choice == 'A':
    print("sorry wrong answer")
    print("Better luck next time")
elif choice == 'B':
    print("Wohooo! Correct answer")
    print("You've promoted to next level")
    print("Hearty congratulations by Jr.NTR")
elif choice == 'C':
    print("sorry wrong answer")
    print("Better luck next time")
elif choice == 'D':
    print("sorry wrong answer")
    print("Better luck next time")
else:
    print("Thanks for your valuable time")
marks = int(input("Enter marks:: "))
if marks > 100 or  marks < 0:
      print("please enter correct marks")
else:
     if marks >= 95 or marks == 100:
         print("A+ Grade")
         print("congratulations")
     elif marks >= 60 and marks < 95:
         print("A Grade")
     elif marks >=50 and marks < 60:
         print("B grade")
     elif marks >= 35 and marks < 50:
        print("pass")
     else:
          print("fail")




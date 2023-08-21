#Calculator using Python Language
while True:
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   print("5. Modulus")
   print("6. Exit")
   print("Enter Your Choice (1-6): ")
   ch = int(input())
   if ch>=1 and ch<=5:
      num1 = int(input("enter first number :"))
      num2 = int(input("enter second number :"))
   if ch==1:
      res = num1 + num2 # type: ignore
      print("\n Result = ", res)
   elif ch==2:
      res = num1 - num2 # type: ignore
      print("\n Result = ", res)
   elif ch==3:
      res = num1 * num2 # type: ignore
      print("\n Result = ", res)
   elif ch==4:
      res = num1 / num2 # type: ignore
      print("\n Result = ", res)
   elif ch==5:
      res = num1 %  num2 # type: ignore
      print("\n Result = ", res)
   elif ch==6:
      break
   else:
      print("\nInvalid Input!..Try Again!")



                                                   # AN

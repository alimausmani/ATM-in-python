
print ("ATM program")
print("****************")
print("**************************")
print("****welcome *to* SBI ATM****")
card=(input("please insert your card:"))
if card=="atm card":
    print("please do not remove your card during entire transaction") 
    language=input("please enter your language:")
    if language== "english" or language=="hindi":
        print("prosess")
        pin=int(input("enter your pin 4 digit pin number:"))
        if pin==4444:
           print("correct pin")
           account=input("enter your account:")
           if account=="saving" or "current":
               print("prosess")
               transaction=input("please choose your transaction")
               total_amt=50000
               if transaction=="withdraw" or transaction=="balance enquiry" or transaction=="quite": 
                  amt=int(input("enter the withdwrawal amount"))
                  balance=total_amt-amt
                  print("you have remaining balance")
                  amount=input("enter the amount")
                  if amount=="2000":
                      print("amount")
                      money=int(input("enter your money"))
                      if balance%100==0:
                         print(balance)
                         recipt=input("do you want to recipt")
                         if recipt=="yes" or recipt=="no":
                                print("your transaction is prosessing please wait")
                                print("transaction complite")
                                print("thank you so much")  
                         else:
                              print("please take card")
                      else:
                           print("not money")
                  else:
                       print("prosess")
               else:
                   print("your transaction is success fully")
           else:
               print("other account")
        else:
            print("wrong pin")
    else:
       print("other language")
else:
    print("any card")




                
        


                


            


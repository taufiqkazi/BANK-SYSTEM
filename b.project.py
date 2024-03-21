class User:

        def __init__(self,name,contact,email,password,adhaar):
                self.name=name
                self.contact=contact
                self.email=email
                self.password=password
                self.adhaar=adhaar


        def __str__(s):
                return s.name+"\t"+str(s.contact)+"\t"+s.email+"\t"+s.password+"\t"+str(s.adhaar)
                a=User('taufeeq','7858568789','tauf@gmail','5698024345345','ta1324')
class bank:
        balance=0
        
        users=[]

        def opensaving_acc(s):
                print("Enter Name , Contact , Email , Password,adhaar")
                print("|---------------------------------------------|")
                name=input("Enter Name : ")
                print("|---------------------------------------------|")
                contact=input("Enter Contact : ")
                if (contact.isdigit() and len(contact)==10):
                        contact=int(contact)
                else:
                        print("invalid contact")
                print("|---------------------------------------------|")
                email=input("Enter Email : ")
                print("|---------------------------------------------|")
                password=input("Enter Password : ")
                print("|---------------------------------------------|")
                adhaar=input("Enter adhaar no:")
                s.users.append(User(name,contact,email,password,adhaar))
                print("|---------------------------------------------|")
                print("your account is open successfully")
                print("|---------------------------------------------|")
                print("your account no is",adhaar[::-1])
                print("|---------------------------------------------|")
                print("your username is ",email)
                print("|---------------------------------------------|")
                print("your password is",password)
                print("|---------------------------------------------|")        

        def opencurrent_acc(s):
                print("Enter Name , Contact , Email , Password,adhaar")
                print("|---------------------------------------------|")
                name=input("Enter Name : ")
                print("|---------------------------------------------|")
                contact=input("Enter Contact : ")
                if (contact.isdigit() and len(contact)==10):
                        contact=int(contact)
                
                else:
                        print("invalid contact")
                print("|---------------------------------------------|")
                email=input("Enter Email : ")
                print("|---------------------------------------------|")
                password=input("Enter Password : ")
                print("|---------------------------------------------|")
                adhaar=int(input("Enter adhaar no:"))
                s.users.append(User(name,contact,email,password,adhaar))
                print("|---------------------------------------------|")
                print("your account is open successfully")
                print("|---------------------------------------------|")
                print("your account no is",adhaar[::-1])
                print("|---------------------------------------------|")
                print("your username is ",email)
                print("|---------------------------------------------|")
                print("your password is",password)
                print("|---------------------------------------------|")
                
        def login(s):
                print("Enter Email & Password")
                print("|---------------------------------------------|")
                email=input("Enter Email : ")
                print("|---------------------------------------------|")
                password=input("Enter Password : ")
                print("|---------------------------------------------|")
                for i in s.users:
                        if email==i.email and password==i.password:
                                return i

        def depositeaAmount(s):
                print("|-----------Enter the amount-----------|")
                print("|--------------------------------------|")
                amount=int(input("enter the amount"))
                s.balance=s.balance+amount
                print("balance",s.balance)

                
        def withdrawAmount(s):
                print("--------------Enter the amount---------------")
                print("---------------------------------------------")
                amount=int(input("enter the amount"))
                s.balance=s.balance-amount
                print("---------------------------------------------")
                if amount>s.balance:
                        print("insufficient balance")
                        print("---------------------------------------------")
                elif amount >=100 and amount<=s.balance:
                        print("thank you for visiting")
                        print("---------------------------------------------")
                elif amount<=100:
                        print("you can't withdraw amount less than 100")
                        print(amount)

   
        def balanceAmount(s):
                print("---------------------------------------------")
                print("amount",s.balance)


        def transfer(s,User):
                amount=int(input("enter a amount to transfer"))
                if amount>User.balance:
                        print("inssuficent balance")
                elif amount>=1 and amount<=User.balance:
                        
                        User.balance=User.balance-amount
                        print("Amount transfer successfully your balance:" ,User.balance)
        
        def  home(s):
                c=True
                while(c):
                        
                        print("|------------------Enter 1 for deposite--------------------|")
                        print("|------------------Enter 2 for withdraw--------------------|")
                        print("|------------------Enter 3 for checkbalance----------------|")
                        print("|------------------Enter 4 for transfer--------------------|")
                        print("|------------------Enter 5 for exit------------------------|")

                        j=int(input("enter the choice"))
                        if j==1:
                                print("---------------------------------------------")
                                s.depositeaAmount()
                        elif j==2:
                                print("---------------------------------------------")
                                s.withdrawAmount()
                        elif j==3:
                                print("---------------------------------------------")
                                s.balanceAmount()
                                
                        elif j==4:
                                print("---------------------------------------------")
                                s.transfer(User)
                        elif j==5:
                                print("---------------------------------------------")
                                c=False
                                break
                        

        def call(s):
                a=True
                while(a):
                        print("|----------------------well come to AXIS BANK------------------------------|")
                        print("|----------------------Enter 1 For open savingacc--------------------------|")
                        print("|----------------------Enter 2 For open currentacc ------------------------|")
                        print("|----------------------Enter 3 for login-----------------------------------|")
                        print("|----------------------Enter 4 for exit------------------------------------|")
                        print("---------------------------------------------")

                        i=int(input("enter choice"))
                        print("---------------------------------------------")
                        if i==1:
                                print("---------------------------------------------")
                                s.opensaving_acc()
                        elif i==2:
                                print("---------------------------------------------")
                                s.opencurrent_acc()
                        elif i==3:
                                print("---------------------------------------------")
                                u=s.login()
                                if u is not None:
                                        s.home()
                        elif i==4:
                                a=False
                                break
x=bank()
x.call()






        

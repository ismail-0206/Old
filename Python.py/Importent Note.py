#                       Its First time.
#print("hello world")



#                       01.Now Variable & data type.
#
#PS="Ismail is a student."
#print(PS)



#                       02.Data type of Python.
#
#   1.Number 2.string 3.Booleans 4.List 5.tupple 6.set 7.Dictionary
#
#1.Number data type: Integer & floaing point.
#INTEGER is always REAL NUMBER but none decimal number. [Like:10 50 60 75 250 1540 etc.]
#FLOATING is always REAL NUMBER but decimal number. [Like:15.5 25.8 50 40 60.855 etc]
#
#String always can be letter or Other symbles. as like: "Ismail" "10" "@" etc
#
# 3.BOLEANS always can be TRUE or FALSE.
#
#                       Oparetor in Python.
#
#Oparetor is a Symble as like: + - ? ! etc.



#                       03.Type of Oparetor.
#1.Arithmatic: +(Addition), -(Substraction), *(Multiplication), /(division{Decimal value}), 
#**(Exponentitation){TO THE POWER}, %(Reminder){Reminder [ভাগশেষ]},
#//(floor division):{None Decimal divsion value}
#
#2.Assignment: =(Same to Arithmatic). As like:(X+=Y){It means X+Y}.
#
#3.Comparison:>(Greater than), <(Less than), >=(greater than equal), ==(Equality), !=(Not equality),
#Its basicaly show True or False.
#
#4.Logical:         and                or                 not                       
#              ( a = (15)        ) (a = (15)        ) (a = (15)        )                                     
#              ( b = (20)        ) (b = (20)        ) (b = (20)        )                                 
#              ( c = a<b and b>a ) (c = a<b or b>a  ) (c = not b>a     )                                 
#              ( print(c) = True ) (print(c) = True ) (print(c) = True )                          
#          and = (Truth table; TT=True )
#                (             TF=False)
#                (             FT=False)
#                (             FF=False)
#                                       or = (Truh table; TT=True )
#                                            (            TF=True )
#                                            (            FT=True )
#                                            (            FF=False)
#                                                                  not = (Reverse {এটা Output এ True কে  )
#                                                                        (        {False & False কে True})
#          
#5.Indentity: 
#
#6.Membership:  {Its get True or False from the List}
#      in : (Its get real True from List )
#  not in : (Its ger fake True from List )
#                           in                                                    not in
#             ( a = ["Ismail","Rayhan","Yeasin","Azmain"] ) (a = ["Ismail","Rayhan","Yeasin","Azmain"] )
#             ( b = "Azmain" in a                         ) (b = "Chotto" not in a                     )
#             ( print(b) = True                           ) (print(b) = True                           )



#                       04.Working with number of data type.
# Gatting the type of numerical value. [type()]
#
#                       Python number mathod.
# ROUNDing a number. 1.round(number,ndigit}.   like: (a = 3.14159     )
#                                                    (x = round(a,2)  )
#                                                    (print(x) = 3.14 )

# Rising a number to a POWER. 1.pow(base,exp). Like: (x = pow(5,2)    )
#                                                    (print(x)  = 5*5 )
#
#                       getting absolute value.
#Its a none negetive value of a number.
#                                      ( a = abs(-567)  )
#                                      ( print(a) = 567 )
#
#                       getting quotient & reminder.
#এটি দুটি ans দেয় = (ভাগফল,ভাগশেষ).
#                                   (  x = divmod(5,2)  )
#                                   (  print(2,1)       )



#                       05.Working with string in python.
# Single or double qutes:
# Single qutes: a = "Ismail is a Student"
# Double qutes: a = "Ismail is 'OverPower' "
#
# Multy line string: ( a = """Ismail is a good boy. )
#                    ( Its a multyple line"""       )
#
# Concatenating string: ( a = "Ismail "             )
#                       ( b = "student"             )
#                       ( c = a+b                   )
#                       ( print(c) = Ismail student )

#                       Accessing part of a string.
# Indexing: (a = "Ismail is a student"  ) 
#           (print(a[0]) = I            ) {এটি লিখতে হয় [] এর মাঝে & এটি  }
#                                         {শুরু  হয় 0,1,2,3,4,5,6,7,8,9 etc}
# Slicing:  ( a = "Ismail is a student" )
#           ( print(a[0:5]) = Ismail    ) {এটি লিখতে হয় [] এর মাঝে & এটি  }
#                                         {শুরু  হয় 0,1,2,3,4,5,6,7,8,9 etc}

#                       string mathod.
#
# Capitalize string:     ( a = "ismail is a boy"      )
#                        ( x = a.capitalize()         )
#                        (     print(x) = Ismail is a boy )
#
# Upper string:          ( a = "ismail is a boy"      )
#                        ( x = a.upper()              )
#                        ( print(x) = ISMAIL IS A BOY )
#
# lower string:          ( a = "ISMAIL IS A BOY"      )
#                        ( x = a.lower()              )
#                        ( print(x) = ismail is a boy )
#
# length  string:        ( a = "Ismail is a student" ) {Its counting per character}
#                        ( print(len(a)) = 19        )
#
# Replacing part string: ( a = "Ismail is a student"         )
#                        ( print(a.replace("student","Boy")  )



#                       06.User input in Python
#Use ofInput: ( a =input("Enter your name : " )                            )
#             ( print("Welcome ",a) = Input(Ismail),Output{Welcome Ismail} )
#
#Type convertion: ( a = input("Enter 1st Number: ") = 50   )
#                 ( b = input("enter 2nd Number: ") = 50   )
#                 ( c = int(a)+int(b)                      )
#                 ( print(c)                        = 100  )



#                       07.List in Python.
#  [We can change any Elements stored in the List] {List is Cangeble}
#        NB:{We can store any type of Data Type in the List}
#List is ordered container.
#   a = [] {Emepty List}
#Use of List: {Its provided for viewing multiple Lists }
#            ( a = ["Ismail","Rayhan","Yeasin","Azmain"]       )                
#            ( print(a) = ['Ismail,'rayhan','Yeasin','Azmain'] )
#
#use of Positive Indexing:   {Its provided for viewing single List by Positve Number}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"] ) {     a = ["0","1","2","3"]         }
#                          (  print(a[3]) = Azmain                      ) {Indexing started to 0,1,2,3,4,5 etc}
#
#Use of Negetive Indexing:   {Its provided for viewing single List by Negetive Number}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"] ) {     a = ["-4","-3","-2","-1"]     }
#                          (  print(a[-1]) = Azmain                     ) {Indexing started to 0,1,2,3,4,5 etc}
#
#Use of Rang of Indexes:     {Its provided for viewing perticuler rang of Indxes}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"] ) {     a = ["0","1","2","3"]         }
#                          (  print(a[2:4]) = ['Yeasin','Azmain'      ] ) {Indexing started to 0,1,2,3,4,5 etc}
#
#Adding Items by APPEND:     {Its automatic added Item to end of the list}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"]                )
#                          (  a.append("Chotto")                                       )
#                          (  print(a) = ['Ismail','Rayhan','Yasin','Azmain','Chotto'] )
#
#Adding Items by INSERT:     {Its manually added a Item to the perticuler Index}       
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"]                 )
#                          (  a.insert(0,"Chotto")                                      )
#                          (  print(a) = ['Chotto','Ismail','Rayhan','Yeasin','Azmain'] )
#
#Delete Item by POP:         {Its deleted the last string from THE List}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"]                 )
#                          (  a.pop()                                                   )
#                          (  print(a) = ['Ismail','Rayhan','Yeasin']                   )
#
#Delete Item by REMOVE:      {Its deleted Manually string from the List}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"]                 )
#                          (  a.remove("Ismail")                                        )
#                          (  print(a) = ['Rayhan','Yeasin','Azmain']                   )
#
#List Length by LEN:         {Its provided for viewing the length of the List}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"]                 )
#                          (  print(len(a)) = 4                                         )
#
#Changing a Item value:      {Its change a perticuler value.}
#                          (  a = ["Ismail","Rayhan","Yeasin","Azmain"]                 )
#                          (  a[3] = "Chotto"                                           )  
#                          (  print(a) = ['Ismail','Rayhan','Yeasin','Chotto']          )
#
#Extending a List:           {Its make a single List from double List}
#                          (  a = [1,2,3]                                               )
#                          (  c = [4,5,6]                                               )
#                          (  a.extend(c)                                               )
#                          (  print(a) = [1,2,3,4,5,6]                                  )



#                       07.Tuple in Python.
#   [We can't change Tuple] {Tuple unchangeble}
#Indexing:     {Its too same as List.} 
#          (It means Use of Tuple is Like List But Its unchangeble)
#        ( a = ("Ismail","Rayhan","Yeasin","Azmain") )
#        ( b = (a[3])                                )
#        ( print(b)  = Azmain                        )



#                       08.Fanction in python.
#Fanction declaretion: {Its create a Fanction.}  (Its reuseble)
#   DEF:  ( def a():                                        )
#         (     print("Ismail","Rayhan","Yeasin","Azmain")  )
#         ( a() = Ismail Rayhan Yeasin Azmain               )
#         ( a() = Ismail Rayhan Yeasin Azmain               )
#         ( a() = Ismail Rayhan Yeasin Azmain               )
# NB: [We can get Mutiple Output from single Fanction]
#
#PARAMETER & ARGUMENTS: {We can add parameter in the created name.} {We can add arguments in Fanction calling.}
#                     ( def fanction(parameter):                                               )
#                     (     b = "Ismail","Rayhan","Yeasin","Azmain" + parameter                )
#                     (     print(b)                                                           )
#                     ( fanction(" Chotto") = ('Ismail', 'Rayhan', 'Yeasin', 'Azmain Chotto')  )
#
#Calculate with Fanction: {}
#                        ( def fanction(x,y):                  )
#                        (     b = int(x) + int(y)   = 50 + 50 )
#                        (     print(b)                        )
#                        ( fanction(input(),input()) =   100   )



#                       09.if satemnet.
#use of IF,ELF,ELSE: {Its provid some condition.}
#                   (  a = (60)                                             )
#                   (  b = (60)                                             )
#                   (  if a<b:                                              )
#                   (      print("Ismail")                                  )
#                   (  elif a>b:                                            )
#                   (      print("Rayhan")                                  )
#                   (  else:                                                )
#                   (      print("Yeasin") (Output = Yeasin)                )
#
#Driving License:    {Its for practice.}
#                   (  a = int(input("Enter your age "))                    )
#                   (                                                       )
#                   (  if a>=18 and a<=45:                                  )
#                   (      print("Congresulation")                          )
#                   (  elif a>45 and a<=65:                                 )
#                   (      print("Your age is to High")                     )
#                   (  else:                                                )
#                   (      print("Sorry")                                   )
#
#nested IF statement:  {1st if fancyion False(Doesn't show nested staement)}
#                    (  a = 70                                              )
#                    (  b = 60                                              )
#                    (  if a>b:                                             )
#                    (      print("a more than b")                          )
#                    (      if a<80:                                        )
#                    (          print("a less than b")                      )
#                    (      else:                                           )
#                    (          print("wrong")                              )
#                    (  else:                                               )
#                    (      print("write the correct ans") = a more than b  )
#                    (                                     = a less than b  )



#                       10.Dictionary in python.
#Creating a dictionary: {}
#                      ( a = {                                                                     )
#                      (     "Ismail":"18",                                                        )
#                      (     "Rayhan":"16",                                                        )
#                      (     "Yeasin":"8",                                                         )
#                      (     "Azmain":"4"                                                          )
#                      ( }                                                                         )
#                      ( print(a) = {'Ismail': '18', 'Rayhan': '16', 'Yeasin': '8', 'Azmain': '4'} )
#
#Access in peticuler Number:  {Access a perticuler item from Dictinary.}
#                           (  a = {                           )
#                           (      "Ismail":"18", [key:value]  )
#                           (      "Rayhan":"16", [key:value]  )
#                           (      "Yeasin":"8",  [key:value]  )
#                           (      "Azmain":"4"   [key:value]  )
#                           (  }                               )
#                           (  x = a["Ismail"]                 )
#                           (  y = a["Rayhan"]                 )
#                           (  z = a["Yeasin"]                 )
#                           (  print("Ismail:",x) = Ismail: 18 )
#                           (  print("Rayhan:",y) = Rayhan: 16 )
#                           (  print("Yeasin:",z) = Yeasin: 8  )
#
#GET method:  {Access a perticular stored value from Dictinary.}
#
#ADDing a Item:  {We can add a kye & value in Dictinary.}
#              ( a = {                                                                          )
#              (     "Ismail":18,                                                               )
#              (     "Rayhan":16,                                                               )
#              (     "Yeasin":8,                                                                )
#              (     "Azmain":4                                                                 )
#              ( }                                                                              )
#              ( a["Chooto"] = 4                                                                )
#              ( print(a) = {'Ismail': 18, 'Rayhan': 16, 'Yeasin': 8, 'Azmain': 4, 'Chooto': 4} )
#
#Item value CHANGE:  {We can change a value from Dictinary.}
#                  ( a = {                                                                         )
#                  (     "Ismail":18,                                                              )
#                  (     "Rayhan":16,                                                              )
#                  (     "Yeasin":8,                                                               )
#                  (     "Azmain":4                                                                )
#                  ( }                                                                             )
#                  ( a["Yasin"] = 9                                                                )
#                  ( print(a) = {'Ismail': 18, 'Rayhan': 16, 'Yeasin': 8, 'Azmain': 4, 'Yasin': 9} )
#
#REMOVE kye:  {We can remove kye from Dictinary}
#           ( a = {                                               )
#           (     "Ismail":18,                                    )
#           (     "Rayhan":16,                                    )
#           (     "Yeasin":8,                                     )
#           (     "Azmain":4                                      )
#           ( }                                                   )
#           ( a.pop("Ismail")                                     )
#           ( print(a) = {'Rayhan': 16, 'Yeasin': 8, 'Azmain': 4} )
#
#NESTED Dictinary: {We can get another dictinary in current dictinary.}
#                 ( inf = {                                                                                             )
#                 (     "bro":{                                                                                         )
#                 (         "Ismail":18,                                                                                )
#                 (         "Rauhan":16,                                                                                )
#                 (         "Yeasin":8,                                                                                 )
#                 (         "Azmain":4,                                                                                 )
#                 (     },                                                                                              )
#                 (     "edu":{                                                                                         )
#                 (         "ismail":"Class 11",                                                                        )
#                 (         "Rayhan":"Class 9",                                                                         )
#                 (         "Yeasin":"Class 5",                                                                         )
#                 (         "Azmain":"Class 0",                                                                         )
#                 (     },                                                                                              )
#                 (     "ser":{                                                                                         )
#                 (         "ISMAIL":"1st",                                                                             )
#                 (         "RAYHAN":"2nd",                                                                             )
#                 (         "YEASIN":"3rd",                                                                             )
#                 (         "AZMAIN":"4th",                                                                             )
#                 (     },                                                                                              )
#                 ( }                                                                                                   )
#                 ( print("Full ifo: ", inf["bro"]["Ismail"])                                                           )
#                 ( print("Education: ",inf["edu"])                                                                     )
#                 ( print("ser: ",inf["ser"]["AZMAIN"]                                                                  )
#                 ( = Full ifo:  18                                                                                     )
#                 (   Education:  {'ismail': 'Class 11', 'Rayhan': 'Class 9', 'Yeasin': 'Class 5', 'Azmain': 'Class 0'} )
#                 (   ser:  4th                                                                                         )
#



#                       11.While loop.
#Createing for 4 times:  {}
#                      ( a = 1                                          )
#                      ( while a<8:                                     )
#                      (     print("Ismail Hossain") =  Ismail Hossain  )
#                      (     a +=2                      Ismail Hossain  )
#                      (                                Ismail Hossain  )
#                      (                                Ismail Hossain  )



#                       12.For loop.
#for loop in List:  {Its make a list Line BY Line}
#                 ( a=("Ismail","Rayhan","Yeasin","Azmain") )
#                 ( for x in a:                             )
#                 (     print(x)                            )
#                 (             = Ismail                    )
#                 (             = Rayhan                    )
#                 (             = Yeasin                    )
#                 (             = Azmain                    )
#
#
#for loop in String:  {Its make a string value Line BY Line}
#                   ( a=("Ismail")               )
#                   ( for b in a:                )
#                   (     print(b)               )
#                   (             =I             )
#                   (             =s             )
#                   (             =m             )
#                   (             =a             )
#                   (             =i             )
#                   (             =l             )
#
#                   ( for x in range(5):         )
#                   (     print("Ismail")        )
#                   (                    =Ismail )
#                   (                    =Ismail )
#                   (                    =Ismail )
#                   (                    =Ismail )
#                   (                    =Ismail )
#                   (                    =Ismail )
#
#nested for loop:  {Its make a nested value in Multiple List.}
#                (a=("Ismail","Rayhan","Yeasin","Azmain")                             )
#                (b=("student",)                                                      )
#                (c=("Honest",)                                                       )
#                (                                                                    )
#                (for x in a:                                                         )
#                (    for y in b:                                                     )
#                (        for z in c:                                                 )
#                (            print(x+" is a "+y+" & "+z)                             )
#                (                                       =Ismail is a student & Honest)
#                (                                       =Rayhan is a student & Honest)
#                (                                       =Yeasin is a student & Honest)
#                (                                       =Azmain is a student & Honest)



#                       13.Break & continue.
#Break:             {}
#                ( a=("Ismail","Rayhan","Yeasin","Azmain","Chotto") )
#                ( for x in a:                                      )
#                (     if x=="Chotto":                              )
#                (         break                                    )
#                (     print(x)                                     )
#                (             =Ismail                              )
#                (             =Rayhan                              )
#                (             =Yeasin                              )
#                (             =Azmain                              )
#
#continue:         {Its continue List to Before & After}
#                (a=("Ismail","Rayhan","Chotto","Yeasin","Azmain",) )
#                (for x in a:                                       )
#                (    if x=="Chotto":                               )
#                (        continue                                  )
#                (    print(x)                                      )
#                (            =Ismail                               )
#                (            =Rayhan                               )
#                (            =Yeasin                               )
#                (            =Azmain                               )



#                       14.File in python.
#File mode "w":  {Its for write in File.}
#              ( f=open("trial.txt","w")              )
#              ( f.write("I'm Ismail.")               )
#              ( f.close()                            )
#              ( "I'm Ismail." Its in trial.txt file  )
#
#File mode "a":  {Its for add some sentence.}
#             ( f=open("trial.txt","a")               )
#             ( f.write(".I'm a Good boy")            )
#             ( f.close()                             )
#             ( ".I'm Good boy" Its in trial.txt file )
#
#File mode "r":  {Its for read that File.[Full]}
#              ( f=open("trial.txt","r")       )
#              ( x=f.read()                    )
#              ( print(x)                      )
#              ( f.close()                     )
#              ( [Now we can Read trial.txt]   )
#
#File mode "r":  {Its for read a single line from that File}
#              ( f=open("trial.txt","r")     )
#              ( x=f.readline()              )
#              ( print(x)                    )
#              ( y=f.read()                  )
#              ( print(y)                    )
#              ( f.close()                   )
#              ( [Now we can Read trial.txt] )
#
#File mode "remove":  {Its for reomve a File}
#                   ( import os                 )
#                   ( os.remove("trial.txt")    )
#                   ( f=open("trial.txt","r")   )
#                   ( f.close()                 )
#                   ( [Now remove that File]    )
#
#Existing file Access:  {}
#                     ( f=open(r"C:\Users\ISMAIL\OneDrive\Desktop\NB.txt","r") )
#                     ( x=f.read()                                             )
#                     ( print(x)                                               )
#                     ( f.close()                                              )
#                     ( Now we can Access that File                            )



#                       15.Pip & module.
#math module:  {We can Calculate any math by it.}
#            ( import math          )
#            ( x=2                  )
#            ( a=math.sqrt(x)       )
#            ( print(a)             )
#            ( =1.4142135623730951  )



#                       14.Advance Python.
#Create a Class:  {}
#               ( class x:                                )
#               (     a="Ismail is a good Boy"            )
#               (     b="Rayhan is a Good boy"            )
#               (     c="Yeasin is a good boy"            )
#               (     d="Azmain is a Good Boy"            )
#               ( y=x()                                   )
#               ( a=y.a                                   )
#               ( b=y.b                                   )
#               ( c=y.c                                   )
#               ( d=y.d                                   )
#               ( print("1st: ",a)                        )
#               ( print("2nd: ",b)                        )
#               ( print("3rd: ",c)                        )
#               ( print("4th: ",d)                        )
#               ( =1st:  Ismail is a good Boy             )
#               ( =2nd:  Rayhan is a Good boy             )
#               ( =3rd:  Yeasin is a good boy             )
#               ( =4th:  Azmain is a Good Boy             )
#
#1.Class with Attribute & 2.Methods:  {}
#                      ( class me:                                     )
#                      (     def __init__(one,name,studies,age):       ) [one parameter is access to Attribute & methods]
#                      (         one.name=name                         )
#                      (         one.studies=studies                   )
#                      (         one.age=age                           )
#                      (     def Methods(one):                         )
#                      (             print("Hi "+one.name+" I'm fine." )                                 
#                      ( obj_instance=me("Ismail",11, 18)              ) [Instance are always unique]
#                      (                                               )
#                      ( obj_instance.Methods()                        )
#                      (                                               )
#                      ( a=obj_instance.name                           )
#                      ( b=obj_instance.studies                        )
#                      ( c=obj_instance.age                            )
#                      ( print("Name:",a)                              )
#                      ( print("Class:",b)                             )
#                      ( print("Age:",c)                               )
#                      (                                               )
#                      ( =Hi Ismail I'm fine.                          )
#                      (                                               )
#                      ( =Name: Ismail                                 )
#                      ( =Class: 11                                    )
#                      ( =Age: 18                                      )
#



#                       15.Inharitance in Python.
#inharitance:  {}
#            ( class parants:)
#            (     def __init__(self,name,age):   )
#            (         self.name=name             )
#            (         self.age=age               )
#            (     def p_mathods(self):           )
#            (         print("Me "+self.name)     )
#            (                                    )
#            ( class child(parants):              )
#            (     def __init__(self,name,age):   )
#            (         super().__init__(name,age) )
#            (     def c_parameter(self):         )
#            (         print("me "+self.name)     )
#            (                                    )
#            ( x=child("Ismail",1)                )
#            ( y=child("18",1)                    )
#            (                                    )
#            ( x.p_mathods()                      )
#            ( y.c_parameter()                    )
#            ( =Me Ismail                         )
#            ( =me 18                             )




#                   DATA structure.
#List
#Stack Rukle {LIFO} = [Last In Fast Out]
#                   ( push(item): Put the item on the top of the stack. )
#                   ( pop(): Remove an item from top of the stack.      )
#                   ( peek(): Returns the value of top in the stack.    )
#
#Queue Rule {FIFO} = [Fast In Fast Out]
#Dictionary 
#Tree
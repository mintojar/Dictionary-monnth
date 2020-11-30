months={
  "February":{
    'Days':29
  },
  "May":{
    'days':31
  },
  "January":{
    'days':31
  },
  "March":{
    'days':31
  },
  "April":{
    'days':31
  },
  'June':{
    'days':30
  },
  'july':{
    'days':31
  },
  'Agust':{
    'days':31
  },
  'september':{
    'days':30
  },
  "october":{
    'days':31
  },
  'november':{
    'days':30
  },
'december':{
    'days':31
  }
}
correct=(0)
for x in months:
  print(x)
  user=input("many days are in february ")
  if user==('29'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user2=input("many days are in may ")
  if user2==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user2=input("many days are in may ")
  if user2==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user3=input("many days are in January ")
  if user3==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user4=input("many days are in march ")
  if user4==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user5=input("many days are in april ")
  if user5==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user6=input("many days are in june ")
  if user6==('30'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user7=input("many days are in july ")
  if user7==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user8=input("many days are in agust ")
  if user8==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user9=input("many days are in september ")
  if user9==('30'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user10=input("many days are in october ")
  if user10==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user11=input("many days are in november ")
  if user11==('30'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  user12=input("many days are in december ")
  if user12==('31'):
    print('nice job')
    correct+=1
  else:
    print('wrong')
  break
print(correct)
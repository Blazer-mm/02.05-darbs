x = int(input("Pirkuma summa: "))
if 200<=x<500:
  print("Jāsamaksā: ",x*0.9)
elif x>=500:
  print("Jāsamaksā: ",x*0.8)
else:
  print("Jāsamaksā: ",x)
import statistics
import random


dataset = random.sample(range(0,200),100)
print(dataset)
dataset.sort()
print(dataset)
bin1 = []
bin2 = []
bin3 = []
bin4 = []
bin5 = []
mbin1 = []
mbin2 = []
mbin3 = []
mbin4 = []
mbin5 = []
Mbin1 = []
Mbin2 = []
Mbin3 = []
Mbin4 = []
Mbin5 = []
for i in range(0,20):
  bin1.append(dataset[i])
print(bin1)
for i in range(20,40):
  bin2.append(dataset[i])
print(bin2)
for i in range(40,60):
  bin3.append(dataset[i])
print(bin3)
for i in range(60,80):
  bin4.append(dataset[i])
print(bin4)
for i in range(80,100):
  bin5.append(dataset[i])
print(bin5)
m1 = round((statistics.mean(bin1)))
m2 = round((statistics.mean(bin2)))
m3 = round((statistics.mean(bin3)))
m4 = round((statistics.mean(bin4)))
m5 = round((statistics.mean(bin5)))
print("Smoothing by bin means")
for i in range(20):
  mbin1.append(m1)
  mbin2.append(m2)
  mbin3.append(m3)
  mbin4.append(m4)
  mbin5.append(m5)
print(mbin1)
print(mbin2)
print(mbin3)
print(mbin4)
print(mbin5)
print("Smoothing by bin median")
M1 = round((statistics.median(bin1)))
M2 = round((statistics.median(bin2)))
M3 = round((statistics.median(bin3)))
M4 = round((statistics.median(bin4)))
M5 = round((statistics.median(bin5)))
for i in range(20):
  Mbin1.append(M1)
  Mbin2.append(M2)
  Mbin3.append(M3)
  Mbin4.append(M4)
  Mbin5.append(M5)
print(Mbin1)
print(Mbin2)
print(Mbin3)
print(Mbin4)
print(Mbin5)
print("Smoothing by bin boundary")
max1 = max(bin1)
min1 = min(bin1)
max2 = max(bin2)
min2 = min(bin2)
max3 = max(bin3)
min3 = min(bin3)
max4 = max(bin4)
min4 = min(bin4)
max5 = max(bin5)
min5 = min(bin5)

for i in range(20):
  if ( bin1[i]-min1 < max1 - bin1[i]):
    bin1[i] = min1
  else:
    bin1[i] = max1
  if ( bin2[i]-min2 < max2 - bin2[i]):
    bin2[i] = min2
  else:
    bin2[i] = max2
  if ( bin3[i]-min3 < max3 - bin3[i]):
    bin3[i] = min3
  else:
    bin3[i] = max3
  if ( bin4[i]-min4 < max4 - bin4[i]):
    bin4[i] = min4
  else:
    bin4[i] = max4
  if ( bin5[i]-min5 < max5 - bin5[i]):
    bin5[i] = min5
  else:
    bin5[i] = max5
    
print(bin1)
print(bin2)
print(bin3)
print(bin4)
print(bin5)

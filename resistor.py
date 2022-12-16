#Input color 
print("----------Input Color ----------")
bar1 = input("Enter Bar1: ")
bar2 = input("Enter Bar2: ")
bar3 = input("Enter Bar3: ")
bar4 = input("Enter Bar4: ")

#tier
tierI = [
    {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'purple':7,'gray':8,'white':9},
    {'black':1,'brown':10,'red':10**2,'orange':10**3,'yellow':10**4,'green':10**5,'blue':10**6,'purple':10**7,'gray':10**8,'white':10**9,'gold':10**-1,'silver':10**-2}
    ]


#resistor
resis = ( (tierI[0][bar1]*10) + tierI[0][bar2] ) * tierI[1][bar3]


#discrepancy
tierII = [
    {'brown':(0.01)*resis,'red':(0.02)*resis,'yellow':(0.05)*resis,'green':(0.005)*resis,'blue':(0.0025)*resis,'purple':(0.001)*resis,'gray':(0.0005)*resis,'gold':(0.05)*resis,'silver':(0.1)*resis,'non':(0.2)*resis},
    {'brown':'1%','red':'2%','yellow':'5%','green':'0.5%','blue':'0.25%','purple':'0.1%','gray':'0.05%','gold':'5%','silver':'10%','non':'20%'}
]


#result
result_1 = resis - tierII[0][bar4]
result_2 = resis + tierII[0][bar4]

print("Resistance value of the Resistor: ")
print('= ' + str(resis) + ' + ' + str(tierII[1][bar4]+' Ω'))

# 2200 + 2%
# 2.2k Ω
# result_1 Ω - result_2 Ω


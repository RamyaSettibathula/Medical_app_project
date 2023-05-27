#!/usr/bin/env python
# coding: utf-8

# # Medical App

# In[1]:


medicine = {
    1 : {"medicine1":"paracetomol", 'Quantity':10,'cost':10},
    
    2 : {"medicine2":"cetrizine", 'Quantity':10,'cost':10},
    
    3 : {"medicine3":"dolo 650", 'Quantity':15,'cost':20},
    
    4 : {"medicine4":"ceptas 200", 'Quantity':20,'cost':30},
    
    5 : {"medicine5":"eye drops", 'Quantity':5,'cost':65}}


# In[2]:


def patientdetails():
    print('Enter your details:')
    name = input('enter patient name: ')
    prob = input('enter patient problem/disease:')
    address = input('enter your address/area/location: ')
    distance = int(input('enter your distance from this hospital/medical store:'))
    return name,prob,address,distance


# In[3]:


def medicinelist():
    print('\n medicine available in this medical store')
    print('--------------------------------------------------------')
    print('%1s %20s %10s %10s' %('Sno','List of medicine','Quantity','Cost '))
    print('--------------------------------------------------------')
    print("%1s %15s %15d %10d"%('1',medicine[1]['medicine1'],medicine[1]['Quantity'],medicine[1]['cost']))
    print("%1s %15s %15d %10d"%('2',medicine[2]['medicine2'],medicine[2]['Quantity'],medicine[2]['cost']))
    print("%1s %15s %15d %10d"%('3',medicine[3]['medicine3'],medicine[3]['Quantity'],medicine[3]['cost']))    
    print("%1s %15s %15d %10d"%('4',medicine[4]['medicine4'],medicine[4]['Quantity'],medicine[4]['cost']))
    print("%1s %15s %15d %10d"%('5',medicine[5]['medicine5'],medicine[5]['Quantity'],medicine[5]['cost']))
    print('--------------------------------------------------------')
   


# In[4]:


def medicinerequire():
    print('enter the medicine according to doctor description below')
    p = int(input('\nHow many paracetomol tablets are you required?: '))
    ct = int(input('\nHow many cetrizine tablets are you required?: '))
    d = int(input('\nHow many dolo 650 tablets are you required?: '))
    c = int(input('\nHow many ceptas 200 tablets are you required?: '))
    e = int(input('\nHow many eye drop bottles are you required?: '))
    
    print('\n------------------MEDICAL BILL RECIEPT---------------------------------')
    print('patient Name:',name)
    print('Disease: ', prob)
    print('\n Delivery Address:',address)
    print('------------------------------------------------------------------------')
    print('Required medicine list')
    print('------------------------------------------------------------------------')
    print('%1s %15s %10s %10s %10s' %('\n Sno','List of medicine','Quantity','your Cost','stock available'))
    print('------------------------------------------------------------------------')
    print("%1s %10s %15d %10d %10d"%('1',medicine[1]['medicine1'],p,p*medicine[1]['cost'],10-p))
    print("%1s %10s %15d %10d %10d"%('2',medicine[2]['medicine2'],ct,ct*medicine[2]['cost'],10-ct))
    print("%1s %10s %15d %10d %10d"%('3',medicine[3]['medicine3'],d,d*medicine[3]['cost'],15-d))
    print("%1s %10s %15d %10d %10d"%('4',medicine[4]['medicine4'],c,c*medicine[4]['cost'],20-p))
    print("%1s %10s %15d %10d %10d"%('5',medicine[5]['medicine5'],e,e*medicine[5]['cost'],5-p))
    tcost = p*medicine[1]['cost'] + ct*medicine[2]['cost'] + d*medicine[3]['cost'] + c*medicine[4]['cost'] + e*medicine[5]['cost'] 
    print('------------------------------------------------------------------------')
    print()
    print('OVERALL MEDICAL BILL AMOUNT')
    return tcost
   


# In[5]:


def delivery(distance,tcost):
    if distance > 0 and distance <= 5:
        delivery_charge = 10
        final_cost = tcost + delivery_charge
       
    elif distance > 5 and distance <= 10:
        delivery_charge = 12
        final_cost = tcost + delivery_charge
        
    elif distance > 10 and distance <= 15:
        delivery_charge = 14
        final_cost = tcost + delivery_charge
        
    else:
        delivery_charge = 20
        final_cost = tcost + delivery_charge
    print('-----------------------------------------------------------------------')
    print('%20s %20s %20s ' %('Total cost','Delivery cost','Final cost'))
    print('-----------------------------------------------------------------------')
    print('%15d %15d %20d ' %(tcost,delivery_charge,final_cost))
    
    return final_cost    


# In[6]:


while True:
    name,prob,address,distance=patientdetails()
    medicinelist()
    tcost = medicinerequire()
    delivery(distance,tcost)
    choose = input("\n Do you need any other medicine (yes/no) ")
    if choose == 'no':
        print('\n---GET WELL SOON---')
        break
    else:
        continue


# In[7]:


medicine = {
    1 : {"medicine1":"paracetomol", 'Quantity':10,'cost':10},
    
    2 : {"medicine2":"cetrizine", 'Quantity':10,'cost':10},
    
    3 : {"medicine3":"dolo 650", 'Quantity':15,'cost':20},
    
    4 : {"medicine4":"ceptas 200", 'Quantity':20,'cost':30},
    
    5 : {"medicine5":"eye drops", 'Quantity':5,'cost':65}}
def patientdetails():
    print('Welcome to medical app')
    print('\n here all types of medicines available to cure your health problem')
    print('\n Enter your details:')
    name = input('enter patient name: ')
    prob = input('enter patient health problem:')
    address = input('enter your address/area/location: ')
    distance = int(input('enter your distance from the hospital/medical store:'))
    return name,prob,address,distance
def medicinelist():
    print('\n medicine available in this medical store')
    print('--------------------------------------------------------')
    print('%1s %20s %10s %10s' %('Sno','List of medicine','Quantity','Cost '))
    print('--------------------------------------------------------')
    print("%1s %15s %15d %10d"%('1',medicine[1]['medicine1'],medicine[1]['Quantity'],medicine[1]['cost']))
    print("%1s %15s %15d %10d"%('2',medicine[2]['medicine2'],medicine[2]['Quantity'],medicine[2]['cost']))
    print("%1s %15s %15d %10d"%('3',medicine[3]['medicine3'],medicine[3]['Quantity'],medicine[3]['cost']))    
    print("%1s %15s %15d %10d"%('4',medicine[4]['medicine4'],medicine[4]['Quantity'],medicine[4]['cost']))
    print("%1s %15s %15d %10d"%('5',medicine[5]['medicine5'],medicine[5]['Quantity'],medicine[5]['cost']))
    print('--------------------------------------------------------')
def medicinerequire():
    print('enter the medicine according to doctor description below')
    p = int(input('\nHow many paracetomol tablets are you required?: '))
    ct = int(input('\nHow many cetrizine tablets are you required?: '))
    d = int(input('\nHow many dolo 650 tablets are you required?: '))
    c = int(input('\nHow many ceptas 200 tablets are you required?: '))
    e = int(input('\nHow many eye drop bottles are you required?: '))
    print('\n These medicines cure your health problem')
    
    print('\n------------------MEDICAL BILL RECIEPT---------------------------------')
    print('patient Name:',name)
    print('\n Disease: ', prob)
    print('\n Delivery Address:',address)
    print('------------------------------------------------------------------------')
    print('Required medicine list')
    print('------------------------------------------------------------------------')
    print('%1s %20s %10s %10s %10s' %('\n Sno','List of medicine','Quantity','your Cost','stock available'))
    print('------------------------------------------------------------------------')
    print("%1s %15s %15d %10d %10d"%('1',medicine[1]['medicine1'],p,p*medicine[1]['cost'],10-p))
    print("%1s %15s %15d %10d %10d"%('2',medicine[2]['medicine2'],ct,ct*medicine[2]['cost'],10-ct))
    print("%1s %15s %15d %10d %10d"%('3',medicine[3]['medicine3'],d,d*medicine[3]['cost'],15-d))
    print("%1s %15s %15d %10d %10d"%('4',medicine[4]['medicine4'],c,c*medicine[4]['cost'],20-p))
    print("%1s %15s %15d %10d %10d"%('5',medicine[5]['medicine5'],e,e*medicine[5]['cost'],5-p))
    tcost = p*medicine[1]['cost'] + ct*medicine[2]['cost'] + d*medicine[3]['cost'] + c*medicine[4]['cost'] + e*medicine[5]['cost'] 
    print('------------------------------------------------------------------------')
    print()
    print('OVERALL MEDICAL BILL AMOUNT')
    return tcost
def delivery(distance,tcost):
    if distance > 0 and distance <= 5:
        delivery_charge = 10
        final_cost = tcost + delivery_charge
       
    elif distance > 5 and distance <= 10:
        delivery_charge = 12
        final_cost = tcost + delivery_charge
        
    elif distance > 10 and distance <= 15:
        delivery_charge = 14
        final_cost = tcost + delivery_charge
        
    else:
        delivery_charge = 20
        final_cost = tcost + delivery_charge
    print('-----------------------------------------------------------------------')
    print('%20s %20s %20s ' %('Total cost','Delivery cost','Final cost'))
    print('-----------------------------------------------------------------------')
    print('%15d %15d %20d ' %(tcost,delivery_charge,final_cost))
    
    return final_cost
while True:
    name,prob,address,distance=patientdetails()
    medicinelist()
    tcost = medicinerequire()
    delivery(distance,tcost)
    choose = input("\n Do you need any other medicine (yes/no) ")
    if choose == 'no':
        print('\n-----------------------GET WELL SOON------------------------')
        break
    else:
        continue


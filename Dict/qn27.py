#27. How do you nest dictionaries and access deeply nested values?
d={'Cars': 
   { 
      'name':"BYD", 
      'cost':"Rs 60 lakh", 
      'Tax':"Rs 40000/year" , 
      'showroom':{ 
          'city1':'Dhading', 
          'city2':'Kathmandu' 
      } 
   }, 
   'Bikes': 
   { 
      'name':"Cyclone", 
      'cost':"Rs 35 lakh", 
      'Tax':"Rs 33000/year" , 
      'showroom':{ 
          'city1':'Rasuwa', 
          'city2':'Kathmandu' 
      } 
   }, 
   } 
print(d['Bikes']['name']) 
print(d['Cars']['showroom']['city1']) 
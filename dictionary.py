# dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {'USA' : 'Washington',
            'United Kingdom' : 'London',
            'Norway' : 'Oslo',
            'Iceland' : 'Reykjavik'
          }

#print(capitals['Iceland'])
#print(capitals.get('Germany')) #to check if a key is inside the dic
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items()) #the entire dic

capitals.update({'Germany' : 'Berlin'})
capitals.update({'USA' : 'Las Vegas'})
capitals.pop('Iceland') #to remove that key
#capitals.popitem() #remove the last item
# capitals.clear() #to remove all

for key,value in capitals.items():
  print(key,value) #to print the entire dic
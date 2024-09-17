#You can put Lists as Tuple elements and the other way around
city_1 = ('London', 'UK', 8.98)
city_2 = ('Mosocw', 'Russia', 13.01)
city_3 = ('Bangkok', 'Thailand', 10.53)
capitals = [('London', 'UK', 8.98),('Mosocw', 'Russia', 13.01), ('Bangkok', 'Thailand', 10.53)]
for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2]) 

#Lists in Tuples
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
print(user_data[3]) #In other versions of Python I could use only this without print
user_data[3].append (79.6)
print(user_data)
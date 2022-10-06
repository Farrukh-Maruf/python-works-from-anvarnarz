lists={'uzbekistan':'Tashkent',
       'Korea':'Seoul',
       'Japan':'Tokio',
       'USA':'New York',
       'UK':'London'
       }
print('Countries: ')
for country in sorted(lists):
    print(country.upper())
print('\nCapitals: ') 
for country in sorted(lists.values()):
    print(country.title())
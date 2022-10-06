words={'string':"words",
       "integer":"numbers",
       'float':'any number',
       'if':"agar",
       "else":'next one'       
       }
ask=input('Please, ask any words related to python:\n>>>').lower()
translate=words.get(ask)
if translate== None:
    print("there is words like this")
else:
    print(f'{ask.title()} word translate like>>>{translate}')
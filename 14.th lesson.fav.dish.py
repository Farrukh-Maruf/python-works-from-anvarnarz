words={'string':"words",
       "integer":"numbers",
       'float':'any number',
       'if':"agar",
       "else":'next one'       
       }
ask=input('Please, ask any words related to python:\n>>>')
print(words.get(ask,"there is no definition for this word(("))
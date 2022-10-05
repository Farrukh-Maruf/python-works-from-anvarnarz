products=['apple','banana','peach','kiwi','tomato','mango','melon']
bucket=[]
for n in range(5):
    bucket.append(input(f'add {n+1} item in the bucket: '))
items=[]
no_items=[]
for item in bucket:
    if item in products:
        items.append(item)
    else:
        no_items.append(item)
if no_items:
    print("we have these items: ")
    for item in no_items:
        print(item)
else:
   print("we have all products")        

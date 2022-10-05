products=['apple','banana','peach','kiwi','tomato']
bucket=[]
for n in range(5):
    bucket.append(input(f'add {n+1} item in the bucket: '))
for item in bucket:
    if item in products:
        print(f"we have {item}")
    else: print(f"there is no {item}")
usernames=['lola','bola','jack','backi','poul']
newcomers=input("please, choose a login name: ")
if newcomers.lower() in usernames:
    print("login band")
else:
    print(f'hush kelibsz,{newcomers.title()} ')
word = "Donkey"

with open ("file.txt","r") as f:
    content = f.read()

ContentNew = content.replace(word,"######")

with open ("file.txt","w") as f:
    content = f.write(ContentNew)
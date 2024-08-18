with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("The content is matched. same content")
else:
    print("The content is Not matched. different content")


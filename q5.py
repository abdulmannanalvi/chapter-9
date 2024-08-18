word = ["Donkey King", "movie", "Cartoon"]
replacement = ["Glass Door", "Pak movie", "Cartoon_real life story"]

with open("file_q5.txt", "r") as f:
    content = f.read()

for w, r in zip(word, replacement):
    content = content.replace(w, r)

with open("file_q5.txt", "w") as f:
    f.write(content)

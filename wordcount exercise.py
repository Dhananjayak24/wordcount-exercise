# we are opening txt file by with function so that we dont need to close file every time.
# we also mentioned encoding so that charmap error won"t show up.
with open("wordcount.txt","r", encoding="utf-8") as file :
    file=file.read()
#for counting we split the words at space " ".
    file=file.split(" ")
#count total words by len function.
    print(len(file))

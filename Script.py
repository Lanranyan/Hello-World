text = " In the dark, cold night, comes the phantoms of the night. They lurk around the corners of alleys and their " \
        "agility is quicker than the mind. Once followed, begins an endless chase  "
print(text)
changes = {'dark': 'light','comes':'arrives','mind':'wits'}

list_text = text.split()
new_list = []
for word in list_text:
    translation = changes.get(word)
    new_list.append(translation if  )
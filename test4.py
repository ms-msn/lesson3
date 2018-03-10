c = "{type=Point, coordinates=[37.48725773, 55.56213474]}"
print(type(c))
c = c.replace('{type=Point, coordinates=[', '').replace(']}', '').replace(' ', '')
c = c.split(',')
c 
print(c)
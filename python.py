from os import sep


with open('/Users/baaghi/Desktop/neer world/whatsapp problem/output3.html','w') as s,open('/Users/baaghi/Desktop/neer world/whatsapp problem/numbers.txt','r') as o:
    lines = []
    lin = o.readlines()
    lines.append(str(lin))
    for i in range(len(lines)):
        lines[i]=lines[i].replace('\\n','')
        lines[i]=lines[i].replace("'","")
        print(''.join(lines))
    for i in lines:
      #s.write(f'<a target="blank"href={"https://api.whatsapp.com/send/?phone=91"+lines+"&text=Namasteji"} >'+lines+'</a>'+' ')
      print(int(lines[i]))
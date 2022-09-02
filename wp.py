with open('/Users/baaghi/Desktop/neer world/whatsapp problem/numbers.txt','r') as o, open('/Users/baaghi/Desktop/neer world/whatsapp problem/array.txt','r') as p:
    lines = o.readlines()
    py = p.readline()
    for lines in lines:
        p.write(f'<a target="blank"href={"https://api.whatsapp.com/send/?phone=91"+lines+"&text=namasteji"} >'+lines+'</a>')
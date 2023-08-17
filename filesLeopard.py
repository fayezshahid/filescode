import pandas as pd
from datetime import datetime
import re
from allcities import cities
import spacy

date = input("Enter date: ")
flag = 0
dates = []
if 'r ' in date:
    flag = 1
    dates = date.split(',')
    if dates:
        dates[0] = dates[0].replace('r ', '')
    else:
        dates.append(date.replace('r ', ''))

b = ["DE FORELS", "NAME LIST", "JEWELLERY HUB", "DA ELODEAA"]

if 'w ' in date or 'p ' in date or 'r ' in date:
    brands = ["DE FORELS"]
elif 'j ' in date:
    brands = ["BRANDED JEWELERY"]
elif 'f ' in date:
    brands = ['FLOIR']
else:
    brands = []
    s = int(input('\nEnter sequence: '))
    seq = []

    while s != 0:
        seq.append(s%10)
        s = int(s / 10)

    seq.reverse()

    for x in seq:
        brands.append(b[int(x-1)])


print("\nEnter orders below: ")

data = []

if 'w ' in date or 'r ' in date or 'j ' in date:
    data.append('https')

while True:
    inp = input()
    data.append(inp)
    if inp == "quit":
        break

# if 'w ' in date or 'r ' in date or 'j ' in date:
#     c = 0
#     while c < len(data):
#         if not data[c] and not data[c + 1]:
#             data[c + 1] = 'https'
#             while not data[c]:
#                 c = c + 1
#         elif 'xxx' in data[c].lower():
#             data[c] = ''
#         c += 1

if 'j ' in date or 'r ' in date or 'w ' in date:
    c = 0
    while c < len(data):
        if not data[c]:
            data[c] = 'https'
            while not data[c+1]:
                c = c + 1
        c = c + 1

table1 = []

a = 0
k = 0
adr = ""
nmb = ""
cod = ""
ins = ""
name = ""
tmp = ""
dest = ""

i = 0
j = 0

today = date + " " + datetime.now().strftime('%h')

c = cities.filter(country_code='PK')
cities = []
for city in c:
    if city.name != 'Chak':
        cities.append(city.name)
cities.extend(['Attock', 'Umerkot', 'Sheikhupura', 'Wah Cantt', 'Kamoki', 'Muzaffarabad', 'Pirmahal', 'Balakot', 'Mirpurkhas',
               'Daska', 'Jhang', 'Taxila'])

replace_city = {'Kotli': 'Kotli (a. k)', 'Muzaffarabad': 'Muzaffarabad(ak)', 'Swat': 'Mingora (SWAT)', 'Timargara': 'Tamirgaraha',
                'Mingora': 'Mingora (SWAT)', 'Mirpur': 'Mirpur (a. k)', 'Nawabshah': 'Nawab Shah', 'Kamoke': 'Kamoki', 'Karak': 'Kark',
                'Toba Tek Singh': 'Toba Tek Sing','Lakki': 'Lakki Marwat', 'Taunsa': 'Taunsa Sharif', 'Mirpurkhas': 'Mirpur Khas',
                'Gwadar': 'Gawadar', 'Dera Murad Jamali': 'Dera Murad Jama', 'Panjgur': 'Panjgour', 'Sobhodero': 'Sobho dero',
                'Tando Muhammad Khan': 'Tando Mohd.Khan', 'Sharqpur Sharif': 'Sharaqpur Shari', 'Thal': 'Thull', 'Nasirabad': 'Gilgit',
                'Battagram': 'Batgram', 'Thatta': 'Thatha', 'Kalabagh': 'Kala Bagh', 'Matiari': 'Matiyari', 'Jauharabad': 'Jauhrabad',
                'Mirwah Gorchani': 'Mirpur Khas', 'Bagh': 'Bagh (a.k.)', 'Renala Khurd': 'RenalaKhurd', 'Kashmor': 'Kashmoor',
                'Tando Allahyar': 'Tando ala yar', 'Jalalpur Jattan': 'Jalal Pur Jattan', 'Chichawatni': 'Chicha watni',
                'Umerkot': 'Umer kot', 'Shakargarh': 'Shakar garh', 'Shahdadpur': 'Shadadpur'}

while i < (len(data)):

    if data[i] == "quit":
        break

    if "http" in data[i - 1] or 'http' in data[i]:  # daily_files
        if 'http' in data[i]:
            i += 1
        if "YmMyMTA2M2Y" in data[i] or 'YmyMTA2M2Y' in data[i]:
            i += 1
        j = i
        name = data[i]
    elif 'Rafay Files' in data[i - 1] or i == 0:  # pending_files
        if i == 0:
            i += 1
        pattern = 'Rafay Files: (.*)'
        try:
            name = re.findall(pattern, data[i - 1])[0]
            adr += name + ' '
            data[i - 1] = name
        except:
            name = ''
        j = i - 1

    # if ("karachi" in data[i].lower() or "malir" in data[i].lower() or "korangi" in data[i].lower()) \
    #         and 'j ' not in date and 'f ' not in date and 'p ' not in date:
    if 0:
        f = open(rf"C:\Users\USER\Desktop\Karachi Files\k {today}.txt", "a")

        i = j
        while not ("quit" in data[i] or "http" in data[i]):
            if "Rafay Files" in data[i]:
                # j = i + 1
                break
            elif data[i] != "":
                try:
                    f.write(data[i] + "\n")
                except:
                    pass
            i += 1

        f.write("\n\n" + brands[k] + " " + date +
                "\n--------------------------------------------------------------------"
                "-----------------------------------------------------------------\n\n")
        f.close()

        if "de forels" in data[i].lower() or "name list" in data[i].lower() or "jewellery hub" in data[i].lower() or \
                "da elodeaa" in data[i].lower():
            k += 1
            # table1.append("")

        adr = ""
        nmb = ""
        cod = ""
        ins = ""
        name = ""
        tmp = ""
        dest = ""

    elif ("address" in data[i].lower() or "store" in data[i].lower() or "house" in data[i].lower() or "street" in data[
        i].lower() or "city" in data[i].lower() or "road" in data[i].lower() or "pakistan" in data[
              i].lower() or "hotel" in data[i].lower() or "bus stop" in data[i].lower() or "colony" in data[
              i].lower() or "college" in data[i].lower() or "center" in data[i].lower() or "gali" in data[
              i].lower() or "near" in data[i].lower() or "town" in data[i].lower() or "pump" in data[
              i].lower() or "tehsil" in data[i].lower() or "district" in data[i].lower() or "hospital" in data[
              i].lower() or "home" in data[i].lower() or "hostel" in data[i].lower()):
        adr += data[i] + " "

    elif ("cod" in data[i].lower() and "code" not in data[i].lower()) or (
            "tot" in data[i].lower() and "totala" not in data[i].lower()
            ) or 'cood' in data[i].lower() or 'cid' in data[i].lower() or 'c0d' in data[i].lower():
        cod = ""
        c = str(data[i])

        for x in c:
            if x.isdigit():
                cod = cod + x

        a = 0
        i = i + 1
        ins = ""
        while not ("quit" in data[i] or "https" in data[i]):
            if "Rafay Files" in data[i]:
                # j = i + 1
                # i += 1
                break
            elif data[i] != "":
                ins = ins + str(data[i]) + " "
            i = i + 1

        if not nmb.strip() and adr:
            for x in range(len(adr)):
                if (adr[x] == '0' and adr[x + 1] == '3') or (adr[x] == 'O' and adr[x + 1] == '3'):
                    tmpStr = ''
                    for m in range(x, len(adr)):
                        if adr[m].isdigit():
                            tmpStr += adr[m]
                    if len(tmpStr) >= 11:
                        nmb = tmpStr[:11]
                    break
                    # y = 0
                    # while y < 11:
                    #     if adr[x].isdigit():
                    #         nmb += adr[x]
                    #         y += 1
                    #     x += 1
                    # break
                elif adr[x] == '9' and adr[x + 1] == '2':
                    tmpStr = ''
                    for m in range(x, len(adr)):
                        if adr[m].isdigit():
                            tmpStr += adr[m]
                    if len(tmpStr) >= 12:
                        nmb = tmpStr[2:12]
                    break
                    # y = 0
                    # while y < 12:
                    #     if adr[x].isdigit():
                    #         nmb += adr[x]
                    #         y += 1
                    #     x += 1
                    # break

        if len(name) > 64 or not name:
            if len(ins) <= 64:
                name = ins
            else:
                name = nmb

        try:
            nmb = int(nmb)
        except:
            pass

        # cod = int(cod)

        try:
            cod = int(cod)
        except:
            # print(data[i - 5])
            print(name)
            quit()

        for city in cities:
            if city.lower() in adr.lower():
                dest = city

        dest = replace_city.get(dest, dest)

        if 'send details to confirm your order:' in adr.lower() or 'for order confirmation send the details mentioned below:' in adr.lower():
            adr = adr.replace('Send details to confirm your order:', '')
            adr = adr.replace('For Order Confirmation send the details Mentioned below: ', '')
            adr = adr.replace('Alternate phone number (if any)', 'Alternate: ')

        # if not dest:
        #     nlp = spacy.load('CityClassification/model/model-best')
        #     doc = nlp(adr)
        #     city = max(doc.cats, key=lambda k: doc.cats[k])
        #     dest = city

        if 'j ' in date:
            t = [brands[k] + date.replace('j', ''), '', '', '', 'karachi', name, '', nmb, adr, dest, cod, '', ins, 500,
                'overnight', 1, '', '']
        elif 'f ' in date:
            t = [brands[k] + date.replace('f', ''), '', '', '', 'karachi', name, '', nmb, adr, dest, cod, '', ins, 500,
                'overnight', 1, '', '']
        else:
            if not flag:
                t = [brands[k] + " " + date, '', '', '', 'karachi', name, '', nmb, adr, dest, cod, '', ins, 500,
                    'overnight', 1, '', '']
            else:
                t = ["DE FORELS r " + dates[k], '', '', '', 'karachi', name, '', nmb, adr, dest, cod, '', ins, 500,
                    'overnight', 1, '', '']

        table1.append(t)

        adr = ""
        nmb = ""
        cod = ""
        ins = ""
        name = ""
        tmp = ""
        dest = ""

        if dates and 'Rafay Files: ' + dates[k] in data[i]:  # return_files
            k += 1
            i += 2
            # table1.append("")
        else:  # daily_files
            for x in brands:
                if x.lower() in data[i].lower():
                    k += 1
                    # table1.append("")
                    break

    elif "name" in data[i].lower() or "receiver" in data[i].lower():
        name = data[i]
        adr += data[i] + " "

    elif "phone" in data[i].lower() or "alter" in data[i] or "03" in data[i] or "O3" in data[i] or "923" in data[i]:
        adr += data[i] + ' '
        a = a + 1
        n = str(data[i]).replace(' ', '')
        if not nmb:
            for x in range(len(n)):
                if (n[x] == '0' and n[x + 1] == '3') or (n[x] == 'O' and n[x + 1] == '3'):
                    tmpStr = ''
                    for m in range(x, len(data[i])):
                        if data[i][m].isdigit():
                            tmpStr += data[i][m]
                    if len(tmpStr) >= 11:
                        nmb = tmpStr[:11]
                    break

                    # nmbCount = 0
                    # while nmbCount < 11:
                    #     if n[x].isdigit():
                    #         nmb += n[x]
                    #         nmbCount += 1
                    #     x += 1
                    # break
                elif n[x] == '9' and n[x + 1] == '2' and n[x + 2] == '3':
                    tmpStr = ''
                    for m in range(x, len(data[i])):
                        if data[i][m].isdigit():
                            tmpStr += data[i][m]
                    if len(tmpStr) >= 12:
                        nmb = tmpStr[2:12]
                    break
                    # nmbCount = 0
                    # while nmbCount < 12:
                    #     if n[x].isdigit():
                    #         nmb += n[x]
                    #         nmbCount += 1
                    #     x += 1
                    # break

    else:
        if not (data[i] == ""):
            adr += data[i] + " "

    i += 1


df = pd.DataFrame(table1,
                  columns=['shipperName', 'shipperPhone', 'shipperAddress', 'shipperEmail',
                           'Origin City Name', 'consigneeName', 'consigneeEmail', 'consigneePhone', 'consigneeAddress',
                           'Destination CityName', 'bookedPacketCollectAmount', 'bookedpacketorderid', 'ProductDescription',
                           'bookedPacketWeight', 'shipment_type', 'numberOfPieces', 'return_city', 'return_address'])
if 'j ' in date:
    df.to_excel(rf'C:\Users\USER\Desktop\Branded Jewellery Excel Files\{today}.xlsx', index=False)
elif 'f ' in date:
    df.to_excel(rf'C:\Users\USER\Desktop\Floir Excel Files\{today}.xlsx', index=False)
elif 'w ' in date:
    df.to_excel(rf'C:\Users\USER\Desktop\Whatsapp Excel Files\{today}.xlsx', index=False)
else:
    df.to_excel(rf'C:\\Users\USER\Desktop\Excel Files\{today}.xlsx', index=False)

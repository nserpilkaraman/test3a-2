import json

n = {"id": 27,
    "name": "neriman",
    "sehir": "istanbul"
    }


with open('info.json', 'r+', encoding="utf-8") as dosya:
    veri = json.load(dosya)
    # veri["info"].append(n)
    # dosya.seek(0)
    # json.dump(veri, dosya, indent=4)
    # print("Verimiz kayıt edildi")

aranan_id = 267
yeni_name = "serpil nur"

for ticket in veri.get("info", []):
    if ticket.get("id") == aranan_id:
        print("İstenilen veri bulundu!")
        ticket["name"] = yeni_name
        with open('info.json', 'w', encoding="utf-8") as dosya:
            json.dump(veri, dosya, ensure_ascii=False, indent=2)
            print(f"Datadaki {aranan_id} id'sine sahip verinin (name) değişkeni {yeni_name} olarak güncellendi")
        break 
else:
    print("istenilen id'ye sahip veri bulunamadı")
        
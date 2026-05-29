import requests
# כתובת ה-API של פוקימון - API ציבורי ופתוח לכולם
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
# url = "https://pokeapi.co/api/v2/pokemon/blahblah"

# שולחים בקשת GET לשרת
response = requests.get(url)

# בודקים שהשרת ענה בהצלחה (קוד 200 = הכל טוב!)
if response.status_code == 200:
    print("✅ הצלחנו! קיבלנו תשובה מהשרת")
    print("קוד סטטוס:", response.status_code)
    
    # ממירים את התשובה ל-Dictionary של Python
    data = response.json()
    
    # שולפים מידע ספציפי
    print("שם:", data["name"])
    print("משקל:", data["weight"])
    print("גובה:", data["height"])
    
else:
    print("❌ משהו השתבש. קוד שגיאה:", response.status_code)

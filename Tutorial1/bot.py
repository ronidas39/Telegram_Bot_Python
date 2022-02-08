import requests

url="https://api.telegram.org/bot5263771325:AAGUKqXXupsyQL-KsMWghgOLEjuTbVlg3eM/sendMessage?chat_id=-1001617343156&text="
for i in range(0,10):
    requests.get(url+"messgeid:"+str(i))
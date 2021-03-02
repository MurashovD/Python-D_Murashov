import requests
from datetime import datetime


def currency_rates(code):
    content = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    if code == "":
        return
    r = content.text[content.text.find(">" + code + "<"):]
    r = r[r.find("<Value>"):r.find("</Value>")]
    r = r[len("<Value>"):]
    date = content.text[content.text.find("Date="):]
    date = date[6:16].split(".")
    date_t = datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]))
    if r == "":
        return "Введите корректный код валюты."
    return code, date_t, r


r1, r2, r3 = currency_rates("USD")
print("Курс валюты({}) на {}: {}".format(r1, r2, r3))

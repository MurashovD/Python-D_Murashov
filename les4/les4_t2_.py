import requests


def currency_rates(code):
    if code == "":
        return
    content = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    r = content.text[content.text.find(">"+code+"<"):]
    r = r[r.find("<Value>"):r.find("</Value>")]
    r = r[len("<Value>"):]
    if r == "":
        return "Введите корректный код валюты."
    return code, r


r1, r2 = currency_rates("USD")
print("Курс валюты({}): {}".format(r1, r2))

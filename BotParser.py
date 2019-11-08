import csv
import telebot
import ParserTest
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

raspisaniye = []

def parse(html):
    soup = BeautifulSoup(html,'html.parser')



    predm = soup.find_all('td',id='predm')

    rowInt=0

    for row in soup.find_all('td',id='group')[7:]:
        group = row.text
        pr1 = predm[rowInt].text
        pr2 = predm[rowInt+1].text
        pr3 = predm[rowInt+2].text
        pr4 = predm[rowInt+3].text
        pr5 = predm[rowInt+4].text

        raspisaniye.append ({
            'group':"Группа:"+group+"|",
            'pr1':"0. "+pr1+"|",
            'pr2':"1. "+pr2+"|",
            'pr3':"2. "+pr3+"|",
            'pr4':"3. "+pr4+"|",
            'pr5':"4. "+pr5
        })

        rowInt += 5
	print(raspisaniye)

bot = telebot.TeleBot("1048261255:AAGzkKbwSSwRiqaww2cEOrYXB3oNejtnrV4")

raspis = {}
  

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет , напиши мне номер группы что-бы посмотреть актуальное расписание(взято с сайта kre.dp.ua)")

@bot.message_handler(commands=['update'])
def ResloaDAct(message):
    parse(get_html("https://www.kre.dp.ua/education-process/timetable"))
    bot.reply_to(message, "Updated")


@bot.message_handler(content_types = ["text"])
def send_raspisanye(message):
  answInt = 0
  try:
    if int(message.text) == 50:
      answInt=12
    elif int(message.text) == 51:
      answInt=1
    elif int(message.text) == 52:
      answInt=2
    elif int(message.text) == 53:
      answInt=3
    elif int(message.text) == 54:
      answInt=4
    elif int(message.text) == 55:
      answInt=5
    elif int(message.text) == 56:
      answInt=6
    elif int(message.text) == 45:
      answInt=7
    elif int(message.text) == 46:
      answInt=8
    elif int(message.text) == 47:
      answInt=9
    elif int(message.text) == 48:
      answInt=10
    elif int(message.text) == 49:
      answInt=11
    elif int(message.text) == 38:
      answInt=13
    elif int(message.text) == 39:
      answInt=14
    elif int(message.text) == 41:
      answInt=15
    elif int(message.text) == 42:
      answInt=16
    elif int(message.text) == 44:
      answInt=17
    elif int(message.text) == 32:
      answInt=18
    elif int(message.text) == 33:
      answInt=19
    elif int(message.text) == 36:
      answInt=20
    elif int(message.text) == 37:
      answInt=21
    else:
      exit
    answ4 = str(raspisaniye[answInt-1]).replace("\'", "")
    answ3 = answ4.replace(",","\n")
    answ2 = answ3.replace("[","")
    answ = answ2.replace("]","")
    print(message.text + " " + message.chat.first_name)
    bot.reply_to(message,answ)
  except:
    answ = "Error"
    bot.reply_to(message,answ)

bot.polling()
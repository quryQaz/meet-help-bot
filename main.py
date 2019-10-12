from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import random

TG_TOKEN = "798290356:AAFbCMlWoqeXIlWg7pw1N4CpSWt7roMwI4s"
TG_API_URL = "https://telegg.ru/orig/bot"



Ans=['Выпить по стопке острого соуса'
,'Вдвоем выпить по стопке текилы и рассказать свою самую пьяную историю'
,'Накормить друг друга тортом с завязанными глазами'
,'Поменять аватар в любой соцсети на совместное фото с напарником '
,'По очереди позвонить маме и сказать, что ждешь ребенка '
,'Спеть караоке без музыки под аккомпанемент напарника '
,'Целоваться в течение минуты '
,'Посмотреть вместе порно '
,'Обклеить напарнику все лицо скотчем' 
,'Удалить у напарника 10 первых друзей из вк' 
,'Укусить друг друга за ягодицу '
,'Объявить о помолвке в интаграм и не удалять пост до завтра'
,'Оставить друг другу засос '
,'Рассосать один чупа-чупс на двоих'
,'Выпить 300 гр коньяка на двоих' 
,'Нарисовать мускулы на торсе напарника']
global rnd1,rnd2,rnd3,rnd4
rnd1=rnd2=rnd3=rnd4=False
global rnd1End,rnd2End,rnd3End,rnd4End
rnd1End=rnd2End=rnd3End=rnd4End=False
global IsGameStart
IsGameStart = False

global DelCom
DelCom=[]



def do_start(bot,update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Для начала игры напишите Start и действуйте согасно инструкциям в задании\n",
    )

def do_echo(bot,update):
    text=update.message.text
    global numbOfChoise
    global rnd1,rnd2,rnd3,rnd4
    global rnd1End,rnd2End,rnd3End,rnd4End
    global DelCom
    global Com

    global IsGameStart
    
    if (text=="start" or text == "Start") and rnd1!=True:
        print('Start')
        StartGame(bot,update)
        IsGameStart=True
    elif (text=="exit" or text=="Exit") and IsGameStart:
        IsGameStart=False
        rnd1=rnd2=rnd3=rnd4=False
        rnd1End=rnd2End=rnd3End=rnd4End=False
        DelCom=[]
        Com=[]
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Игра завершена, для начала введите Start\n"+
        "Помощь - help")
    elif text=="help":   
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Для начала игры напишите Start и действуйте согасно инструкциям в задании\n"+
        "Чтобы прервать игру напишите Exit")
    elif text.isdigit() and len(Com)!=1:
        if int(text)==0 and (rnd1 or rnd2 or rnd3):
                bot.send_message(
                chat_id=update.message.chat_id,
                text="Введите номер задания, которое хотите исключить!")
            
        if(int(text)<0 or int(text)>len(Com)) and (rnd1 or rnd2 or rnd3):
                bot.send_message(
                chat_id=update.message.chat_id,
                text="Введите номер задания, которое хотите исключить!")
        elif(text=='1' or text=='2' or text=='3' or text=='4' or text=='5') and rnd4:
                if(int(text)<0 or int(text)>len(DelCom)):
                    bot.send_message(
                    chat_id=update.message.chat_id,
                    text="Введите номер задания, которое хотите исключить!")
                else:
                    print("RND4 post")
                    Raund4(int(text),bot,update)
        else:
            if(text=='1' or text=='2' or text=='3' or text=='4' or text=='5') and rnd1:
                Raund1(int(text),bot,update)
            elif(text=='1' or text=='2' or text=='3' or text=='4' or text=='5') and rnd2:
                Raund2(int(text),bot,update)
            elif(text=='1' or text=='2' or text=='3' or text=='4' or text=='5') and rnd3:
                print("RND3 post")
                print(rnd1)
                Raund3(int(text),bot,update)
        
    elif (text=="Готово" or text=="готово") and rnd1End:
        print("Rnd1End1")
        StartRnd2(bot,update)
    elif (text=="Готово" or text=="готово") and rnd2End:
            print("Rnd2End2")
            StartRnd3(bot,update)
    elif (text=="Готово" or text=="готово") and rnd3End:
        StartRnd4(bot,update)
    elif (text=="Готово" or text=="готово") and rnd4End:
        IsGameStart=False
        rnd1=rnd2=rnd3=rnd4=False
        rnd1End=rnd2End=rnd3End=rnd4End=False
        DelCom=[]
        Com=[]
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Отлично!!!\nВы выполнили все задания, чтобы начать снова напишите Start\n"+
        "Помощь - help")
    else:
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Try help")
        print(rnd1)
        
    
    
    #bot.send_message(
    #    chat_id=update.message.chat_id,
    #    text=text,
    #)



def main():
    print("OK")
    bot=Bot(token=TG_TOKEN, base_url=TG_API_URL)
    updater=Updater(bot=bot,)


    start_handler = CommandHandler("start",do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    message_handler2 = MessageHandler(Filters.text, StartGame)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(message_handler2)

    updater.start_polling()
    updater.idle()


def qwe(bot,update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="123")


def StartGame(bot,update):
    global TMP
    global rnd1
    rnd1=True
    TMP=Ans.copy()
    bot.send_message(
    chat_id=update.message.chat_id,
    text="Игра началась \n\n-----Раунд 1-----")
    RandAns()
    bot.send_message(
    chat_id=update.message.chat_id,
    text=("Выберите задание, которое хотите исключить: \n1. "+
    Com[0]+"\n2. "+
    Com[1]+"\n3. "+
    Com[2]+"\n4. "+
    Com[3]+"\n5. "+
    Com[4]+"\n"
    ))

        
def RandAns():
    AnsTMP=TMP.copy()
    global Com
    global DelCom
    Com=[]
    for i in range(5):
        num=random.randint(0,len(TMP)-1)
        k=random.randint(0,10)
        if len(DelCom)<5 and k<5:
            DelCom.append(AnsTMP[num])
        Com.append(AnsTMP[num])
        AnsTMP.pop(num)
        TMP.pop(num)
    


def Raund1(n,bot,update):
    global rnd1End
    if len(Com)==2:
        rnd1End=True
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Отлично, выполняйте оставшееся задание: \n\n"+
        Com[0]+"\n\nКак закончите напишите Готово")
        
    else:
        Com.pop(n-1)
        res = ""
        for i in range(len(Com)):
            res+=str(i+1)+". "+Com[i]+'\n'
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Хорошо, выберите следующее задание, которое хотите исключить: \n"+res)
    

def StartRnd2(bot,update):
    global rnd1,rnd2
    rnd1=False
    rnd2=True
    print('Start2')
    bot.send_message(
    chat_id=update.message.chat_id,
    text="Игра началась \n\n-----Раунд 2-----")
    RandAns()
    bot.send_message(
    chat_id=update.message.chat_id,
    text=("Выберите задание, которое хотите исключить: \n1. "+
    Com[0]+"\n2. "+
    Com[1]+"\n3. "+
    Com[2]+"\n4. "+
    Com[3]+"\n5. "+
    Com[4]+"\n"
    ))

def Raund2(n,bot,update):
    global rnd1End,rnd2End
    print(len(Com))
    if len(Com)==2:
        rnd1End=False
        rnd2End=True
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Отлично, выполняйте оставшееся задание: \n\n"+
        Com[0]+"\n\nКак закончите напишите Готово")
        print("Change-----------------------------------")
        
    else:
        Com.pop(n-1)
        res = ""
        for i in range(len(Com)):
            res+=str(i+1)+". "+Com[i]+'\n'
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Хорошо, выберите следующее задание, которое хотите исключить: \n"+res)




def StartRnd3(bot,update):
    global rnd2,rnd3
    rnd2=False
    rnd3=True
    print('Start3')
    bot.send_message(
    chat_id=update.message.chat_id,
    text="Игра началась \n\n-----Раунд 3-----")
    RandAns()
    bot.send_message(
    chat_id=update.message.chat_id,
    text=("Выберите задание, которое хотите исключить: \n1. "+
    Com[0]+"\n2. "+
    Com[1]+"\n3. "+
    Com[2]+"\n4. "+
    Com[3]+"\n5. "+
    Com[4]+"\n"
    ))

def Raund3(n,bot,update):
    global rnd2End,rnd3End
    print("GET rnd3")
    if len(Com)==2:
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Отлично, выполняйте оставшееся задание: \n\n"+
        Com[0]+"\n\nКак закончите напишите Готово")
        rnd2End=False
        rnd3End=True
        
    else:
        print("Com --")
        print(len(Com))
        if len(DelCom)<5:
            DelCom.append(Com[n-1])
        Com.pop(n-1)
        res = ""
        for i in range(len(Com)):
            res+=str(i+1)+". "+Com[i]+'\n'
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Хорошо, выберите следующее задание, которое хотите исключить: \n"+res)



def StartRnd4(bot,update):
    global rnd3,rnd4,DelCom
    rnd3=False
    rnd4=True
    print('Start4')
    bot.send_message(
    chat_id=update.message.chat_id,
    text="Игра началась \n\n-----Раунд 4-----")
    bot.send_message(
    chat_id=update.message.chat_id,
    text=("Выберите задание, которое хотите исключить: \n1. "+
    DelCom[0]+"\n2. "+
    DelCom[1]+"\n3. "+
    DelCom[2]+"\n4. "+
    DelCom[3]+"\n5. "+
    DelCom[4]+"\n"
    ))

def Raund4(n,bot,update):
    global rnd3End,rnd4End,DelCom
    print("GET rnd4")
    if len(DelCom)==2:
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Отлично, выполняйте оставшееся задание: \n\n"+
        Com[0]+"\n\nКак закончите напишите Готово")
        rnd3End=False
        rnd4End=True
        
    else:
        DelCom.pop(n-1)
        res = ""
        for i in range(len(DelCom)):
            res+=str(i+1)+". "+DelCom[i]+'\n'
        bot.send_message(
        chat_id=update.message.chat_id,
        text="Хорошо, выберите следующее задание, которое хотите исключить: \n"+res)




if __name__ == '__main__':
    main()
    

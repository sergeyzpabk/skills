import random

user = 'Сергей Спокойный'
text = "{hello}, {username}{emj1} {buy} был успешно оплачен. {time} вы сможете его забрать. Мы вам {send}"
key = {}
key_text = """
hello=Добрый день
hello=Здравствуйте
hello=Доброго времени суток
hello=Приветсвую вас
hello=Рада вам сообщить
emj1=)
emj1=!
emj1=.
emj1=😊
emj1=🙂
emj1=☺️
emj1=😊
buy=Ваш заказ
buy=Ваш товар
time=В ближайшее время 
time=В ближайшие дни 
time=Через пару дней
send=сообщим
send=напишем
send=напомним
""".split('\n')

def gen_text(text:str,key_text) -> str:
    for k in key_text:
        if  k.find('=') != -1:
            _t = k[:k.find('=')]
            t_ = k[k.find('=')+1:]

            if _t in key:
                key[_t].append(t_)
            if not _t in key:
                key.update({_t: [t_]})

    for k in key:
        kk = '{'+k+'}'

        while text.find(kk) != -1:
            rand_text = random.choice( key[k] )
            #print(rand_text)
            text = text.replace(kk,rand_text)

    return text


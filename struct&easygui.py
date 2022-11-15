from art import tprint
import easygui

#Напишите функцию, которая будет выводить на экран имя, номера квартиры и дома, 
#названия улицы и города, почтовый индекс и название страны. 
Home_BTC =  {
    "name" : '',
    "home_number" : int(-1),
    "name_street" : '',
    "name_city" : '',
    "poshtovyi_index" : int(-1),
    "name_country" : ''
}

count = int(input('Кількість осіб:'))

print('mas')
mas_1 = ['']
for i in range(count):
    print('i = '+ str(i))

    Home_BTC["name"] = input('Ім\'я жителя :')
    Home_BTC["home_number"] = int(input('Номер будинку :'))
    Home_BTC["name_street"] = input('Назва вулиці :')
    Home_BTC["name_city"] = input('Назва міста :')
    Home_BTC["poshtovyi_index"] = int(input('Поштовий індекс:'))
    Home_BTC["name_country"] = input('Країна :')
    mas_2 = [ Home_BTC["name"], Home_BTC["home_number"], Home_BTC["name_street"], Home_BTC["name_city"], Home_BTC["poshtovyi_index"], Home_BTC["name_country"],  ]
    if i != 0:
        mas_1.append(mas_2)
    else:
        mas_1[i] = mas_2

for n in range(count):
    print('mas_1[' + str(n + 1) + '] :' + str(mas_1[n]))


'''print('Sroka')
value_1 = 3
while value_1 >= 0:
    string = easygui.enterbox(msg='You can somethink input:', title="Romikver", default = 'qwerty')
    value_1 = value_1 - 1

flavor = easygui.choicebox("What is your favorite ice cream flavor?",
choices = ['Vanilla', 'Chocolate', 'Strawberry'] ) # створили інформаійне вікно з 3-ох кнопок 
easygui.msgbox ("You picked " + flavor)
easygui.msgbox("Hello There!")  #message box создает информационное окно.
value = easygui.ynbox('Shall I continue?', 'Title_Romikver', ('Yeah', 'No')) # yes_no_box информационное окно
print('value: ' + str(value)) 
'''

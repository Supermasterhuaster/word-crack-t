# WordCrackT
<p align="center">

<img src="https://github.com/Supermasterhuaster/word-crack-t/raw/master/doc/logo.png" width="300px" height="300px" alt="WordCrackT">

</з>
В приложении банка Tinkoff (или Tбанк) есть игра в которой надо угадать слова из 5 букв, при угадывании всех слов вы получаете небольшие привилегии и подарки от банка в виде скидок и т.д. Данное приложение помогает пользователю отгадать загаданное слово с более высокой вероятностью на успех, используя довольно простой анализ и фильтр частотности слов.

##### Как это работает:
1. приложение предлагает вам случайное слово из 5 букв которое является существительным 
вы вводите это слово в приложении
2. приложении банка сообщает вам какие буквы есть в слове, и какие буквы стоят на своих местах
3. WordCrackT спрашивает какие буквы есть в слове (эти буквы подсвечен белым - не серым), нужно ввести их номера через пробел и нажать enter
4. WordCrackT спрашивает какие буквы есть в слове и они располагаются на своих местах (эти буквы подсвечены желтым), нужно ввести их порядковые номера через пробел и нажать enter
5. WordCrackT предложит вам следующие наиболее вероятное слово 
6. повторяйте пока не отгадаете слово или не исчерпаете кол-во попыток 
7. для выхода можно нажать Ctrl+C 


## Установка


Самый простой способ установить WordCrackT это скачать уже [скомпилированные файлы](https://github.com/Supermasterhuaster/word-crack-t/tree/master/build) для вашей ОС. Они доступны на GitHub в папке build для Windows 11, Ubuntu 24.04 LTS, и Armbian 23 (OrangePI3) 

1. Установка для Windows: 
 - Для ОС Windows установка и запуск не чем ни отличается от других программ. [Скачиваете инсталлятор](https://github.com/Supermasterhuaster/word-crack-t/tree/master/build/windows), выбираете папку для установки, после установки запускаете  word-crack-t.exe

2. Установка для Linux:
 - скачайте [архив с программой](https://github.com/Supermasterhuaster/word-crack-t/tree/master/build/linux)
 - создайте папку для приложения ``` mkdir word-crack-t```
 - Распакуйте скачанный архив в эту папку ```tar -xvJf word-crack-t.tar.zx -C word-crack-t ```
 - перейдите в папку с программой ``` cd word-crack-t ``` 
 - сделайте бинарный файл исполняемым chmod +x word-crack-t.bin
 - можно запускать файл как через GUI так и через консоль выполнив ``` ./word-crack-t.bin``` 
3. Запуск Python кода:
 - Для работы вам необходим Python 3.12.* и git любой версии 
 - Удостоверьтесь что у вас установлены данные утилиты выполнив в консоли команду ``` python -V ``` и ``` git -v ``` если утилиты установлены вы должны увидеть соответсвующее версии ПО 
 - С клонируйте этот репозиторий выполнив ``` git clone https://github.com/Supermasterhuaster/word-crack-t.git ``` 
 - создайте виртуальное окружения
 - перейдите в папку с проектом из консоли
   - Для Winodws в CMD ``` cd C:\word-crack-t ```
   - для Linux ``` cd ./word-crack-t ```
 - Создайте виртуальное окружение
   - Для Winodws в CMD ``` python -m venv env ```
   - для Linux ``` python3 -m venv venv ```
 - Активируйте виртуальное окружение
   - Для Winodws в CMD ``` cd env/Scripts && activate && cd ../../ ```
   - для Linux ``` source venv/bin/activate ```
 - Установите зависимости проекта (для Winodws и Linux) ``` pip install -r requirements.txt ```
 - После окончания установки можно запускать приложения из исходного кода Python ``` python main.py ``` 

Я в этой жизни больше не на что ни рассчитываю, но вдруг... кто-то захочет сказать спасибо...

| Пожертвование | Адрес           | Валюта        |
|:------------- |:---------------:| -------------:|
| Tinkoff       | [https://www.tinkoff.ru/cf/9CMnq5GezZC](https://www.tinkoff.ru/cf/9CMnq5GezZC)  |   RUB |
|   BTC NETWORK            | ``` 15NDWXhkRGvj592KVuyTSozi3FJuF3KT3d ```           |           BTC|
|   USDT ERC20            | ``` 0xa85f1e243d21c1fbcd8f113b1ef9315915c8858b ```         |         USDT|
|   USDT TRC20            | ``` TC7yesqDCzbsHLM4Guf9A7DmACWnvWLWq8 ```         |         USDT|

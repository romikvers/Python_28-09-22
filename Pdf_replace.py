from gtts import gTTS
from art import tprint
import pdfplumber
from  pathlib import Path

def pdf_to_mp3(file_path, language, page_begin=None, page_end=None):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            i = 0
            if page_begin == None and page_end == None:   # book
                pages = [page.extract_text() for page in pdf.pages]
            elif page_begin != None and page_end == None:    # page
                for page in pdf.pages:
                    i = i + 1
                    if i == page_begin:
                       pages = page.extract_text()
            elif page_begin != None and page_end != None:    # pages
                pages = []  # масив, кожна ячейка мітисть дані ожної сторінки
                for page in pdf.pages:
                    i = i + 1 
                    if i >= page_begin and i <= page_end:
                        pages.append(page.extract_text())
        text = ''.join(pages)  # приєднуємо сторінки до купи
        text = text.replace('\n', '')  # заміняємо перенос на нову строку на нічого

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem # получаємо ім'я файлу за допомогой властивості stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!'
    else:
        return 'File not exists, check the file path!'

def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file`s path: ")
    if Path(file_path).suffix != '.pdf': # якщо користувач не увів тип файлу - .pdf, то ця функція дописує самостійно
        file_path = file_path + '.pdf'
    language = input("Choose language, for exampale 'en' or 'ru': ")
    what = str(input("Перетворити цілу книжцу(book), сторінку(page) чи певний проміжок сторінок(pages)?"))
    if what == "page":
        page_begin = int(input("Введіть сторінку: "))
        print(pdf_to_mp3( file_path=file_path, language=language, page_begin=page_begin, page_end=None ))
    elif what == "pages":
        page_begin = int(input("Від якої сторінки почати запис: "))
        page_end = int(input("До якої сторінки зчитувати: "))
        assert page_begin > 0 and page_end > page_begin , "Не вірно введені сторінки!"
        print(pdf_to_mp3(file_path=file_path, language=language, page_begin=page_begin, page_end=page_end )) #'D:\Программування\Pyhton\Python_поиск_и_сортировки.pdf'))
    else:
         print(pdf_to_mp3(file_path=file_path, language=language, page_begin=None, page_end=None ))
 #D:\Программування\Pyhton\Python_поиск_и_сортировки.pdf
if __name__ == '__main__':
    main()


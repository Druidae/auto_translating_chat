from googletrans import Translator


def message_translator(text, src, dest):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        
        return translation.text
    except Exception as ex:
        return ex
    
    
def main():
    print(message_translator(text='Hello', src='en', dest='ru'))


if __name__ == '__main__':
    main()
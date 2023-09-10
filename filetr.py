import Task2 as dp
import os
import configparser

def process_file(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    input_file = config['General']['input_file']
    target_language = config['General']['target_language']
    output_destination = config['General']['output_destination']
    max_characters = int(config['Limits']['max_characters'])
    max_words = int(config['Limits']['max_words'])
    max_sentences = int(config['Limits']['max_sentences'])

    if not os.path.exists(input_file):
        print(f"Помилка: Файл {input_file} не знайдено.")
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

        char_count = 0
        word_count = 0
        sentence_count = 0

        in_word = False

        for char in text:
            char_count += 1

            if char.isspace():
                in_word = False
            elif not in_word:
                in_word = True
                word_count += 1

            if char in ('.', '!', '?'):
                sentence_count += 1

    file_size = os.path.getsize(input_file)

    print("Назва файлу:", input_file)
    print("Розмір файлу:", file_size, "байт")
    print("Кількість символів:", char_count)
    print("Кількість слів:", word_count)
    print("Кількість речень:", sentence_count)
    print("Мова тексту:", dp.LangDetect(text, "lang"))

    with open(input_file, 'r', encoding='utf-8') as file:
        char_count = 0
        word_count = 0
        sentence_count = 0

        in_word = False

        text = ""

        while True:
            char = file.read(1)

            if not char:
                break

            char_count += 1

            text += char

            if char.isspace():
                in_word = False
            elif not in_word:
                in_word = True
                word_count += 1

            if char in ('.', '!', '?'):
                sentence_count += 1

            if char_count >= max_characters or word_count >= max_words or sentence_count >= max_sentences:
                break

    translated_text = dp.TransLate(text, "auto", target_language)

    if output_destination == 'screen':
        print(f"\nПереклад на мову {target_language}:")
        print(translated_text)
    elif output_destination == 'file':
        output_file = input_file.split('.')[0] + '_' + target_language + '.txt'
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("\nOk")
        except Exception as e:
            print("Помилка під час збереження результату:", str(e))
    else:
        print("Помилка: Невірно вказаний вихідний напрямок.")


config_file = 'config.ini'
process_file(config_file)



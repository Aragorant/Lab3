import Task2 as dp


text_to_translate = "Добрий день"
print("Переклад тексту 'Добрий день' на англ. мову:")
print(dp.TransLate(text_to_translate, "auto", "en"))

print("\nВизначення мови та коеф. довіри тексту 'Добрий день':")
print(dp.LangDetect("Hello", "all"))

print("\nНазва мови коду 'uk':")
print(dp.CodeLang("uk"))

print("\nКод мови 'ukrainian':")
print(dp.CodeLang("ukrainian"))

print("\nСписок мов у консолі:")
print(dp.LanguageList("screen"))

print("\nСписок мов у файлі:")
print(dp.LanguageList("file", text_to_translate))
import Task1 as gt


text_to_translate = "Добрий день"
print("Переклад тексту 'Добрий день' на англ. мову:")
print(gt.TransLate(text_to_translate, "auto", "en"))

print("\nВизначення мови та коеф. довіри тексту 'Добрий день':")
print(gt.LangDetect(text_to_translate, "all"))

print("\nНазва мови коду 'uk':")
print(gt.CodeLang("uk"))

print("\nКод мови 'ukrainian':")
print(gt.CodeLang("ukrainian"))

print("\nСписок мов у консолі:")
print(gt.LanguageList("screen"))

print("\nСписок мов у файлі:")
print(gt.LanguageList("file", text_to_translate))

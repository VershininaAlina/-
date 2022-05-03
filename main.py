import random
eng_low = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
eng_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
final_text = ""
add_sim = ""

#Функция расшифровки шифра цезаря
def crypt(langv_en_ru, source_text, add_sim, final_text, offset):
  if langv_en_ru == "ru":
    for i in range(len(source_text)):
      if source_text[i] in rus_low:
        add_sim= rus_low.find(source_text[i])
        final_text += rus_low[add_sim+offset]
      elif source_text[i] in rus_up:
        add_sim= rus_up.find(source_text[i])
        final_text += rus_up[add_sim+offset]  
      elif source_text[i] == " ":
        final_text += " "
      else :
        final_text += source_text[i]
    print(final_text)
      
  if langv_en_ru == "en":
    for j in range(len(source_text)):
      if source_text[j] in eng_low:
        add_sim= eng_low.find(source_text[j])
        final_text += eng_low[add_sim+offset]
      elif source_text[j] in eng_up:
        add_sim= eng_up.find(source_text[j])
        final_text += eng_up[add_sim+offset]  
      elif source_text[j] == " ":
        final_text += " "
      else :
        final_text += source_text[j]
    print(final_text)

#Функция дешифровки, когда мы знаем шаг сдвига    
def decrypt(langv_en_ru, source_text, add_sim, final_text, offset):
  if langv_en_ru == "ru":
    for q in range(len(source_text)):
      if source_text[q] in rus_low:
        add_sim= rus_low.find(source_text[q])
        final_text += rus_low[add_sim-offset]
      elif source_text[q] in rus_up:
        add_sim= rus_up.find(source_text[q])
        final_text += rus_up[add_sim-offset]  
      elif source_text[q] == " ":
        final_text += " "
      else :
        final_text += source_text[q]
    print(final_text)
   
  if langv_en_ru == "en":
    for k in range(len(source_text)):
      if source_text[k] in eng_low:
        add_sim= eng_low.find(source_text[k])
        final_text += eng_low[add_sim-offset]
      elif source_text[k] in eng_up:
        add_sim= eng_up.find(source_text[k])
        final_text += eng_up[add_sim-offset]  
      elif source_text[k] == " ":
        final_text += " "
      else :
        final_text += source_text[k]
    print(final_text)

    
def secret_decrypt(langv_en_ru, source_text, add_sim, final_text, offset):
  for g in range(32):
    if langv_en_ru == "ru":
      for l in range(len(source_text)):
        if source_text[l] in rus_low:
          add_sim= rus_low.find(source_text[l])
          final_text += rus_low[add_sim-g]
        elif source_text[l] in rus_up:
          add_sim= rus_up.find(source_text[l])
          final_text += rus_up[add_sim-g]  
        elif source_text[l] == " ":
          final_text += " "
        else :
         final_text += source_text[l]
      print(final_text,  g)
      print()
      final_text = " "
   
    if langv_en_ru == "en":
      for m in range(len(source_text)):
        if source_text[m] in eng_low:
          add_sim= eng_low.find(source_text[m])
          final_text += eng_low[add_sim-g]
        elif source_text[m] in eng_up:
          add_sim= eng_up.find(source_text[m])
          final_text += eng_up[add_sim-g]  
        elif source_text[m] == " ":
          final_text += " "
        else :
          final_text += source_text[m]
      print(final_text, g)
      print()
      final_text = " "    
def main():    
  print("Добро пожаловать в числовую угадайку")  
  action = input("Требуется зашифровать или расшифровать (e - encrypting, d - decrypting):")
  langv_en_ru = input("'Какой язык шифрования: русский или английский (ru - Russian, en - English):")
  offset = int(input('Введите шаг сдвига: '))
  source_text = input('Введите исходный текст для шифровки/дешифровки: ')

  if action == "e":
    crypt(langv_en_ru, source_text, add_sim, final_text, offset)
  elif action == "d":
    decrypt(langv_en_ru, source_text, add_sim, final_text, offset)
  elif action == "s":
    secret_decrypt(langv_en_ru, source_text, add_sim, final_text, offset)
  else:
    print("Команда неверна")
main()

  

    

  

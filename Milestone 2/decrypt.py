LAST_UPCHAR_CODE = ord('Z')
FIRST_UPCHAR_CODE = ord('A')
LAST_LOWCHAR_CODE = ord('z')
FIRST_LOWCHAR_CODE = ord('a')
CHAR_RANGE = LAST_UPCHAR_CODE - FIRST_UPCHAR_CODE + 1

def ceisar_chiefr(message, shift):
  result = ''
  for char in message:
    if char.isalpha():
      char_code = ord(char)
      new_char_code = char_code + shift
      if char.isupper():
        if new_char_code > LAST_UPCHAR_CODE:
          new_char_code -= CHAR_RANGE
        if new_char_code < FIRST_UPCHAR_CODE:
          new_char_code += CHAR_RANGE
        new_char = chr(new_char_code)
        result += new_char
      else:
        if new_char_code > LAST_LOWCHAR_CODE:
          new_char_code -= CHAR_RANGE
        if new_char_code < FIRST_LOWCHAR_CODE:
          new_char_code += CHAR_RANGE
        new_char = chr(new_char_code)
        result += new_char
    else:
      result += char
  print(result)


user_shift= int(input("Input a shift: integer "))
user_message = input('Input a message: ')

ceisar_chiefr(user_message, user_shift)
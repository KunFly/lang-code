lang-code
=========
This script is used for transcribing ISO-639 language code, in this version, it has been designed to represent most of the major languages of the world. Based on ISO-639-1, language code could be transcribed between ISO-639-1 and ISO-639-3, note that not all language code in ISO-639-3 is listed here.

Part 1 (ISO 639-1:2002) provides a 2 letter code that has been designed to represent most of the major languages of the world.
Part 3 (ISO 639-3:2007) provides a 3 letter code and aims to give as complete a listing of languages as possible, including living, extinct and ancient languages.

More information about ISO-639:
http://www.iso.org/iso/home/standards/language_codes.htm
http://www-01.sil.org/iso639-3/codes.asp

class Lang_Code
Initialize class by inputting original and target language code.

Method:
changeCode(string) : change language code from original code to target code.
get_noDetected(): return number and code of no detected language code.

Exemple:

import lang-code
f = lang-code.Lang_Code("ISO-639-1","ISO-639-3")
code1 = "fr"
code2 = f.changeCode(code1)
print code2
"fra"

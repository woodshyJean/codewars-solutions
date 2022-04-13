'''Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case,
also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior" 

////////////////////////////////// solution /////////////////////////// '''

def to_camel_case(text):
    t2 = text.replace('_','-').split('-')
    t3 = [word.replace(word, word.title()) for word in t2[1:]]
    return str(t2[0]) + (str(''.join(t3[0:])))
  

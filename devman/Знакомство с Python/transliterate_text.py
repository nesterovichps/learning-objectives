import num2words
import transliterate

text = '''Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...'''
print(transliterate.translit(text, 'ru'), end='\n\n')
print(
    *[f'{i} - {transliterate.translit(num2words.num2words(i), "ru")}' for i in text.replace('.', '').strip().split() if
      i.isdigit()], sep='\n')

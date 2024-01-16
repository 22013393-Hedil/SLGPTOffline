import argostranslate.package as ap
import argostranslate.translate as at
import time

def translateText(from_code:str, to_code:str, TexttoTranslate:str)->str:
    ap.update_package_index()
    available_packages = ap.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    ap.install_from_path(package_to_install.download())
    # Translate
    translatingText = at.translate(TexttoTranslate, from_code, to_code)
    return translatingText

def word_counter(text:str)->int:
    # Counting words
    return len(text.split())

def main(TextGPT):
    tic = time.perf_counter()
    # Translate
    translatingText = translateText('id', 'en', TextGPT)
    print(translatingText)
    toc = time.perf_counter()
    print(f'Length of words non-translated: {word_counter(TextGPT)}\nLength of words translated words: {word_counter(translatingText)}\nIt took {toc - tic:0.4f}s')

if __name__ == '__main__':
     # Your input text in the variable TextGPT
    TextGPT:str = input('Input: ')
    main(TextGPT)
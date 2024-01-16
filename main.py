import argostranslate.package as ap
import argostranslate.translate as at
from transformers import pipeline

model = pipeline('text2text-generation', model = "MBZUAI/LaMini-Flan-T5-248M")

def get_response(input_prompt):
    return model(input_prompt, max_length=512, do_sample=True)[0]['generated_text']

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

def translationLang(from_code, to_code, input_prompt)->str:
    return translateText(to_code, from_code, get_response(translateText(from_code, to_code, input_prompt)))

def main(language)->str:
    if language == 'en' or language == 'english':
        # Does not translate
        input_prompt = str(input("Please enter your question: "))
        return f'Response: {get_response(input_prompt)}'

    if language == 'id' or language == 'indonesia':
        # Translate
        input_prompt = str(input("Silakan masukkan pertanyaan Anda: "))
        translatingText2 = translationLang('id','en',input_prompt)
        return f'Tanggapan: {translatingText2}'

    return 'Invalid input. Please try again.'

if __name__ == '__main__':
   while True:
    answer = input('Do you want to continue? (y/n)')
    if answer == 'y':
        language = str(input("Please enter your language: ").lower())
        result = main(language)
        print(result)
    else:
        print('Thank you for using this program.')
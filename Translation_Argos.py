import argostranslate.package as ap
import argostranslate.translate as at

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

# Your input text in the variable TextGPT
TextGPT:str = input('Input: ')

# Translate
translatingText = translateText('en', 'id', TextGPT)
print(translatingText)
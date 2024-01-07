from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import argostranslate.package as ap
import argostranslate.translate as at

# Load Language Model
modelName = 'bert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(modelName)
model = AutoModelForSequenceClassification.from_pretrained(modelName)

# If the dataset is gated/private, make sure you have run huggingface-cli login
dataset = load_dataset("nampdn-ai/tiny-textbooks")
train_set = dataset["train"]
val_set = dataset["validation"]

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


# Tokenize the input text
tokenized_inputs = tokenizer(TextGPT, padding=True, truncation=True, return_tensors='pt')

print(tokenized_inputs)
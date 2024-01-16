# pip install -q transformers
from transformers import pipeline
import time

checkpoint = "MBZUAI/LaMini-Flan-T5-248M"

model = pipeline('text2text-generation', model = checkpoint)

def get_response(input_prompt):
    generated_text = model(input_prompt, max_length=512, do_sample=True)[0]['generated_text']
    return generated_text

tic = time.perf_counter()
input_prompt = str(input("Please enter your question: "))
print("Response:", get_response(input_prompt))
print("Time taken:", time.perf_counter() - tic)

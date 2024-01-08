
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small", legacy=False)
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

input_text = "translate English to Indonesian: Hello, how are all of you feeling today?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids, max_new_tokens=100)
print(tokenizer.decode(outputs[0]))

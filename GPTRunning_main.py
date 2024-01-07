#from langchain.chains import LLMChain
import torch
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM

model_id = 'google/flan-t5-small'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(
    model_id,
    load_in_8bit=True,
    low_cpu_mem_usage=True,
    framework='pt',
    device=torch.device('cpu'),
    device_map='auto'
    )

generate = pipeline(
    'text2text-generation',
    model=model,
    tokenizer=tokenizer,
    max_length=100
)

#local_llm = HuggingFacePipeline(pipeline=pipeline)

#llm_chain = LLMChain(prompt='translate from english to french: ',llm=local_llm)

question = 'What is the meaning of life?'

print(generate(question, max_length=100)[0]['generated_text'])
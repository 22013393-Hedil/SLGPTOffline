# Service Learning: Offline ChatGPT
The aim of this project is to produce a working ChatGPT response in prompt command that will also translate into bahasa Indonesian language, without the need of internet.

We are going through the step-by-step installments and codings that would help proceed to offline, due to the setting in github to be a virtual environment.

Reference:
- [Hugging Face](https://huggingface.co/)
- [Hugging Face Models](https://huggingface.co/models)

# Installation:
1. Install the packages/dependencies from requirements.txt (Note: bash and cmd commands are similar for this)
```bash
pip install -r requirements.txt
```
2. After installing the requirements, need to download the Models from files and install the individual files and put it as one folder (Note: Ensure the files in the foler correspond to the Models)
    - [indo-pure Model](https://huggingface.co/CLAck/indo-pure/tree/main)
    - [BART-base](https://huggingface.co/facebook/bart-base) (Noted: Supports translation)
    - [flan-t5-small](https://huggingface.co/google/flan-t5-small) (Note: Supports translation)
** Take note that translation need certain tokens, if noted that it supports. Please read its description

3. Ensure you add in the model either using pipeline function or from_pretrained function
   ```python
    pip install -r requirements.txt
    ```

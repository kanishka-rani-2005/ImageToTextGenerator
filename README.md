## Image to Text Generator 

##### You just need to upload an image 
##### The model will generate the text from the image
##### Then Model will automatically generate a story according to that text 
##### You can use this model for your own projects, just make sure to give credit to the original


## Clone the Repository
```bash
git init
git clone https://github.com/kanishka-rani-2005/ImageToTextGenerator.git
```

## Create Virtual environment
```bash
conda create -p venv -y
```

## Create .env file
```bash
HUGGINGFACE_API_TOKEN='Your api key'
GROQ_API_KEY='Your api key'

```

## Create requirements.txt
```bash
requests
streamlit
langchain
transformers
python-dotenv
typing
langchain_community
langchain_groq
langchain_core
torch
```

## Install requirements using command 
```bash
pip install -r requirements.txt
```

## Run the model using command
```bash
streamlit run app.py
```

## Model Architecture
The model architecture is a combination of several pre-trained models and libraries. The image to text generator uses
- **LangChain**: A library for building conversational AI models. 
- **Transformers**: A library of pre-trained models for natural language processing tasks. 
- **PyTorch**: A library for building and training deep learning models.
- **Streamlit**: A library for building web applications.
- **Requests**: A library for making HTTP requests. 
- **Python-dotenv**: A library for loading environment variables from a .env file. 
- **Typing**: A library for type checking Python code. 
- **LangChain Groq**: A library for building conversational AI models. 


## Author 
This model was created by Kanishka Rani kanishka22043@gmail.com

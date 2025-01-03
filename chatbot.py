import json
from chatterbot import ChatBot
# import spacy
# spacy.load('en_core_web_sm')
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('<b>UniVerse</b>')

# nlp=spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response':"<b>Hi there, Welcome to UniVerse! 👋 If you need any assistance, I'm always here.<br>Which section you want to explore?<br>1. Campus<br>2. Courses Offered<br>3. Admissions<br>4. Placements<br>5. Campus Life<br>6. Alumni from NIE<br>7. NIE Portals</b><br>",
            'maximum_similarity_threshold': 0.95
        }
    ],
    database_uri='mongodb://localhost:27017/chatterbot'
) 
trainer = ListTrainer(chatbot)

with open('./dataset.json', 'r',encoding='utf-8') as file:
    data = json.load(file)
    for entry in data:
        trainer.train([entry['input'], entry['response']])

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter')
    for file in os.listdir('/mnt/e/Projects/Banking-Chatbot/data'):
        print(file)
        convData = open(r'/mnt/e/Projects/Banking-Chatbot/data/' + file, encoding='latin-1').readlines()
        print("set trainer")
        trainer = ListTrainer(chatbot)
        print("train")
        trainer.train(convData)
        print("Training completed")
    

setup()

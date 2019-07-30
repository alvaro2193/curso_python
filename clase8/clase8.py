#!/usr/bin/env python
# -*-coding: utf-8 -*-


from chatterbot import ChatBot
chatbot = ChatBot ("Ron Obvious")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hola",
    "Hola!",
    "Como estas?",
    "Lo estoy haciendo genial",
    "Es bueno oir eso",
    "Gracias",
    "De nada"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)
while True:
    palabra = input ("Hola, en que te puedo ayudar? ")
    response = chatbot.get_response(palabra)
    print(response)
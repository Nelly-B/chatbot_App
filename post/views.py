from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create your views here.

bot = ChatBot('chatbot',read_only=False, 
              logic_adapters=[
                  {
                    'import_path':'chatterbot.logic.BestMatch',
                    'default_response':"Sorry i don't know what that means",
                    'maximun_similarity_threshold':0.90   
                  }
                  ])

list_to_train = [
    "Hi!",
    "Hi, there",
    "What's  your name?",
    "I'm just a chatbot",
    "What is your favourite food",
    "I like cheese",
]

chatterbotcorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotcorpusTrainer.train('chatterbot.corpus.english')

# list_trainers = ListTrainer(bot)
# list_trainers.train(list_to_train)


def index(request):
    return render(request, 'home.html')

# def specific(request):
#     return HttpResponse("list1")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

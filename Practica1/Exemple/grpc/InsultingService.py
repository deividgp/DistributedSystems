import random

class InsultingService:

    def __init__(self):
        self.insultsSet = set()

    def addInsult(self, insult):
        print('new insult received ' + insult)
        self.insultsSet.add(insult)
        return 'Done'

    def getInsults(self):
        return list(self.insultsSet)

    def insultme(self):
        chosenInsult = list(self.insultsSet)[random.randrange(0, len(self.insultsSet))]
        print('new insult requested ' + chosenInsult)
        return chosenInsult


insultingService = InsultingService()

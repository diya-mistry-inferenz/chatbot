from botbuilder.core import TurnContext,ActivityHandler,RecognizerResult,MessageFactory
from botbuilder.ai.luis import LuisApplication,LuisPredictionOptions,LuisRecognizer


class LuisBot(ActivityHandler):
    def __init__(self):
        luis_app = LuisApplication("9e82e687-72f1-451f-8320-6732f80bcaad","db7c274707274ba6b408419fb4b5a302","https://chatbotdia.cognitiveservices.azure.com/")
        luis_option = LuisPredictionOptions(include_all_intents=True,include_instance_data=True)
        self.LuisReg = LuisRecognizer(luis_app,luis_option,True)
 

    async def on_message_activity(self,turn_context:TurnContext):
        luis_result = await self.LuisReg.recognize(turn_context)
        intent = LuisRecognizer.top_intent(luis_result)
        await turn_context.send_activity(f"Top Intent : {intent}")
        retult = luis_result.properties["luisResult"]
        await turn_context.send_activity(f" Luis Result {retult.entities[0]}")
        
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionCustomResponse(Action):
    def name(self):
        return "action_custom_response"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="This is a custom response from an action.")
        return []


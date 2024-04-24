from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient

class ActionProgramDetails(Action):
    def name(self) -> Text:
        return "action_program_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017")
        db = client["TIS"]
        collection = db["New"]

        # Query MongoDB to fetch program details
        program_details = collection.find_one({"course_name": "Psychology"})

        if program_details:
            response = (
                f"The Psychology program at {program_details['university_name']} offers both "
                f"{program_details['course_name']} tracks. It is a full-time, on-campus program with a duration of "
                f"{program_details['program_duration']} starting from {program_details['start_date']}. The yearly tuition fees are "
                f"{program_details['program_fees']}. You can find more information [here]({program_details['university_url']})."
            )
        else:
            response = "Sorry, I couldn't find information about the Psychology program."

        dispatcher.utter_message(text=response)

        return []

class ActionScholarshipDetails(Action):
    def name(self) -> Text:
        return "action_scholarship_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017")
        db = client["TIS"]
        collection = db["New"]

        # Query MongoDB to fetch scholarship details
        scholarship_details = collection.find_one({"scholarship_name": "The Dr. C. Ravi and Shanti Ravindran Award for Outstanding Doctoral Thesis"})

        if scholarship_details:
            response = (
                f"{scholarship_details['scholarship_provider']} offers the {scholarship_details['scholarship_name']}. It's a merit-based "
                f"scholarship providing {scholarship_details['scholarship_providedfund']}. Unfortunately, the deadline is not specified. "
                f"You can find more information [here]({scholarship_details['scholarship_url']})."
            )
        else:
            response = "Sorry, I couldn't find information about the scholarship."

        dispatcher.utter_message(text=response)

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import aiohttp

class ActionShowCatPicture(Action):
    def name(self) -> Text:
        return "action_show_cat_picture"

    async def run(
        self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_key = "live_r3U3U1iBkt3sGt77WkbMqCGtoKMpxZw7OR57rZLqyJfuVUCOuJ0Hr7uZAMA2gmmX"  # Your API key
        url = 'https://api.thecatapi.com/v1/images/search'
        
        headers = {
            'x-api-key': api_key
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data and len(data) > 0:
                            cat_image_url = data[0]['url']
                            dispatcher.utter_message(text="Here's a cute cat for you!", image=cat_image_url)
                        else:
                            dispatcher.utter_message(text="No cat picture found.")
                            print("No data returned from API.")
                    else:
                        dispatcher.utter_message(text="Sorry, I couldn't retrieve a cat picture right now.")
                        print(f"Failed to fetch cat picture, status code: {response.status}")
        except Exception as e:
            dispatcher.utter_message(text="An error occurred while fetching the cat picture.")
            print(f"Error: {e}")

        return []

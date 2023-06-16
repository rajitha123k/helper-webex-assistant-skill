from webex_skills.api import SimpleAPI
from webex_skills.dialogue import responses
from webex_skills.models.mindmeld import DialogueState
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api = SimpleAPI()


@api.handle(pattern=r'.*\sheadlines\s?.*')
async def turn_on(current_state: DialogueState) -> DialogueState:
    print(current_state.text)
    new_state = current_state.copy()

    text = 'Ok, showing todays headlines.'
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=38ff818927ec46e2a52da6cc2c84527e"

    response = requests.get(url)

    response_json = response.json()
    headlines=[]
    for x in response_json['articles']:
        headlines.append(x['title'])

    assistant_event_payload = {
        'name': 'Switch',
        'payload': {
            'text': headlines,
        },     
    }
    
    new_state.directives = [
        responses.Reply(text),
        responses.Speak(text),

        # 2. Create `assistant-event` directive and include payload
        responses.AssistantEvent(payload=assistant_event_payload),

        responses.Sleep(10),
    ]

    return new_state

@api.handle(pattern=r'.*\sweather\s?.*')
async def turn_on(current_state: DialogueState,  query: str) -> DialogueState:
    print(current_state.text)
    new_state = current_state.copy()

    spl_word = 'in'
    city_id=0

    res=query[query.find(spl_word)+len(spl_word)+1:]
    # res = res[:res.find(" ")+1]

    print(res)
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'cityList.json')

    with open(file_path, 'r') as f:
        data = json.load(f)
    for x in data:
        if x['name'].lower() == res.lower():
            city_id=x['id']
    

    
    url = "https://roomos-device-widgets.wbx.ninja/api/weather?id="+str(city_id)+"&units=imperial"

    response = requests.get(url)

    response_json = response.json()
    print(response_json)
    text = 'Its '+str(response_json['temp'])+' degrees and '+str(response_json['description'])+' in '+str(response_json['place'])+' today.'

    # assistant_event_payload = {
    #     'name': 'Switch',
    #     'payload': {
    #         'text': headlines,
    #     },     
    # }
    
    new_state.directives = [
        responses.Reply(text),
        responses.Speak(text),

        # # 2. Create `assistant-event` directive and include payload
        # responses.AssistantEvent(payload=assistant_event_payload),

        responses.Sleep(10),
    ]

    return new_state

@api.handle(pattern=r'.*\sbookings\s?.*')
async def turn_on(current_state: DialogueState,  query: str) -> DialogueState:
    print(current_state)
    new_state = current_state.copy()

    access_token=os.getenv('WEBEX_ACCESS_TOKEN')
    
    text = 'Ok, showing todays headlines.'
    new_state.directives = [
        responses.Reply(text),
        responses.Speak(text),
        responses.DisplayWebView("https://df90-67-21-186-154.ngrok-free.app","Cisco"),
        responses.Sleep(10),
    ]

    return new_state

@api.handle(pattern=r'.*\soff\s?.*')
async def turn_off(current_state: DialogueState) -> DialogueState:
    new_state = current_state.copy()

    text = 'Ok, turning lights off.'

    new_state.directives = [
        responses.Reply(text),
        responses.Speak(text),

        # 2. Create `clear-web-view` directive
        responses.ClearWebView(),

        responses.Sleep(10),
    ]

    return new_state
from json.decoder import JSONDecodeError
import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And ' \
            'this is a second message","timestamp":"2021-06-04 16:41:01"}]} '

try:
    obj = json.loads(json_text)
    messages = obj.get("messages")
    second_message_text = messages[1].get("message")
    print(f"Required message text is: {second_message_text}")
except JSONDecodeError:
    print("\'json_text\' is not a JSON")
except Exception as e:
    print("Something went wrong. Google it using text below: " + str(e))


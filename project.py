import requests
import json
def get_fact():
    response=requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    content=response.text
    data = json.loads(content)
    fact= data["text"]
    return fact
no_of_facts=int(input())
if no_of_facts>7:
    print("Maximum number of facts per execution is 7")
elif no_of_facts<=0:
    print("Minimum number of facts per execution is 1")
else:
    for i in range(no_of_facts):
        print(get_fact())
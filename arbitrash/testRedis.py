import redis
import json
from pprint import pprint
from redis.commands.json.path import Path
client = redis.Redis(host='localhost', port=6379, db=0)



restaurant = {
    "name": "Ravagh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}
#client.set('123', json.dumps(restaurant))
#pprint(json.loads(client.get('123')))
pprint(client.keys('*'))


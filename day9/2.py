import json

class Ser:

    def serialize(self, data):
        return json.loads(data)
    
    def deseaarlize(self, data):
        return json.dumps(data)
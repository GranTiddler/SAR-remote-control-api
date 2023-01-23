import requests

class Misty:
    def __init__(self, ip):
        self.ip = ip

    def post(self, command, headers, parameters):
        text = ""
        for i in parameters.keys():
            text += f"{i}={parameters[i]}"
            text += "&"

        return requests.post(
            f"http://{self.ip}/api/{command}?{text}",
            json=parameters,
            headers=headers
        )


Chuck = Misty("172.22.174.127")

print(Chuck.post(
    "drive", 
{
    "Content-Type": "application/json"
}, 
{
    "linearVelocity": 100,
    "angularVelocity": 100
}
))

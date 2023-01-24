import requests


class Misty:
    def __init__(self, ip):
        self.ip = ip

    def post(self, command, parameters={}):
        text = ""
        for i in parameters.keys():
            text += f"{i}={parameters[i]}"
            text += "&"

        return requests.post(
            f"http://{self.ip}/api/{command}?{text}",
            json=parameters,
            headers={"Content-Type": "application/json"}
        )

    def get(self, command, parameters={}):
        text = ""
        for i in parameters.keys():
            text += f"{i}={parameters[i]}"
            text += "&"

        return requests.get(
            f"http://{self.ip}/api/{command}?{text}"
        )

    def delete(self, command, parameters={}):
        text = ""
        for i in parameters.keys():
            text += f"{i}={parameters[i]}"
            text += "&"

        return requests.delete(
            f"http://{self.ip}/api/{command}?{text}"
        )

    def display_image(self, filename, alpha):
        self.post("image/display", {"filename": filename, "alpha" : alpha})


Chuck = Misty("172.22.174.127")

print(Chuck.delete("images",{"FileName" : "diglett.png"}))

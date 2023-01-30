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
        return self.post("image/display", {"FileName": filename, "Alpha": alpha})

    def videos_display(self, url, layer):
        return self.post({"URL": url, "Layer": layer})

    def get_image_list(self):
        return self.get("images/list")

    def get_blink_settings(self):
        return self.get("blink/settings")
    
    def audio(self, filename, data, immediatelyapply, overwriteexisting):
       return self.post({"FileName": filename, "Data": data, "ImmediatelyApply": immediatelyapply, "OverwriteExisting": overwriteexisting})

    def images(self, filename, data, width, height, immediatelyapply, overwriteexisting):
        return self.post({"FileName": filename, "Data": data, "Width": width, "Height": height, "ImmediatelyApply": immediatelyapply, "OverwriteExisting": overwriteexisting})
    
    #def video goes here :P

    def change_led(self, red, green, blue):
        return self.post("led", {"red": red, "green": green, "blue": blue})

    def webviews_display(self, url):
        return self.post({"URL": url})

    def pause_audio(self):
        return self.post({  })


Chuck = Misty("172.22.174.127")



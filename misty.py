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
    
    def save_audio(self, filename, data, immediatelyapply, overwriteexisting):
       return self.post("audio", {"FileName": filename, "Data": data, "ImmediatelyApply": immediatelyapply, "OverwriteExisting": overwriteexisting})

    def save_images(self, filename, data, width, height, immediatelyapply, overwriteexisting):
        return self.post("images", {"FileName": filename, "Data": data, "Width": width, "Height": height, "ImmediatelyApply": immediatelyapply, "OverwriteExisting": overwriteexisting})
    
    #def #save_video goes here :P

    def change_led(self, red, green, blue):
        return self.post("led", {"red": red, "green": green, "blue": blue})

    def videos_display(self, url, layer):
        return self.post("videos/display", {"URL": url, "Layer": layer})

    def webviews_display(self, url):
        return self.post("webviews/display", {"URL": url})

    def pause_audio(self,):
        return self.post("audio/pause", {  })

    def get_image_list(self):
        return self.get("images/list")

    def get_blink_settings(self):
        return self.get("blink/settings")
    
    def play_audio(self, filename):
        return self.post("audio/play", {"FileName": filename})

    def trigger_skills_event(self, skill, eventname, payload, customkey, anotherkey, source):
        return self.post("skills/event", {"Skill": skill, "EventName": eventname, "Payload": payload, "CustomKey": customkey, "AnotherKey": anotherkey, "Source": source})
    
    def set_blink(blink):
        return self.post("blink", {"Blink": blink})
    
    def set_blink_settings(self, blinkimages, openeyeminms, openeyemaxms, closedeyeminms, closedeyemaxms, reverttodefault):
        return self.post("blink/settings", {"BlinkImages": blinkimages, "OpenEyeMinMs": openeyeminms, "OpenEyeMaxMs": openeyemaxms, "ClosedEyeMinMs": closedeyeminms, "ClosedEyeMaxMs": closedeyemaxms, "RevertToDefault": reverttodefault})


Chuck = Misty("172.22.174.127")

print(Chuck.delete("images",{"FileName" : "diglett.png"}))

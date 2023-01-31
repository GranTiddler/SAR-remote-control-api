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
    
    def set_blink(self, blink):
        return self.post("blink", {"Blink": blink})
    
    def set_blink_settings(self, blinkimages, openeyeminms, openeyemaxms, closedeyeminms, closedeyemaxms, reverttodefault):
        return self.post("blink/settings", {"BlinkImages": blinkimages, "OpenEyeMinMs": openeyeminms, "OpenEyeMaxMs": openeyemaxms, "ClosedEyeMinMs": closedeyeminms, "ClosedEyeMaxMs": closedeyemaxms, "RevertToDefault": reverttodefault})
    
    def speak(self, text, flush, utteranceid):
        return self.post("tts/speak", {"Text": text, "Flush": flush, "UtteranceId": utteranceid})
    
    def transition_led(self, red, green, blue, red2, green2, blue2, transitiontype, timems):
        return self.post("led/transition", {"Red": red, "Green": green, "Blue": blue, "Red2": red2, "Green2": green2, "Blue2": blue2, "TransitionType": transitiontype, "TimeMS": timems})
    
    def set_display_settings(self, on):
        return self.post("display/settings", {"On": on})
    
    def set_flashlight(self, on,):
        return self.post("flashlight", {"On": on})
    
    def set_image_display_settings(self, layer, size, weight, style, wrap, horizontalalignment, verticalalignment, red, green, blue):
        return self.post("images/settings", {"Layer": layer, "Size": size, "Style": style, "Wrap": wrap, "HorizontalAlignment": horizontalalignment, "VerticalAlignment": verticalalignment, "Red": red, "Green": green, "Blue": blue})
    
    def set_video_display_settings(self, layer, width, height, rotation, repeat, reverttodefault, deleted, visible, opacity, stretch, placeontop, verticalalignment, horizontalalignment):
        return self.post("videos/settings", {"Layer": layer, "Width": width, "Height": height, "Rotation": rotation, "Repeat": repeat, "RevertToDefault": reverttodefault, "Deleted": deleted, "Visible": visible, "Opacity": opacity, "Stretch": stretch, "PlaceOnTop": placeontop, "VerticalAlignment": verticalalignment, "HorizontalAlignment": horizontalalignment})
    
    def set_webview_display_settings(self, layer, visible, reverttodefault, deleted, width, height, stretch, placeontop, horizontalalignment, verticalalignment):
        return self.post("webviews/settings", {"Layer": layer, "Visible": visible, "RevertToDefault": reverttodefault, "Deleted": deleted, "Width": width, "Height": height, "Stretch": stretch, "PlaceOnTop": placeontop, "HorizontalAlignment": horizontalalignment, "VerticalAlignment": verticalalignment})
    
    def send_external_request(self, method, resource, save, apply, filename, authorizationType, Token, Arguments, ContentType):
        return self.post("request", {"Method": method, "Resource": resource, "Save": save, "Apply": apply, "FileName": filename, "authorizationType": authorizationType, "Token": Token, "Arguments": Arguments, "ContentType": ContentType})
    
    def drive(self, linearvelocity, angularvelocity):
        return self.post("drive", {"LinearVelocity": linearvelocity, "AngularVelocity": angularvelocity})
    
    def drive_arc(self, heading, radius, timems, reverse):
        return self.post("drive/arc", {"Heading": heading, "Radius": radius, "TimeMs": timems, "Reverse": reverse})
    
    def drive_heading(self, heading, distance, timems, reverse):
        return self.post("drive/hdt", {"Heading": heading, "Distance": distance, "TimeMs": timems, "Reverse": reverse})
    

    



Chuck = Misty("172.22.174.127")

print(Chuck.delete("images",{"FileName" : "diglett.png"}))

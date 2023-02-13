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


    def videos_display(self, url, layer):
        return self.post("videos/display", {"URL": url, "Layer": layer})

    def get_image_list(self):
        return self.get("images/list")

    def get_blink_settings(self):
        return self.get("blink/settings")

    def audio(self, filename, data, immediatelyapply, overwriteexisting):
        return self.post({"FileName": filename, "Data": data, "ImmediatelyApply": immediatelyapply, "OverwriteExisting": overwriteexisting})

    def change_led(self, red, green, blue):
        return self.post("led", {"red": red, "green": green, "blue": blue})


    def webviews_display(self, url):
        return self.post("webviews/display", {"URL": url})

    def pause_audio(self,):
        return self.post("audio/pause", {  })


    #! Skill management stuff
    def cancel_skill(self, skill):
        return self.post("skills/cancel", {"Skill": skill})


    def get_blink_settings(self):
        return self.get("blink/settings")
    
    def play_audio(self, filename, volume):
        return self.post("audio/play", {"FileName": filename, "Volume": volume})

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
    
    def set_display_settings(self, reverttodefault):
        return self.post("display/settings", {"RevertToDefault": reverttodefault})
    
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
    
    def save_audio(self, filename, data, immediatelyapply, overwriteexisting):
        return self.post("videos", {"FileName": filename, "Data": data, "ImmedatelyApply": immediatelyapply, "OverwriteExisting": overwriteexisting})

    def drive_time(self, linearvelocity, angularvelocity, timems, degrees):
        return self.post("drive/time", {"LinearVelcoity": linearvelocity, "AngularVelocity": angularvelocity, "TimeMS": timems, "Degrees": degrees})

    def drive_track(self, lefttrackspeed, righttrackspeed):
        return self.post("drive/track", {"LeftTrackSpeed": lefttrackspeed, "RightTrackSpeed": righttrackspeed})

    def halt(self):
        return self.post("halt",{})

    def move_arm(self, arm, position, velocity, units):
        return self.post("arms", {"Arm": arm, "Position": position, "Units": units, "Velocity": velocity})

    def move_arms(self, leftarmposition, rightarmposition, leftarmvelocity, rightarmvelocity, units):
        return self.post("arms/set", {"LeftArmPosition": leftarmposition, "RightArmPosition": rightarmposition, "LeftArmVelocity": leftarmvelocity, "RightArmVelocity": rightarmvelocity, "Units": units})

    def move_head(self, pitch, roll, yaw, velocity, units, duration):
        return self.post("head", {"Pitch": pitch, "Roll": roll, "Yaw": yaw, "Velocity": velocity, "Units": units, "Duration": duration})
    
    def stop(self, hold):
        return self.post("drive/stop", {"Hold": hold})
    
    def drive_to_location(self, destination):
        return self.post("drive/coordinates", {"Destination": destination})
    
    def follow_path(self, path, velocity, fullspinduration, waypointaccuracy, rotatethreshold):
        return self.post("drive/path", {"Path": path, "Velocity": velocity, "FullSpinDuration": fullspinduration, "WaypointAccuracy": waypointaccuracy, "RotateThreshold": rotatethreshold})
    
    def rename_slam_map(self, key, name):
        return self.post("slam/map/rename", {"Key": key, "Name": name})
    
    def slam_reset(self, ):
        return self.post("slam/reset", { })
    
    def set_current_slam_map(self, key):
        return self.post("slam/map/current", {"Key": key})
    
    def set_slam_ir_exposure_gain(self, exposure, gain):
        return self.post("slam/settings/ir", {"Exposure": exposure, "Gain": gain})
    
    def set_slam_visible_exposure_gain(self, exposure, gain):
        return self.post("slam/settings/visible", {"Exposure": exposure, "Gain": gain})
    
    def start_locating_docking_station(self, startstreamingtimeout, enableirtimeout, enableautoexposure):
        return self.post("slam/docking/start", {"StartStreamingTimeout": startstreamingtimeout, "EnableIrTimeout": enableirtimeout, "EnableAutoExposure": enableautoexposure})
    
    def start_mapping(self):
        return self.post("slam/map/start", {})
    
    def start_slam_streaming(self):
        return self.post("slam/streaming/start", {})
    
    def start_tracking(self):
        return self.post("slam/track/start", {})
    
    def stop_locating_docking_station(self, stopstreamingtimeout, disableirtimeout):
        return self.post("slam/docking/stop", {"StopStreamingTimeout": stopstreamingtimeout, "DisableIrTimeout": disableirtimeout})
    
    def stop_mapping(self):
        return self.post("slam/map/stop", {})
    
    def stop_slam_streaming(self):
        return self.post("slam/streaming/stop", {})
    
    def stop_tracking(self):
        return self.post("slam/track/stop",{})
    
    def update_hazard_settings(self, reverttodefault, disabletimeofflights, disablebumpsensors, bumpsensorsenabled, sensorname, enabled, timeofflightthreshold, threshold):
        return self.post("hazard/updatebasesettings", {"RevertToDefault": reverttodefault, "DisableTimeOfFlights": disabletimeofflights, "DisableBumpSensors": disablebumpsensors, "BumpSensorsEnabled": bumpsensorsenabled, "sensorName": sensorname, "enabled": enabled, "TimeOfFlightThreshold": timeofflightthreshold, "threshold": threshold})
    
    def cancel_face_training(self):
        return self.post("faces/training/cancel", {})
    
    def capture_speech(self, requirekeyphrase, overwriteexisting, maxspeechlength, silencetimeout):
        return self.post("audio/speech/capture", {"RequireKeyPhrase": requirekeyphrase, "OverwriteExisting": overwriteexisting, "MaxSpeechLength": maxspeechlength, "SilenceTimeout": silencetimeout})
    
    def capture_speech_azure(self, requirekeyphrase, overwriteexisting, maxspeechlength, silencetimeout, capturefile, speechrecognitionlanguage, azurespeechkey, azurespeechregion):
        return self.post("audio/speech/capture", {"RequireKeyPhrase": requirekeyphrase, "OverwriteExisting": overwriteexisting, "MaxSpeechLength": maxspeechlength, "SilenceTimeout": silencetimeout, "CaptureFile": capturefile, "SpeechRecognitionLanguage": speechrecognitionlanguage, "AzureSpeechKey": azurespeechkey, "AzureSpeechRegion": azurespeechregion})
    
    
    
    



    def delete_skill(self, skill):
        return self.delete("skills", {"Skill": skill})


    def get_running_skills(self):
        return self.get("skills/running")

    def get_skills(self):
        return self.get("skills")

    def load_skill(self, skill):
        return self.post("skills/load", {"Skill": skill})
        
    def reload_skills(self):
        return self.post("skills/reload")

    def run_skill(self, skill):
        return self.post("skills/start", {"Skill": skill})

    def upload_skill(self, file, run_immedeiately, overwrite):
        return self.post("skills", {"File" : file, "ImmedeatelyApply" : run_immedeiately, "OverwriteExisting" : overwrite})


Chuck = Misty("172.22.174.127")

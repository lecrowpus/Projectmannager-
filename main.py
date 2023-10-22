import GUI
import os,json
import threading
import backend
import requests
from tkinter import *
class backend_process:
    def __init__(self) -> None:
        self.bp=backend.backendworks()
        pass
    def getModules_dict(self):
        Temp_Modules={"modules":{}}
        return Temp_Modules
    def getModule(self,mdlname,version):
        url = f"https://pypi.org/pypi/{mdlname}/json"
        response = requests.get(url)
        if  response.status_code == 200:
            version=str(version)
            if version in response.json()["releases"] or version=="":
                return True
            else:
                return "no such version"
        else:
            return "no such module"
    def getmodules_json(self,dir):
        with open(dir, "r") as json_file:
            data = json.load(json_file)
        return data
    def createproj(self,r,st,sr,rq,d,md):
        readmevalue,staticvalue,srcvalue,reqvalue,dirr,mdldata=r,st,sr,rq,d,md
        THred1 = threading.Thread(target=self.bp.stratproject,args=(readmevalue,staticvalue,srcvalue,reqvalue,dirr,mdldata,))
        THred1.start()
if __name__=="__main__":
    app=GUI.App()
    app.loop()
    pass
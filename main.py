import GUI
import os,json
import threading
import backend
import requests
from tkinter import *
class backend_process:
    def __init__(self,CWP) -> None:
        self.bp=backend.backendworks(CWP=CWP)
        pass
    
    def createproj(self,r,st,sr,rq,d,md):
        CreateProject_thread = threading.Thread(target=self.bp.stratproject,args=(r,st,sr,rq,d,md,))
        CreateProject_thread.start()
if __name__=="__main__":
    app=GUI.App()
    app.loop()
    pass
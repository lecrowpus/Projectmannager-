import customtkinter as ctk
import customtkinter
from tkinter import filedialog
from tkinter import *
import os,time
import main
import threading
import json
from tkinter import messagebox

class App(customtkinter.CTk):
    def __init__(self):
        #all configuration
        self.bk=main.backend_process()
        super().__init__()
        customtkinter.set_appearance_mode("system")  
        ctk.set_default_color_theme("dark-blue")
        self.title("my app")
        self.geometry("1000x600")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        

        # defining variables
        self.moduleCheckBoxList_name=[]#this list contains the checkbox that are created in for loop
        self.moduleversionList_version=[]
        self.Mdnvrlist=[]
        self.moduledata=self.bk.getModules_dict()
        self.ddir="None"
        
        #crating main frames
        self.nav=ctk.CTkFrame(self,bg="blue")
        self.nav.grid(sticky="ns",padx=10,pady=10)

        self.startbtn=ctk.CTkButton(self.nav,text="➕ New project",fg_color="#0286fa",command=self.Frame_createprojframe)
        self.startbtn.grid(column=0,padx=10,pady=10)
        with open('data.json', 'r') as file:
            ProjectData = json.load(file)
        for project in ProjectData["Project"]:
            viewProvectbtn=ctk.CTkButton(self.nav,text=project,command=lambda i=project: self.viewProjectFunc(projectName=i))
            viewProvectbtn.grid(column=0,padx=10,pady=10)
        

        self.workspaceFrame=ctk.CTkFrame(self,bg="blue")
        self.workspaceFrame.grid(row=0,column=1,sticky="nsew",pady=10)
        self.workspaceFrame.grid_columnconfigure(1, weight=200)
        self.workspaceFrame.grid_rowconfigure(0,weight=200)

        self.python_projsettings=ctk.CTkFrame(self.workspaceFrame)
        self.python_projsettings.grid(column=1,row=0,sticky="nsew",padx=10,pady=10)
        # creating widgets of CreateNewProject 
        self.python_projsettings.grid_columnconfigure(1,weight=2)
        self.python_projsettings.grid_columnconfigure(1,weight=20)
        self.python_projsettings.grid_rowconfigure(6,weight=2)

        """all the widgets for the create python project """
        self.ChooseDir=ctk.CTkButton(self.python_projsettings,text="Choose folder",command=self.choosedir)
        
        self.path_lable=ctk.CTkLabel(self.python_projsettings,text="placeholder/path/to/project")
        
        self.rdcheck=IntVar()
        self.readmecheck=ctk.CTkCheckBox(self.python_projsettings,text="Readme",onvalue=1,variable=self.rdcheck)
        
        self.staticcheckvar=IntVar()
        self.staticcheck=ctk.CTkCheckBox(self.python_projsettings,text="Static folder",onvalue=1,variable=self.staticcheckvar)
        
        self.reqcheckvar=IntVar()
        self.ReqTxtCheck=ctk.CTkCheckBox(self.python_projsettings,text="Req.txt",onvalue=1,variable=self.reqcheckvar)
        
        self.srcditcheck=IntVar()
        self.SrcDirCheck=ctk.CTkCheckBox(self.python_projsettings,text="SourceCode folder",onvalue=1,variable=self.srcditcheck)    
        
        self.createbtn=ctk.CTkButton(self.python_projsettings,text="Create",fg_color="#0286fa",command=self.createproject)
        
        self.addMbtn=ctk.CTkButton(self.python_projsettings,text="✔️",fg_color="#32a852",width = 50 ,command=self.addmodule)
        self.remMbtn=ctk.CTkButton(self.python_projsettings,text="❌",fg_color="#a83232",width = 50,command=self.remmodule)
        
        self.VersionWariningLable=ctk.CTkLabel(self.python_projsettings,text="invalid version ",text_color="red")


        self.versionVar=StringVar()
        self.versionentry=ctk.CTkEntry(self.python_projsettings,textvariable=self.versionVar)

        self.ModuleWariningLable=ctk.CTkLabel(self.python_projsettings,text="invalid module",text_color="red")

        self.moduleVar=StringVar()
        self.moduleEntey=ctk.CTkEntry(self.python_projsettings,textvariable=self.moduleVar)

        self.modulenameframe=ctk.CTkFrame(self.python_projsettings)
        self.moduleversionframe=ctk.CTkFrame(self.python_projsettings)
        
        
        # self.addmodulesentryes(moduledata_=self.moduledata)
        
        """all the wordgets for Viewing creted project """

        #display the modules installed
        #Git
    
    def viewProjectFunc(self,projectName):
        with open('data.json', 'r') as file:
            ProjectData = json.load(file)
        dir=str(ProjectData["Project"][projectName]["settings"]).replace("/", "\\")
        self.modulenameframe.grid(row=6,column=1,sticky="nwe",padx=10,columnspan=3)
        self.moduleversionframe.grid(row=6,column=0,sticky="nwe",padx=10)
        self.moduledata=self.bk.getmodules_json(dir=str(dir))
        print(self.moduledata)
        self.addmodulesentryes(moduledata_=self.moduledata)
    def addmodulesentryes(self,moduledata_):
        
        self.moduleCheckBoxList_name=[]
        self.moduleVersionList_version=[]
        self.Mdnvrlist=[]

        self.Mdnlist=[]
    
        for item in moduledata_["modules"]:
            varMdn=StringVar()
            self.Mdnlist.append(varMdn)
            mdlNamecheckB=ctk.CTkCheckBox(self.modulenameframe,text=item,variable=varMdn,onvalue=item,offvalue="off")
            self.moduleCheckBoxList_name.append(mdlNamecheckB)
            
            mdlVersioncheckB=ctk.CTkLabel(self.moduleversionframe,text=self.moduledata["modules"][item])
            self.moduleCheckBoxList_name.append(mdlVersioncheckB)
    def blank(self,*args):
        print(args)
        pass
    def Frame_createprojframe(self):
        self.ChooseDir.grid(padx=10,pady=10)
        self.path_lable.grid(column=1,row=0,sticky="w",padx=10,columnspan=10)
        self.readmecheck.grid(row=1,column=0,sticky="nw",padx=10,pady=30)
        self.staticcheck.grid(row=2,column=0,sticky="nw",padx=10)
        self.ReqTxtCheck.grid(row=1,column=1,sticky="nw",padx=10,pady=30)
        self.SrcDirCheck.grid(row=2,column=1,sticky="nw",padx=10)
        self.createbtn.grid(column=1,row=3,padx=10,pady=30,sticky="nw")
        self.addMbtn.grid(column=2,row=5,padx=10,pady=30,sticky="n")
        self.remMbtn.grid(column=3,row=5,padx=10,pady=30,sticky="n")

        self.versionentry.grid(row=5,column=0,sticky="we",padx=10,pady=10)
        self.moduleEntey.grid(row=5,column=1,sticky="we",padx=10,pady=10)
        
        self.modulenameframe.grid(row=6,column=1,sticky="nswe",padx=10,columnspan=3)
        self.moduleversionframe.grid(row=6,column=0,sticky="nswe",padx=10)
        for Cb in self.moduleCheckBoxList_name:
            Cb.grid(padx=10,pady=10)
        for Cb in self.moduleVersionList_version:
            Cb.grid(padx=10,pady=10)
        self.startbtn.configure(state="disabled")
    def Frame_remprojframe(self):
        self.python_projsettings.grid_forget()
        for Cb in self.moduleCheckBoxList_name:
            Cb.grid_forget()
        for Cb in self.moduleVersionList_version:
            Cb.grid_forget() 
        self.startbtn.configure(state="normal")
        
    def loop(self):
        self.mainloop()

    def choosedir(self):
        self.ddir=filedialog.askdirectory()
        self.path_lable.configure(text=self.ddir)
        
    def addmodule(self):
        if self.bk.getModule(self.moduleVar.get(),self.versionVar.get())=="no such module":
            self.ModuleWariningLable.grid(row=4,column=1,sticky="s")
            
            
        elif self.bk.getModule(self.moduleVar.get(),self.versionVar.get())=="no such version":
            self.VersionWariningLable.grid(row=4,column=0,sticky="s")
            
        else:
            
            self.ModuleWariningLable.grid_forget()
            self.VersionWariningLable.grid_forget()
            for Cb in self.moduleCheckBoxList_name:
                Cb.grid_forget()
            for Cb in self.moduleVersionList_version:
                Cb.grid_forget()
            
            # tempdict={self.moduleVar.get():self.versionVar.get()}
            self.moduledata["modules"][self.moduleVar.get()] = str(self.versionVar.get())
            
            self.addmodulesentryes()
            for Cb in self.moduleCheckBoxList_name:
                Cb.grid(padx=10,pady=10)
            for Cb in self.moduleVersionList_version:
                Cb.grid(padx=10,pady=10)

            
    def remmodule(self):
        for Cb in self.moduleCheckBoxList_name:
            Cb.grid_forget()
        for Cb in self.moduleVersionList_version:
            Cb.grid_forget()
        
        

        # Step 2: Remove the item from the dictionary
        i=0
        for var_ in self.Mdnlist:
            if var_.get() != "off":
                if var_.get() in self.moduledata["modules"]:
                    del self.moduledata["modules"][var_.get()]
                    var_.set(0)
                    self.Mdnlist.remove(var_)
                    self.moduleCheckBoxList_name.pop(i)

            i=i+1
        self.addmodulesentryes()
        for Cb in self.moduleCheckBoxList_name:
            Cb.grid(padx=10,pady=10)
        for Cb in self.moduleVersionList_version:
            Cb.grid(padx=10,pady=10)
        pass    
    def createproject(self):
        if self.ddir=="None":
            messagebox.showwarning("Warning", "Choose the directory!")
            return True
        self.bk.createproj(r=self.rdcheck.get(),st=self.staticcheckvar.get(),sr=self.srcditcheck.get(),rq=self.reqcheckvar.get(),d=self.ddir,md=self.moduledata)

        self.Frame_remprojframe()
if __name__=="__main__":

    app = App()
    app.mainloop()
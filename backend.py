import os,json
import requests

class backendworks:
    def __init__(self,CWP) -> None:
        self.Current_working_project=str(CWP) 
        with open('data.json', 'r') as file:
            data = json.load(file)
        self.CWD_env=data["Project"][self.Current_working_project]["env"]
        self.CWD_settings=data["Project"][self.Current_working_project]["settings"]
        self.CWD_path=data["Project"][self.Current_working_project]["path"].replace("/", "\\")
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
    def getmodules_json(self):
        # with open(self.CWD_settings, "r") as settings_porject:
        #     data = json.load(settings_porject)
        # return data
        modules_versions_dict = {"modules":{}}

        # Read information from req.txt and populate the dictionary
        with open(f"{self.CWD_path}\\requirements.txt", 'r') as file:
            for line in file:
                # Split the line into module name and version
                module_name, module_version = line.strip().split('==')
                # Add the module and its version to the dictionary
                modules_versions_dict["modules"][module_name] = module_version

        # Print the resulting dictionary
        return modules_versions_dict
    def stratproject(self,readmevalue,staticvalue,srcvalue,reqvalue,dirr,mdldata,*args):
        cwd=os.getcwd()
        os.chdir(dirr)
        os.system("virtualenv env ")
        os.system(f"{dirr}/env/Scripts/activate")
        print(mdldata["modules"])
        for mdls in mdldata["modules"]:
            verison_ofmdl=str(mdldata['modules'][mdls]).replace("/",".")
            if verison_ofmdl=="":
                os.system(f"""{dirr}/env/Scripts/activate && pip install {str(mdls)}""")
            else:    
                os.system(f"""{dirr}/env/Scripts/activate && pip install {str(mdls)}=={verison_ofmdl}""")
        if readmevalue==1:
            with open("README.md","w+") as readMeFile:
                readMeFile.write("# readme.md")
                pass
        if staticvalue==1:
            os.mkdir(f"{dirr}/static")
        if srcvalue==1:
            os.mkdir(f"{dirr}/src")
        if reqvalue==1:
            os.system(f"""{dirr}/env/Scripts/activate && pip freeze > requirements.txt""")
            # with open("requirements.txt","w"):
            #     pass

        with open("setting.json","w+") as settings:
            json.dump(mdldata, settings, indent=4)

        os.chdir(cwd)
        with open('data.json', 'r') as file:
            data = json.load(file)
        last_directory = os.path.basename(os.path.normpath(dirr))
        DataTemplate={"language": "Python",
            "path": dirr,
            "env": f"{dirr}/env/Scripts/activate.bat",
            "settings": f"{dirr}/setting.json"}
       
        # Step 2: Modify the data
        data["Project"][last_directory] = DataTemplate

        # Step 3: Write back to the JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.changeproject(last_directory)
        with open(f"{self.CWD_path}\\requirements.txt", 'w') as req_file:
            for module, version in self.getmodules_json().items():
                req_file.write(f"{module}=={version}\n")

    def changeproject(self,CWP):
        self.Current_working_project=str(CWP) 
        with open('data.json', 'r') as file:
            data = json.load(file)
        self.CWD_env=data["Project"][self.Current_working_project]["env"]
        self.CWD_settings=data["Project"][self.Current_working_project]["settings"]
        self.CWD_path=data["Project"][self.Current_working_project]["path"].replace("/", "\\")
    def Uninstall_Modules(self,Mdl):
        os.chdir(self.CWD_path)
        with open("setting.json","r")as file:
            data=json.load(file)
        
        for module in Mdl:
            os.system(f"""{self.CWD_path}/env/Scripts/activate && echo y | pip uninstall {str(module)}""")
            print(Mdl)
            del data["modules"][module]
       
        with open(f"{self.CWD_path}\\requirements.txt", 'w') as req_file:
            for module, version in self.getmodules_json().items():
                req_file.write(f"{module}=={version}\n")
          
    def Install_Module(self,modules_To_install):
        os.chdir(self.CWD_path)
        os.system(f"{self.CWD_path}/env/Scripts/activate")
        for mdls in modules_To_install:
            verison_ofmdl=str(modules_To_install[mdls]).replace("/",".")
            if verison_ofmdl=="":
                os.system(f"""{self.CWD_path}/env/Scripts/activate && pip install {str(mdls)}""")
            else:    
                os.system(f"""{self.CWD_path}/env/Scripts/activate && pip install {str(mdls)}=={verison_ofmdl}""")
        with open(f"{self.CWD_path}\\requirements.txt", 'w') as req_file:
            for module, version in self.getmodules_json().items():
                req_file.write(f"{module}=={version}\n")

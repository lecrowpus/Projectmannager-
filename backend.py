import os,json
class backendworks:
    def __init__(self) -> None:
        pass
    def stratproject(self,readmevalue,staticvalue,srcvalue,reqvalue,dirr,mdldata,*args):
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
        
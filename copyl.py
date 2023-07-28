import shutil
import os

class filehandling:
    def __init__(self,dest,src):
        self.destination=dest
        self.source=src

    def copy(self):
        try:
            if os.path.isfile(self.destination+"/"+self.source):
                # os.remove(self.destination+"/"+self.source)
                return "file already Exits"
            else:
                t=shutil.copy(self.source,self.destination)
                result=f"file copied to new location : {self.destination}"
                return result
            
        except FileExistsError:
             return "File already existed"
        
    def removefile(self):
        try:
            if os.path.isfile(self.destination+"/"+self.source):
                os.remove(self.destination+"/"+self.source)
                return "File removed"
        except :
            return f"file {self.destination} not found"
        


    def replaced(self):
        try:
            if os.path.isfile(self.destination):
                shutil.copyfile(self.source,self.destination)
                return "File is overwritted successfully"
            else:
                return "File Not Found"
            
        except FileNotFoundError:
            return "File doesn't Exits"


    def rename(self,Nname):
        try:
            if os.path.isfile(self.destination):
                os.rename(self.source,Nname)
                return f"File Renamed Successfully"
            else:
                return "File Not Found"
            
        except IsADirectoryError:
            return "source is file but destination is the directory"
  
        except NotADirectoryError:
            return "source is directory but destination is file"
        


if __name__=="__main__":
    
    source=input("Enter the Source path of the file: ")
    destination=input("Enter the Destination Path of the file : ")
    j=filehandling(destination,source)
    choice=int(input("Enter the Choice in Number: 1)Copy File 2)Rename file 3)Replace file data :"))
   
    if choice==1:
        print(j.copy())
    elif choice==2:
        newName=input("Enter the new name of the file:")
        print(j.rename(newName))
    elif choice==3:
        print(j.replaced())
       

# AUTHOR : ISHAN SRIVASTAVA 
#E-Mail : srivastava.ishan77gmail.com
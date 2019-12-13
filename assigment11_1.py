'''Design automation script which accept directory name and display checksum of all files.
Usage : DirectoryChecksum.py “Demo”
Demo is name of directory.'''
import sys
import os
import hashlib
import MarvellousChecksum

def Display(path):
    flag = os.path.isabs(path)
    if flag ==False:
        path=os.path.abspath(path)
        
    exists = os.path.isdir(path)
    
    if exists :
        for foldername,subfolder,filname in os.walk(path):
            print("Current folder is :"+foldername)
            for filen in filname:
                path=os.path.join(foldername,filen)
                #print(path)
                file_hash=MarvellousChecksum.hashfile(path)
                return file_hash
            print("----------------------")
            print("")
    else:
        print("Invalid path ")
def main():
    print("-----------Marvellous infosystems-------------")
    print("\n Application name:",sys.argv[0])
    
    if(len(sys.argv)==1):
        print("Error :invalid number of arguments")
        exit()
    if(len(sys.argv)<=2):
        if(sys.argv[1]=='-h') or(sys.argv[1]=='-H'):
            print("This script which accept directory name and display checksum of all files")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : DirectoryChecksum.py “Demo”")
            exit()
        
    
    try:
        arr=Display(sys.argv[1]) 
        print(arr)
    except ValueError:
        print("Error : Invvalied datatype of input ")
    except Exception:
        print("Error : Invalid input ")
    finally:
        print("Thank You  !!!!!")


if __name__=="__main__":
    main()
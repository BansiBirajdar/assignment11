'''Design automation script which accept directory name and write names of duplicate files from
that directory into log file named as Log.txt. Log.txt file should be created into current
directory.
Usage : DirectoryDusplicate.py “Demo”
Demo is name of directory.'''
import sys
import os
import MarvellousChecksum
def DirectoryDusplicate(path):
    flag = os.path.isabs(path)
    if flag ==False:
        path=os.path.abspath(path)
        
    exists = os.path.isdir(path)
    data = {}
    if exists :
        for foldername,subfolder,filname in os.walk(path):

            for filen in filname:
                path=os.path.join(foldername,filen)
                checksum=MarvellousChecksum.hashfile(path)
                
                if checksum in data:
                    data[checksum].append(filen)
                else:
                    data[checksum] = [filen]

        newdata = []
        newdata = list(filter(lambda x: len(x)>1,data.values()))
        #print(newdata)
        count = 0
        line = "-"*40
        fobj = open("Log.txt",'w')
        
        fobj.write(line+"\n")
        fobj.write("Marvellous names of duplicate files\n") 
        fobj.write(line+"\n")
        for outer in newdata:
            icnt = 0;
            for inner in outer:
                icnt+=1;
                if icnt >= 2:
                    count+=1
                    #print("filename",inner)
                    fobj.write(inner+"\n")
        print("Total Duplicate files ",count);
        fobj.close();
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
            print("This script which accept directory name and write names of duplicate files from  \
                that directory into log file named as Log.txt. Log.txt file should be created into current directory")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : DirectoryChecksum.py \
                Demo is name of directory ")
            exit()
    
        try:
            DirectoryDusplicate(sys.argv[1])
        except ValueError:
            print("Error : Invvalied datatype of input ")
        except Exception:
            print("Error : Invalid input ")
        finally:
            print("Thank You  !!!!!")

if __name__=="__main__":
    main()
import Tix
import os
import subprocess
import glob
import Tkinter
import ttk
import tkMessageBox
	
lis=[]	
minn=100000000

pathsave="time\ table"  #path of checkboxes that are checked


dictall={}  #stores all checkboxes
dicti={}


flist=[]  #MAIN

def Finallist():  #FINAL WORK
	#print 'yo'
	for i in flist:
		print i
	
def RunSample(w):
    
    top = Tix.Label(w, padx=20, pady=10, bd=1, relief=Tix.RAISED,
                    anchor=Tix.CENTER, text='Select directories you wish to update\n')

    box = Tix.ButtonBox(w, orientation=Tix.HORIZONTAL)
    box.add('ok', text='OK', underline=0, width=5,
            command=lambda w=w: Finallist())
    box.add('close', text='Cancel', underline=0, width=5,
            command=lambda w=w: w.destroy())
    box.pack(side=Tix.BOTTOM, fill=Tix.X)
    top.pack(side=Tix.TOP, fill=Tix.BOTH, expand=1)

def doit():
	global minn
	minn=100000000
	for root, dirs, files in os.walk("/home/varun/Desktop/KNUTH"):
	    path = root.split('/')
	    minn=min(minn,len(path)-1)
	    y=(len(path) - 1-minn) *'-' +    os.path.basename(root)   
	    if y!='.':
	    	lis.append(y)
	    for file in files:
		x=(len(path)-minn)*'-'+file
		if x!='.':
			lis.append(x)

class View(object):
    def dashcount(self,x):
	count=0	
	for i in range(0,len(x)):
		if x[i]!='-':
			break
		else:
			count=count+1	
	return count		
    def removedash(s):
    	ind=0
    	while s[ind]=='-':
    		ind=ind+1
    	ret=s[ind:len(s)-1]
    	return ret	

    def __init__(self, root):
    	RunSample(root)
        self.root = root
        self.makeCheckList()
        
        
    def makeCheckList(self):
    	
        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        self.cl.pack()
   	count=1
   	self.cl.config(height=700)
   	self.cl.config(width=700)
    	for i in lis:
    		cn=self.dashcount(i)
    		if cn in dicti:
    			dicti[cn]=dicti[cn]+1
    		else:
    			dicti[cn]=1
    		self.cl.hlist
    		if 1 in dicti:
	    		s="CL"+str(dicti[1])
	    		for j in range(cn-1):
	    			if j+2 in dicti:
	    				s=s+"."+str(dicti[j+2])
	    		print s
	    		dictall[s]=i
	    		foo=str(i)
	    		foo=foo.lstrip('-')
	    		self.cl.hlist.add(s,text=foo)	
	    		self.cl.setstatus(s,"off")
	    		self.cl.autosetmode()	
	# print dicti	

    def selectItem(self, item):
        #print item, self.cl.getstatus(item)
        what=item
        lenn=len(what)
        for i in dictall:
        	if i[0:lenn]==what:
        		self.cl.setstatus(i,self.cl.getstatus(item))
        		print i,self.cl.getstatus(i)
        		till=dictall[i]
        		till=till.lstrip('-')
        			
        		#print pathsave+"/"+str(till)
        		
        		if self.cl.getstatus(i)=="on":
        			flist.append(pathsave+"/"+str(till))
        		elif self.cl.getstatus(i)=="off":
        			flist.remove(pathsave+"/"+str(till))	
        		
        		
        		
        	


def main():
    root = Tix.Tk()
    
    root.geometry('{}x{}'.format(1000,1000))
	
    view = View(root)
    
    root.update()

    root.mainloop()
    
if __name__ == '__main__':    
    #unmount="""sudo umount -f -a -t cifs -l"""
    #mount="""sudo mount -t cifs //fileserver2/Study\ Material/time\ table /home/varun -o user=13103535,password=9899496277,workgroup=workgroup,ip=172.16.68.30"""
    #c=subprocess.check_output(unmount, shell=True)
    #b= subprocess.check_output(mount, shell=True)
    doit()
    main()
    #RunSample(root)

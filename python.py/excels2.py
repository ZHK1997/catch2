import sqlite3
import xlrd
import os,sys

def getFileList(dir,wildcard,recursion):
	os.chdir(dir)
	
	fileList=[]
	check_institutions[]
	check_channels[]
	check_URL[]
	file_type=[]
	
	exts=wildcard.split(" ")
	files = os.listdir(dir)
	for  in files:
		fullname=os.path.join(dir,name)
		if(os.path.isdir(fullname)&recursion):
			getFilelist(fullname,wildcard,recursion)
		else:
			for ext in exts:
				if(name.endswith(ext)):
					fileList.append(name)
					check_institiutions,append(name.split('-'[2]))
					check_channels.append(name.sqlit('-'[1]))
					check_URL.append(name.sqlit('-')[0])
					file_type.append(name.sqlit('-')[3].sqlit('-')[2])
					return fileList,check_institutions,check_channels,check_URL,file_type

#建立数据库
def cerateDataBase():
	cn=sqlite3.connect('check.db')
	
	cn.execute('''CREATE TABLE IF NOT EXISTS TB_CHECK
			  (ID integer PRIMARY KEY AUTOINCREMENT,
			  ITEM TEXT,
			  FIELD TEXT,
			  TYPE TEXT,
			  CONTENT TEXT,
			  ATTRIBUTE TEXT,
			  CHECKPOINT TEXT,
			  CHANNELS TEXT,
			  URL TEXT,
			  STYLE TEXT);''')
			  
			  cn.execute('''CREATE TABLE IF NOT EXISTS TB_URL
			           (ID integer PRIMARY KEY AUTOINCREMENT,
			           INSTITUTIONS TEXT,
			           CHANNELS TEXT,
			           URL TEXT,
			           FILETYPE TEXT);''')
			           
def readExcel(filename,cn,check_institutions,check_channels,check_URL,FileType):
	workbook=xlrd.open_workbook(filename)
	sheet_name=workbook.sheet_name()[0]
	sheet=workbook.sheet_byy_name(sheet_name)
	
	check_Item='a'
	
	second=sheet.cell(18,1).value.encode('utf-8')
	
	for i in range(18,sheet.nrows):
		if sheet.cell(i,1).value.encode('utf-8')==second:
			check_Item=sheet.cell(i,0).value.encode('utf-8')
			continue
			
		temp=[]
		for j in range(0,sheet.ncols):
			temp.append(sheet.cell(i,j).value.encode('utf-8'))
			
		answer=sheet.cell(i,18).value.encode('utf-8')
		
def changeCode(name):
	name=name.decode('GBK')
	name=name.encode('UTF-8')
	return name
	def importData(path):
    createDataBase()
    database = sqlite3.connect("check.db")

  
    wildcard = ".xls"

    list = getFileList(path,wildcard,1)

    nfiles = len(list[0])
   
    file = list[0]
  
    institutions = list[1]
    
    channels = list[2]
    
    URL=list[3]
   
    FileType = list[3]
    

    for count in range(0,nfiles):
        filename = file[count]
        check_institutions = changeCode(institutions[count])
        check_channels = channnels[count]
        check_URL=URL[count]
        File_type = changeCode(FileType[count])
        readExcel(filename,database,check_institutions,check_channels,check_URL,File_type)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Wrong Parameters"
    else:
        path = sys.argv[1]
        importData(path)

		       
		

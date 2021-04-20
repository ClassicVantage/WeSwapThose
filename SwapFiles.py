def SwapThoseFiles():
    FileName1=input("FileName1=")
    FileName2=input("FileName2=")

    file1=open(FileName1,'r')
    file2=open(FileName2,'r')

    Data1=file1.read()
    Data2=file2.read()

    file1=open(FileName1,'w')
    file1.write(Data2)

    file2=open(FileName2,'w')
    file2.write(Data1)

SwapThoseFiles()


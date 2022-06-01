import csv
def write_info_csv(info_list):

   with open('studentinfo.csv','a',newline='') as csv_file:

     writer=csv.writer(csv_file)

     if csv_file.tell() ==0 :

        writer.writerow(["name","age","job","dob"])
    
     writer.writerow(info_list)



Condition=True

while(Condition):
    
    studentinfo=input("enter student information IN THE FORMAT OF :NAME,AGE,JOB,DOB:")
    print("ENTERED VALUE" + studentinfo)


    spt=studentinfo.split(" ")
    print("table",spt)
    print("\n The entered infos-\nname: {}\nage: {}\njob : {} \ndob : {}"
            .format( spt[0], spt[1], spt[2], spt[3]))
    
    write_info_csv(spt)
    
    Con=input("if you want to enter another student data YES (or) NO :" )

    if Con=="yes":
    
        Condition=True

    elif Con=="no":

        Condition=False
   

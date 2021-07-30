import csv
import os
files=os.listdir('C:\\Users\\RidgeHood\\Desktop\\MashupStacks-projects\\python\\testfolder')
write_permission=os.access('C:\\Users\\RidgeHood\\Desktop\\MashupStacks-projects\\python', os.W_OK)

print(write_permission)


  


def file_reader(file_name):

    extention_check = os.path.splitext(file_name)

    if extention_check[1]=='.csv':

        import csv 
        with open(f'C:\\Users\\RidgeHood\\Desktop\\MashupStacks-projects\\python\\testfolder\\{file_name}','r') as samp:
         read=csv.reader(samp) 
         exp=[]
         for x in read:
             exp.append(x)

    if exp:
        return exp




if write_permission==True:

    new_file=[]

    for i in range(len(files)):
        
        csvfile_individual=file_reader(files[i])
        if csvfile_individual:
            csvfile_individual.pop(0)
            for j in range(len(csvfile_individual)):
                new_file.append(csvfile_individual[j])



    num=1
    for k in range(len(new_file)):
        new_file[k].pop(0)
        new_file[k].insert(0,num)
        num=num+1



    new_csv=open('merged.csv','w')

    csvwriter=csv.writer(new_csv)

    csvwriter.writerow(['id', 'date', 'location', 'car name', 'model name', 'seller name', 'seller address', 'price'])
    csvwriter.writerows(new_file)
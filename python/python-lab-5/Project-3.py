import csv
with open('projectcsv.csv','r') as car:
    car_read=csv.reader(car)
    csvlist=[]
    header=[]
    for x in car_read:
        csvlist.append(x)
    
    
    print('\nThird row is--\n',csvlist[2])
   
    print('\n2nd column is---\n')
    for i in range(len(csvlist)):
        print(csvlist[i][1])
    
    print('\nFirst 3 lines are----\n')
    y=0
    while y<3:
        print(csvlist[y])
        y=y+1
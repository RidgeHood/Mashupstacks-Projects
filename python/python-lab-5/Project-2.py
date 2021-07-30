import os
files=os.listdir('C:\\Users\\RidgeHood\\Desktop\\MashupStacks-projects\\python\\testfolder')
files.sort()

months={
    '01':'jan',
    '02':'feb',
    '03':'mar',
    '04':'apr',
    '05':'may',
    '06':'jun',
    '07':'jul',
    '08':'aug',
    '09':'sept',
    '10':'oct',
    '11':'nov',
    '12':'dec'
}
for i in range(len(files)) :
    x=files[i][2:4]
    print(f"{months[x]}-{files[i]}")
   


#print(files[5][2:4])
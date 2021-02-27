import time

#colors


red='\033[91m'
b='\033[21m'
gren='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
blue='\033[94m'

print (red+b+"""
 _       _     _ _         __  __     _
| |_ ___| |__ (_) | ____ _|  \/  | __| |_ __
| __/ __| '_ \| | |/ / _` | |\/| |/ _` | '_ \
| || (__| | | | |   < (_| | |  | | (_| | |_) |
 \__\___|_| |_|_|_|\_\__,_|_|  |_|\__,_| .__/
                                       |_|

"""+b+red)

print (gren+b+"            <===[[ coded by tchikamodz ]]===>"+b+gren)
print (" ")
print (yellow+b+"     <---( YouTube/tchikaModz)--->"+b+yellow)
print (" ")

length=int(raw_input(cyan+b+"Entrer le nombre de caractere: "+b+cyan))
print (" ")
name=raw_input(cyan+b+"Nommez votre .txt : "+b+cyan)
tic = time.clock()
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
print (yellow+b+"Generation de la liste!"+b+yellow)
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
lista=[0 for x in xrange(length)]
x=length-1
string="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
list_of_results=[]

file1=file(name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange (length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print (red+b+"<<<========================================>>>"+b+red)
print (" ")
print (gren+b+"Finit en "+str(ttn)+" seconde."+b+gren)
print (" ")
print (gren+b+"Go check "+str(name)+" dans votre repertoire 'tchikamdp' "+b+gren)
print (" ")
print (red+b+"<<<========================================>>>"+b+red)
print (" ")

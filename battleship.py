import random




diff = int(input('choose a level of difficulty from 2 to 10'));
r = [1,2,3,4,5,6,7,8,9,10];
level = r[:diff];
play = int(input('type 1 to play battleship'));

def countships(a):
    shipcount=0;
    for x in a:
        for y in x:
            if y==1:
                shipcount+=1;
    return shipcount;


def newfield(level):
    """ Input is an array, random width and height between 1 and n, returns an array of 0s and 1s with dimensions width x height"""
    x = list(range(random.choice(level)));#choose random number from ordered list called level and create a list from 0 up to the number selected
    y = list(range(random.choice(level)));
    a = [];
    for i in x:
        a.append([]);#so you add x number of empty lists
        for n in y: #nested for loop - eg a[i] where i is the empty list
            rand = random.choice([0,1]);
            a[i].append(rand) #keep adding
    return a; #eg [[1,0],[0,0],[1,0]]

a=newfield(level)
e=countships(a);
'''
def drawfield(a):
"""input will show direct hits, converts array in"""
    z=[];
    for i in a:
        z+=([]);
        for x in i:
            z+=('X');
    z[xattack][yattack]==1;
    print(z);
    return z;
        '''

def battleship(a,e):
    """ where inputs are x, the rows, y, the columns, and a the battlefield. Output is a string"""
    if e==0:
        print('all enemy ships destroyed. Congratulations captain!');
        return;
    print('you have ' + str(e) + ' battleships left to destroy');
    
    xattack = int(input('choose an x attack coordinate between 0 and ' + str(len(a)-1))); #this is width (columns)
    yattack = int(input('choose an y attack coordinate between 0 and ' + str(len(a[0])-1))); #this is height (rows)
    print('# of rows in array is ' + str(len(a)));
    print('number you chose is ' + str(xattack));
    if xattack>=len(a)  or yattack>=len(a[0]):
        print('oops! please stick to the boundaries!');
        battleship(a,e);
    else: 
        if a[xattack][yattack]==1: #1 means there's a ship there
            print('Yeeha! A direct hit!')
            a[xattack][yattack]=2;
            #draw graf here
        
            graf = '' #empty string will print out complete string 
            for i in a: # eg [[1,0],[0,0],[1,0]] i is [1,0]
                graf+='\n' #add new line here
                for l in i:#the columns
                    if l != 2: #where there's no direct hit add an 'X'
                        graf+='X'
                    else:
                        graf+='O'
            print (graf);
            battleship(a,e-1);
        else:
            print('you missed! Try another location');
            #and here
            battleship(a,e);
            


if play == 1:
    battleship(a,e);


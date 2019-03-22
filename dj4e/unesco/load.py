import csv 

from unesco.models import Category, Region, States, Iso, Site

file = open('whc-sites-2018-small_v1.csv')
reader = csv.reader(file)

Category.objects.all().delete()
Region.objects.all().delete()
States.objects.all().delete()
Iso.objects.all().delete()
Site.objects.all().delete()

i = 0
for row in reader:
    print(row)
    if i == 0:
        print('SKIPPING')
        i += 1
        continue
    #ISO
    try:
        i = Iso.objects.get(name=row[10])
    except:
        print("Inserting Iso",row[10])
        i = Iso(name=row[10])
        i.save()
        
    #Category   
    try:
        c = Category.objects.get(name=row[7])
    except:
        print("Inserting Category",row[7])
        c = Category(name=row[7])
        c.save()
        
    #Region
    try:
        r = Region.objects.get(name=row[9])
    except:
        print("Inserting Region",row[9])
        r = Region(name=row[9])
        r.save()
    
    #States
    try:
        s = States.objects.get(name=row[8])
    except:
        print("Inserting States",row[8])
        s = States(name=row[8])
        s.save()
    
    #dealing with empty columns
    try: 
        n = row[0]
    except:
        n = None
    
    try: 
        d = row[1]
    except:
        d = None
    
    try:
        j = row[2]
    except: 
        j = None
    
    try:
        y =int(row[3])
    except: 
        y = None
    try:
        la =float(row[4])
    except: 
        la=None
    try:
        lo =float(row[5])
    except: 
        lo=None
    try:
        ar=float(row[6])
    except: 
        ar=None
    
    #Sites
    E = Site(name=n, description=d, justification=j, year=y, latitude=la, longitude=lo, area_hectares=ar, iso=i, category=c, region=r, states=s)
    
    E.save()
        
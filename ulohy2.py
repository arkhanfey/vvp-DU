jmeno="Vít Langer"
print(type(jmeno))
vek=22                              #proměnná typu int
vek_float=float(vek)
print(vek,vek_float)
seznam=[1,2,3]
print(seznam[1])
seznam.insert(1,4)
print(len(seznam))
slovnik={
    "jmeno":"Vít Langer",
    "vek":"22"
    }
print(slovnik["jmeno"])
slovnik["mesto"]="Ostrava"
print(slovnik.keys())
cislo="5"
cislo_int=int(cislo)
print(cislo,cislo_int)
boolean=True
print(type(boolean))
prazdny_list=[]
print(type(prazdny_list))
cislo1=5
cislo2=5
print(id(cislo1)==id(cislo2))       #true
retezec1="ahoj"
retezec2="ahoj"
print(id(retezec1)==id(retezec2))   #true
seznam1=[1,2,3]
seznam2=[1,2,3]
print(id(seznam1)==id(seznam2))     #false


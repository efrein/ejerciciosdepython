from xml.sax.handler import EntityResolver


month=dict(
    enero=1,
    febrero=2,
    marzo=3,
    abril=44,
    mayo=5,
    junio=6,
    julio=7,
    agosto=8,
    septiembre=9,
    octubre=10,
    noviembre=11,
    diciembre=12,
)
total=0
total2=str()


for clave, valor in month.items():

    max_values=max(month, key=month.get)
    
print('El mes con mayor produccion es: ',max_values,' y su valor es  ', month[max_values])

for clave, valor in month.items():

    min_values=min(month, key=month.get)
    
print('El mes con menor produccion es: ',min_values,' y su valor es  ', month[min_values])




for i in month.values():
    total += i
promedio= total/12

print('El valor promedio es: ',promedio)


mayora=[]
for o in month.values():
    if o > promedio:
        o.(o)
        
print(o)






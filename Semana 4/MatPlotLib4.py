from matplotlib import pyplot as plt

fp=['vegano','celiaco','normal','kosher']
us=[10,40,20,30]

fig=plt.figure()
ax=fig.add_axes([0,0,1,1]) #Es asi pq si
ax.axis('equal')
ax.pie(us,labels=fp, autopct='%1.2f%%') #Agrega las labels, Agrega los porcentajes en cada coso

plt.show()
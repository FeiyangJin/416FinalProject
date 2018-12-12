from final import *
import networkx as nx
import matplotlib.pyplot as plt

MinnPath = r"minnesota.edgelist"
MinnGraphNx = nx.read_weighted_edgelist(MinnPath,nodetype = int)
#print(len(MinnGraphNx.nodes))
#print MinnGraphNx.number_of_edges()
karate = nx.read_gml('dolphins.gml', label='id')
print karate.number_of_edges()

comList = []
comList2 = []
i = 2
while i < 20:
	karate = nx.read_gml('dolphins.gml', label='id')
	com2 = betweennessBasedClustering(karate, i)
	karate = nx.read_gml('dolphins.gml', label='id')
	com = modularityMaximization(karate, i)
	comList.append(com)
	comList2.append(com2)
	i=i+2

#print com

print "test"
cl = {}
karate = nx.read_gml('dolphins.gml', label='id')
print len(comList)
for cc in comList:
	#print "-----------------"
	for c in list(cc):
		#print len(c)
		ms = 0.0
		cs = 0.0
		#print "component", list(c)
		for node in list(c):
			#print "nei", list(karate.neighbors(node))
			for nei in karate.neighbors(node):
				#print "hhh", nei
				if nei in list(c):
					#print "yes"
					ms += 1
				else :
					#print "no"
					cs +=1
		#print cl
		if ms + cs == 0:
			cs
		else: 
			#print "res:", cs/(ms*2+cs)
			cl[len(c)] = cs/(ms*2+cs)

key1 = cl.keys()

values1 = []
for k in cl.keys():
	values1.append(cl[k])

cl = {}
karate = nx.read_gml('dolphins.gml', label='id')
print len(comList2)
for cc in comList2:
	#print "-----------------"
	for c in list(cc):
		#print len(c)
		ms = 0.0
		cs = 0.0
		#print "component", list(c)
		for node in list(c):
			#print "nei", list(karate.neighbors(node))
			for nei in karate.neighbors(node):
				#print "hhh", nei
				if nei in list(c):
					#print "yes"
					ms += 1
				else :
					#print "no"
					cs +=1
		#print cl
		if ms + cs == 0:
			cs
		else: 
			#print "res:", cs/(ms*2+cs)
			cl[len(c)] = cs/(ms*2+cs)

key2 = cl.keys()

values2 = []
for k in cl.keys():
	values2.append(cl[k])

plt.loglog(key1,values1,'bo', key2, values2, 'ro')
plt.title("Dolphins Graph")
plt.xlabel("number of nodes in the cluster")
plt.ylabel("conductance of cluster")
plt.gca().legend(('modularityMaximization','betweennessBasedClustering'))
plt.show()


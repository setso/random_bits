from bulbs.neo4jserver import Graph
from py2neo import neo4j,node,rel 


def connect():
    try:
        gdb = neo4j.GraphDatabaseService('http://localhost:7474/db/data/')
	gdb.clear()
    except rest.ResourceNotFound:
        print 'Database service not found'
    return gdb

##def batch_create(index, 
## input the dbpedia dataset
def parse_dbpedia(fname): 
	batch = neo4j.WriteBatch(g)
	f =  open(fname);
	## skip the first comment line
	f.readline()
	
	old_nodename = ""
        try:
		for line in f:	
			fsplit =line.split(" ")
			if len(fsplit) == 4:
                		vals = [fsplit[i].split("/")[4][:-1] for i in range(0,3)]
				if vals[0] != old_nodename:
					try:	
						if len(batch) > 0:	
							nodes = batch.submit()
							batch.clear()
							for i in nodes:
								batch.create(rel(nodes[0],"knows",i)) 
							batch.submit()		
					except:
						print 'Batch Submit Error'
					print "Changing node from ",old_nodename+" to "+ vals[0]
					batch.create(node({"name":vals[0]}))	
				batch.create(node({"name":vals[2]}))
				old_nodename = vals[0]
        except:
                print "Unable to parse string"
		pass;	
       
##
# Bulbs 0.3 Neo4j Batch Example
# by James Thornton (http://jamesthornton.com)
## gist 1949517
# Batch isn't fully baked yet, but this works...
#>>> from bulbs.neo4jserver import Neo4jBatch
#>>> from bulbs.neo4jserver import Graph
#>>> g = Graph()
#>>> batch = Neo4jBatch(g.client)
#>>> message1 = g.client.message.create_vertex({'name':'James'})
#>>> message2 = g.client.message.create_vertex({'name':'Julie'})
#>>> batch.add(message1)
#>>> batch.add(message2)
#>>> batch.send()


## create the Graph
#g = Graph()
#g.clear()
g=connect()

## down page_links_en.nt from dpedia site
#parse_dbpedia("/mnt/page_links_en.nt")  
parse_dbpedia("/tmp/test_output.nt")  

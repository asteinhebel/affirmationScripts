import random
import array


def pretty():
	adj=['wonderful','majestic','beautiful','gorgeous','stunning','iridescent','radiant','shimmering','wonderous']
	noun=['rainbow','sunrise','sunset','star','ray of light','sunbeam','moonbeam','butterfly','unicorn']

	randAdj=random.randint(1,len(adj))-1
	randNoun=random.randint(1,len(noun))-1


	print "You "+str(adj[randAdj])+" "+str(noun[randNoun])+"!"

	print "You're doing great!"

def hard():
	adj=['bad','badass','hardcore','smart','dopeass','damn successful']
	noun=['betch','warrior','muthafucka','hardass','leader','trailblazer']

	randAdj=random.randint(1,len(adj))-1
	randNoun=random.randint(1,len(noun))-1


	print "You are a "+str(adj[randAdj])+" "+str(noun[randNoun])+"!"

	print "No one can f*** wit you. You got this."


methodVar=bool(random.getrandbits(1))

if methodVar:
	pretty()
else:
	hard()

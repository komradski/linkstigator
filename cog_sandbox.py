from cog.torque import Graph

g = Graph("authors", cog_home="cog_home", cog_path_prefix=None)

# try:
#     g.put("Maureen Clare Murphy","authorsfor","electronic_intifada")
# except e:
#     raise 
    
print(g.v().has("authorsfor", 'electronic_intifada').all())
# print(g.count())
import pyjeo as pj

fn = '../geodata/vegetation/GPPmean08-11.tif'
# fn = '../geodata/vegetation/GPPmean08-11_3035.tif'
vfn = '../geodata/shp/polygons.sqlite'
jim = pj.Jim(fn)
jim[jim<0]=-1
print(jim.stats.getStats())
v = pj.JimVect(vfn)
extracted = pj.geometry.extract(v, jim, rule=['mean', 'stdev', 'min'], output='/vsimem/temp.sqlite', oformat='SQLite', srcnodata = -1, verbose = 0)

# print(extracted.dict())
# rm -f geodata/shp/polygons_stat.*
# pkextractogr -srcnodata -339999995214436424907732413799364296704   -r mean -r stdev -r min    -i geodata/vegetation/GPPmean08-11.tif -s  geodata/shp/polygons.sqlite    -o   geodata/shp/polygons_stat.sqlite
# pkextractogr -f "ESRI Shapefile" -srcnodata -339999995214436424907732413799364296704   -r mean -r stdev -r min -i geodata/vegetation/GPPmean08-11.tif -s  geodata/shp/polygons.sqlite -o   geodata/shp/polygons_stat.shp

# # we can also create a csv that can be manipulate later on with awk
# rm  -f geodata/shp/polygons_stat.csv
# pkextractogr -f CSV -srcnodata -339999995214436424907732413799364296704   -r mean -r stdev -r min    -i ../geodata/vegetation/GPPmean08-11.tif -s  ../geodata/shp/polygons.sqlite    -o   ../geodata/shp/polygons_stat.csv

vfn = '../geodata/shp/presence.shp'
# vfn = '../geodata/shp/presence_3035.sqlite'
v = pj.JimVect(vfn)
print(v.dict())
print(v.properties.getFeatureCount())
buffer = jim.properties.getDeltaX()
extracted = pj.geometry.extract(v, jim, rule=['mean'], output='/tmp/point_buf.sqlite', oformat='SQLite', srcnodata = -1, buffer = buffer, verbose = 3)
# extracted = pj.geometry.extract(v, jim, rule=['mean'], output='/tmp/point_buf.sqlite', oformat='SQLite', srcnodata = -1, buffer = buffer, verbose = 3)
# extracted = pj.geometry.extract(v, jim, rule=['mean'], output='/vsimem/point_buf.sqlite', oformat='SQLite', srcnodata = -1, buffer = 2, verbose = 3)
# # extracted = pj.geometry.extract(v, jim, rule=['mean', 'stdev', 'min'], output='/tmp/test.sqlite', oformat='SQLite', srcnodata = -1, buffer = 2, verbose = 1)
# print(extracted.dict())
# extracted.io.write('/tmp/test.sqlite')
# # pkextractogr -f CSV -buf 2 -srcnodata -339999995214436424907732413799364296704 -r mean -r stdev -r min -i geodata/vegetation/GPPmean08-11.tif -s geodata/shp/presence.shp -o geodata/shp/point-buf_stat.csv

import spatialIUU.processGFW as siuu


# Set global constants
global GFW_DIR, GFW_OUT_DIR_CSV, GFW_OUT_DIR_FEATHER, PROC_DATA_LOC, MAX_SPEED, REGION, lon1, lon2, lat1, lat2

siuu.GFW_DIR = '/data2/GFW_point/'
siuu.GFW_OUT_DIR_CSV = '/home/server/pi/homes/woodilla/Data/GFW_point/Patagonia_Shelf/csv/'
siuu.GFW_OUT_DIR_FEATHER = '/home/server/pi/homes/woodilla/Data/GFW_point/Patagonia_Shelf/feather/'
siuu.PROC_DATA_LOC = '/home/server/pi/homes/woodilla/Projects/Anomalous-IUU-Events-World-Map/data/'
siuu.REGION = 'Argentina'
siuu.MAX_SPEED = 32

siuu.region = 1
siuu.lon1 = -68
siuu.lon2 = -51
siuu.lat1 = -48
siuu.lat2 = -39


# Puerto Madryn region for 2018
siuu.compileData('2017-12-30', '2018-12-29', 1, parallel=True, ncores=20)

import serial

#declare global variables for latitude and longitude
lati_float = 0
longi_float = 0

#gets the current latitude and longitude of the GPS device
def getLocation():
	
	#instatiate gps
	gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)

	#declare lat and lon as strings
	lat = ""
	lon = ""

	#declare loop counter and set to 10
	i = 25

	#begin the loop
	while i >= 0:
		i -= 1
		
		#read a line from the gps data feed
		line = gps.readline()
		
		#separate the line into objects using comma limiters
		data = line.split(b',')
		
		#if the line contains the latitude and longitude...
		if data[0] == b"$GPRMC":
			
			#and if the data is marked as valid
			if data[2] == b"A":
				
				#grab the latitude and longitude as strings
				lat = data[3]
				lon = data[5]

	#now fill the global variables
	latitude = str(lat)
	longitude = str(lon)

	#remove extraneous data from the latitude global string
	latitude = latitude.replace("b", "")
	latitude = latitude.replace("'", "")
	latitude = latitude.replace("'", "")

	#remove the extraneous data from the longitude global string
	longitude = longitude.replace("b", "")
	longitude = longitude.replace("'", "")
	longitude = longitude.replace("'", "")
	
	#convert latitude and longitude to floats
	lat_float = float(latitude)
	lon_float = float(longitude)
	
	#return a tuple containing latitude and longitude	
	return lat_float, lon_float

################# end of getLocation() method #################


lati_float, longi_float = getLocation()

print(lati_float)
print(longi_float)

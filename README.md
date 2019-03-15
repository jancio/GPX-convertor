# GPX convertor
Convert GPX waypoints tags to GPX track, tracksegment and trackpoints tags accepted by [mapy.cz](https://en.mapy.cz/).

## Example
Input GPX file:

	<?xml version="1.0" encoding="utf-8"?>
	<gpx version="1.0" creator="QGIS" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/0" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd">
		<wpt lat="49.154852183619" lon="20.079387909889">
			<name>01 Popradské pleso</name>
		</wpt>
		<wpt lat="49.154418318319" lon="20.082042533533">
			<name>02 odbočka z chodníka</name>
		</wpt>
		...
	</gpx>

Output GPX file:

	<?xml version="1.0" encoding="utf-8"?>
	<gpx version="1.0" creator="QGIS" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/0" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd">
		<trk>
			<trkseg>
				<trkpt lat="49.154852183619" lon="20.079387909889">
					<name>01 Popradské pleso</name>
				</trkpt>
				<trkpt lat="49.154418318319" lon="20.082042533533">
					<name>02 odbočka z chodníka</name>
				</trkpt>
				...
			</trkseg>
		</trk>
	</gpx>

## Requirements
* Python 3
* [xmltodict](https://github.com/martinblech/xmltodict) Python module

## Usage
From command line run:

	python3 convert_GPX.py path_to_input_GPX_files
	

import sys
import glob
import os
import xmltodict
import json


def convert_gpx_dict(gpx_dict: dict, verbose: bool = False) -> dict:
	"""
	Convert parsed GPX with waypoints tags to GPX with track, tracksegment and trackpoints tags.

	:param gpx_dict: GPX dictionary with waypoints tags
	:param verbose: whether to print
	:return: GPX dictionary with track, tracksegment and trackpoints tags
	"""

	if verbose:
		print(f'Input GPX:\n{json.dumps(gpx_dict, indent=4)}')

	# Nest the body of <gpx> into <trkseg> and then the whole into <trk>, replacing <wpt> with <trkpt>
	gpx_dict['gpx']['trk'] = {}
	gpx_dict['gpx']['trk']['trkseg'] = {}
	gpx_dict['gpx']['trk']['trkseg']['trkpt'] = gpx_dict['gpx']['wpt']
	del gpx_dict['gpx']['wpt']

	if verbose:
		print(f'Output GPX:\n{json.dumps(gpx_dict, indent=4)}')

	return gpx_dict


if __name__ == '__main__':

	if len(sys.argv) != 2:
		raise ValueError('As the first argument, please, provide a path to the directory with input GPX files!')

	input_dir = sys.argv[1]
	output_dir = './output_GPX'
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	for i, input_file_path in enumerate(glob.glob(os.path.join(input_dir, '*.gpx'))):

		with open(input_file_path, 'r') as gpx_input_file:
			gpx_dict = xmltodict.parse(gpx_input_file.read())

		gpx_dict = convert_gpx_dict(gpx_dict)

		output_file_path = os.path.join(output_dir, input_file_path.split('/')[-1])
		with open(output_file_path, 'wb') as gpx_output_file:
			gpx_output_file.write(xmltodict.unparse(gpx_dict, pretty=True).encode('utf-8'))

	print(f'Converted {i + 1} GPX files.')

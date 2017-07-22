from obspy import read
from os import listdir
from os.path import isfile, join
import subprocess
from multiprocessing import Pool
import sys
import params
import datetime
from params import construct_filename

madStatsCommand= 'python MAD.py %s %s %s'
fingerprintCommand = 'python finger_print.py %s %s %s'

def call_fingerprint(args):
	print "Fingerprinting " + str(args)
	process = subprocess.Popen((fingerprintCommand % (args, mad_file, station)),
			stdout=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	return output, error

def call_mad():
	print "Processing for MAD"
	process = subprocess.Popen((madStatsCommand % (start_time, end_time, station)),
			stdout=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	print output
	return 'mad%s-%s-%s%s.txt' % (station, params.channel, start_time, end_time)

if __name__ == '__main__':
	start_time = sys.argv[1]
	end_time = sys.argv[2]
	station = sys.argv[3]

	# Preprocess to calculate MAD
	mad_file = call_mad()

	# Fingerprint
	p = Pool(params.NUM_FP_THREAD)
	args = []
	time = datetime.datetime.strptime(start_time, "%y-%m")
	while time < datetime.datetime.strptime(end_time, "%y-%m"):
		fname = construct_filename(time, station)
		args.append(fname)
		time += params.INTERVAL
	print(p.map(call_fingerprint, args))


###############################################################################

from pandas import read_csv
import matplotlib.pyplot as plt



class IOHelper():
	datasets_path = "data/"
	submissions_path = "submissions/"
	analysis_path = "analysis/"
	results_path = "results/"

	@staticmethod
	def _write_to_csv(dataframe, file):
		dataframe.to_csv(path_or_buf=file, encoding="ascii",
						 float_format="%.4f")

	@staticmethod
	def read_dataset(filename):
		print "Reading dataset"
		
		file = IOHelper.datasets_path+filename+".csv"
		dataframe = read_csv(filepath_or_buffer=file, encoding="ascii",
			                 na_values=-1, skip_blank_lines=False,
			                 index_col=0)
		return dataframe

	@staticmethod
	def store_analysis(dataframe, filename):
		csv_file = IOHelper.analysis_path+filename+".csv"
		IOHelper._write_to_csv(dataframe, csv_file)

		png_file = IOHelper.analysis_path+filename+".png"
		plt.savefig(png_file)
		plt.close()

	@staticmethod
	def store_submission(dataframe, filename):
		print "Storing submission"

		file = IOHelper.submissions_path+filename+".csv"
		IOHelper._write_to_csv(dataframe, file)

	@staticmethod
	def store_results(dataframe, filename):
		print "Storing results"

		file = IOHelper.results_path+filename+".csv"
		IOHelper._write_to_csv(dataframe, file)

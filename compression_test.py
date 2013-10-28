import os
import subprocess
from collections import OrderedDict

from testify import *

import compression

class HelperMethods(TestCase):

	@setup
	def setup(self):
		self.valid_segment_length = 3
		self.invalid_segment_length = 0
		self.output_list = [0, 1, 2, 1, 2, 3, 4, 5, 1, 2, 1]
		self.initial_legend = OrderedDict([('a', ('value', 0)), 
							  ('b', ('value', 1)), ('c', ('value', 2)), 
							  ('d', ('value', 3)), ('e', ('value', 4))])

	def test_greater_than_zero_or_raise(self):
		#boundary test
		self.assertRaises(ValueError, compression.greater_than_zero_or_raise, 
						  self.invalid_segment_length)
		#structured basis, good data
		assert not compression.greater_than_zero_or_raise(self.valid_segment_length)

	def test_segment_ready_to_be_added(self):

		#structured basis, good data
		assert not compression.segment_ready_to_be_added('aaa', 4, 'a', 'b')
		assert compression.segment_ready_to_be_added('aaa', 2, 'a', 'b')
		assert compression.segment_ready_to_be_added('aaa', 4, '', 'b')
		assert compression.segment_ready_to_be_added('aaa', 4, 'a', '.')
		assert compression.segment_ready_to_be_added('aaa', 4, '.', 'b')

	def test_format_printouts(self):
		#structured basis, good data
		assert_equals(compression.format_printouts(self.output_list, self.initial_legend),
					  ("0 1 2 1 2 3 4 5 1 2 1 ", "(a: 0) (b: 1) (c: 2) (d: 3) (e: 4) "))
		assert_equals(compression.format_printouts(self.output_list, OrderedDict()),
					  ("0 1 2 1 2 3 4 5 1 2 1 ", ""))
		assert_equals(compression.format_printouts([], self.initial_legend),
					  ("", "(a: 0) (b: 1) (c: 2) (d: 3) (e: 4) "))
		assert_equals(compression.format_printouts([], OrderedDict()), ('', ''))

#boundary
class EmptyFile(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'w')
		self.test_file.write('')
		self.test_file.close()	
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.valid_segment_length = 3
		self.invalid_segment_length = -4

	def test_invalid_segment_length(self):
		#boundary
		self.assertRaises(ValueError, compression.compress_file, self.path, 
						  self.invalid_segment_length, 'output.txt')

	def test_compression(self):
		compression.compress_file(self.path, self.valid_segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "\n")
		assert_equals(initial_legend, "")

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

#boundary
class OneLetterFile(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'w')
		self.test_file.write('a')
		self.test_file.close()	
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.valid_segment_length = 3

	def test_compression(self):
		compression.compress_file(self.path, self.valid_segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 \n")
		assert_equals(initial_legend, "(a: 0) ")

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

class OnlyOneOfEachSegmentType(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'w')
		self.test_file.write('abcb.v') #segments abc b . v
		self.test_file.close()	
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.valid_segment_length = 3

	def test_compression(self):
		compression.compress_file(self.path, self.valid_segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 3 \n")
		assert_equals(initial_legend, "(abc: 0) (b: 1) (.: 2) (v: 3) ")

#structured basis, good data
class PunctuationOnly(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'w')
		self.test_file.write(". ' \"!")
		self.test_file.close()
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.valid_segment_length = 3

	def test_compression(self):
		compression.compress_file(self.path, self.valid_segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 1 3 4 \n")
		assert_equals(initial_legend, "(.: 0) ( : 1) (': 2) (\": 3) (!: 4) ")


	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

class AlpaNumericalOnly(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'w')
		self.test_file.write('abc d fghid qr\n')
		self.test_file.close()
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.segment_length = 3

	def test_compression(self):
		compression.compress_file(self.path, self.segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 1 3 4 2 5 6 \n")
		assert_equals(initial_legend, 
					  "(abc: 0) ( : 1) (d: 2) (fgh: 3) (id: 4) (qr: 5) (\\n: 6) ")

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

class RepeatingElements(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'wb+')
		self.test_file.write("abc ab abc abc. ab. d\n")
		self.test_file.close()
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.segment_length = 3

	def test_compression(self):
		compressed_file = compression.compress_file(self.path, self.segment_length, 
													'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		self.output.close()	
		assert_equals(output_list, "0 1 2 1 2 1 1 3 2 3 2 2 4 5 \n")
		assert_equals(initial_legend, 
					  "(abc: 0) ( : 1) (ab: 2) (.: 3) (d: 4) (\\n: 5) ")

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

#structured basis, bad data
class BadInputPath(TestCase):
	
	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'wb+')
		self.test_file.write("abc ab abc abc. ab. d\n")
		self.test_file.close()
		self.path = os.path.abspath('incorrect_name.txt')
		self.output = open("output.txt", 'w+b')
		self.segment_length = 3

	def test_compression(self):
		self.assertRaises(IOError, compression.compress_file, self.path, 
						  self.segment_length, 'output.txt')

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

class BadOutputPath(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'wb+')
		self.test_file.write("abc ab abc abc. ab. d\n")
		self.test_file.close()
		self.path = os.path.abspath('test_file.txt')
		self.segment_length = 3

	def test_compression(self):
		#compression.compress_file(self.path, self.segment_length, '')
		p = subprocess.Popen(['python', '-c', "import compression; compression.compress_file('" + 
							 self.path + "', " + str(self.segment_length) + ", '')"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		assert_equals(out, "0 1 2 1 2 1 1 3 2 3 2 2 4 5 \n(abc: 0) ( : 1) (ab: 2) (.: 3) (d: 4) (\\n: 5) \n")

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
  
class StressTest(TestCase):
	"""
	A stress test for compression that reads all of Moby Dick
	I cannot say what the output for something this big should be
	"""
	
	@setup
	def setup(self):
		self.path = os.path.abspath('test.txt')
		self.output = open("output.txt", 'w+b')
		self.segment_length = 3

	def test_compression(self):
		compressed_file = compression.compress_file(self.path, self.segment_length, 
													'output.txt')

	@class_teardown
	def tear_down(self):
		os.remove('output.txt')

if __name__ == '__main__':
	run()
from __future__ import print_function
import os

from testify import *

import compression

class EmptyFile(TestCase):

	@setup
	def setup(self):
		print("", file=test_file)
		output = open("output.txt", 'rw')
		segment_length = 3


	def test_compression(self):
		compressed_file = compression.compress(self.test_file, self.segment_length, 'ouput.txt')
		ouput_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "")
		assert_equals(initial_legend, "")

	@class_teardown
	def tear_down():
		os.remove('test_file.txt')
		os.remove('output.txt')

class PunctuationOnly(TestCase):

	@setup
	def setup(self):
		print(". ' \"!" , file=test_file)
		output = open("output.txt", 'rw')
		segment_length = 3

	def test_compression(self):
		compressed_file = compression.compress(self.test_file, self.segment_length, 'ouput.txt')
		ouput_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 1 3 4")
		assert_equals(initial_legend, "0 1 2 1 3 4")

	@class_teardown
	def tear_down():
		os.remove('test_file.txt')
		os.remove('output.txt')

class AlpaNumericalOnly(TestCase):

	@setup
	def setup(self):
		print("abc d fghid qr", file=test_file)
		output = open("output.txt", 'rw')
		segment_length = 3

	def test_compression(self):
		compressed_file = compression.compress(self.test_file, self.segment_length, 'ouput.txt')
		ouput_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 1 3 4 2 5")
		assert_equals(initial_legend, "0 1 2 1 3 4 1 5")

	@class_teardown
	def tear_down():
		os.remove('test_file.txt')
		os.remove('output.txt')

class RepeatingElements(TestCase):

	@setup
	def setup(self):
		print("abc ab abc abc. ab. d", file=test_file)
		self.output = open("output.txt", 'rw')
		self.segment_length = 3

	def test_compression(self):
		compressed_file = compression.compress(self.test_file, self.segment_length, 'ouput.txt')
		ouput_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 1 2 1 1 3 2 3 2 2 4")
		assert_equals(initial_legend, "0 1 2 1 0 1 0 3 1 2 3 1 4"

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

if __name__ == "__main":
	run()
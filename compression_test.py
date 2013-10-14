from __future__ import print_function
import os

from testify import *

import compression

class EmptyFile(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'w')
		self.test_file.write('')
		self.test_file.close()	
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.segment_length = 3


	def test_compression(self):
		compression.compress(self.path, self.segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "")
		assert_equals(initial_legend, "")

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

class PunctuationOnly(TestCase):

	@setup
	def setup(self):
		self.test_file = open('test_file.txt', 'w')
		self.test_file.write(". ' \"!")
		self.test_file.close()
		self.path = os.path.abspath('test_file.txt')
		self.output = open("output.txt", 'w+b')
		self.segment_length = 3

	def test_compression(self):
		compression.compress(self.path, self.segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 1 3 4")
		assert_equals(initial_legend, "0 1 2 1 3 4")

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
		compression.compress(self.path, self.segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		assert_equals(output_list, "0 1 2 1 3 4 2 5")
		assert_equals(initial_legend, "0 1 2 1 3 4 1 5")

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
		compressed_file = compression.compress(self.path, self.segment_length, 'output.txt')
		output_list = self.output.readline()
		initial_legend = self.output.readline()
		self.output.close()	
		assert_equals(output_list, "0 1 2 1 2 1 1 3 2 3 2 2 4")
		assert_equals(initial_legend, "0 1 2 1 0 1 0 3 1 2 3 1 4")

	@class_teardown
	def tear_down(self):
		os.remove('test_file.txt')
		os.remove('output.txt')

if __name__ == "__main":
	run()
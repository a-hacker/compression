from collections import OrderedDict

from linked_list import LinkedList
from linked_list import LLNode

def compress_file(file_to_be_segmented, segment_length, output_location=None):
	"""
	A method to compress a file by segmenting the text then allocating an integer value to represent that segmented string
	then optimize the compression by creating a list of positions of each segment at a given time 
	"""

	#Edge Case: we can't do anything if the segment_length doesn't make sense
	greater_than_zero_or_raise(segment_length)

	position_list = LinkedList() 	#doubly linkedlist of nodes that correspond to a segment for easy reordering
	segment = '' 					#to represent a section of text
	initial_legend = OrderedDict() 	#to store segment as a key with (corresponding LLNode reference, compression value) as value
	output_list = [] 				#the compressed text as a list of positions of compressed values from position_list

	compression_value = 0			#an integer to represent a segment counting from 0 up by when it was added
	current_letter_index = 1		#an interger to remember where in the text the current letter is for seeking back
	with open(file_to_be_segmented) as text:

		current_letter = text.read(1)
		while current_letter:

			segment += current_letter

			
			next_letter = text.read(1)
			text.seek(current_letter_index)
			current_letter_index += 1

			#check if the segment is ready to be added
			if segment_ready_to_be_added(segment, segment_length, current_letter, next_letter):
				
				#if segment in dictionary: create an LLNode and add last position to output_list
				if segment in initial_legend:
					output_list.append(initial_legend[segment][0].position)
					position_list.move_to_head(initial_legend[segment][0])
					segment = ""

				#if segment not in dictionary: find it in head and add position to output_list
				else:
					new_node = LLNode()
					position_list.add_to_head(new_node)
					output_list.append(compression_value)
					initial_legend[segment] = (new_node, compression_value)
					compression_value += 1
					segment = ""

			current_letter = text.read(1)

	(output_list_as_string, output_legend) = format_printouts(output_list, 
															  initial_legend)

	if not output_location:
		print output_list_as_string
		print output_legend
	else:
		output_file = open(output_location, 'w+b')
		output_file.write(output_list_as_string + '\n') #print string object of output_list with spaces seperating numbers
		output_file.write(output_legend) #print string of dictionary values in order
		output_file.close()


def greater_than_zero_or_raise(segment_length):
	"""
	a method to throw an error if the segment_length is not large enough to segment the file
	"""
	if segment_length <= 0:
		raise ValueError

def segment_ready_to_be_added(segment, segment_length, letter, next_letter):
	return len(segment) >= segment_length or not next_letter or not next_letter.isalnum() or not letter.isalnum()

def format_printouts(output_list, initial_legend):
	output_list_as_string = ''
	output_legend = ''

	for cell in output_list:
		output_list_as_string += str(cell) + " "	

	for segment, compressed_value in initial_legend.iteritems():
		output_legend += '(' + str(segment) + ": " + str(compressed_value[1]) + ") "

	output_legend = output_legend.replace('\n','\\n')
	return (output_list_as_string, output_legend)
from linked_list import LinkedList
from linked_list import LLNode

def compress(to_be_segmented, segment_length, output_location):
	"""
	A method to compress a file by segmenting the text then allocating an integer value to represent that segmented string
	then optimize the compression by creating a list of positions of each segment at a given time 
	"""

	#Edge Case: we can't do anything if the segment_length doesn't make sense
	if segment_length <= 0:
		return

	position_list = LinkedList() 	#doubly linkedlist of nodes that correspond to a segment for easy reordering
	segment = '' 					#to represent a section of text
	initial_legend = {} 			#to store segment as a key with (corresponding LLNode reference, compression value) as value
	output_list = [] 				#the compressed text as a list of positions of compressed values from position_list

	compression_value = 0			#an integer to represent a segment counting from 0 up by when it was added
	current_letter = 0				#an interger to remember where in the text the current letter is for seeking back
	with open(to_be_segmented) as text:

		while True:
			
			#End Case (if the current letter is the end of the file, we break the while true loop)
			letter = text.read(1)
			if not letter:
				break

			segment = segment + letter

			
			next = text.read(1)
			text.seek(current_letter)
			current_letter += 1

			
			#check if the segment is ready to be added
			if len(segment) < segment_length and not next and not next.isalnum() and letter.isalnum():
				continue

			
			#if segment in dictionary: create an LLNode and add last position to output_list
			if segment in initial_legend:
				output_list.append(initial_legend[segment][0].position)
				position_list.move_to_head(initial_legend[segment][0])
				segment = ""

			
			#if segment not in dictionary: find it in head and add position to output_list
			if segment not in initial_legend:
				new_node = LLNode()
				position_list.add_to_head(new_node)
				output_list.append(compression_value)
				compression_value += 1
				initial_legend[segment] = (new_node, compression_value)
				segment = ""

	output_file = open(output_location, 'w+b')
	output_file.write(str(map(str, output_list)) + '\n') #print string object of output_list with spaces seperating numbers
	output_file.write(str(map(str, initial_legend))) #print string of dictionary values in order
	output_file.close()
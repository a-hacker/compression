from linked_list import LinkedList
from linked_list import LLNode

def segment_and_store(to_be_segmented, segment_length, output_location):

	"""
	create: 
	    head - head of doubly linkedlist
    	segment - to represent a section of text
	    dictionary - to store segment as a key with a linked list node reference as value
	    output_list - the compressed text
	"""
	head = LinkedList()
	segment = ''
	dictionary = {}
	output_list = []

	"""
	legend = 0
	"""
	legend = 0
	
	"""
	open to_be_segmented
	"""
	current_letter = 0
	with open(to_be_segmented) as f:

		"""
		for each letter (letter) in to_be_segmented:
		"""
		while True:
			letter = f.read(1)
			if not letter:
				break

			"""
			add letter to segment
			"""
			segment = segment + letter

			"""
			if length of segment < segment_length and next is not end and next is not alphanumerical and letter is alphanumerical:
				continue
			"""
			next = f.read(1)
			f.seek(current_letter)
			current_letter += 1
			if len(segment) < segment_length and not next and not next.isalnum() and letter.isalnum():
				continue

			"""
			if segment in dictionary:
				find corresponding node using segment as key in dictionary
				add position of node to output_list and move node to front of list
				empty segment
			"""
			if segment in dictionary:
				output_list.append(dictionary[segment][0].position)
				head.move_to_head(dictionary[segment][0])
				segment = ""

			"""
			if segment not in dictionary:
				create new linkedlist node and append to the front of the list
				add legend - 1 to output_list
				add (segment: (node, legend)) to dictionary y
				empty segment
			"""
			if segment not in dictionary:
				x = LLNode()
				head.add_to_head(x)
				output_list.append(legend)
				legend += 1
				dictionary[segment] = (x, legend)
				segment = ""

	"""
	print string object of output_list with spaces seperating numbers
	print string of dictionary values in order
	"""
	d = open(output_location)
	d.write(map(str, output_list))
	d.write(map(str, dictionary))
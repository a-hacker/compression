"""
void segment_and_store(file to_be_segmented, int segment_length):

	open to_be_segmented

	create: 
	    head - head of doubly linkedlist
    	segment - to represent a section of text
	    dictionary - to store segment as a key with a linked list node reference as value
	    output_list - the compressed text

	if empty then
		return an empty string

	legend = 0
	for each letter (letter) in to_be_segmented:
		
		add letter to segment

		if length of segment < segment_length and next is not end and next is not alphanumerical and letter is alphanumerical:
			continue

		if segment in dictionary:
			find corresponding node using segment as key in dictionary
			add position of node to output_list and move node to front of list
			empty segment

		if segment not in dictionary:
			create new linkedlist node and append to the front of the list
			add legend - 1 to output_list
			add (segment: (node, legend)) to dictionary y
			empty segment

	close to_be_segmented

	print string object of output_list with spaces seperating numbers
	print string of dictionary values in order
"""
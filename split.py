line_break = '\n'
dot = '.'
invisible_char = '‌'

def char_split(data, limit, break_char, child_split):
	while (len(data) > limit):
		closest_break = data.rfind(break_char, 0, limit + 1)

		while (data[closest_break + 1] == break_char):
			closest_break = data.rfind(break_char, 0, closest_break)

		if (closest_break == -1):
			closest_break = data.find(break_char, limit + 1)
			if (closest_break == -1):
				closest_break = len(data) - 1
			consumed = 0

			for chunk in child_split(data[0 : closest_break + 1], limit):
				yield chunk
				consumed += len(chunk)
				if (closest_break - consumed <= limit):
					break

			data = data[consumed + 1 :]

		else:
			yield data[0 : closest_break + 1]
			data = data[closest_break + 1 :]

	if (len(data) > 0):
		yield data

def force_split(data, limit):
	for i in range(0, len(data) + limit, limit):
		yield data[i : i + limit]

def sentence_split(data, limit):
	yield from char_split(data, limit, dot, force_split)

def paragraph_split(data, limit):
	for chunk in char_split(data, limit, line_break, sentence_split):
		if (chunk[len(chunk) - 1] == line_break):
			chunk = chunk[0 : len(chunk) - 1]
		if (chunk[len(chunk) - 1] == line_break):
			yield f'{chunk}{invisible_char}'
		else:
			yield chunk

split = paragraph_split
def final_direction(i, t):
	l = {"N": "W", "W": "S", "S": "E", "E":"N"}
	r = {"N": "E", "E": "S", "S": "W", "W":"N"}
	for j in t:
		if j == "L":
			i = l[i]
		else:
			i = r[i]
	return i

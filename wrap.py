def wrap(iterable):
	"""Yields the same list, but where the first element occurs last too"""
	i = 0
	while i < len(iterable):
		yield iterable[i]
		i += 1
	yield iterable[0]

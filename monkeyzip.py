# Name inspired by monkey bars, in the sense that each bar represents one element from the iterable
# and one tuple represents what hands is grabbing onto what bars

#        \/           \/           \/
#  A   (A, B)   B   (B, C)   C   (C, D)   D 
# =+============+============+============+=
#   \  @@@@@@  /
#    \ | . .| /
#     \ __¨_ /
#      |    |
#      |    |
#      |____|
#       |  |
#       |  |
#       |_ |_
 
# Useful for stuff like having a list of points and having to interpolate a curve between each set

def monkeyzip(iterable):
  """Yields tuples of elements that are close together"""
	for i in range(len(iterable) - 1):
		yield iterable[i], iterable[i+1]

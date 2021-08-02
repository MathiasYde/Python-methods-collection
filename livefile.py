import json

# Usage:
# 
# with LiveFile("settings.json") as settings:
#   settings.name = "Mathias Yde"
#   settings.isadmin = True
#

class LiveFile():
  """Changes to the returned dictionary will automatically be saved to disk after use"""
  def __init__(self, filepath, decode=json.load, encode=json.dump):
    """
    Decode and encode functions must be able to interpret an _io.TextIOWrapper directly
    """
    self.filepath = filepath
    self.encode = encode
    self.decode = decode
    with open(self.filepath, "r") as file:
      self.data = self.decode(file)

  def __enter__(self):
    return self.data

  def __exit__(self, exc_type, exc_val, exc_tb):
    with open(self.filepath, "w") as file:
      self.encode(self.data, file)

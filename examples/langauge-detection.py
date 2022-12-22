"""
An example of fast few-shot language detection using AMI with zlib. 
"""


from ami import ami


sp = '. '.join([
  'este fragmento de texto esta escrito en espanol',
  'el espanol es una lengua romance que se habla en espana y en gran parte de america central y del sur',
  'un gato blanco sentado en la alfombra',
])


en = '. '.join([
  'this piece of text is written in english',
  'england is a country that is part of the united kingdom',
  'a white cat is sitting on a mat'
])


def detect_language(string):
  return ami(string, sp) < ami(string, en)


detect_language('pizza is the best food in the world') # returns 1 - English

detect_language('la pizza es la mejor comida del mundo') # returns 0 - Spanish

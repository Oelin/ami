"""
An example of fast few-shot document classification using AMI with zlib. 
"""


from ami import match


spanish_context = '. '.join([
  'este fragmento de texto esta escrito en espanol',
  'el espanol es una lengua romance que se habla en espana y en gran parte de america central y del sur',
  'un gato blanco sentado en la alfombra',
])


english_examples = '. '.join([
  'this piece of text is written in english',
  'england is a country that is part of the united kingdom',
  'a white cat is sitting on a mat'
])

"""
An example of fast few-shot document classification using AMI with zlib. 
"""


from ami import match


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


match(
  'pizza is the best food in the world',
  'la pizza es la mejor comida del mundo',
  context = sp,
) # returns 1 - the second sentence is more likely to be Spanish.


match(
  'pizza is the best food in the world',
  'la pizza es la mejor comida del mundo',
  context = en,
) # returns 0 - the first sentence is more likely to be English.

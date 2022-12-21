"""
An example of fast few-shot document classification using AMI with zlib. 
"""


from ami import match


train_spanish = '. '.join([
  'este fragmento de texto esta escrito en espanol',
  'el espanol es una lengua romance que se habla en espana y en gran parte de america central y del sur',
  'un gato blanco sentado en la alfombra',
])


train_english = '. '.join([
  'this piece of text is written in english',
  'england is a country that is part of the united kingdom',
  'a white cat is sitting on a mat'
])


def classify(x):
  return match(train_spanish, train_english, x)


classify('pizza is the best food in the world') # returns 0 (English)
classify('la pizza es la mejor comida del mundo') # returns 1 (Spanish)

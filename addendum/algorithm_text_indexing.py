"""
Salton (1989), Har- man (1991), Krovetz (1995), Hull (1996). Hollink et al. (2004) provide detailed results for the 
effectiveness of language-specific methods on 8 European lan- guages. In terms of percent change in mean average 
precision (see page 159) over a baseline system, diacritic removal gains up to 23% (being especially helpful for 
Finnish, French, and Swedish). Stemming helped markedly for Finnish (30% improvement) and Spanish (10% improvement), 
but for most languages, including English, the gain from stemming was in the range 0– 5%, and results from a lemmatizer 
were poorer still. Compound splitting gained 25% for Swedish and 15% for German, but only 4% for Dutch. Rather than 
language-particular methods, indexing character k-grams (as we sug- gested for Chinese) could often give as good or 
better results: using within- word character 4-grams rather than words gave gains of 37% in Finnish, 27% in Swedish, 
and 20% in German, while even being slightly positive for other languages, such as Dutch, Spanish, and English.
ref:
"""

class Tokenization:
	"""
	ref: 
	"""
	pass


class LanguageIdentification:
	pass


class DiacriticRemoval:
	pass


class CompoundSplitter:
	pass


class WordSegmentation:
	def hidden_markov_model():
		pass

	def conditional_random_fields():
		pass


class StopWordRemoval:
	pass


class TokenNormalization:
	"""
	antidiscriminatory ~ anti-discriminatory
	ref: 
	"""
	pass


class EquivalenceClasses:
	"""
	car ~ automobile
	ref:
	"""
	pass

class CaseHandling:
	class CaseFolding:
		"""
		ref:
		"""
		pass

	class Truecasing:
		"""
		ref:
		"""
		pass


class Stemmer:
	"""
	ref: http://www.cs.waikato.ac.nz/ ̃eibe/stemmers/
		 http://www.comp.lancs.ac.uk/computing/research/stemming/
	"""
	pass
	def porter_stemmer():
		"""
		ref: http://www.tartarus.org/ ̃martin/PorterStemmer/
		"""
		pass

	def lovins_stemmer():
		"""
		ref: 
		"""
		pass

	def paice_husk_stemmer():
		"""
		ref: 
		"""
		pass


class Lemmatizer:
	"""
	ref: 
	"""
	pass


class PartsOfSpeechTagging:
	"""
	ref:
	"""
	pass


class Indexing:
	def biword_index():
		"""
		ref: intro_to_info_retrieval; section 2.4.1
		"""
		pass

	def positional_intersect():
		"""
		aka: proximity
		ref: intro_to_info_retrieval; figure 2.12
		positional
		"""
		pass
	
	def next_word_index():
		"""
		ref: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.2.6254&rep=rep1&type=pdf
			 https://people.eng.unimelb.edu.au/jzobel/fulltext/sigir02bwz.pdf
			 https://www.alhenshiri.net/Lecture10.pdf
		"""
		pass

	def word_segmentation():
		"""
		most commonly used for japanese
		ref: 
		"""
		pass

	def character_bigram_index():
		"""
		most commonly used for chinese
		ref:
		"""
		pass
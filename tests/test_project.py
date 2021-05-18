import unittest
import lib.translate_word as t
import lib.word

class TestDictionary(unittest.TestCase):
	def test_translate_ENG_Arr_Single_definition(self):
		#If an English word only has 1 Arrernte Word
		word = "a"
		translation = t.get_word_translation("eng", word)
		self.assertEqual(translation, "anyente")

	@unittest.skip("Skipping for testing")
	def test_translate_ENG_ARR_Multiple_definition(self):
		#If an English word has multiple Arrernte Words
		word = "ache"
		translation = t.get_word_translation("eng", word)
		self.assertEqual(translation, ["arnteme","kwarneme","arlkweme"])

class TestWordObject(unittest.TestCase):
	def test_word_init(self):
		try: 
			word_object = Word()
		except:
			self.fail("Unable to create error")



if __name__ == '__main__':
    unittest.main()
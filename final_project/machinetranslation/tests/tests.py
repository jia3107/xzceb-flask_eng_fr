import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    #this function is to translate English to French
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    #this function is to translate French to English
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return english_text.get("translations")[0].get("translation")

#translate from english to french
translation = language_translator.translate(
    text='Hello',
    model_id='en-fr').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

#translate from french to english
translation = language_translator.translate(
    text='Bonjour',
    model_id='fr-en').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

import unittest

from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #test when input is Hello, output is Bonjour
        self.assertEqual(english_to_french('I love bread'), "J'adore le pain") #test when input is I love bread, output is j'aime le pain
        self.assertNotEqual(english_to_french('This is a small dog'), "C'est un petit chat") #test when input is This is a small dog, output is not c'est un petit chien

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #test when input in Bonjour, output is Hello
        self.assertEqual(french_to_english("Ce café est délicieux"), "This coffee is delicious") #test when input is Ce café est délicieux, output is This coffee is delicious
        self.assertNotEqual(french_to_english("Joyeux anniversaire"), 'Happy New Year') #test when input is Joyeux anniversaire, output is not Happy Birthday

unittest.main()


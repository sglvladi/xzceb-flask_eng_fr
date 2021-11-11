"""Translator API module

This module provides functions for translating between English and French
using the Watson API.

"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


def get_translator():
    """Authenticate with Watson API and return translator instance

    Returns
    -------
        LanguageTranslatorV3
            A Watson Language translator instance
    """
    load_dotenv()

    apikey = os.environ['apikey']
    url = os.environ['url']

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    return language_translator


def englishToFrench(english_text):
    """Translate English to French

    Parameters
    ----------
    english_text : str
        English text to translate

    Returns
    -------
    str
        Translated text in French
    """
    # If text is empty or None, return empty str
    if not english_text:
        return ''

    language_translator = get_translator()
    response = language_translator.translate(text=english_text,
                                             model_id='en-fr').get_result()
    french_text = response['translations'][0]['translation']
    return french_text


def frenchToEnglish(french_text):
    """Translate French to English

    Parameters
    ----------
    french_text : str
        French text to translate

    Returns
    -------
    str
        Translated text in English
    """
    # If text is empty or None, return empty str
    if not french_text:
        return ''

    language_translator = get_translator()
    response = language_translator.translate(text=french_text,
                                             model_id='fr-en').get_result()
    english_text = response['translations'][0]['translation']
    return english_text

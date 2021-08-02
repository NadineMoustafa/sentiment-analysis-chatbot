# import os
# unknown_dir = os.system("echo 'Hello World!' | translate en zh-TW")
# print(unknown_dir)
# from google_trans_new import google_translator
# sentence = input("Enter your message:")
# translator = google_translator()
# translate_text = translator.translate(
#     sentence, lang_src='en', lang_tgt='ar')
# print(translate_text)
import six
from google.cloud import translate_v2 as translate
def translate_text_with_model(target, text, model="nmt"):
    """Translates text into the target language.

    Make sure your project is allowlisted.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    

    translate_client = translate.Client('./service-account-file.json')

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target, model=model)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


translate_text_with_model("ar", "Hello world")
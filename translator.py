import polib
from googletrans import Translator

# Load the .po file
po = polib.pofile('locale/ru/LC_MESSAGES/django.po')  # Replace with your .po file path

# Initialize the translator
translator = Translator()

# Define the target language
target_language = 'ru'  # Change this to the desired target language code

# Translate and update the .po file
for entry in po:
    if not entry.msgstr:  # Translate only if the translation is empty
        translation = translator.translate(entry.msgid, src='auto', dest=target_language)
        entry.msgstr = translation.text
    
    print(entry)

# Save the updated .po file
po.save()
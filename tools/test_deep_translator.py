from deep_translator import GoogleTranslator

try:
    tr = GoogleTranslator(source='hi', target='en')
    res = tr.translate("किसने व्यपगत के सिद्धन्त की रचना की?")
    print("Translation result:", res)
except Exception as e:
    print("Error:", e)

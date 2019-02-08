import os
import speech_recognition as sr

#> LANGS: http://www.lingoes.net/en/translator/langcode.htm

recordings = [
    {"lang": "en-US", "filename": "brooklyn.flac"},
    {"lang": "es", "filename": "el-ninyo.flac"},
    {"lang": "jp", "filename": "arigato.flac"},
    {"lang": "fr", "filename": "french.aiff"},
    {"lang": "bg-BG", "filename": "bulgarian.flac"},
    {"lang": "zh", "filename": "chinese.flac"},

]

client = sr.Recognizer()

for r in recordings:
    lang = r["lang"]
    print("-------------------")
    print("LANG:", lang)

    filepath = os.path.join(os.path.dirname(__file__), "..", "sounds", r["filename"])

    try:

        with sr.AudioFile(filepath) as source:
            audio = client.record(source)

        #transcript = client.recognize_google(audio) #> 'how old is the Brooklyn Bridge'
        #print("TRANSCRIPT: " + transcript)
        response = client.recognize_google(audio, language=lang, show_all=True) #> {'alternative': [{'transcript': 'how old is the Brooklyn Bridge', 'confidence': 0.987629}], 'final': True}
        alternative = response["alternative"][0]
        print("TRANSCRIPT: " + alternative["transcript"])
        print("CONFIDENCE: " + str(alternative["confidence"]))

    except Exception as e:
        print("ERROR:", e)

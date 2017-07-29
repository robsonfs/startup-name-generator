from googletrans import Translator
from languages import LANGS as langs

translator = Translator()

def get_names(base_name):
    base_code = translator.detect(base_name).lang
    sugestted_names = []
    for lang in langs:
        if lang[1] != base_code:
            try:
                t = translator.translate(text=base_name, src=base_code, dest=lang[1])
                sugestted_names.append(t.text)
            except:
                print(lang)
    return sugestted_names

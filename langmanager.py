import json


def load_json(lang):
    with open(f"languages/{lang}.json", "r", encoding="utf-8") as f:
        return json.load(f)


class LangManager:
    def __init__(self, lang='en', langs=None):
        if langs is None:
            langs = []
        self.language = lang
        self.languages = langs

        self.flags = {}
        self.json_langs = {}

        self.load_languages()
        self.load_flags()



    def load_flags(self):
        for lang in self.languages:
            self.flags[lang] = self.json_langs[lang]["flag"]


    def load_languages(self):
        for lang in self.languages:
            self.json_langs[lang] = load_json(lang)


    def set_lang(self, lang, guild):
        if lang in self.languages:
            self.language = lang
        else:
            raise ValueError(f"Langue not supported: {lang}")

    def command_get(self, command, key):
        return self.json_langs[self.language][command][key]

    def event_get(self, event, key):
        return self.json_langs[self.language]["events"][event][key]

    def info_get(self, key):
        return self.json_langs[self.language][key]

    def get_flag(self, lang):
        return self.flags[lang]

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
        self.load_flags()

    def load_flags(self):
        for lang in self.languages:
            json_lang = load_json(lang)
            self.flags[lang] = json_lang["flag"]

    def set_lang(self, lang, guild):
        if lang in self.languages:
            self.language = lang
        else:
            raise ValueError(f"Langue not supported: {lang}")

    def command_get(self, command, key):
        json_lang = load_json(self.language)
        return json_lang[command][key]

    def event_get(self, event, key):
        json_lang = load_json(self.language)
        return json_lang["events"][event][key]

    def error_get(self, key):
        json_lang = load_json(self.language)
        return json_lang["error"][key]

    def info_get(self, key):
        json_lang = load_json(self.language)
        return json_lang[key]

    def get_flag(self, lang):
        return self.flags[lang]

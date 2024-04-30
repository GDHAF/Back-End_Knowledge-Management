from rake_nltk import Rake


class Analyser:

    @staticmethod
    def Create_Base(text):
        r = Rake(language="portuguese")

        r.extract_keywords_from_text(text)

        keywords = r.get_ranked_phrases()

        print(keywords)

        return keywords

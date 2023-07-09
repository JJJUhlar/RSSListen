import whisper
import feedparser
import requests

class RSSListen:

    def __init__(self, media: str):
        self.model = whisper.load_model("base")
        self.media = media
        self.feed = None
        self.details = None
        self.items = None

    def getDetails(self):
        return self.details

    def getFeed(self):
        d = feedparser.parse(self.media)
        # self.feed = {
        #     "title": d['title'],
        #     "link": d['link'],
        #     "description": d['description'],
        #     "published": d['published']
        # }
        self.feed = d
        self.items = d['entries']
        return d

    def config(self, provider):
        pass

    def validate_feed(self):
        pass

    def transcribeOne(self, index=0, format="text"):
        audio = None;
        print(">",self.items[index])
        print(">",self.items[index].links)
        for link in self.items[index].links:
            print(link)
            if 'audio' in link.type:
                audio = link.href
            else:
                pass
        print(audio)

        result = self.model.transcribe(audio)
        result = {
            "title": self.items[index].title,
            "subtitle": self.items[index].subtitle,
            "authors": self.items[index].authors,
            "updated": self.items[index].updated,
            "transcript": result.text
        }
        return result

    def transcribeAll(self, format="text"):
        transcripts = []
        for i in range(len(self.items)):
            transcripts.append(self.transcribeOne(i, format))
        return transcripts

    def downloadEntry(self, name: str, link:str):
        file = requests.get(link)
        with open(f'{name}.mp3', 'wb') as f:
            f.write(file.content)
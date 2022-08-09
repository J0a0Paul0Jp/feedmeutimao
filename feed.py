import re
import feedparser

class MeuTimao:
    class Noticia:
        def __init__(self, title, content, media_thumbnail, link):
            self.title = title
            self.content = content
            self.media_thumbnail = media_thumbnail
            self.link = link
            self.id_noticia = int(re.findall('[0-9]+', link)[0])
        
        def __repr__(self):
            return f'{self.title}(id={self.id_noticia})'
    
    def __init__(self):
        self.url = 'https://www.meutimao.com.br/rss'

    def last_new(self):
        try:
            with open("noticia.id", 'r') as f:
                id_noticia_ant = int(f.read())
        except FileNotFoundError:
            id_noticia_ant = -1
        
        r = self.news()[0]
        id_noticia = r.id_noticia
        
        if id_noticia != id_noticia_ant:
            with open("noticia.id", 'w') as f:
                f.write(str(id_noticia))
            return r
        
        return None

    def news(self):
        entries_rss = feedparser.parse(self.url).entries
        news_ = []

        for entries in entries_rss:
            
            title = entries.title
            content = entries.summary
            text = content
            link = entries.link

            try:
                media_thumbnail = 'https:'+entries.media_thumbnail[0]['url']
            except:
                media_thumbnail = 'https://static.gazetaesportiva.com/uploads/imagem/2020/06/23/fernando-dantas-1.jpg'
            
            news_.append(self.Noticia(title, text, media_thumbnail, link))
        
        return news_


class Blog(scrapy.Spider):
    name = 'blog'

    def start_requests(self):
        return scrapy.Request(
            "https://kamil.kwapisz.pl",
            meta={'date': "12.10.2020"},
            callback=self.parse_article
        )

    def parse_article(self, response: scrapy.http.Response):
        article = ArticleItem()
        article['title'] = response.xpath(
            './/h1[@class="entry-title"]//text()').get()  # '7 najczęstszych błędów podczas nauki programowania'
        article['date'] = response.xpath('.//span[@class="posted-on"]//text()').get()  # '9 lipca 2020'
        article['author'] = response.xpath('.//a[@class="url fn n"]//text()').get()  # "Kamil Kwapisz"
        article['tags'] = response.xpath(
            './/meta[@property="article:tag"]//@content').getall()  # ['błędy', 'nauka programowania', 'nauka python', 'python']
        # [...]
        article_text = response.xpath('.//p//text()').getall()
        article['text'] = ''.join(article_text)
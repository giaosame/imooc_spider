from imooc.baike_spider import url_manager, html_downloader, html_parser, html_outputer


class MainSpider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.dowloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        # To record the sequence number of the current crawled url:
        cnt = 1
        # First, add the root url to the manager:
        self.urls.add_new_url(root_url)
        # Begin the crwaling loop because there has existed a url in the manager:
        while self.urls.has_next_url():
           try:
               # Get a url which is waiting to be crawled:
               new_url = self.urls.get_next_url()
               print('Crawl %d: %s' % (cnt, new_url))

               # Then use the downloader to download the webpage, and store it in html_cont
               html_cont = self.dowloader.download(new_url)
               # The downloaded webpage will be parsed by the parser;
               # Then, get the new list of urls and new data:
               new_urls, new_data = self.parser.parse(new_url, html_cont)
               self.urls.add_new_urls(new_urls)

               # Collect data:
               self.outputer.collect_data(new_data)

               if cnt == 1000:
                   break
               cnt = cnt + 1

           except:
               print('Crawl failed...')

        self.outputer.output_html()

# The main function of the spider program:
if __name__ == '__main__':
    # The entry url of the crawler:
    root_url = 'https://baike.baidu.com/item/Python'
    spider = MainSpider()
    # Start the crawler program:
    spider.crawl(root_url)


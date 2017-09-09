class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        Add a new url into the manager。
        :param root_url: It can be the root url which is the first to be added into the manager.
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_next_url(self):
        """
        To judge whether there is a new url, which is waiting to be crawled, in the url manager.
        :return:
        """
        return len(self.new_urls) != 0

    def get_next_url(self):
        """
        Get the next crawled url from the url manager.
        :return:
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, urls):
        """
        Add a list of or some urls into the manager:
        :param urls:
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)


import requests
from bs4 import BeautifulSoup as BS
from datetime import date

PARAM_MONTH = {'января':1, 'февраля':2}

class Tengri:
    site = 'https://www.tengrinews.kz'
    list_of_links = []
    data_post = []
    def get_links(self):
        """get all links of posts"""
        r = requests.get(self.site)
        html = BS(r.content, 'html.parser')
        links = html.find_all('a', class_='tn-tape-title', href=True)
        for link in links:
            if link['href'].startswith('https'):
                pass
            else:
                self.list_of_links.append(self.site + link['href'])
        return self.list_of_links

    def get_post(self, links):
        """info about posts"""
        for i, link in enumerate(links):
            content_post = ''
            list_of_data = []
            r = requests.get(link)
            html = BS(r.content, 'html.parser')
            title_post = html.find('h1', class_='tn-content-title').text.split('\n')[0]
            date_post = html.select('h1 > span')[0].text
            date_and_time = date_post.rstrip().split(',')
            corect_data = self.correct(date_and_time[0])
            content = html.select('article > p')
            for i in content[:-2]:
                content_post += i.text
            list_of_data.append(link)
            list_of_data.append(title_post)
            list_of_data.append(content_post)
            list_of_data.append(corect_data)
            list_of_data.append(date_and_time[1])
            self.data_post.append(list_of_data)
        self.data_post.reverse()
        return self.data_post

    def correct(self, data):
        d = data.split(' ')
        month = PARAM_MONTH[d[1]]
        d = date(int(d[2]), month, int(d[0]))
        return d




if __name__ == '__main__':

    test = Tengri()
    #test.get_links()
    a = test.get_post(['https://tengrinews.kz/show/shvartsenegger-protsitiroval-terminatora-privivayas-426648/'])
    print(a)
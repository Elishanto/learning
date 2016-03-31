import urllib.request as ur
from bs4 import BeautifulSoup
import os.path


def save_imgs(pa):
    for img in pa.find_all('img'):  # iterate through all img tags in page
        src = img['src']  # get src attribute from img tag
        if 'images/lessons/' in src:  # check if img belongs to lesson
            directory = 'levels/' + src
            path = '/'.join(directory.rsplit('/')[:-1])
            # if directory doesn't exists
            if not os.path.exists(path):
                os.makedirs(path)
            ur.urlretrieve('http://javarush.ru/levels/' + src, directory)


def remove_elements(pag, tag, class_):
    for t in pag.find_all(tag, class_):
        t.extract()


if __name__ == '__main__':
    for i in range(1, 41):
        # get document
        url = 'http://javarush.ru/levels/level{0:0=2d}.html'.format(i)  # get level html with correct number format
        s = ur.urlopen(url).read().decode('utf-8')  # encoding fight
        page = BeautifulSoup(s, 'html.parser', from_encoding='utf-8')  # encoding fight

        # delete useless and excess stuff
        page.find('div', 'header').extract()  # header
        page.find('div', 'level-ref').extract()  # pagination between levels
        remove_elements(page, 'button', 'section_footer')  # next lesson button
        remove_elements(page, 'button', 'profile-tariff-button-popular')  # donate button
        page.find('section', 'lesson')['style'] = ''  # 'display: none'
        page.find('link')['href'] = 'main.css'  # style href correction

        # reverse lessons
        wrapper = page.find('div', 'wrapper')  # lessons div
        sections = page.find_all('section', 'lesson')[::-1]  # reverse existing lessons
        for section in page.find_all('section', 'lesson'):
            section.extract()  # remove lesson from page
        for section in sections:
            wrapper.append(section)  # add lesson from reversed list to page

        save_imgs(page)  # save all images from page

        open('levels/level' + str(i) + '.html', 'w').write(str(page.html))  # save level html file
        print(i)

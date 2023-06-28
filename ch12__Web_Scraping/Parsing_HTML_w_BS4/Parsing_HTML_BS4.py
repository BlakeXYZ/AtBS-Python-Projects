#! python3

### Parse (analyzes and identify) HTML using beautiful soup module
###
###

# import requests, bs4
# from pathlib import Path

# p = Path(__file__)
# base_dir = p.resolve().parent
# destination_dir = p.resolve().parent / '_'

###                                                                                 Web Parse
# res = requests.get('https://nostarch.com')
# try:
#     res.raise_for_status() # will raise an exception if error downloading file, will do nothing if download successful
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# bs4_Web_Parse = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(bs4_Web_Parse))

###


###                                                                                 Local File Parse
# exampleFile = open(base_dir / 'example.html')
# bs4_File_Parse = bs4.BeautifulSoup(exampleFile, 'html.parser')
# # print(type(bs4_File_Parse))

# # elems = bs4_File_Parse.select('#author')

# # print(type(elems))
# # print(len(elems))
# # print(type(elems[0]))
# # print('***')
# # print(str(elems[0]))
# # print(elems[0].get_text())
# # print(elems[0].attrs)

# p_elems = bs4_File_Parse.select('p')
# print(len(p_elems))

# for i in range(len(p_elems)):
#     print(str(p_elems[i].get_text()))
#     print(str(p_elems[i].attrs))
###

###                                                                                 Getting Data From Element's Attributes
## Here we use select() to find any <span> elements and then store the
## first matched element in spanElem. Passing the attribute name 'id' to get()
## returns the attribute’s value, 'author'

# exampleFile = open(base_dir / 'example.html')
# soup = bs4.BeautifulSoup(exampleFile, 'html.parser')

# spanElem = soup.select('span')[0]

# print(str(spanElem))
# print(str(spanElem.get('id')))
# print(str(spanElem.get('nonexistent_id') == None))
# print(str(spanElem.attrs))









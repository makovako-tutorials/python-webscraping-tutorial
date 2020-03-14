from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My webpage</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
        <img src="https://source.unsplash.com/200x200/?nature,water" alt="" srcset=""/>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque veniam, amet maxime minima voluptatibus odio id sapiente ex culpa itaque fugit quam omnis est delectus impedit, totam doloremque corporis consectetur eligendi in! Molestiae eum ex dolorem ut? Nesciunt consectetur qui magni soluta libero repellendus odio, tempore culpa accusantium. Error, delectus.</p>

    </div>
    <div id="section-2">
        <ul class="items">
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 2</a></li>
            <li class="item"><a href="#">Item 3</a></li>
        </ul>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct

if False:
    print(soup.body)
    print(soup.head)
    print(soup.head.title)

# find() - gives first found element

el = soup.find('div')

# find_all() or findAll()- gives all found

el = soup.find_all('div')

el = soup.find(id='section-1')

el = soup.find(class_="items")

el = soup.find(attrs={"data-hello":"hi"})

# select - by css selectors, always returns in list

el = soup.select('#section-1')
el = soup.select('#section-1')[0]

el = soup.select('.item')

# get_text()

el = soup.find(class_="item").get_text()

for item in soup.select('.item'):
    break
    print(item.get_text())

# Navigation

el = soup.body.contents # gives list with line breaks
el = soup.body.contents[1].contents[1]
el = soup.body.contents[1].contents[1].next_sibling.next_sibling
el = soup.body.contents[1].contents[1].find_next_sibling()

el = soup.find(id="section-2").find_previous_sibling()

el = soup.find(class_="item").find_parent()

el = soup.find('h3').find_next_sibling('p')

import requests

response = requests.get('url')
soup = BeautifulSoup(response.text, 'html.parser')

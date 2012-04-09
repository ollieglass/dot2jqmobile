import sys
import pydot
from pprint import pprint


# first arg is the dot file
if len(sys.argv) < 2:
    print "usage: python dot2jqmobile.py dotfile.dot > jqmfile.html"
    exit()

g = pydot.graph_from_dot_file(sys.argv[1])

JQM_HEADER = '''
<!DOCTYPE html>
<html>
<head>
    <title>JQuery Mobile Boilerplate</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.0.1/jquery.mobile-1.0.1.min.css" />
    <script src="http://code.jquery.com/jquery-1.6.4.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.0.1/jquery.mobile-1.0.1.min.js"></script>

    <meta name="apple-mobile-web-app-capable" content="yes" />
</head>
<body>
'''

JQM_FOOTER = '</body>'

class Page():
    def __init__(self, name):
        self.name = name
        self.links = set()

    def __repr__(self):
        links_to_pages = ''
        for link in self.links:
            links_to_pages += '<a href="#%s" data-role="button">%s</a>' % (link, link)

        return """
    <div data-role="page" id="%s">
        <div data-role="header">
            <h1>%s</h1>
        </div>

        <div data-role="content">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pellentesque ultricies augue, eget luctus libero auctor vitae. Vivamus sed erat et nisl hendrerit malesuada. Phasellus feugiat nulla ut sapien consequat pretium. Nunc eget velit eros, quis ultricies neque</p>

            %s
        </div>
    </div>
    """ % (self.name, self.name, links_to_pages)

# work out all the node names - why can't pydot do this??
nodes = []

for edge in g.get_edge_list():
    if edge.get_destination() not in nodes:
        nodes.append(edge.get_destination())

    if edge.get_source() not in nodes:
        nodes.append(edge.get_source())

# build pages
pages = {node:Page(node) for node in nodes}

# add links
for edge in g.get_edge_list():
    pages[edge.get_source()].links.update([edge.get_destination()])
    pages[edge.get_destination()].links.update([edge.get_source()])

# build html
print JQM_HEADER
for page in pages:
    print pages[page]
print JQM_FOOTER

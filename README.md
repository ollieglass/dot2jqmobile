dot2jqmobile
========

dot2jqmobile generates a skeletal jQuery Mobile site from a DOT graph.

Usage
-----

Supply a dot file, pipe the output to an html file.


    python dot2jqmobile.py dotfile.dot > jqmfile.html


Example
-------

Here's a DOT graph:

    graph condiments {
        ketchup -- mayonnaise -- tartar -- lemon
        ketchup -- bbq
    }

And here's the generated jQuery Mobile site: http://db.tt/CV2UKgqW

**Bonus:** render an image of the graph with dot

![rendered graph](http://dl.dropbox.com/u/19419/dotmobile/test.png)

References
----------

* [jQuery Mobile](jquerymobile.com/)
* [DOT language](http://en.wikipedia.org/wiki/DOT_language)
* Pixelglow's [Graphviz](http://www.pixelglow.com/graphviz/) dot image renderer

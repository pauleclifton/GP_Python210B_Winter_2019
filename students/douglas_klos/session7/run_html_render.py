#!/usr/bin/env python3
#pylint: disable=C0103,W0612,W0622

# Douglas Klos
# March 1st, 2019
# Python 210, Session 7
# run_html_render.py

""" A simple script to run and test your html rendering classes. """

import time
from io import StringIO
import html_render as hr


def render_page(page, filename, indent=None):
    """
    Render the tree of elements.

    This uses StringIO to render to memory, then dump to console and write to file -- very handy!
    """

    f = StringIO()
    if indent is None:
        page.render(f)
    else:
        page.render(f, indent)

    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


def step1():
    """ Step 1 """
    page = hr.Element()
    page.append("Here is a paragraph of text -- there could be more of them, "
                "but this is enough to show that we can do some text")
    page.append("And here is another piece of text -- you should be able to add any number")

    render_page(page, "test_html_output1.html")


def step2():
    """ Step 2 """
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)

    render_page(page, "test_html_output2.html")


def step3():
    """ Step 3 """

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)

    render_page(page, "test_html_output3.html")


def step4():
    """ Step 4 """
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))

    page.append(body)

    render_page(page, "test_html_output4.html")


def step5():
    """ Step 5 """
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    page.append(body)

    render_page(page, "test_html_output5.html")


def step6():
    """ Step 6 """
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    body.append("And this is a ")
    body.append(hr.A("http://google.com", "link"))
    body.append("to google")
    page.append(body)

    render_page(page, "test_html_output6.html")


def step7():
    """ Step 7 """
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.H(2, "PythonClass - Class 6 example"))
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    list = hr.Ul(id="TheList", style="line-height:200%")
    list.append(hr.Li("The first item in a list"))
    list.append(hr.Li("This is the second item", style="color: red"))
    item = hr.Li()
    item.append("And this is a ")
    item.append(hr.A("http://google.com", "link"))
    item.append("to google")
    list.append(item)
    body.append(list)
    page.append(body)

    render_page(page, "test_html_output7.html")


def step8and9():
    """ Steps 8 and 9 """

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Meta(charset="UTF-8"))
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.H(2, "PythonClass - Class 6 example"))
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    list = hr.Ul(id="TheList", style="line-height:200%")
    list.append(hr.Li("The first item in a list"))
    list.append(hr.Li("This is the second item", style="color: red"))
    item = hr.Li()
    item.append("And this is a")
    item.append(hr.A("http://google.com", "link"))
    item.append("to google")
    list.append(item)
    body.append(list)
    page.append(body)

    render_page(page, "test_html_output8.html")
    render_page(page, "test_html_output9.html", "    ")


def main():
    """
    html_render main.

    Setup to loop specified number of times and report back the time it took.
    Was used to test if difference in f-string speed in the html_render class
    """

    # Execution times for 100,000 loops through the program in seconds
    # normal   59.82036113739014
    #          59.391337633132935
    #          59.326234340667725
    #          58.6301965713501
    # fstrings 59.7968487739563
    #          59.057918310165405
    #          58.57264804840088
    #          57.64731240272522
    # While not a huge difference, f-strings did on average execute slightly faster
    # Note code has changed a fair amount more since tests and speeds now are better.

    start = time.time()
    loop_counter = 1
    function_list = [step1, step2, step3, step4, step5, step6, step7, step8and9]

    for loop in range(loop_counter):
        for function in function_list:
            function()

    end = time.time()
    print(f'Execution time = {end - start}')


if __name__ == '__main__':
    main()

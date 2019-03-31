#!/usr/bin/env python3
#pylint: disable=W0401,W0612,C0103,E1120
""" Test cases for html_render.py """

# Douglas Klos
# March 14st, 2019
# Python 210, Session 9, Mailroom OO
# test_html_render.py


import io
import pytest
from html_render import *


def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """

    outfile = io.StringIO()
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()


def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    element = Element()
    element = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    element = Element("this is some text")
    element.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    element = Element("this is some text")
    element.append("and this is some more text")
    file_contents = render_result(element).strip()
    print(file_contents)

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.index("this is") < file_contents.index("and this")
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")
    assert file_contents.count("<html>") == 1
    assert file_contents.count("</html>") == 1


def test_render_element2():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    element = Element()
    element.append("this is some text")
    element.append("and this is some more text")
    file_contents = render_result(element).strip()
    print(file_contents)

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.index("this is") < file_contents.index("and this")
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


def test_html():
    """ Tests the <html> tag """
    html = Html("this is some text")
    html.append("and this is some more text")

    file_contents = render_result(html).strip()
    print(file_contents)

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.endswith("</html>")


def test_body():
    """ Tests the <body> tag """
    body = Body("this is some text")
    body.append("and this is some more text")
    file_contents = render_result(body).strip()
    print(file_contents)

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_head():
    """ Tests that you can add the <head> tag """
    head = Head("this is some text")
    head.append("and this is some more text")
    file_contents = render_result(head).strip()
    print(file_contents)

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.startswith("<head>")
    assert file_contents.endswith("</head>")


def test_p():
    """ Tests the <p> tag """
    p = P("this is some text")
    p.append("and this is some more text")
    file_contents = render_result(p).strip()
    print(file_contents)

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """ Tests that you can add another element and still render properly """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")
    file_contents = render_result(page)
    print(file_contents)

    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    assert "<p>" in file_contents
    assert "</p>" in file_contents


def test_title():
    """
    Tests that you can add a title element to the page
    and that expected tags are properly included
    """
    title = Title("This is a title")
    file_contents = render_result(title).strip()
    print(file_contents)

    assert "<title>This is a title</title>" in file_contents
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")
    assert "\n" not in file_contents


def test_one_line_tag_append():
    """ You should not be able to append content to a OneLineTag """
    olt = OneLineTag("the initial content")
    with pytest.raises(NotImplementedError):
        olt.append("some more content")
    file_contents = render_result(olt).strip()
    print(file_contents)

    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")
    assert "the initial content" in file_contents
    assert "some more content" not in file_contents


def test_attributes():
    """ Tests that attributes can be added to elements """
    p = P("A paragraph of text", style="text-align: center", id="intro")
    file_contents = render_result(p).strip()
    print(file_contents)

    assert "A paragraph of text" in file_contents
    assert file_contents.startswith("<p ")
    assert file_contents.endswith("</p>")
    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents
    assert file_contents[:-1].index(">") > file_contents.index('id="intro"')
    assert file_contents[:file_contents.index(">")].count(" ") == 3


def test_self_closing_tag():
    """
    Tests that you can add a SelfClosingTag

    SelfClosingTag class inherits from Element, which has tag type html
    We expect this to render a self closing html tag.
    A nonsensical tag but relevant for testing the base class
    """
    sct = SelfClosingTag()
    file_contents = render_result(sct).strip()
    print(file_contents)

    assert file_contents == "<html />"


def test_self_closing_tag2():
    """ Tests that you can not append to a self closing tag """
    sct = SelfClosingTag()
    with pytest.raises(NotImplementedError):
        sct.append("This is some text")
    file_contents = render_result(sct).strip()
    print(file_contents)

    assert "This is some text" not in file_contents


def test_self_closing_tag_content():
    """ Tests that you can not init SelfClosingTag with content """
    html = Html()
    with pytest.raises(TypeError):
        html.append(SelfClosingTag("This is some appended content"))
    file_contents = render_result(html).strip()
    print(file_contents)

    assert "This is some appended content" not in file_contents


def test_hr():
    """ Tests that a basic <hr /> tag can be added """
    hr = Hr()
    file_contents = render_result(hr).strip()
    print(file_contents)

    assert file_contents == '<hr />'


def test_hr_attr():
    """ Tests that a hr can be added with attributes """
    hr = Hr(width=400)
    file_contents = render_result(hr).strip()
    print(file_contents)

    assert file_contents == '<hr width="400" />'


def test_br():
    """ Tests that a basic <br /> tag can be added """
    br = Br()
    file_contents = render_result(br).strip()
    print(file_contents)

    assert file_contents == '<br />'


def test_br_attr():
    """ Tests that a basic <br /> tag can accepts no attributes """
    html = Html()
    with pytest.raises(TypeError):
        html.append(Br(width=400))
    file_contents = render_result(html).strip()
    print(file_contents)

    assert 'width="400"' not in file_contents


def test_meta():
    """ Tests the meta tag """
    head = Head()
    head.append(Meta(charset="UTF-8"))
    head.append("This is some text")
    file_contents = render_result(head).strip()
    lines = file_contents.split('\n')
    print(file_contents)

    assert file_contents.startswith("<head>")
    assert lines[1] == ('<meta charset="UTF-8" />')
    assert file_contents.endswith("</head>")


def test_anchor1():
    """ Tests that you can add an anchor """
    a = A("http://google.com", "link to google")
    file_contents = render_result(a).strip()
    print(file_contents)

    assert file_contents.startswith('<a href="http://google.com">')
    assert file_contents.endswith('</a>')
    assert 'link to google' in file_contents


def test_anchor2():
    """ Tests that you can not add an empty anchor """
    with pytest.raises(TypeError):
        a = A()


def test_anchor3():
    """ Tests that anchor must have link and content """
    with pytest.raises(TypeError):
        a = A("http://google.com")


def test_ul_li():
    """ Tests that you can add unordered lists and list items """
    with pytest.raises(TypeError):
        ul = Ul("Should fail")
    ul = Ul(style='list-style-type:disc;')
    ul.append(Li("List item 1"))
    ul.append(Li("List item 2"))
    file_contents = render_result(ul).strip()
    print(file_contents)

    assert file_contents.startswith("<ul ")
    assert file_contents.endswith("</ul>")
    assert "List item 1" in file_contents
    assert "List item 2" in file_contents
    assert file_contents.count("<li>") == 2
    assert file_contents.count("</li>") == 2


def test_header1():
    """ Tests that you can add a OneLineTag of type H containing content """
    with pytest.raises(ValueError):
        h = H("Undefined header level")
    h = H(1, "Header level 1")
    file_contents = render_result(h).strip()
    print(file_contents)

    assert file_contents.startswith("<h1>")
    assert file_contents.endswith("</h1>")
    assert "<h1>Header level 1</h1>" in file_contents


def test_header2():
    """ Tests that other types of header tags can be added into a body """
    body = Body()
    body.append(H(2, "Header level 2"))
    body.append(H(3, "Header level 3"))
    body.append(H(4, "Header level 4"))
    file_contents = render_result(body).strip()
    print(file_contents)

    assert "<h2>Header level 2</h2>" in file_contents
    assert "<h3>Header level 3</h3>" in file_contents
    assert "<h4>Header level 4</h4>" in file_contents


def test_doctype():
    """ Tests that the html class properly adds a doctype only once to the start of the file """
    html = Html("This is HTML block")
    file_contents = render_result(html).strip()
    print(file_contents)

    assert file_contents.startswith("<!DOCTYPE html>")
    assert file_contents.count("<!DOCTYPE html>") == 1


def test_indent():
    """ Tests that the indentation gets passed through to the renderer """
    html = Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()  # remove the end newline
    lines = file_contents.split("\n")
    print(file_contents)

    assert lines[0].startswith("<!DOCTYPE html>")
    assert lines[1].startswith("<html>")
    assert lines[2].startswith("   some content")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")
    lines = file_contents.split("\n")
    print(file_contents)

    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
    """ Make sure multiple levels get indented fully """
    body = Body()
    body.append(P("some text"))
    html = Html(body)
    file_contents = render_result(html)
    lines = file_contents.split("\n")
    print(file_contents)

    for i in range(3):
        assert lines[i + 1].startswith(i * Element.indent + "<")
    assert lines[4].startswith(3 * Element.indent + "some")


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    We are expecting to to look like this:

    <html>
        this is some text
    </html>

    More complex indentation should be tested later.
    """
    element = Element("this is some text")
    file_contents = render_result(element).strip()
    assert "this is some text" in file_contents
    lines = file_contents.split('\n')
    assert lines[0] == "<html>"
    assert lines[1].startswith(Element.indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")


def test_tables1():
    """ Tests table tags 'table, th, tr, td' """
    indent = '    '
    page = Html()
    head = Head()
    head.append(Meta(charset="UTF-8"))
    head.append(Title("test_html_render"))
    page.append(head)
    body = Body()
    body.append(H(2, "test html render"))
    table = Table(border=1)
    table.append(Caption('caption'))
    table.append(Th('Name'))
    table.append(Th('Age'))
    table.append(Th('Sex'))
    table_row = Tr()
    table_row.append(Td('Doug'))
    table_row.append(Td('39'))
    table_row.append(Td('Male'))
    table.append(table_row)
    body.append(table)
    page.append(body)
    file_contents = render_result(page, indent)
    print(file_contents)

    lines = file_contents.split('\n')
    assert lines[0] == '<!DOCTYPE html>'
    assert lines[1] == '<html>'
    assert lines[2] == indent + '<head>'
    assert lines[3] == indent*2 + '<meta charset="UTF-8" />'
    assert lines[4] == indent*2 + '<title>test_html_render</title>'
    assert lines[5] == indent*1 + '</head>'
    assert lines[6] == indent*1 + '<body>'
    assert lines[7] == indent*2 + '<h2>test html render</h2>'
    assert lines[8] == indent*2 + '<table border="1">'
    assert lines[9] == indent*3 + '<caption>caption</caption>'
    assert lines[10] == indent*3 + '<th>Name</th>'
    assert lines[11] == indent*3 + '<th>Age</th>'
    assert lines[-10] == indent*3 + '<th>Sex</th>'
    assert lines[-9] == indent*3 + '<tr>'
    assert lines[-8] == indent*4 + '<td>Doug</td>'
    assert lines[-7] == indent*4 + '<td>39</td>'
    assert lines[-6] == indent*4 + '<td>Male</td>'
    assert lines[-5] == indent*3 + '</tr>'
    assert lines[-4] == indent*2 + '</table>'
    assert lines[-3] == indent + '</body>'
    assert lines[-2] == "</html>"

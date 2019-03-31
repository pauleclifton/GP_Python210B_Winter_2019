"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()

########
# Step 1
########


def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")

# # Uncomment this one after you get the one above to pass
# # Does it pass right away?


def test_render_element2():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element()
    e.append("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


# # ########
# # # Step 2
# # ########

# tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents


########
# Step 3
########

# Add your tests here!
def test_head_subclass():
    """ 
    Tests the 'head' sublcass is functioning as it should 
    I'm just copying the tests from above for this one.
    """
    page = Head()
    page.append('Just some text to test head subclass')

    file_contents = render_result(page)
    print(file_contents)

    assert "some text to" in file_contents
    assert "head subclass" in file_contents
    assert "<head>" in file_contents
    assert "</head>" in file_contents


def test_one_line_tag():
    """ Tests subclass OneLineTag operating on its own using a random tag """
    page = OneLineTag()
    page.tag = 'swizzle'
    page.append('Testing OneLineTag with swizzle')

    file_contents = render_result(page)
    print(file_contents)

    assert 'Testing OneLineTag' in file_contents
    assert '<swizzle>' in file_contents
    assert '<swizzle> Testing OneLineTag with swizzle </swizzle>' in file_contents


def test_title():
    """ 
    Testing the Title subclass of OneLineTag.
    Checking to see if it's all on one line.
    """
    page = Title()
    page.append('Testing title subclass')
    page.append('Adding some more text to the test')

    file_contents = render_result(page)
    print(file_contents)

    assert "title subclass" in file_contents
    assert "Adding some more"
    assert "<title>" in file_contents
    assert ("<title> Testing title subclass"
            "Adding some more text to the test </title>") in file_contents


def test_kwargs_render():
    """
    Testing render function with kwargs. Specifically to see if they are unpacked
    and inserted properly with only one and with multiple kwargs.
    """
    page = Html()

    head = Head()
    head.append("Render Kwargs Test")

    page.append(head)

    body = Body()
    body.append(Title("This is magical test", style="color: purple;"))
    body.append(P("Just some text in the body",
                  clas="super-cool", height="400px", width="250px"))

    p_attrs = {'style': "font-size: 5rem;",
               'height': "500px", 'width': "350px"}
    body.append(
        P("Additional text in the body to test unpacking attributes", **p_attrs))

    page.append(body)

    file_contents = render_result(page)
    print(file_contents)

    assert "<head>\nRender Kwargs Test\n</head>" in file_contents
    assert "<title style=" in file_contents
    assert "<p style='font-size" in file_contents
    assert "class='super-cool' height='400px' width='250px'" in file_contents

    # This one is for the unpacked p_attrs test
    assert "<p style='font-size: 5rem;' height='500px'" in file_contents


def test_self_closing():
    """ Testing the self closing tag subclass with and without kwargs """
    page = Html()
    head = Head()
    head.append(Title('The self closing tag test'))
    page.append(head)

    body = Body()
    body.append(Hr())
    body.append(Br())
    body.append(Hr(clas='horizontal', style='color: red'))

    page.append(body)

    file_contents = render_result(page)
    print(file_contents)

    assert '<hr />' in file_contents
    assert "<hr class='horizontal'" in file_contents
    assert '<br />' in file_contents


def test_a_tag():
    """ Testing the a tag. """
    page = Html()
    head = Head()
    head.append(Title('Testing the a tag'))
    page.append(head)

    body = Body()
    body.append(A('www.google.com', 'Google'))
    body.append(
        A('www.youtube.com', 'Still google, sort of', style='color:red;'))
    page.append(body)

    file_contents = render_result(page)
    print(file_contents)

    assert "<a href='www.google" in file_contents
    assert "<a style='color" in file_contents


def test_doctype():
    """ Testing to see if doctype is inserted at top of file """
    page = Html()

    file_contents = render_result(page)
    print(file_contents)

    assert "<!DOCTYPE" in file_contents

def test_meta_charset():
    page = Html()
    head = Head()
    head.append(Meta(charset="UTF-8"))
    page.append(head)

    file_contents = render_result(page)
    print(file_contents)

    assert "charset='UTF" in file_contents

# #####################
# # indentation testing
# #  Uncomment for Step 9 -- adding indentation
# #####################

# def test_indent():
#     """
#     Tests that the indentation gets passed through to the renderer
#     """
#     html = Html("some content")
#     file_contents = render_result(
#         html, ind="   ").rstrip()  # remove the end newline

#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[0].startswith("   <")
#     print(repr(lines[-1]))
#     assert lines[-1].startswith("   <")

# def test_indent_contents():
#     """
#     The contents in a element should be indented more than the tag
#     by the amount in the indent class attribute
#     """
#     html = Element("some content")
#     file_contents = render_result(html, ind="")

#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[1].startswith(Element.indent)

# def test_multiple_indent():
#     """
#     make sure multiple levels get indented fully
#     """
#     body = Body()
#     body.append(P("some text"))
#     html = Html(body)

#     file_contents = render_result(html)

#     print(file_contents)
#     lines = file_contents.split("\n")
#     for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
#         assert lines[i + 1].startswith(i * Element.indent + "<")

#     assert lines[4].startswith(3 * Element.indent + "some")

# def test_element_indent1():
#     """
#     Tests whether the Element indents at least simple content

#     we are expecting to to look like this:

#     <html>
#         this is some text
#     <\html>

#     More complex indentation should be tested later.
#     """
#     e = Element("this is some text")

#     # This uses the render_results utility above
#     file_contents = render_result(e).strip()

#     # making sure the content got in there.
#     assert("this is some text") in file_contents

#     # break into lines to check indentation
#     lines = file_contents.split('\n')
#     # making sure the opening and closing tags are right.
#     assert lines[0] == "<html>"
#     # this line should be indented by the amount specified
#     # by the class attribute: "indent"
#     assert lines[1].startswith(Element.indent + "thi")
#     assert lines[2] == "</html>"
#     assert file_contents.endswith("</html>")

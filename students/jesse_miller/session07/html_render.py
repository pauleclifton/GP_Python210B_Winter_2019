#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class Element():
    '''
    The base rendering class
    '''
    tag = 'html'
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = []
        if content is not None:
            self.contents = [content]

    def append(self, new_content):
        '''
        Appends strings as called
        '''
        self.contents.append(new_content)

    def attrib(self):
        """
        This was the only way I could get attributes to work properly.  I
        think I just still get mired in funcitons
        """
        attrb = "".join([' {}="{}"'.format(key, val)
                         for key, val in self.attributes.items()]
                        )
        return attrb

    def make_open_tag(self, cur_ind=""):
        """
        Renders tags with content
        """
        open_tag = "<{}{}>".format(self.tag, self.attrib())
        return cur_ind + open_tag

    def render(self, out_file, cur_ind=""):
        #pylint: disable=W0613
        '''
        Writes the outfile in question using data set and HTML tags
        '''
        out_file.write(cur_ind)
        out_file.write(self.make_open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(str(content) + "\n")
        out_file.write(cur_ind)
        out_file.write("</{}>\n".format(self.tag))


class OneLineTag(Element):
    '''
    This is the class that processes HTML tags.
    '''
    tag = "Title"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self.make_open_tag())
        for content in self.contents:
            out_file.write(str(content))
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
    #pylint: disable=W0221
        raise NotImplementedError

class SelfClosingTag(Element):
    """
    This will render tags without content
    """
    #pylint: disable=W0221
    def append(self, *args, **kwargs):
        raise TypeError("A self closing tag should have no content")

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    #pylint: disable=W0221
    def render(self, out_file, cur_ind=""):
        open_tag = self.make_open_tag()
        out_file.write(cur_ind)
        out_file.write(open_tag.replace(">", " />"))
        out_file.write("\n")

class Br(SelfClosingTag):
    """
    Guess what, it's a <br> tag!
    """
    tag = "br"

class Hr(SelfClosingTag):
    """
    Class def for <hr> tag
    """
    tag = "hr"

class Html(Element):
    '''
    Class definition for <html> tag
    '''
    tag = 'html'

    #pylint: disable=W0221
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

class Body(Element):
    '''
    Class definition for <body> tag
    '''
    tag = 'body'

#pylint: disable=C0103
class P(Element):
    '''
    Class definition for <p> tag
    '''
    tag = 'p'


class Head(Element):
    '''
    Class definition for <head> tag
    '''
    tag = 'head'


class Title(OneLineTag):
    #pylint: disable=W0223
    '''
    Class definition for <title> tag
    '''
    tag = "title"

class A(OneLineTag):
    #pylint: disable=W0223
    """
    Class def for <a>
    """
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):
    #pylint: disable=W0223
    """
    Class definition for <H>
    """
    tag = 'H'

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(content, **kwargs)

class Ul(Element):
    """
    AttributeError: module 'html_render' has no attribute 'Ul
    """
    tag = 'Ul'

class Li(Element):
    """
    AttributeError: module 'html_render' has no attribute 'Li
    """
    tag = 'Li'

class Meta(SelfClosingTag):
    """
    Meta tags
    """
    tag = "meta"

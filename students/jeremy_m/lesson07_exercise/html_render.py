#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, contents=None, **kwargs):
        if contents:
            self.contents = [contents]
        else:
            self.contents = []

        self.kwargs = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_indent=''):
        # out_file.write(ind)
        if self.kwargs:
            out_file.write("{}<{}".format(cur_indent, self.tag))
            self.render_kwargs(out_file)
            out_file.write(">\n")
        else:
            out_file.write("{}<{}>\n".format(cur_indent, self.tag))

        self.render_content(out_file)

        out_file.write('\n')
        out_file.write("</{}>\n".format(self.tag))

    def render_kwargs(self, out_file):
        for kwarg, value in self.kwargs.items():
            if kwarg == 'clas':
                out_file.write(" class='{}'".format(value))
            else:
                out_file.write(" {}='{}'".format(kwarg, value))

    def render_content(self, out_file):
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                # out_file.write(ind)
                out_file.write(content)


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_indent=''):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class OneLineTag(Element):
    def render(self, out_file, cur_indent=''):
        out_file.write(cur_indent)
        if self.kwargs:
            out_file.write("<{}".format(self.tag))
            self.render_kwargs(out_file)
            out_file.write("> ")
        else:
            out_file.write("<{}> ".format(self.tag))

        self.render_content(out_file)
        out_file.write(" </{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class H(OneLineTag):
    tag = 'h'

    def __init__(self, level, contents=None, **kwargs):
        """ 
        I'm pretty confused about how to properly pass variables to the superclass'
        init. Just saw some people asked about it for the weeks office hours so
        I'll watch that, review my notes, and hopefully come back to fix this.
        """
        Element.__init__(self)
        self.level = level
        if contents:
            self.contents = [contents]
        else:
            self.contents = []
        self.kwargs = kwargs

    def render(self, out_file, cur_indent=''):
        out_file.write(cur_indent)
        if self.kwargs:
            out_file.write("<{}{}".format(self.tag, self.level))
            self.render_kwargs(out_file)
            out_file.write("> ")
        else:
            out_file.write("<{}{}> ".format(self.tag, self.level))

        self.render_content(out_file)
        out_file.write(" </{}{}>\n".format(self.tag, self.level))


class SelfClosingTag(Element):
    def render(self, out_file, cur_indent=''):
        out_file.write(cur_indent)
        if self.kwargs:
            out_file.write("<{}".format(self.tag))
            self.render_kwargs(out_file)
            out_file.write(" />\n")
        else:
            out_file.write("<{} />\n".format(self.tag))

        self.render_content(out_file)


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class Meta(SelfClosingTag):
    tag = "meta"


class A(Element):
    tag = 'a'

    def __init__(self, link, contents=None, **kwargs):
        """ 
        I'm a little confused about where to call 'Element.__init__'.
        I can't pass 'contents' to it without getting:
            AttributeError: 'str' object has no attribute 'contents'
        haven't figured out why yet but it works the way it is.
        """
        Element.__init__(self)
        self.link = link
        if contents:
            self.contents = [contents]
        else:
            self.contents = []
        self.kwargs = kwargs

    def render(self, out_file, cur_indent=''):
        out_file.write(cur_indent)
        if self.kwargs:
            out_file.write("<{}".format(self.tag))
            self.render_kwargs(out_file)
            out_file.write("href='{}'".format(self.link))
            out_file.write(">")
        else:
            out_file.write("<{} href='{}'>".format(self.tag, self.link))

        self.render_content(out_file)
        out_file.write("</{}>\n".format(self.tag))

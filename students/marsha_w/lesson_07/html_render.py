#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'  # this is a class object

    indent = '  '

    def __init__(self, content=None, **kwargs):
        self.contents = [content]  # contents to an ordered list
        self.attributes = kwargs

    def append(self, new_content):
        '''append new content to the content list'''
        self.contents.append(new_content)

    def _open_tag(self):
        return '<{}'.format(self.tag)

    def _close_tag(self):
        return '</{}>\n'.format(self.tag)

    def render(self, out_file, cur_ind=""):
        '''loop through the list of contents'''
        open_tag = [self._open_tag()]
        for keys, values in self.attributes.items():
            element_attributes = ' ' + keys + '=' + '"' + str(values) + '"'  # this is clunky
            open_tag.append(element_attributes)
        open_tag.append('>\n')

        out_file.write(cur_ind)
        out_file.write("".join(open_tag))

        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                    out_file.write('\n')
        out_file.write(cur_ind)
        out_file.write(self._close_tag())


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=""):

        '''loop through the list of contents'''

        out_file.write('<!DOCTYPE html>\n')
        open_tag = [self._open_tag()]

        for keys, values in self.attributes.items():
            element_attributes = ' ' + keys + '=' + '"' + str(values) + '"'  # this is clunky
            open_tag.append(element_attributes)
        open_tag.append('>\n')

        out_file.write(cur_ind)
        out_file.write("".join(open_tag))

        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                    out_file.write('\n')

        out_file.write(cur_ind)
        out_file.write(self._close_tag())


class Body(Element):
    tag = 'body'



class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        open_tag = [self._open_tag()]
        open_tag.append('> ')

        out_file.write(cur_ind)
        out_file.write("".join(open_tag))
        out_file.write(self.contents[0])
        out_file.write(cur_ind)
        out_file.write(self._close_tag())

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class H2(OneLineTag):
    tag = 'h2'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = 'hr'

    def render(self, out_file, cur_ind=""):
        tag = [self._open_tag()]
        for keys, values in self.attributes.items():
            element_attributes = ' ' + keys + '=' + '"' + str(values) + '"'  # this is clunky
            tag.append(element_attributes)
        tag.append(" />\n")

        out_file.write(cur_ind)
        out_file.write("".join(tag))


class Br(Hr):
    tag = 'br'

class Meta(Hr):
    tag = 'meta'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

    def render(self, out_file, cur_ind=""):
        open_tag = [self._open_tag()]
        for keys, values in self.attributes.items():
            element_attributes = ' ' + keys + '=' + '"' + str(values) + '"'  # this is clunky
            open_tag.append(element_attributes)
        open_tag.append('>')

        out_file.write(cur_ind)
        out_file.write("".join(open_tag))
        out_file.write(self.contents[0])

        out_file.write(cur_ind)
        out_file.write(self._close_tag())


class Li(Element):
    tag = 'li'


class Ul(Element):
    tag = 'ul'


class H(OneLineTag):

    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        self.tag = '{}{}'.format('h', str(level))
        super().__init__(content, **kwargs)













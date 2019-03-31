#!/usr/bin/env python3
import pytest

"""
A class-based system for rendering html.
"""

# This is the framework for the base class


class Element(object):
    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        try:
            self.contents.append(content)
        except AttributeError:
            self.contents = []
            if content is not None:
                self.contents.append(content)

    def append(self, new_content):
        "appends content with new_content"
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(f'{cur_ind}')
        self._open_tag(out_file)
        out_file.write('>\n')
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(f'{cur_ind}{self.indent}')
                out_file.write(content)
            out_file.write('\n')
        out_file.write(f'{cur_ind}')
        self._close_tag(out_file)

    def _open_tag(self, out_file, cur_ind=""):
        if self.attributes:
            out_file.write(f'<{self.tag} ')
            open_tag =[f'{key}="{value}" ' for key,value in self.attributes.items()]
            open_tag_string = ''.join(open_tag).rstrip()
            out_file.write(f'{open_tag_string}')
        else:
            out_file.write(f'<{self.tag}')

    def _close_tag(self, out_file, cur_ind=""):
        out_file.write(f'</{self.tag}>')


class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind="")# I could change this to "   " so html gets indented


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(f'{cur_ind}{self.indent}')
        out_file.write(f'<{self.tag}>')
        for content in self.contents:
            out_file.write(content)
        out_file.write(f'</{self.tag}>')

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(f'{cur_ind}{self.indent}')
        super()._open_tag(out_file)
        out_file.write(f' />')


class Hr(SelfClosingTag):
    tag = "hr"

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Br(SelfClosingTag):
    tag = "br"

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class A(Element):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(f'{cur_ind}{self.indent}')

        Element._open_tag(self, out_file)
        out_file.write(f'>')
        for content in self.contents:
            out_file.write(content)
        out_file.write(f'</{self.tag}>')


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(Element):
    def __init__(self, level, content=None, **kwargs):
        level = str(level)
        self.tag = f'h{level}'
        super().__init__(content=content, **kwargs)


class Meta(SelfClosingTag):
    tag = 'meta'

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

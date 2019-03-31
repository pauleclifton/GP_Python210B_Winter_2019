#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
import functools


# This is the framework for the base class
class Element(object):
    indent = ''
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.attrs = kwargs
        if content:
            self.content = [content]
        else:
            self.content = []

    def _front_tag(self):
        """Creates the front/opening tag"""
        return f'<{self.tag}>'

    def _end_tag(self):
        """Creates the ending tag"""
        return f'</{self.tag}>'

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_name, indent="", ind_count=0):

        self.indent = indent * ind_count

        file_name.write(f'{self.indent}{self._front_tag()[:-1]}')
        for key, value in self.attrs.items():
            file_name.write(f' {key}="{value}"')
        file_name.write(f'{self._front_tag()[-1:]}\n')

        for content in self.content:
            if hasattr(content, 'render'):
                content.render(file_name, indent, ind_count + 1)
            else:
                file_name.write(f'{self.indent}{indent}{content}\n')

        file_name.write(f'{self.indent}{self._end_tag()}\n')


class Html(Element):
    """
    html sublcass
    """
    tag = 'html'

    def render(self, file_name, indent="", ind_count=0):
        self.indent = indent
        file_name.write(f'<!DOCTYPE html>\n')
        super().render(file_name, indent)


class P(Element):
    """
    class for p tag
    """
    tag = 'p'


class Body(Element):
    """
    class for p tag
    """
    tag = 'body'


"""
Step 3: print on one line
"""


class OneLineTag(Element):

    def append(self, new_content):

        raise NotImplementedError

    def render(self, file_name, indent="", ind_count=0):

        self.indent = indent * ind_count

        file_name.write(f'{self.indent}{self._front_tag()[:-1]}')
        for key, value in self.attrs.items():
            file_name.write(f' {key}="{value}"')
        file_name.write(f'{self._front_tag()[-1:]}')
        file_name.write(f'{self.content[0]}')
        file_name.write(f'{self._end_tag()}\n')


class Head(Element):
    tag = "head"


"""
Step 5: Self closing tag
"""


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):

        if content: raise TypeError
        self.attrs = kwargs

    def append(self, new_content):
        raise NotImplementedError


    def render(self, file_name, indent="", ind_count=0):

        """
        if content is entered this tells user that self closing tags
        can't have conent and resets the conent to an empty string.
        """

        self.indent = indent * ind_count

        file_name.write(f'{self.indent}{self._front_tag()[:-1]}')
        for k, v in self.attrs.items():
            file_name.write(f' {k}="{v}"')
        file_name.write(f' />\n')


"""
Step 6
"""


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        if not (content and link):
            raise TypeError

        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Hr(SelfClosingTag):

    tag = 'hr'


# <br /> is XHTML format
class Br(SelfClosingTag):
    tag = 'br'

    def __init__(self, content=None, **kwargs):

        if kwargs: raise TypeError

        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'

    def __init__(self, content=None, **kwargs):

        if content: raise TypeError

        self.contents = []
        self.attrs = kwargs


class Li(Element):
    """
    Step 7: Li class
    """
    list_element = ''


class Meta(SelfClosingTag):
    """
    add meta tag
    """

    tag = 'meta'

class Title(OneLineTag):

    tag = 'title'

class H(OneLineTag):

    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        try:
            int(level)
        except ValueError:
            raise ValueError

        self.tag = f'h{level}'
        super().__init__(content, **kwargs)

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# Base class
class Element():
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = []
        if content is not None:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def attrib(self):
        attribs = "".join([' {}="{}"'.format(key, val)
                         for key, val in self.attributes.items()]
                        )
        return attribs

    def open_tag(self, cur_ind=""):
        open_tag = "<{}{}>".format(self.tag, self.attrib())
        return cur_ind + open_tag

    def render(self, out_file, cur_ind=""):
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


# Process HTML tags
class OneLineTag(Element):
    tag = 'onelinetag'

    def append(self, new_content):
        raise NotImplementedError

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' ' + key + '="' + str(value) + '"')
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write('\n')


# Render tags without content
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, cur_ind=""):
        tag = cur_ind + self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Title(OneLineTag):
    tag = "title"


class Br(SelfClosingTag):

    tag = "br"


class Hr(SelfClosingTag):

    tag = "hr"


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    tag = 'H'

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'Ul'


class Li(Element):
    tag = 'Li'


class Meta(SelfClosingTag):
    tag = "meta"
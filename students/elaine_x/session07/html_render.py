#!/usr/bin/env python3
'''
##########################
#Python 210
#Session 07 - HTML Render Exercise
#Elaine Xu
#Feb 27, 2019
###########################
'''
"""
A class-based system for rendering html.
"""

####################
#Step 1
####################
# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        #print(self.attributes)
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' ' + key + '="' + str(value) + '"')
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind+self._open_tag())
        out_file.write('\n')
        #loop through the list of contents
        for content in self.contents:
            try:
                content.render(out_file, cur_ind+self.indent)
            except AttributeError:
                out_file.write(cur_ind+self.indent+content)
                out_file.write("\n")
        out_file.write(cur_ind+self._close_tag())
        out_file.write('\n')


####################
#Step 2
####################
class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind = ""):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'


####################
#Step 3
####################
class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    tag = 'title'


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

class Title(OneLineTag):
    tag = 'title'

####################
#Step 4
####################
#updating Element() with **kwargs

####################
#Step 5
####################
class SelfClosingTag(Element):
    tag = 'hr'
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, cur_ind=""):
        tag = cur_ind + self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'


####################
# Step 6
####################
class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

####################
# Step 7
####################
class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        tag = 'h' + str(level)
        self.tag = tag
        super().__init__(content=content, **kwargs)


####################
#Step 8
####################
#updating Html() to include <!DOCTYPE html>
class Meta(SelfClosingTag):
    tag = 'meta'

####################
#Step 9
####################
#add indent to Element(), modify def render()

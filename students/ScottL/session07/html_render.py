#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class Element:
    """Base object to initialize and render other objects for creating HTML code"""

    tag = "html"
    indent = " " * 4

    def __init__(self, content=None, **kwargs):
        """
        Initialize element objects as instance lists or empty lists
        :param content: can be a string or another object based on the 'Element' class
        :param kwargs: variable-length dictionary to store object attributes
        """
        self.attributes = kwargs
        if content:
            self.content_list = [content]
        else:
            self.content_list = []

    def append(self, new_content):
        """
        Add new content to an existing object.
        :param new_content: string or other object based on the 'Element' class
        """
        self.content_list.append(new_content)

    def render_attributes(self, curr_indent=""):
        """
        Perform repetitive formatting for tags
        :param curr_indent: a string of blank spaces for formatting the output for legibility
        :return: a string containing the tag name and any formatting (i.e. attributes)
        """
        tag_start = [f"\n{curr_indent}<{self.tag}"]
        for attribute in self.attributes:
            tag_start.append(str(attribute) + '="' +
                             str(self.attributes[attribute]) + '"')
        return " ".join(tag_start)

    def render(self, out_file, curr_indent=""):
        """
        Recursively write the contents of HTML objects to a disk/location.
        :param out_file: file location to write text
        :param curr_indent: a string of blank spaces for formatting the output for legibility
        """
        out_file.write(self.render_attributes(curr_indent) + '>')
        for item in self.content_list:
            if isinstance(item, str):
                out_file.write(f"\n{curr_indent + self.indent}{item}")
            else:
                item.render(out_file, curr_indent + self.indent)
        out_file.write(f"\n{curr_indent}</{self.tag}>")


class Html(Element):
    """An 'Element' object for 'html' tags"""

    tag = "html"

    def render(self, out_file, curr_indent=""):
        out_file.write("<!DOCTYPE html>")
        Element.render(self, out_file, curr_indent)


class Body(Element):
    """An 'Element' object for 'body' tags"""

    tag = "body"


class H(Element):
    """An 'Element' object for 'head' tags"""

    tag = "head"


class P(Element):
    """An 'Element' object for paragraph or 'p' tags"""

    tag = "p"


class OneLineTag(Element):
    """An 'Element' object for writing an opening and closing tag on one line"""

    def render(self, out_file, curr_indent=""):
        """
        A variation on the base 'Element' render function to open and close on a single line
        :param out_file: file location to write text
        :param curr_indent: a string of blank spaces for formatting the output for legibility
        """
        out_file.write(self.render_attributes(curr_indent) + ">")
        out_file.write(f"{self.content_list}</{self.tag}>")


class Title(OneLineTag):
    """A 'OneLineTag' object specifically for displaying the 'Title' of an html page"""

    tag = "title"

    def __init__(self, content=None, **kwargs):
        """
        Over-ride the object initializer to use a single text item as content, not a list
        :param content: string containing the title of the page
        :param kwargs: variable-length dictionary to store object attributes
        """
        super(Title, self).__init__()
        self.content_list = content
        self.attributes = kwargs


class SelfClosingTag(Element):
    """A special subset of 'Element' class that takes only attributes, not 'content'"""

    def __init__(self, **kwargs):
        """
        Initialize object with a dictionary of attributes
        :param kwargs: variable-length argument to store object attributes
        """
        super(SelfClosingTag, self).__init__()
        self.attributes = kwargs

    def render(self, out_file, curr_indent=""):
        """
        Write the attributes to file
        :param out_file: file/memory location
        :param curr_indent: a string of blank spaces for formatting the output for legibility
        """
        out_file.write(self.render_attributes(curr_indent) + " />")


class Meta(SelfClosingTag):
    """A subset of the 'SelfClosingTag' for storing character type)"""

    tag = "meta"

    def __init__(self, charset="UTF-8"):
        """
        Over-ride initializer to store the key word and its argument
        :param charset: string denoting the character encoding
        """
        super(Meta, self).__init__()
        self.attributes = {"charset": charset}


class Hr(SelfClosingTag):
    """A specific subset of the SelfClosingTag object"""

    tag = "hr"


class Br(SelfClosingTag):
    """A specific subset of the SelfClosingTag object"""

    tag = "br"


class A(Element):
    """A type of 'Element' object that stores and renders hyperlinks for websites"""

    tag = "a"

    def __init__(self, link=None, content=None):
        """
        Initializer that accepts a url link and a name/description for the link
        :param link: string containing a URL for a website
        :param content: string to describe the link
        """
        super(A, self).__init__()
        self.link = link
        self.content = content

    def render(self, out_file, curr_indent=""):
        """
        Override the render function to create a hyperlink from the web address
        :param out_file: location of the file/memory allocation for writing the data
        :param curr_indent: a string of blank spaces for formatting the output for legibility
        """
        out_file.write(f"\n{curr_indent}<{self.tag} "
                       f"href={self.link}>{self.content}</{self.tag}>")


class Li(Element):
    """A subset of the 'Element' class for storing data on individual lines"""

    tag = "li"


class Ul(Element):
    """A subset of the 'Element' class for grouping lines together"""

    tag = "ul"


class Head(OneLineTag):
    """A subset of 'OneLineTag' for incorporating an integer into the heading tag"""

    def __init__(self, level=None, content=None):
        """

        :param level: integer designating the level of the heading
        :param content: string for adding additional content to the heading level tag
        """
        super(Head, self).__init__()
        self.tag = f"h{level}"
        self.content_list = content



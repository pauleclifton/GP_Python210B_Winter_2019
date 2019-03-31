
#-------------------
#!/usr/bin/env python3
#Session 07 Exercise:HTML_Render
#Shirin Akther
#-------------------------

"""
A class-based system for rendering html.
"""
# This is the framework for the base class

class Element(object):
    tag = 'html'
    indent = "   "
    def __init__(self, content=None, **kwargs):
        """Initializing the Element class"""
        if content:
            self.contents = [content]
        else:
            self.contents = []
        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def att_output(self):
        att_output = []
        for k, v in self.attributes.items():
            att_output.append(f'{k}="{v}"')
        return ' '.join(att_output)


    def append(self, new_content):
        """appending the contents to the class object"""

        self.contents.append(new_content)


    def open_tag(self):
        if self.att_output():
            return f'<{self.tag} {self.att_output()}>'
        else:
            return f'<{self.tag}>'


    def render(self, out_file, cur_ind=""):
      
        out_file.write(cur_ind + self.open_tag() + '\n')
        """loop through the list of contents"""
        for content in self.contents:
            if isinstance(content, str):
                out_file.write(cur_ind + self.indent + content)
                out_file.write('\n')
            else:
                """ write content to the out_file"""
                content.render(out_file, cur_ind + self.indent)
        out_file.write(cur_ind + f'</{self.tag}>\n')


class Html(Element):
    tag = 'html'
    def open_tag(self):
       return f'<!DOCTYPE {self.tag}>\n<{self.tag}>'


class P(Element):
    tag = 'p'


class Body(Element):
    tag = 'body'


class Head(Element):
    tag = 'head'


class Onelinetag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.open_tag())
        """loop through the list of contents"""
        for content in self.contents:
            if isinstance(content, str):
                out_file.write(cur_ind + self.indent + content)
            else:
                """write content to the out_file"""
                content.render(out_file, cur_ind + self.indent)
        out_file.write(cur_ind + f'</{self.tag}>\n')

        
class Title(Onelinetag):
    tag = 'title'

    
class Selftag(Element):
    def __init__(self, **kwargs):

        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def render(self, out_file, cur_ind=""):
        if self.attributes:
            out_file.write(cur_ind + f'<{self.tag} {self.att_output()} />\n')
        else:
            out_file.write(cur_ind + f'<{self.tag} />\n')

            
class Hr(Selftag):
    tag = 'hr'

    
class Br(Selftag):
    tag = 'br'

    
class A(Onelinetag):
    tag = 'a'
    def __init__(self, link, content):
        super().__init__(content, href=link)

        
class Ul(Element):
    tag = 'ul'

    
class Li(Element):
    tag = 'li'

    
class H(Onelinetag):
    def __init__(self, num, content):
      self.tag = f'h{num}'
      super().__init__(content)


class Meta(Selftag):
    tag = 'meta'




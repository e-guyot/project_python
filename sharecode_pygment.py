from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_lexer_for_filename
from pygments.formatters import HtmlFormatter
from IPython.display import display, HtmlFormatter


template = """<style>
{}
</style>
{}
"""

def show_file(filename):
    lexer = get_lexer_for_filename(filename)
    formatter = HtmlFormatter(cssclass='pygments')
    
    with open(filename) as f:
        code = f.read()
    
    html_code = highlight(code, lexer, formatter)
    css = formatter.get_style_defs('.pygments')
    
    html = template.format(css, html_code)
    
    display(HTML(html))
show_file('model.py')
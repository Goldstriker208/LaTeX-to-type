import re

def latex_to_typeable(latex_str):
    # Replace LaTeX fractions \frac{a}{b} with (a/b)
    latex_str = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1/\2)', latex_str)
    
    # Replace \left and \right parentheses
    latex_str = latex_str.replace(r'\left', '').replace(r'\right', '')
    
    # Replace LaTeX \arctan with arctan
    latex_str = latex_str.replace(r'\arctan', 'arctan')
    
    # Replace LaTeX \sin with sin
    latex_str = latex_str.replace(r'\sin', 'sin')
    
    # Replace LaTeX * operators
    latex_str = re.sub(r'\\cdot', '*', latex_str)
    
    # Remove any additional LaTeX syntax, like "+C" (C should be left as is)
    latex_str = latex_str.replace(r'+C', ' + C')
    
    return latex_str

# Example usage
latex_expr = input("Enter Latex expression: ") #r'\frac{1}{54}\left(\arctan \left(\frac{x}{3}\right)+\frac{1}{2}\sin \left(2\arctan \left(\frac{x}{3}\right)\right)\right)+C'
human_readable = latex_to_typeable(latex_expr)
print(human_readable)


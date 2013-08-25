# -*- coding: utf8 -*-
#
# The MIT License (MIT)
# 
# Copyright (c) 2013 Lee <lee.github@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sublime
import sublime_plugin
import re

# Convert unicode escape sequences to characters
# Python 2.6.5 used (?i) to ignore case
def convert(tb):
  # Escape sequences: swedish, german, italian, dutch, french, french, portuguese
  tb = re.sub(r'(?i)\\u00C5', 'Å', tb)

  tb = re.sub(r'(?i)\\u00C4', 'Ä', tb)
  tb = re.sub(r'(?i)\\u00CB', 'Ë', tb)
  tb = re.sub(r'(?i)\\u00CF', 'Ï', tb)
  tb = re.sub(r'(?i)\\u00D6', 'Ö', tb)
  tb = re.sub(r'(?i)\\u00DC', 'Ü', tb)
  tb = re.sub(r'(?i)\\u0178', 'Ÿ', tb)

  tb = re.sub(r'(?i)\\u00C0', 'À', tb)
  tb = re.sub(r'(?i)\\u00C8', 'È', tb)
  tb = re.sub(r'(?i)\\u00CC', 'Ì', tb)
  tb = re.sub(r'(?i)\\u00D2', 'Ò', tb)
  tb = re.sub(r'(?i)\\u00D9', 'Ù', tb)

  tb = re.sub(r'(?i)\\u00C9', 'É', tb)
  tb = re.sub(r'(?i)\\u00D3', 'Ó', tb)

  tb = re.sub(r'(?i)\\u00C2', 'Â', tb)
  tb = re.sub(r'(?i)\\u00CA', 'Ê', tb)
  tb = re.sub(r'(?i)\\u00CE', 'Î', tb)
  tb = re.sub(r'(?i)\\u00D4', 'Ô', tb)
  tb = re.sub(r'(?i)\\u00DB', 'Û', tb)

  tb = re.sub(r'(?i)\\u00C6', 'Æ', tb)
  tb = re.sub(r'(?i)\\u00C7', 'Ç', tb)
  tb = re.sub(r'(?i)\\u0152', 'Œ', tb)

  tb = re.sub(r'(?i)\\u00E5', 'å', tb)

  tb = re.sub(r'(?i)\\u00E3', 'ã', tb)
  tb = re.sub(r'(?i)\\u00F5', 'õ', tb)

  tb = re.sub(r'(?i)\\u00E4', 'ä', tb)
  tb = re.sub(r'(?i)\\u00EB', 'ë', tb)
  tb = re.sub(r'(?i)\\u00EF', 'ï', tb)
  tb = re.sub(r'(?i)\\u00F6', 'ö', tb)
  tb = re.sub(r'(?i)\\u00FC', 'ü', tb)
  tb = re.sub(r'(?i)\\u00FF', 'ÿ', tb)

  tb = re.sub(r'(?i)\\u00E0', 'à', tb)
  tb = re.sub(r'(?i)\\u00E8', 'è', tb)
  tb = re.sub(r'(?i)\\u00EC', 'ì', tb)
  tb = re.sub(r'(?i)\\u00F2', 'ò', tb)
  tb = re.sub(r'(?i)\\u00F9', 'ù', tb)

  tb = re.sub(r'(?i)\\u00E1', 'á', tb)
  tb = re.sub(r'(?i)\\u00E9', 'é', tb)
  tb = re.sub(r'(?i)\\u00ED', 'í', tb)
  tb = re.sub(r'(?i)\\u00F3', 'ó', tb)
  tb = re.sub(r'(?i)\\u00FA', 'ú', tb)

  tb = re.sub(r'(?i)\\u00E2', 'â', tb)
  tb = re.sub(r'(?i)\\u00EA', 'ê', tb)
  tb = re.sub(r'(?i)\\u00EE', 'î', tb)
  tb = re.sub(r'(?i)\\u00F4', 'ô', tb)
  tb = re.sub(r'(?i)\\u00FB', 'û', tb)

  tb = re.sub(r'(?i)\\u00E6', 'æ', tb)
  tb = re.sub(r'(?i)\\u00E7', 'ç', tb)
  tb = re.sub(r'(?i)\\u0153', 'œ', tb)

  return tb

class UnicodeEscapeSequencesToCharactersCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Returns a reference to the selection
    region = self.view.sel()[0]
    # Returns full region if no reference to selection
    if region.begin() == region.end():
      region = sublime.Region(0, self.view.size())
    # Set encoding
    tb = self.view.substr(region).encode('utf-8')
    # Convert
    string = convert(tb)
    # Update view text buffer
    self.view.replace(edit, region, string.decode('utf-8'))
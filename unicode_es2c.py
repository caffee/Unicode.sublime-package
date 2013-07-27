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
def convert(tb):
  # Escape sequences: swedish, german
  tb = re.sub(r'\\u00C5', 'Å', tb)
  tb = re.sub(r'\\u00C4', 'Ä', tb)
  tb = re.sub(r'\\u00D6', 'Ö', tb)
  tb = re.sub(r'\\u00DC', 'Ü', tb)

  tb = re.sub(r'\\u00E5', 'å', tb)
  tb = re.sub(r'\\u00E4', 'ä', tb)
  tb = re.sub(r'\\u00F6', 'ö', tb)
  tb = re.sub(r'\\u00FC', 'ü', tb)

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
    pass
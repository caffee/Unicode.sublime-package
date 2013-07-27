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

# Convert unicode characters to escape sequences
def convert(tb):
  # Special characters: swedish, german
  tb = re.sub('Å', '\u00C5', tb)
  tb = re.sub('Ä', '\u00C4', tb)
  tb = re.sub('Ö', '\u00D6', tb)
  tb = re.sub('Ü', '\u00DC', tb)

  tb = re.sub('å', '\u00E5', tb)
  tb = re.sub('ä', '\u00E4', tb)
  tb = re.sub('ö', '\u00F6', tb)
  tb = re.sub('ü', '\u00FC', tb)

  return tb

class UnicodeCharactersToEscapeSequencesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Retain original encoding
    encoding = 'utf-8' if self.view.encoding() == 'Undefined' else self.view.encoding()
    # Returns a reference to the selection
    region = self.view.sel()[0]
    # Returns full selection if no reference to selection
    if region.begin() == region.end():
      region = sublime.Region(0, self.view.size())
    # Set encoding to text buffer
    tb = self.view.substr(region).encode(encoding)
    # Convert
    string = convert(tb)
    # Update view text buffer
    self.view.replace(edit, region, string)
# Copyright (c) 2009-2014 Stefan Marr <http://www.stefan-marr.de/>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import re

from .adapter import GaugeAdapter, OutputNotParseable

from ..model.data_point  import DataPoint
from ..model.measurement import Measurement


class RPythonGCLogAdapter(GaugeAdapter):

    def __init__(self, include_faulty, executor):
        super(RPythonGCLogAdapter, self).__init__(include_faulty, executor)

    def parse_data(self, data, run_id, invocation):
        iteration = 1
        data_points = []
        current = DataPoint(run_id)

        # pretty bad code, but will do for now
        lines = data.split("\n")
        for l in reversed(lines):
            if "CUMULATIVE:" in l:
                value = int(l.split(" ")[-1])
                current.add_measurement(Measurement(invocation, iteration, value, 'bytes', run_id))
                data_points.append(current)
                return data_points

        raise OutputNotParseable(data)
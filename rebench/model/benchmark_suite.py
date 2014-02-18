# Copyright (c) 2009-2014 Stefan Marr <http://www.stefan-marr.de/>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
from rebench.model import value_or_list_as_list


class BenchmarkSuite(object):

    def __init__(self, suite_name, vm, global_suite_cfg):
        """Specialize the benchmark suite for the given VM"""
        
        self._name = suite_name
        
        ## TODO: why do we do handle input_sizes the other way around?
        if vm.input_sizes:
            self._input_sizes = vm.input_sizes
        else:
            self._input_sizes = global_suite_cfg.get('input_sizes')
        if self._input_sizes is None:
            self._input_sizes = [None]
        
        self._location        = global_suite_cfg.get('location', vm.path)
        self._cores           = global_suite_cfg.get('cores',    vm.cores)
        self._variable_values = value_or_list_as_list(global_suite_cfg.get(
                                                'variable_values', [None]))

        self._vm                 = vm
        self._benchmarks         = value_or_list_as_list(
                                                global_suite_cfg['benchmarks'])
        self._performance_reader = global_suite_cfg['performance_reader']
        self._command            = global_suite_cfg['command']
        self._max_runtime        = global_suite_cfg.get('max_runtime', -1)

    @property
    def input_sizes(self):
        return self._input_sizes
    
    @property
    def location(self):
        return self._location
    
    @property
    def cores(self):
        return self._cores
    
    @property
    def variable_values(self):
        return self._variable_values
    
    @property
    def vm(self):
        return self._vm
    
    @property
    def benchmarks(self):
        return self._benchmarks
    
    @property
    def performance_reader(self):
        return self._performance_reader

    @property
    def name(self):
        return self._name
    
    @property
    def command(self):
        return self._command

    @property
    def max_runtime(self):
        return self._max_runtime

    def has_max_runtime(self):
        return self._max_runtime != -1

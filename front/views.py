# -*- coding: utf-8 -*-
# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import GreetingForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        form = GreetingForm(request.POST)
        if form.is_valid():
            _form = form
        else:
            _form = None
        return self.render_to_response({'form': _form})

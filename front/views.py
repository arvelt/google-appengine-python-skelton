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

import requests
import json
from logging import basicConfig, getLogger, DEBUG

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import GreetingForm

basicConfig(level=DEBUG)
logger = getLogger(__name__)


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


class JsonView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(JsonView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        _id = "130010" # Tokyo
        URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s" % _id
        # URL = "http://google.com"
        logger.debug("URL %s", URL)
        res = requests.get(URL)
        try:
            forecast = json.loads(res.text)
        except (TypeError, ValueError) as e:
            return HttpResponse(status=503)
        return HttpResponse(str(forecast), content_type="text/plain")

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=200)

# coding: utf-8

"""
NotificationsApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""



import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class NotificationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_notifications(self, **kwargs):
        """
        Get the stream of notifications
        The Notifications resource returns a continuous stream of notifications in a long-lived connection. The client may use a query parameter 'filter' to specify one or more notification categories in order to receive only certain types of notifications. If no filter is specified, all notifications will be published. The response is an HTTP response with Transfer-Encoding set to chunked. Each notification is a separate JSON object and is written to the response body as a separate chunk. In addition, each notification is newline-delimited, where newline is '\r\n' (hex 0x0D0A). The filter parameter can be any of the following: data (packets from motes), events (network and system events), hr (health reports) or config (configuration changes).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Filter for notifications
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notifications" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/notifications'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['dust_basic']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='Notification',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

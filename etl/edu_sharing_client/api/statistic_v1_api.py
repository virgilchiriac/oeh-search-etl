# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from edu_sharing_client.api_client import ApiClient


class STATISTICV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get(self, context, body, **kwargs):  # noqa: E501
        """Get statistics of repository.  # noqa: E501

        Statistics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get(context, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: context, the node where to start (required)
        :param Filter body: filter (required)
        :param list[str] properties: properties
        :return: Statistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_with_http_info(context, body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(context, body, **kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, context, body, **kwargs):  # noqa: E501
        """Get statistics of repository.  # noqa: E501

        Statistics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_with_http_info(context, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context: context, the node where to start (required)
        :param Filter body: filter (required)
        :param list[str] properties: properties
        :return: Statistics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['context', 'body', 'properties']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'context' is set
        if ('context' not in params or
                params['context'] is None):
            raise ValueError("Missing the required parameter `context` when calling `get`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'context' in params:
            path_params['context'] = params['context']  # noqa: E501

        query_params = []
        if 'properties' in params:
            query_params.append(('properties', params['properties']))  # noqa: E501
            collection_formats['properties'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statistic/v1/facettes/{context}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Statistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_global_statistics(self, **kwargs):  # noqa: E501
        """Get stats.  # noqa: E501

        Get global statistics for this repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_statistics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: primary property to build facettes and count+group values
        :param list[str] sub_group: additional properties to build facettes and count+sub-group values
        :return: StatisticsGlobal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_statistics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_global_statistics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_global_statistics_with_http_info(self, **kwargs):  # noqa: E501
        """Get stats.  # noqa: E501

        Get global statistics for this repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_statistics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: primary property to build facettes and count+group values
        :param list[str] sub_group: additional properties to build facettes and count+sub-group values
        :return: StatisticsGlobal
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group', 'sub_group']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_statistics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group' in params:
            query_params.append(('group', params['group']))  # noqa: E501
        if 'sub_group' in params:
            query_params.append(('subGroup', params['sub_group']))  # noqa: E501
            collection_formats['subGroup'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statistic/v1/public', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatisticsGlobal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statistics_node(self, grouping, date_from, date_to, **kwargs):  # noqa: E501
        """get statistics for node actions  # noqa: E501

        requires either toolpermission TOOLPERMISSION_GLOBAL_STATISTICS_NODES for global stats or to be admin of the requested mediacenter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_node(grouping, date_from, date_to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grouping: Grouping type (by date) (required)
        :param int date_from: date range from (required)
        :param int date_to: date range to (required)
        :param str mediacenter: the mediacenter to filter for statistics
        :param list[str] additional_fields: additionals fields of the custom json object stored in each query that should be returned
        :param list[str] group_field: grouping fields of the custom json object stored in each query (currently only meant to be combined with no grouping by date)
        :param object body: filters for the custom json object stored in each entry
        :return: list[TrackingNode]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statistics_node_with_http_info(grouping, date_from, date_to, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statistics_node_with_http_info(grouping, date_from, date_to, **kwargs)  # noqa: E501
            return data

    def get_statistics_node_with_http_info(self, grouping, date_from, date_to, **kwargs):  # noqa: E501
        """get statistics for node actions  # noqa: E501

        requires either toolpermission TOOLPERMISSION_GLOBAL_STATISTICS_NODES for global stats or to be admin of the requested mediacenter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_node_with_http_info(grouping, date_from, date_to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grouping: Grouping type (by date) (required)
        :param int date_from: date range from (required)
        :param int date_to: date range to (required)
        :param str mediacenter: the mediacenter to filter for statistics
        :param list[str] additional_fields: additionals fields of the custom json object stored in each query that should be returned
        :param list[str] group_field: grouping fields of the custom json object stored in each query (currently only meant to be combined with no grouping by date)
        :param object body: filters for the custom json object stored in each entry
        :return: list[TrackingNode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grouping', 'date_from', 'date_to', 'mediacenter', 'additional_fields', 'group_field', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statistics_node" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grouping' is set
        if ('grouping' not in params or
                params['grouping'] is None):
            raise ValueError("Missing the required parameter `grouping` when calling `get_statistics_node`")  # noqa: E501
        # verify the required parameter 'date_from' is set
        if ('date_from' not in params or
                params['date_from'] is None):
            raise ValueError("Missing the required parameter `date_from` when calling `get_statistics_node`")  # noqa: E501
        # verify the required parameter 'date_to' is set
        if ('date_to' not in params or
                params['date_to'] is None):
            raise ValueError("Missing the required parameter `date_to` when calling `get_statistics_node`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'grouping' in params:
            query_params.append(('grouping', params['grouping']))  # noqa: E501
        if 'date_from' in params:
            query_params.append(('dateFrom', params['date_from']))  # noqa: E501
        if 'date_to' in params:
            query_params.append(('dateTo', params['date_to']))  # noqa: E501
        if 'mediacenter' in params:
            query_params.append(('mediacenter', params['mediacenter']))  # noqa: E501
        if 'additional_fields' in params:
            query_params.append(('additionalFields', params['additional_fields']))  # noqa: E501
            collection_formats['additionalFields'] = 'multi'  # noqa: E501
        if 'group_field' in params:
            query_params.append(('groupField', params['group_field']))  # noqa: E501
            collection_formats['groupField'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statistic/v1/statistics/nodes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TrackingNode]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statistics_user(self, grouping, date_from, date_to, **kwargs):  # noqa: E501
        """get statistics for user actions (login, logout)  # noqa: E501

        requires either toolpermission TOOLPERMISSION_GLOBAL_STATISTICS_USER for global stats or to be admin of the requested mediacenter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_user(grouping, date_from, date_to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grouping: Grouping type (by date) (required)
        :param int date_from: date range from (required)
        :param int date_to: date range to (required)
        :param str mediacenter: the mediacenter to filter for statistics
        :param list[str] additional_fields: additionals fields of the custom json object stored in each query that should be returned
        :param list[str] group_field: grouping fields of the custom json object stored in each query (currently only meant to be combined with no grouping by date)
        :param object body: filters for the custom json object stored in each entry
        :return: list[Tracking]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statistics_user_with_http_info(grouping, date_from, date_to, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statistics_user_with_http_info(grouping, date_from, date_to, **kwargs)  # noqa: E501
            return data

    def get_statistics_user_with_http_info(self, grouping, date_from, date_to, **kwargs):  # noqa: E501
        """get statistics for user actions (login, logout)  # noqa: E501

        requires either toolpermission TOOLPERMISSION_GLOBAL_STATISTICS_USER for global stats or to be admin of the requested mediacenter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_user_with_http_info(grouping, date_from, date_to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str grouping: Grouping type (by date) (required)
        :param int date_from: date range from (required)
        :param int date_to: date range to (required)
        :param str mediacenter: the mediacenter to filter for statistics
        :param list[str] additional_fields: additionals fields of the custom json object stored in each query that should be returned
        :param list[str] group_field: grouping fields of the custom json object stored in each query (currently only meant to be combined with no grouping by date)
        :param object body: filters for the custom json object stored in each entry
        :return: list[Tracking]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grouping', 'date_from', 'date_to', 'mediacenter', 'additional_fields', 'group_field', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statistics_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grouping' is set
        if ('grouping' not in params or
                params['grouping'] is None):
            raise ValueError("Missing the required parameter `grouping` when calling `get_statistics_user`")  # noqa: E501
        # verify the required parameter 'date_from' is set
        if ('date_from' not in params or
                params['date_from'] is None):
            raise ValueError("Missing the required parameter `date_from` when calling `get_statistics_user`")  # noqa: E501
        # verify the required parameter 'date_to' is set
        if ('date_to' not in params or
                params['date_to'] is None):
            raise ValueError("Missing the required parameter `date_to` when calling `get_statistics_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'grouping' in params:
            query_params.append(('grouping', params['grouping']))  # noqa: E501
        if 'date_from' in params:
            query_params.append(('dateFrom', params['date_from']))  # noqa: E501
        if 'date_to' in params:
            query_params.append(('dateTo', params['date_to']))  # noqa: E501
        if 'mediacenter' in params:
            query_params.append(('mediacenter', params['mediacenter']))  # noqa: E501
        if 'additional_fields' in params:
            query_params.append(('additionalFields', params['additional_fields']))  # noqa: E501
            collection_formats['additionalFields'] = 'multi'  # noqa: E501
        if 'group_field' in params:
            query_params.append(('groupField', params['group_field']))  # noqa: E501
            collection_formats['groupField'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/statistic/v1/statistics/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Tracking]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

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


class TOOLV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_tool_defintition(self, repository, body, **kwargs):  # noqa: E501
        """Create a new tool definition object.  # noqa: E501

        Create a new tool definition object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tool_defintition(repository, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param object body: properties, example: {\"{http://www.alfresco.org/model/content/1.0}name\": [\"test\"]} (required)
        :param bool rename_if_exists: rename if the same node name exists
        :param str version_comment: comment, leave empty = no inital version
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_tool_defintition_with_http_info(repository, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_tool_defintition_with_http_info(repository, body, **kwargs)  # noqa: E501
            return data

    def create_tool_defintition_with_http_info(self, repository, body, **kwargs):  # noqa: E501
        """Create a new tool definition object.  # noqa: E501

        Create a new tool definition object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tool_defintition_with_http_info(repository, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param object body: properties, example: {\"{http://www.alfresco.org/model/content/1.0}name\": [\"test\"]} (required)
        :param bool rename_if_exists: rename if the same node name exists
        :param str version_comment: comment, leave empty = no inital version
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'body', 'rename_if_exists', 'version_comment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tool_defintition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `create_tool_defintition`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_tool_defintition`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'rename_if_exists' in params:
            query_params.append(('renameIfExists', params['rename_if_exists']))  # noqa: E501
        if 'version_comment' in params:
            query_params.append(('versionComment', params['version_comment']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tool/v1/tools/{repository}/tooldefinitions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_tool_instance(self, repository, tool_definition, body, **kwargs):  # noqa: E501
        """Create a new tool Instance object.  # noqa: E501

        Create a new tool Instance object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tool_instance(repository, tool_definition, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str tool_definition: ID of parent node must have tool_definition aspect (required)
        :param object body: properties, example: {\"{http://www.alfresco.org/model/content/1.0}name\": [\"test\"]} (required)
        :param bool rename_if_exists: rename if the same node name exists
        :param str version_comment: comment, leave empty = no inital version
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_tool_instance_with_http_info(repository, tool_definition, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_tool_instance_with_http_info(repository, tool_definition, body, **kwargs)  # noqa: E501
            return data

    def create_tool_instance_with_http_info(self, repository, tool_definition, body, **kwargs):  # noqa: E501
        """Create a new tool Instance object.  # noqa: E501

        Create a new tool Instance object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tool_instance_with_http_info(repository, tool_definition, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str tool_definition: ID of parent node must have tool_definition aspect (required)
        :param object body: properties, example: {\"{http://www.alfresco.org/model/content/1.0}name\": [\"test\"]} (required)
        :param bool rename_if_exists: rename if the same node name exists
        :param str version_comment: comment, leave empty = no inital version
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'tool_definition', 'body', 'rename_if_exists', 'version_comment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tool_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `create_tool_instance`")  # noqa: E501
        # verify the required parameter 'tool_definition' is set
        if ('tool_definition' not in params or
                params['tool_definition'] is None):
            raise ValueError("Missing the required parameter `tool_definition` when calling `create_tool_instance`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_tool_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'tool_definition' in params:
            path_params['toolDefinition'] = params['tool_definition']  # noqa: E501

        query_params = []
        if 'rename_if_exists' in params:
            query_params.append(('renameIfExists', params['rename_if_exists']))  # noqa: E501
        if 'version_comment' in params:
            query_params.append(('versionComment', params['version_comment']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tool/v1/tools/{repository}/{toolDefinition}/toolinstances', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_tool_object(self, repository, toolinstance, body, **kwargs):  # noqa: E501
        """Create a new tool object for a given tool instance.  # noqa: E501

        Create a new tool object for a given tool instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tool_object(repository, toolinstance, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str toolinstance: ID of parent node (a tool instance object) (required)
        :param object body: properties, example: {\"{http://www.alfresco.org/model/content/1.0}name\": [\"test\"]} (required)
        :param bool rename_if_exists: rename if the same node name exists
        :param str version_comment: comment, leave empty = no inital version
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_tool_object_with_http_info(repository, toolinstance, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_tool_object_with_http_info(repository, toolinstance, body, **kwargs)  # noqa: E501
            return data

    def create_tool_object_with_http_info(self, repository, toolinstance, body, **kwargs):  # noqa: E501
        """Create a new tool object for a given tool instance.  # noqa: E501

        Create a new tool object for a given tool instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tool_object_with_http_info(repository, toolinstance, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str toolinstance: ID of parent node (a tool instance object) (required)
        :param object body: properties, example: {\"{http://www.alfresco.org/model/content/1.0}name\": [\"test\"]} (required)
        :param bool rename_if_exists: rename if the same node name exists
        :param str version_comment: comment, leave empty = no inital version
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'toolinstance', 'body', 'rename_if_exists', 'version_comment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tool_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `create_tool_object`")  # noqa: E501
        # verify the required parameter 'toolinstance' is set
        if ('toolinstance' not in params or
                params['toolinstance'] is None):
            raise ValueError("Missing the required parameter `toolinstance` when calling `create_tool_object`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_tool_object`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'toolinstance' in params:
            path_params['toolinstance'] = params['toolinstance']  # noqa: E501

        query_params = []
        if 'rename_if_exists' in params:
            query_params.append(('renameIfExists', params['rename_if_exists']))  # noqa: E501
        if 'version_comment' in params:
            query_params.append(('versionComment', params['version_comment']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tool/v1/tools/{repository}/{toolinstance}/toolobject', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_tool_definitions(self, repository, **kwargs):  # noqa: E501
        """Get all ToolDefinitions.  # noqa: E501

        Get all ToolDefinitions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_tool_definitions(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_tool_definitions_with_http_info(repository, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_tool_definitions_with_http_info(repository, **kwargs)  # noqa: E501
            return data

    def get_all_tool_definitions_with_http_info(self, repository, **kwargs):  # noqa: E501
        """Get all ToolDefinitions.  # noqa: E501

        Get all ToolDefinitions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_tool_definitions_with_http_info(repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_tool_definitions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_all_tool_definitions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tool/v1/tools/{repository}/tooldefinitions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_instance(self, repository, nodeid, **kwargs):  # noqa: E501
        """Get Instances of a ToolDefinition.  # noqa: E501

        Get Instances of a ToolDefinition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_instance(repository, nodeid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str nodeid: ID of node (required)
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_instance_with_http_info(repository, nodeid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_instance_with_http_info(repository, nodeid, **kwargs)  # noqa: E501
            return data

    def get_instance_with_http_info(self, repository, nodeid, **kwargs):  # noqa: E501
        """Get Instances of a ToolDefinition.  # noqa: E501

        Get Instances of a ToolDefinition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_instance_with_http_info(repository, nodeid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str nodeid: ID of node (required)
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'nodeid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_instance`")  # noqa: E501
        # verify the required parameter 'nodeid' is set
        if ('nodeid' not in params or
                params['nodeid'] is None):
            raise ValueError("Missing the required parameter `nodeid` when calling `get_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'nodeid' in params:
            path_params['nodeid'] = params['nodeid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tool/v1/tools/{repository}/{nodeid}/toolinstance', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_instances(self, repository, tool_definition, **kwargs):  # noqa: E501
        """Get Instances of a ToolDefinition.  # noqa: E501

        Get Instances of a ToolDefinition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_instances(repository, tool_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str tool_definition: ID of node (required)
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_instances_with_http_info(repository, tool_definition, **kwargs)  # noqa: E501
        else:
            (data) = self.get_instances_with_http_info(repository, tool_definition, **kwargs)  # noqa: E501
            return data

    def get_instances_with_http_info(self, repository, tool_definition, **kwargs):  # noqa: E501
        """Get Instances of a ToolDefinition.  # noqa: E501

        Get Instances of a ToolDefinition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_instances_with_http_info(repository, tool_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str tool_definition: ID of node (required)
        :return: NodeEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'tool_definition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_instances" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_instances`")  # noqa: E501
        # verify the required parameter 'tool_definition' is set
        if ('tool_definition' not in params or
                params['tool_definition'] is None):
            raise ValueError("Missing the required parameter `tool_definition` when calling `get_instances`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'tool_definition' in params:
            path_params['toolDefinition'] = params['tool_definition']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tool/v1/tools/{repository}/{toolDefinition}/toolinstances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SearchResultNode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'nodes': 'list[Node]',
        'pagination': 'Pagination',
        'facettes': 'list[Facette]',
        'ignored': 'list[str]'
    }

    attribute_map = {
        'nodes': 'nodes',
        'pagination': 'pagination',
        'facettes': 'facettes',
        'ignored': 'ignored'
    }

    def __init__(self, nodes=None, pagination=None, facettes=None, ignored=None):  # noqa: E501
        """SearchResultNode - a model defined in Swagger"""  # noqa: E501

        self._nodes = None
        self._pagination = None
        self._facettes = None
        self._ignored = None
        self.discriminator = None

        self.nodes = nodes
        self.pagination = pagination
        self.facettes = facettes
        if ignored is not None:
            self.ignored = ignored

    @property
    def nodes(self):
        """Gets the nodes of this SearchResultNode.  # noqa: E501


        :return: The nodes of this SearchResultNode.  # noqa: E501
        :rtype: list[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this SearchResultNode.


        :param nodes: The nodes of this SearchResultNode.  # noqa: E501
        :type: list[Node]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def pagination(self):
        """Gets the pagination of this SearchResultNode.  # noqa: E501


        :return: The pagination of this SearchResultNode.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this SearchResultNode.


        :param pagination: The pagination of this SearchResultNode.  # noqa: E501
        :type: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination

    @property
    def facettes(self):
        """Gets the facettes of this SearchResultNode.  # noqa: E501


        :return: The facettes of this SearchResultNode.  # noqa: E501
        :rtype: list[Facette]
        """
        return self._facettes

    @facettes.setter
    def facettes(self, facettes):
        """Sets the facettes of this SearchResultNode.


        :param facettes: The facettes of this SearchResultNode.  # noqa: E501
        :type: list[Facette]
        """
        if facettes is None:
            raise ValueError("Invalid value for `facettes`, must not be `None`")  # noqa: E501

        self._facettes = facettes

    @property
    def ignored(self):
        """Gets the ignored of this SearchResultNode.  # noqa: E501


        :return: The ignored of this SearchResultNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this SearchResultNode.


        :param ignored: The ignored of this SearchResultNode.  # noqa: E501
        :type: list[str]
        """

        self._ignored = ignored

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SearchResultNode, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchResultNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

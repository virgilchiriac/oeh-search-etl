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


class NodeVersionRef(object):
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
        'node': 'NodeRef',
        'major': 'int',
        'minor': 'int'
    }

    attribute_map = {
        'node': 'node',
        'major': 'major',
        'minor': 'minor'
    }

    def __init__(self, node=None, major=None, minor=None):  # noqa: E501
        """NodeVersionRef - a model defined in Swagger"""  # noqa: E501
        self._node = None
        self._major = None
        self._minor = None
        self.discriminator = None
        self.node = node
        self.major = major
        self.minor = minor

    @property
    def node(self):
        """Gets the node of this NodeVersionRef.  # noqa: E501


        :return: The node of this NodeVersionRef.  # noqa: E501
        :rtype: NodeRef
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this NodeVersionRef.


        :param node: The node of this NodeVersionRef.  # noqa: E501
        :type: NodeRef
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def major(self):
        """Gets the major of this NodeVersionRef.  # noqa: E501


        :return: The major of this NodeVersionRef.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this NodeVersionRef.


        :param major: The major of this NodeVersionRef.  # noqa: E501
        :type: int
        """
        if major is None:
            raise ValueError("Invalid value for `major`, must not be `None`")  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this NodeVersionRef.  # noqa: E501


        :return: The minor of this NodeVersionRef.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this NodeVersionRef.


        :param minor: The minor of this NodeVersionRef.  # noqa: E501
        :type: int
        """
        if minor is None:
            raise ValueError("Invalid value for `minor`, must not be `None`")  # noqa: E501

        self._minor = minor

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
        if issubclass(NodeVersionRef, dict):
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
        if not isinstance(other, NodeVersionRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

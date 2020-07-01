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


class AvailableMds(object):
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
        'repository': 'str',
        'mds': 'list[str]'
    }

    attribute_map = {
        'repository': 'repository',
        'mds': 'mds'
    }

    def __init__(self, repository=None, mds=None):  # noqa: E501
        """AvailableMds - a model defined in Swagger"""  # noqa: E501

        self._repository = None
        self._mds = None
        self.discriminator = None

        if repository is not None:
            self.repository = repository
        if mds is not None:
            self.mds = mds

    @property
    def repository(self):
        """Gets the repository of this AvailableMds.  # noqa: E501


        :return: The repository of this AvailableMds.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this AvailableMds.


        :param repository: The repository of this AvailableMds.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def mds(self):
        """Gets the mds of this AvailableMds.  # noqa: E501


        :return: The mds of this AvailableMds.  # noqa: E501
        :rtype: list[str]
        """
        return self._mds

    @mds.setter
    def mds(self, mds):
        """Sets the mds of this AvailableMds.


        :param mds: The mds of this AvailableMds.  # noqa: E501
        :type: list[str]
        """

        self._mds = mds

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
        if issubclass(AvailableMds, dict):
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
        if not isinstance(other, AvailableMds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

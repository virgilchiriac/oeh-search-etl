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


class ListV2(object):
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
        'id': 'str',
        'columns': 'list[ColumnV2]'
    }

    attribute_map = {
        'id': 'id',
        'columns': 'columns'
    }

    def __init__(self, id=None, columns=None):  # noqa: E501
        """ListV2 - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._columns = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if columns is not None:
            self.columns = columns

    @property
    def id(self):
        """Gets the id of this ListV2.  # noqa: E501


        :return: The id of this ListV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListV2.


        :param id: The id of this ListV2.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def columns(self):
        """Gets the columns of this ListV2.  # noqa: E501


        :return: The columns of this ListV2.  # noqa: E501
        :rtype: list[ColumnV2]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ListV2.


        :param columns: The columns of this ListV2.  # noqa: E501
        :type: list[ColumnV2]
        """

        self._columns = columns

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
        if issubclass(ListV2, dict):
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
        if not isinstance(other, ListV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

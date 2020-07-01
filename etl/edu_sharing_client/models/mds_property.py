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


class MdsProperty(object):
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
        'name': 'str',
        'type': 'str',
        'default_value': 'str',
        'processtype': 'str',
        'key_contenturl': 'str',
        'concatewithtype': 'bool',
        'multiple': 'bool',
        'copy_from': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'default_value': 'defaultValue',
        'processtype': 'processtype',
        'key_contenturl': 'keyContenturl',
        'concatewithtype': 'concatewithtype',
        'multiple': 'multiple',
        'copy_from': 'copyFrom'
    }

    def __init__(self, name=None, type=None, default_value=None, processtype=None, key_contenturl=None, concatewithtype=False, multiple=False, copy_from=None):  # noqa: E501
        """MdsProperty - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._default_value = None
        self._processtype = None
        self._key_contenturl = None
        self._concatewithtype = None
        self._multiple = None
        self._copy_from = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.default_value = default_value
        self.processtype = processtype
        self.key_contenturl = key_contenturl
        self.concatewithtype = concatewithtype
        self.multiple = multiple
        self.copy_from = copy_from

    @property
    def name(self):
        """Gets the name of this MdsProperty.  # noqa: E501


        :return: The name of this MdsProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MdsProperty.


        :param name: The name of this MdsProperty.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this MdsProperty.  # noqa: E501


        :return: The type of this MdsProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MdsProperty.


        :param type: The type of this MdsProperty.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def default_value(self):
        """Gets the default_value of this MdsProperty.  # noqa: E501


        :return: The default_value of this MdsProperty.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this MdsProperty.


        :param default_value: The default_value of this MdsProperty.  # noqa: E501
        :type: str
        """
        if default_value is None:
            raise ValueError("Invalid value for `default_value`, must not be `None`")  # noqa: E501

        self._default_value = default_value

    @property
    def processtype(self):
        """Gets the processtype of this MdsProperty.  # noqa: E501


        :return: The processtype of this MdsProperty.  # noqa: E501
        :rtype: str
        """
        return self._processtype

    @processtype.setter
    def processtype(self, processtype):
        """Sets the processtype of this MdsProperty.


        :param processtype: The processtype of this MdsProperty.  # noqa: E501
        :type: str
        """
        if processtype is None:
            raise ValueError("Invalid value for `processtype`, must not be `None`")  # noqa: E501

        self._processtype = processtype

    @property
    def key_contenturl(self):
        """Gets the key_contenturl of this MdsProperty.  # noqa: E501


        :return: The key_contenturl of this MdsProperty.  # noqa: E501
        :rtype: str
        """
        return self._key_contenturl

    @key_contenturl.setter
    def key_contenturl(self, key_contenturl):
        """Sets the key_contenturl of this MdsProperty.


        :param key_contenturl: The key_contenturl of this MdsProperty.  # noqa: E501
        :type: str
        """
        if key_contenturl is None:
            raise ValueError("Invalid value for `key_contenturl`, must not be `None`")  # noqa: E501

        self._key_contenturl = key_contenturl

    @property
    def concatewithtype(self):
        """Gets the concatewithtype of this MdsProperty.  # noqa: E501


        :return: The concatewithtype of this MdsProperty.  # noqa: E501
        :rtype: bool
        """
        return self._concatewithtype

    @concatewithtype.setter
    def concatewithtype(self, concatewithtype):
        """Sets the concatewithtype of this MdsProperty.


        :param concatewithtype: The concatewithtype of this MdsProperty.  # noqa: E501
        :type: bool
        """
        if concatewithtype is None:
            raise ValueError("Invalid value for `concatewithtype`, must not be `None`")  # noqa: E501

        self._concatewithtype = concatewithtype

    @property
    def multiple(self):
        """Gets the multiple of this MdsProperty.  # noqa: E501


        :return: The multiple of this MdsProperty.  # noqa: E501
        :rtype: bool
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this MdsProperty.


        :param multiple: The multiple of this MdsProperty.  # noqa: E501
        :type: bool
        """
        if multiple is None:
            raise ValueError("Invalid value for `multiple`, must not be `None`")  # noqa: E501

        self._multiple = multiple

    @property
    def copy_from(self):
        """Gets the copy_from of this MdsProperty.  # noqa: E501


        :return: The copy_from of this MdsProperty.  # noqa: E501
        :rtype: str
        """
        return self._copy_from

    @copy_from.setter
    def copy_from(self, copy_from):
        """Sets the copy_from of this MdsProperty.


        :param copy_from: The copy_from of this MdsProperty.  # noqa: E501
        :type: str
        """
        if copy_from is None:
            raise ValueError("Invalid value for `copy_from`, must not be `None`")  # noqa: E501

        self._copy_from = copy_from

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
        if issubclass(MdsProperty, dict):
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
        if not isinstance(other, MdsProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

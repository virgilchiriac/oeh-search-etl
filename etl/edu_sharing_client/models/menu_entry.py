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


class MenuEntry(object):
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
        'position': 'int',
        'icon': 'str',
        'name': 'str',
        'url': 'str',
        'is_disabled': 'bool',
        'is_seperate': 'bool',
        'is_seperate_bottom': 'bool',
        'only_desktop': 'bool',
        'path': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'position': 'position',
        'icon': 'icon',
        'name': 'name',
        'url': 'url',
        'is_disabled': 'isDisabled',
        'is_seperate': 'isSeperate',
        'is_seperate_bottom': 'isSeperateBottom',
        'only_desktop': 'onlyDesktop',
        'path': 'path',
        'scope': 'scope'
    }

    def __init__(self, position=None, icon=None, name=None, url=None, is_disabled=False, is_seperate=False, is_seperate_bottom=False, only_desktop=False, path=None, scope=None):  # noqa: E501
        """MenuEntry - a model defined in Swagger"""  # noqa: E501

        self._position = None
        self._icon = None
        self._name = None
        self._url = None
        self._is_disabled = None
        self._is_seperate = None
        self._is_seperate_bottom = None
        self._only_desktop = None
        self._path = None
        self._scope = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if icon is not None:
            self.icon = icon
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if is_seperate is not None:
            self.is_seperate = is_seperate
        if is_seperate_bottom is not None:
            self.is_seperate_bottom = is_seperate_bottom
        if only_desktop is not None:
            self.only_desktop = only_desktop
        if path is not None:
            self.path = path
        if scope is not None:
            self.scope = scope

    @property
    def position(self):
        """Gets the position of this MenuEntry.  # noqa: E501


        :return: The position of this MenuEntry.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this MenuEntry.


        :param position: The position of this MenuEntry.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def icon(self):
        """Gets the icon of this MenuEntry.  # noqa: E501


        :return: The icon of this MenuEntry.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this MenuEntry.


        :param icon: The icon of this MenuEntry.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def name(self):
        """Gets the name of this MenuEntry.  # noqa: E501


        :return: The name of this MenuEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MenuEntry.


        :param name: The name of this MenuEntry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this MenuEntry.  # noqa: E501


        :return: The url of this MenuEntry.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MenuEntry.


        :param url: The url of this MenuEntry.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def is_disabled(self):
        """Gets the is_disabled of this MenuEntry.  # noqa: E501


        :return: The is_disabled of this MenuEntry.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this MenuEntry.


        :param is_disabled: The is_disabled of this MenuEntry.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def is_seperate(self):
        """Gets the is_seperate of this MenuEntry.  # noqa: E501


        :return: The is_seperate of this MenuEntry.  # noqa: E501
        :rtype: bool
        """
        return self._is_seperate

    @is_seperate.setter
    def is_seperate(self, is_seperate):
        """Sets the is_seperate of this MenuEntry.


        :param is_seperate: The is_seperate of this MenuEntry.  # noqa: E501
        :type: bool
        """

        self._is_seperate = is_seperate

    @property
    def is_seperate_bottom(self):
        """Gets the is_seperate_bottom of this MenuEntry.  # noqa: E501


        :return: The is_seperate_bottom of this MenuEntry.  # noqa: E501
        :rtype: bool
        """
        return self._is_seperate_bottom

    @is_seperate_bottom.setter
    def is_seperate_bottom(self, is_seperate_bottom):
        """Sets the is_seperate_bottom of this MenuEntry.


        :param is_seperate_bottom: The is_seperate_bottom of this MenuEntry.  # noqa: E501
        :type: bool
        """

        self._is_seperate_bottom = is_seperate_bottom

    @property
    def only_desktop(self):
        """Gets the only_desktop of this MenuEntry.  # noqa: E501


        :return: The only_desktop of this MenuEntry.  # noqa: E501
        :rtype: bool
        """
        return self._only_desktop

    @only_desktop.setter
    def only_desktop(self, only_desktop):
        """Sets the only_desktop of this MenuEntry.


        :param only_desktop: The only_desktop of this MenuEntry.  # noqa: E501
        :type: bool
        """

        self._only_desktop = only_desktop

    @property
    def path(self):
        """Gets the path of this MenuEntry.  # noqa: E501


        :return: The path of this MenuEntry.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MenuEntry.


        :param path: The path of this MenuEntry.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def scope(self):
        """Gets the scope of this MenuEntry.  # noqa: E501


        :return: The scope of this MenuEntry.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this MenuEntry.


        :param scope: The scope of this MenuEntry.  # noqa: E501
        :type: str
        """

        self._scope = scope

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
        if issubclass(MenuEntry, dict):
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
        if not isinstance(other, MenuEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

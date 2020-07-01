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


class ACE(object):
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
        'editable': 'bool',
        'authority': 'Authority',
        'user': 'UserProfile',
        'group': 'GroupProfile',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'editable': 'editable',
        'authority': 'authority',
        'user': 'user',
        'group': 'group',
        'permissions': 'permissions'
    }

    def __init__(self, editable=False, authority=None, user=None, group=None, permissions=None):  # noqa: E501
        """ACE - a model defined in Swagger"""  # noqa: E501

        self._editable = None
        self._authority = None
        self._user = None
        self._group = None
        self._permissions = None
        self.discriminator = None

        if editable is not None:
            self.editable = editable
        self.authority = authority
        if user is not None:
            self.user = user
        if group is not None:
            self.group = group
        self.permissions = permissions

    @property
    def editable(self):
        """Gets the editable of this ACE.  # noqa: E501


        :return: The editable of this ACE.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this ACE.


        :param editable: The editable of this ACE.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def authority(self):
        """Gets the authority of this ACE.  # noqa: E501


        :return: The authority of this ACE.  # noqa: E501
        :rtype: Authority
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this ACE.


        :param authority: The authority of this ACE.  # noqa: E501
        :type: Authority
        """
        if authority is None:
            raise ValueError("Invalid value for `authority`, must not be `None`")  # noqa: E501

        self._authority = authority

    @property
    def user(self):
        """Gets the user of this ACE.  # noqa: E501


        :return: The user of this ACE.  # noqa: E501
        :rtype: UserProfile
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ACE.


        :param user: The user of this ACE.  # noqa: E501
        :type: UserProfile
        """

        self._user = user

    @property
    def group(self):
        """Gets the group of this ACE.  # noqa: E501


        :return: The group of this ACE.  # noqa: E501
        :rtype: GroupProfile
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ACE.


        :param group: The group of this ACE.  # noqa: E501
        :type: GroupProfile
        """

        self._group = group

    @property
    def permissions(self):
        """Gets the permissions of this ACE.  # noqa: E501


        :return: The permissions of this ACE.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ACE.


        :param permissions: The permissions of this ACE.  # noqa: E501
        :type: list[str]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

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
        if issubclass(ACE, dict):
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
        if not isinstance(other, ACE):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

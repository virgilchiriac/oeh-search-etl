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


class MdsFormProperty(object):
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
        'label': 'str',
        'label_hint': 'str',
        'form_height': 'str',
        'form_length': 'str',
        'widget': 'str',
        'widget_title': 'str',
        'copy_from': 'list[str]',
        'validators': 'list[str]',
        'parameters': 'list[MdsFormPropertyParameter]',
        'values': 'list[MdsFormPropertyValue]',
        'default_values': 'list[str]',
        'multiple': 'bool',
        'place_holder': 'str',
        'style_name': 'str',
        'style_name_label': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'label_hint': 'labelHint',
        'form_height': 'formHeight',
        'form_length': 'formLength',
        'widget': 'widget',
        'widget_title': 'widgetTitle',
        'copy_from': 'copyFrom',
        'validators': 'validators',
        'parameters': 'parameters',
        'values': 'values',
        'default_values': 'defaultValues',
        'multiple': 'multiple',
        'place_holder': 'placeHolder',
        'style_name': 'styleName',
        'style_name_label': 'styleNameLabel',
        'type': 'type'
    }

    def __init__(self, name=None, label=None, label_hint=None, form_height=None, form_length=None, widget=None, widget_title=None, copy_from=None, validators=None, parameters=None, values=None, default_values=None, multiple=False, place_holder=None, style_name=None, style_name_label=None, type=None):  # noqa: E501
        """MdsFormProperty - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._label = None
        self._label_hint = None
        self._form_height = None
        self._form_length = None
        self._widget = None
        self._widget_title = None
        self._copy_from = None
        self._validators = None
        self._parameters = None
        self._values = None
        self._default_values = None
        self._multiple = None
        self._place_holder = None
        self._style_name = None
        self._style_name_label = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.label = label
        self.label_hint = label_hint
        self.form_height = form_height
        self.form_length = form_length
        self.widget = widget
        self.widget_title = widget_title
        self.copy_from = copy_from
        self.validators = validators
        self.parameters = parameters
        self.values = values
        self.default_values = default_values
        self.multiple = multiple
        self.place_holder = place_holder
        self.style_name = style_name
        self.style_name_label = style_name_label
        self.type = type

    @property
    def name(self):
        """Gets the name of this MdsFormProperty.  # noqa: E501


        :return: The name of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MdsFormProperty.


        :param name: The name of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this MdsFormProperty.  # noqa: E501


        :return: The label of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MdsFormProperty.


        :param label: The label of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def label_hint(self):
        """Gets the label_hint of this MdsFormProperty.  # noqa: E501


        :return: The label_hint of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._label_hint

    @label_hint.setter
    def label_hint(self, label_hint):
        """Sets the label_hint of this MdsFormProperty.


        :param label_hint: The label_hint of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if label_hint is None:
            raise ValueError("Invalid value for `label_hint`, must not be `None`")  # noqa: E501

        self._label_hint = label_hint

    @property
    def form_height(self):
        """Gets the form_height of this MdsFormProperty.  # noqa: E501


        :return: The form_height of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._form_height

    @form_height.setter
    def form_height(self, form_height):
        """Sets the form_height of this MdsFormProperty.


        :param form_height: The form_height of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if form_height is None:
            raise ValueError("Invalid value for `form_height`, must not be `None`")  # noqa: E501

        self._form_height = form_height

    @property
    def form_length(self):
        """Gets the form_length of this MdsFormProperty.  # noqa: E501


        :return: The form_length of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._form_length

    @form_length.setter
    def form_length(self, form_length):
        """Sets the form_length of this MdsFormProperty.


        :param form_length: The form_length of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if form_length is None:
            raise ValueError("Invalid value for `form_length`, must not be `None`")  # noqa: E501

        self._form_length = form_length

    @property
    def widget(self):
        """Gets the widget of this MdsFormProperty.  # noqa: E501


        :return: The widget of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._widget

    @widget.setter
    def widget(self, widget):
        """Sets the widget of this MdsFormProperty.


        :param widget: The widget of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if widget is None:
            raise ValueError("Invalid value for `widget`, must not be `None`")  # noqa: E501

        self._widget = widget

    @property
    def widget_title(self):
        """Gets the widget_title of this MdsFormProperty.  # noqa: E501


        :return: The widget_title of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._widget_title

    @widget_title.setter
    def widget_title(self, widget_title):
        """Sets the widget_title of this MdsFormProperty.


        :param widget_title: The widget_title of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if widget_title is None:
            raise ValueError("Invalid value for `widget_title`, must not be `None`")  # noqa: E501

        self._widget_title = widget_title

    @property
    def copy_from(self):
        """Gets the copy_from of this MdsFormProperty.  # noqa: E501


        :return: The copy_from of this MdsFormProperty.  # noqa: E501
        :rtype: list[str]
        """
        return self._copy_from

    @copy_from.setter
    def copy_from(self, copy_from):
        """Sets the copy_from of this MdsFormProperty.


        :param copy_from: The copy_from of this MdsFormProperty.  # noqa: E501
        :type: list[str]
        """
        if copy_from is None:
            raise ValueError("Invalid value for `copy_from`, must not be `None`")  # noqa: E501

        self._copy_from = copy_from

    @property
    def validators(self):
        """Gets the validators of this MdsFormProperty.  # noqa: E501


        :return: The validators of this MdsFormProperty.  # noqa: E501
        :rtype: list[str]
        """
        return self._validators

    @validators.setter
    def validators(self, validators):
        """Sets the validators of this MdsFormProperty.


        :param validators: The validators of this MdsFormProperty.  # noqa: E501
        :type: list[str]
        """
        if validators is None:
            raise ValueError("Invalid value for `validators`, must not be `None`")  # noqa: E501

        self._validators = validators

    @property
    def parameters(self):
        """Gets the parameters of this MdsFormProperty.  # noqa: E501


        :return: The parameters of this MdsFormProperty.  # noqa: E501
        :rtype: list[MdsFormPropertyParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MdsFormProperty.


        :param parameters: The parameters of this MdsFormProperty.  # noqa: E501
        :type: list[MdsFormPropertyParameter]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def values(self):
        """Gets the values of this MdsFormProperty.  # noqa: E501


        :return: The values of this MdsFormProperty.  # noqa: E501
        :rtype: list[MdsFormPropertyValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this MdsFormProperty.


        :param values: The values of this MdsFormProperty.  # noqa: E501
        :type: list[MdsFormPropertyValue]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def default_values(self):
        """Gets the default_values of this MdsFormProperty.  # noqa: E501


        :return: The default_values of this MdsFormProperty.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this MdsFormProperty.


        :param default_values: The default_values of this MdsFormProperty.  # noqa: E501
        :type: list[str]
        """
        if default_values is None:
            raise ValueError("Invalid value for `default_values`, must not be `None`")  # noqa: E501

        self._default_values = default_values

    @property
    def multiple(self):
        """Gets the multiple of this MdsFormProperty.  # noqa: E501


        :return: The multiple of this MdsFormProperty.  # noqa: E501
        :rtype: bool
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this MdsFormProperty.


        :param multiple: The multiple of this MdsFormProperty.  # noqa: E501
        :type: bool
        """
        if multiple is None:
            raise ValueError("Invalid value for `multiple`, must not be `None`")  # noqa: E501

        self._multiple = multiple

    @property
    def place_holder(self):
        """Gets the place_holder of this MdsFormProperty.  # noqa: E501


        :return: The place_holder of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._place_holder

    @place_holder.setter
    def place_holder(self, place_holder):
        """Sets the place_holder of this MdsFormProperty.


        :param place_holder: The place_holder of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if place_holder is None:
            raise ValueError("Invalid value for `place_holder`, must not be `None`")  # noqa: E501

        self._place_holder = place_holder

    @property
    def style_name(self):
        """Gets the style_name of this MdsFormProperty.  # noqa: E501


        :return: The style_name of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._style_name

    @style_name.setter
    def style_name(self, style_name):
        """Sets the style_name of this MdsFormProperty.


        :param style_name: The style_name of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if style_name is None:
            raise ValueError("Invalid value for `style_name`, must not be `None`")  # noqa: E501

        self._style_name = style_name

    @property
    def style_name_label(self):
        """Gets the style_name_label of this MdsFormProperty.  # noqa: E501


        :return: The style_name_label of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._style_name_label

    @style_name_label.setter
    def style_name_label(self, style_name_label):
        """Sets the style_name_label of this MdsFormProperty.


        :param style_name_label: The style_name_label of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if style_name_label is None:
            raise ValueError("Invalid value for `style_name_label`, must not be `None`")  # noqa: E501

        self._style_name_label = style_name_label

    @property
    def type(self):
        """Gets the type of this MdsFormProperty.  # noqa: E501


        :return: The type of this MdsFormProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MdsFormProperty.


        :param type: The type of this MdsFormProperty.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(MdsFormProperty, dict):
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
        if not isinstance(other, MdsFormProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

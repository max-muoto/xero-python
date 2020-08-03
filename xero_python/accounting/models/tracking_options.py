# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class TrackingOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"options": "list[TrackingOption]"}

    attribute_map = {"options": "Options"}

    def __init__(self, options=None):  # noqa: E501
        """TrackingOptions - a model defined in OpenAPI"""  # noqa: E501

        self._options = None
        self.discriminator = None

        if options is not None:
            self.options = options

    @property
    def options(self):
        """Gets the options of this TrackingOptions.  # noqa: E501


        :return: The options of this TrackingOptions.  # noqa: E501
        :rtype: list[TrackingOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TrackingOptions.


        :param options: The options of this TrackingOptions.  # noqa: E501
        :type: list[TrackingOption]
        """

        self._options = options

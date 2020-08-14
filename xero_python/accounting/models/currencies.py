# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Currencies(BaseModel):
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
    openapi_types = {"currencies": "list[Currency]"}

    attribute_map = {"currencies": "Currencies"}

    def __init__(self, currencies=None):  # noqa: E501
        """Currencies - a model defined in OpenAPI"""  # noqa: E501

        self._currencies = None
        self.discriminator = None

        if currencies is not None:
            self.currencies = currencies

    @property
    def currencies(self):
        """Gets the currencies of this Currencies.  # noqa: E501


        :return: The currencies of this Currencies.  # noqa: E501
        :rtype: list[Currency]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """Sets the currencies of this Currencies.


        :param currencies: The currencies of this Currencies.  # noqa: E501
        :type: list[Currency]
        """

        self._currencies = currencies

# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.7
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Organisations(BaseModel):
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
    openapi_types = {"organisations": "list[Organisation]"}

    attribute_map = {"organisations": "Organisations"}

    def __init__(self, organisations=None):  # noqa: E501
        """Organisations - a model defined in OpenAPI"""  # noqa: E501

        self._organisations = None
        self.discriminator = None

        if organisations is not None:
            self.organisations = organisations

    @property
    def organisations(self):
        """Gets the organisations of this Organisations.  # noqa: E501


        :return: The organisations of this Organisations.  # noqa: E501
        :rtype: list[Organisation]
        """
        return self._organisations

    @organisations.setter
    def organisations(self, organisations):
        """Sets the organisations of this Organisations.


        :param organisations: The organisations of this Organisations.  # noqa: E501
        :type: list[Organisation]
        """

        self._organisations = organisations

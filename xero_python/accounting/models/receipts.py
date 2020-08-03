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


class Receipts(BaseModel):
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
    openapi_types = {"receipts": "list[Receipt]"}

    attribute_map = {"receipts": "Receipts"}

    def __init__(self, receipts=None):  # noqa: E501
        """Receipts - a model defined in OpenAPI"""  # noqa: E501

        self._receipts = None
        self.discriminator = None

        if receipts is not None:
            self.receipts = receipts

    @property
    def receipts(self):
        """Gets the receipts of this Receipts.  # noqa: E501


        :return: The receipts of this Receipts.  # noqa: E501
        :rtype: list[Receipt]
        """
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        """Sets the receipts of this Receipts.


        :param receipts: The receipts of this Receipts.  # noqa: E501
        :type: list[Receipt]
        """

        self._receipts = receipts

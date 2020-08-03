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


class LinkedTransactions(BaseModel):
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
    openapi_types = {"linked_transactions": "list[LinkedTransaction]"}

    attribute_map = {"linked_transactions": "LinkedTransactions"}

    def __init__(self, linked_transactions=None):  # noqa: E501
        """LinkedTransactions - a model defined in OpenAPI"""  # noqa: E501

        self._linked_transactions = None
        self.discriminator = None

        if linked_transactions is not None:
            self.linked_transactions = linked_transactions

    @property
    def linked_transactions(self):
        """Gets the linked_transactions of this LinkedTransactions.  # noqa: E501


        :return: The linked_transactions of this LinkedTransactions.  # noqa: E501
        :rtype: list[LinkedTransaction]
        """
        return self._linked_transactions

    @linked_transactions.setter
    def linked_transactions(self, linked_transactions):
        """Sets the linked_transactions of this LinkedTransactions.


        :param linked_transactions: The linked_transactions of this LinkedTransactions.  # noqa: E501
        :type: list[LinkedTransaction]
        """

        self._linked_transactions = linked_transactions

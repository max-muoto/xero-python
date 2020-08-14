# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PaymentMethod(BaseModel):
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
    openapi_types = {"payment_method": "str", "bank_accounts": "list[BankAccount]"}

    attribute_map = {"payment_method": "paymentMethod", "bank_accounts": "bankAccounts"}

    def __init__(self, payment_method=None, bank_accounts=None):  # noqa: E501
        """PaymentMethod - a model defined in OpenAPI"""  # noqa: E501

        self._payment_method = None
        self._bank_accounts = None
        self.discriminator = None

        self.payment_method = payment_method
        if bank_accounts is not None:
            self.bank_accounts = bank_accounts

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentMethod.  # noqa: E501

        The payment method code  # noqa: E501

        :return: The payment_method of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentMethod.

        The payment method code  # noqa: E501

        :param payment_method: The payment_method of this PaymentMethod.  # noqa: E501
        :type: str
        """
        if payment_method is None:
            raise ValueError(
                "Invalid value for `payment_method`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["Cheque", "Electronically", "Manual", "None"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}".format(  # noqa: E501
                    payment_method, allowed_values
                )
            )

        self._payment_method = payment_method

    @property
    def bank_accounts(self):
        """Gets the bank_accounts of this PaymentMethod.  # noqa: E501


        :return: The bank_accounts of this PaymentMethod.  # noqa: E501
        :rtype: list[BankAccount]
        """
        return self._bank_accounts

    @bank_accounts.setter
    def bank_accounts(self, bank_accounts):
        """Sets the bank_accounts of this PaymentMethod.


        :param bank_accounts: The bank_accounts of this PaymentMethod.  # noqa: E501
        :type: list[BankAccount]
        """

        self._bank_accounts = bank_accounts

# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BankAccount(BaseModel):
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
    openapi_types = {"account_name": "str", "account_number": "str", "sort_code": "str"}

    attribute_map = {
        "account_name": "accountName",
        "account_number": "accountNumber",
        "sort_code": "sortCode",
    }

    def __init__(
        self, account_name=None, account_number=None, sort_code=None
    ):  # noqa: E501
        """BankAccount - a model defined in OpenAPI"""  # noqa: E501

        self._account_name = None
        self._account_number = None
        self._sort_code = None
        self.discriminator = None

        self.account_name = account_name
        self.account_number = account_number
        self.sort_code = sort_code

    @property
    def account_name(self):
        """Gets the account_name of this BankAccount.  # noqa: E501

        Bank account name (max length = 32)  # noqa: E501

        :return: The account_name of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this BankAccount.

        Bank account name (max length = 32)  # noqa: E501

        :param account_name: The account_name of this BankAccount.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError(
                "Invalid value for `account_name`, must not be `None`"
            )  # noqa: E501

        self._account_name = account_name

    @property
    def account_number(self):
        """Gets the account_number of this BankAccount.  # noqa: E501

        Bank account number (digits only; max length = 8)  # noqa: E501

        :return: The account_number of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BankAccount.

        Bank account number (digits only; max length = 8)  # noqa: E501

        :param account_number: The account_number of this BankAccount.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError(
                "Invalid value for `account_number`, must not be `None`"
            )  # noqa: E501

        self._account_number = account_number

    @property
    def sort_code(self):
        """Gets the sort_code of this BankAccount.  # noqa: E501

        Bank account sort code (6 digits)  # noqa: E501

        :return: The sort_code of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this BankAccount.

        Bank account sort code (6 digits)  # noqa: E501

        :param sort_code: The sort_code of this BankAccount.  # noqa: E501
        :type: str
        """
        if sort_code is None:
            raise ValueError(
                "Invalid value for `sort_code`, must not be `None`"
            )  # noqa: E501

        self._sort_code = sort_code

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


class EmployeeLeaveBalance(BaseModel):
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
    openapi_types = {
        "name": "str",
        "leave_type_id": "str",
        "balance": "float",
        "type_of_units": "str",
    }

    attribute_map = {
        "name": "name",
        "leave_type_id": "leaveTypeID",
        "balance": "balance",
        "type_of_units": "typeOfUnits",
    }

    def __init__(
        self, name=None, leave_type_id=None, balance=None, type_of_units=None
    ):  # noqa: E501
        """EmployeeLeaveBalance - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._leave_type_id = None
        self._balance = None
        self._type_of_units = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if balance is not None:
            self.balance = balance
        if type_of_units is not None:
            self.type_of_units = type_of_units

    @property
    def name(self):
        """Gets the name of this EmployeeLeaveBalance.  # noqa: E501

        Name of the leave type.  # noqa: E501

        :return: The name of this EmployeeLeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmployeeLeaveBalance.

        Name of the leave type.  # noqa: E501

        :param name: The name of this EmployeeLeaveBalance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this EmployeeLeaveBalance.  # noqa: E501

        The Xero identifier for leave type  # noqa: E501

        :return: The leave_type_id of this EmployeeLeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this EmployeeLeaveBalance.

        The Xero identifier for leave type  # noqa: E501

        :param leave_type_id: The leave_type_id of this EmployeeLeaveBalance.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def balance(self):
        """Gets the balance of this EmployeeLeaveBalance.  # noqa: E501

        The employees current balance for the corresponding leave type.  # noqa: E501

        :return: The balance of this EmployeeLeaveBalance.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this EmployeeLeaveBalance.

        The employees current balance for the corresponding leave type.  # noqa: E501

        :param balance: The balance of this EmployeeLeaveBalance.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def type_of_units(self):
        """Gets the type_of_units of this EmployeeLeaveBalance.  # noqa: E501

        The type of the units of the leave.  # noqa: E501

        :return: The type_of_units of this EmployeeLeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        """Sets the type_of_units of this EmployeeLeaveBalance.

        The type of the units of the leave.  # noqa: E501

        :param type_of_units: The type_of_units of this EmployeeLeaveBalance.  # noqa: E501
        :type: str
        """

        self._type_of_units = type_of_units

# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ReimbursementLine(BaseModel):
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
        "reimbursement_type_id": "str",
        "description": "str",
        "amount": "float",
        "rate_per_unit": "float",
        "number_of_units": "float",
    }

    attribute_map = {
        "reimbursement_type_id": "reimbursementTypeID",
        "description": "description",
        "amount": "amount",
        "rate_per_unit": "ratePerUnit",
        "number_of_units": "numberOfUnits",
    }

    def __init__(
        self,
        reimbursement_type_id=None,
        description=None,
        amount=None,
        rate_per_unit=None,
        number_of_units=None,
    ):  # noqa: E501
        """ReimbursementLine - a model defined in OpenAPI"""  # noqa: E501

        self._reimbursement_type_id = None
        self._description = None
        self._amount = None
        self._rate_per_unit = None
        self._number_of_units = None
        self.discriminator = None

        if reimbursement_type_id is not None:
            self.reimbursement_type_id = reimbursement_type_id
        if description is not None:
            self.description = description
        if amount is not None:
            self.amount = amount
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units

    @property
    def reimbursement_type_id(self):
        """Gets the reimbursement_type_id of this ReimbursementLine.  # noqa: E501

        Xero identifier for payroll reimbursement  # noqa: E501

        :return: The reimbursement_type_id of this ReimbursementLine.  # noqa: E501
        :rtype: str
        """
        return self._reimbursement_type_id

    @reimbursement_type_id.setter
    def reimbursement_type_id(self, reimbursement_type_id):
        """Sets the reimbursement_type_id of this ReimbursementLine.

        Xero identifier for payroll reimbursement  # noqa: E501

        :param reimbursement_type_id: The reimbursement_type_id of this ReimbursementLine.  # noqa: E501
        :type: str
        """

        self._reimbursement_type_id = reimbursement_type_id

    @property
    def description(self):
        """Gets the description of this ReimbursementLine.  # noqa: E501

        Reimbursement line description  # noqa: E501

        :return: The description of this ReimbursementLine.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReimbursementLine.

        Reimbursement line description  # noqa: E501

        :param description: The description of this ReimbursementLine.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def amount(self):
        """Gets the amount of this ReimbursementLine.  # noqa: E501

        Reimbursement amount  # noqa: E501

        :return: The amount of this ReimbursementLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ReimbursementLine.

        Reimbursement amount  # noqa: E501

        :param amount: The amount of this ReimbursementLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this ReimbursementLine.  # noqa: E501

        Rate per unit for leave earnings line  # noqa: E501

        :return: The rate_per_unit of this ReimbursementLine.  # noqa: E501
        :rtype: float
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this ReimbursementLine.

        Rate per unit for leave earnings line  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this ReimbursementLine.  # noqa: E501
        :type: float
        """

        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units(self):
        """Gets the number_of_units of this ReimbursementLine.  # noqa: E501

        Leave earnings number of units  # noqa: E501

        :return: The number_of_units of this ReimbursementLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this ReimbursementLine.

        Leave earnings number of units  # noqa: E501

        :param number_of_units: The number_of_units of this ReimbursementLine.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units
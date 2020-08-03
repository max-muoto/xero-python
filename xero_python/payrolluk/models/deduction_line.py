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


class DeductionLine(BaseModel):
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
        "deduction_type_id": "str",
        "amount": "float",
        "subject_to_tax": "bool",
        "percentage": "float",
    }

    attribute_map = {
        "deduction_type_id": "deductionTypeID",
        "amount": "amount",
        "subject_to_tax": "subjectToTax",
        "percentage": "percentage",
    }

    def __init__(
        self, deduction_type_id=None, amount=None, subject_to_tax=None, percentage=None
    ):  # noqa: E501
        """DeductionLine - a model defined in OpenAPI"""  # noqa: E501

        self._deduction_type_id = None
        self._amount = None
        self._subject_to_tax = None
        self._percentage = None
        self.discriminator = None

        if deduction_type_id is not None:
            self.deduction_type_id = deduction_type_id
        if amount is not None:
            self.amount = amount
        if subject_to_tax is not None:
            self.subject_to_tax = subject_to_tax
        if percentage is not None:
            self.percentage = percentage

    @property
    def deduction_type_id(self):
        """Gets the deduction_type_id of this DeductionLine.  # noqa: E501

        Xero identifier for payroll deduction  # noqa: E501

        :return: The deduction_type_id of this DeductionLine.  # noqa: E501
        :rtype: str
        """
        return self._deduction_type_id

    @deduction_type_id.setter
    def deduction_type_id(self, deduction_type_id):
        """Sets the deduction_type_id of this DeductionLine.

        Xero identifier for payroll deduction  # noqa: E501

        :param deduction_type_id: The deduction_type_id of this DeductionLine.  # noqa: E501
        :type: str
        """

        self._deduction_type_id = deduction_type_id

    @property
    def amount(self):
        """Gets the amount of this DeductionLine.  # noqa: E501

        The amount of the deduction line  # noqa: E501

        :return: The amount of this DeductionLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DeductionLine.

        The amount of the deduction line  # noqa: E501

        :param amount: The amount of this DeductionLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def subject_to_tax(self):
        """Gets the subject_to_tax of this DeductionLine.  # noqa: E501

        Identifies if the deduction is subject to tax  # noqa: E501

        :return: The subject_to_tax of this DeductionLine.  # noqa: E501
        :rtype: bool
        """
        return self._subject_to_tax

    @subject_to_tax.setter
    def subject_to_tax(self, subject_to_tax):
        """Sets the subject_to_tax of this DeductionLine.

        Identifies if the deduction is subject to tax  # noqa: E501

        :param subject_to_tax: The subject_to_tax of this DeductionLine.  # noqa: E501
        :type: bool
        """

        self._subject_to_tax = subject_to_tax

    @property
    def percentage(self):
        """Gets the percentage of this DeductionLine.  # noqa: E501

        Deduction rate percentage  # noqa: E501

        :return: The percentage of this DeductionLine.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this DeductionLine.

        Deduction rate percentage  # noqa: E501

        :param percentage: The percentage of this DeductionLine.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

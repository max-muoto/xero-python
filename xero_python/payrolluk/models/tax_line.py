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


class TaxLine(BaseModel):
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
        "tax_line_id": "str",
        "description": "str",
        "is_employer_tax": "bool",
        "amount": "float",
        "global_tax_type_id": "str",
        "manual_adjustment": "bool",
    }

    attribute_map = {
        "tax_line_id": "taxLineID",
        "description": "description",
        "is_employer_tax": "isEmployerTax",
        "amount": "amount",
        "global_tax_type_id": "globalTaxTypeID",
        "manual_adjustment": "manualAdjustment",
    }

    def __init__(
        self,
        tax_line_id=None,
        description=None,
        is_employer_tax=None,
        amount=None,
        global_tax_type_id=None,
        manual_adjustment=None,
    ):  # noqa: E501
        """TaxLine - a model defined in OpenAPI"""  # noqa: E501

        self._tax_line_id = None
        self._description = None
        self._is_employer_tax = None
        self._amount = None
        self._global_tax_type_id = None
        self._manual_adjustment = None
        self.discriminator = None

        if tax_line_id is not None:
            self.tax_line_id = tax_line_id
        if description is not None:
            self.description = description
        if is_employer_tax is not None:
            self.is_employer_tax = is_employer_tax
        if amount is not None:
            self.amount = amount
        if global_tax_type_id is not None:
            self.global_tax_type_id = global_tax_type_id
        if manual_adjustment is not None:
            self.manual_adjustment = manual_adjustment

    @property
    def tax_line_id(self):
        """Gets the tax_line_id of this TaxLine.  # noqa: E501

        Xero identifier for payroll tax line  # noqa: E501

        :return: The tax_line_id of this TaxLine.  # noqa: E501
        :rtype: str
        """
        return self._tax_line_id

    @tax_line_id.setter
    def tax_line_id(self, tax_line_id):
        """Sets the tax_line_id of this TaxLine.

        Xero identifier for payroll tax line  # noqa: E501

        :param tax_line_id: The tax_line_id of this TaxLine.  # noqa: E501
        :type: str
        """

        self._tax_line_id = tax_line_id

    @property
    def description(self):
        """Gets the description of this TaxLine.  # noqa: E501

        Tax line description  # noqa: E501

        :return: The description of this TaxLine.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaxLine.

        Tax line description  # noqa: E501

        :param description: The description of this TaxLine.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_employer_tax(self):
        """Gets the is_employer_tax of this TaxLine.  # noqa: E501

        Identifies if the amount is paid for by the employee or employer. True if employer pays the tax  # noqa: E501

        :return: The is_employer_tax of this TaxLine.  # noqa: E501
        :rtype: bool
        """
        return self._is_employer_tax

    @is_employer_tax.setter
    def is_employer_tax(self, is_employer_tax):
        """Sets the is_employer_tax of this TaxLine.

        Identifies if the amount is paid for by the employee or employer. True if employer pays the tax  # noqa: E501

        :param is_employer_tax: The is_employer_tax of this TaxLine.  # noqa: E501
        :type: bool
        """

        self._is_employer_tax = is_employer_tax

    @property
    def amount(self):
        """Gets the amount of this TaxLine.  # noqa: E501

        The amount of the tax line  # noqa: E501

        :return: The amount of this TaxLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TaxLine.

        The amount of the tax line  # noqa: E501

        :param amount: The amount of this TaxLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def global_tax_type_id(self):
        """Gets the global_tax_type_id of this TaxLine.  # noqa: E501

        Tax type ID  # noqa: E501

        :return: The global_tax_type_id of this TaxLine.  # noqa: E501
        :rtype: str
        """
        return self._global_tax_type_id

    @global_tax_type_id.setter
    def global_tax_type_id(self, global_tax_type_id):
        """Sets the global_tax_type_id of this TaxLine.

        Tax type ID  # noqa: E501

        :param global_tax_type_id: The global_tax_type_id of this TaxLine.  # noqa: E501
        :type: str
        """

        self._global_tax_type_id = global_tax_type_id

    @property
    def manual_adjustment(self):
        """Gets the manual_adjustment of this TaxLine.  # noqa: E501

        Identifies if the tax line is a manual adjustment  # noqa: E501

        :return: The manual_adjustment of this TaxLine.  # noqa: E501
        :rtype: bool
        """
        return self._manual_adjustment

    @manual_adjustment.setter
    def manual_adjustment(self, manual_adjustment):
        """Sets the manual_adjustment of this TaxLine.

        Identifies if the tax line is a manual adjustment  # noqa: E501

        :param manual_adjustment: The manual_adjustment of this TaxLine.  # noqa: E501
        :type: bool
        """

        self._manual_adjustment = manual_adjustment

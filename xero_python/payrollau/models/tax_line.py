# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.11
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
        "payslip_tax_line_id": "str",
        "amount": "float",
        "tax_type_name": "str",
        "description": "str",
        "manual_tax_type": "ManualTaxType",
        "liability_account": "str",
    }

    attribute_map = {
        "payslip_tax_line_id": "PayslipTaxLineID",
        "amount": "Amount",
        "tax_type_name": "TaxTypeName",
        "description": "Description",
        "manual_tax_type": "ManualTaxType",
        "liability_account": "LiabilityAccount",
    }

    def __init__(
        self,
        payslip_tax_line_id=None,
        amount=None,
        tax_type_name=None,
        description=None,
        manual_tax_type=None,
        liability_account=None,
    ):  # noqa: E501
        """TaxLine - a model defined in OpenAPI"""  # noqa: E501

        self._payslip_tax_line_id = None
        self._amount = None
        self._tax_type_name = None
        self._description = None
        self._manual_tax_type = None
        self._liability_account = None
        self.discriminator = None

        if payslip_tax_line_id is not None:
            self.payslip_tax_line_id = payslip_tax_line_id
        if amount is not None:
            self.amount = amount
        if tax_type_name is not None:
            self.tax_type_name = tax_type_name
        if description is not None:
            self.description = description
        if manual_tax_type is not None:
            self.manual_tax_type = manual_tax_type
        if liability_account is not None:
            self.liability_account = liability_account

    @property
    def payslip_tax_line_id(self):
        """Gets the payslip_tax_line_id of this TaxLine.  # noqa: E501

        Xero identifier for payslip tax line ID.  # noqa: E501

        :return: The payslip_tax_line_id of this TaxLine.  # noqa: E501
        :rtype: str
        """
        return self._payslip_tax_line_id

    @payslip_tax_line_id.setter
    def payslip_tax_line_id(self, payslip_tax_line_id):
        """Sets the payslip_tax_line_id of this TaxLine.

        Xero identifier for payslip tax line ID.  # noqa: E501

        :param payslip_tax_line_id: The payslip_tax_line_id of this TaxLine.  # noqa: E501
        :type: str
        """

        self._payslip_tax_line_id = payslip_tax_line_id

    @property
    def amount(self):
        """Gets the amount of this TaxLine.  # noqa: E501

        The tax line amount  # noqa: E501

        :return: The amount of this TaxLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TaxLine.

        The tax line amount  # noqa: E501

        :param amount: The amount of this TaxLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def tax_type_name(self):
        """Gets the tax_type_name of this TaxLine.  # noqa: E501

        Name of the tax type.  # noqa: E501

        :return: The tax_type_name of this TaxLine.  # noqa: E501
        :rtype: str
        """
        return self._tax_type_name

    @tax_type_name.setter
    def tax_type_name(self, tax_type_name):
        """Sets the tax_type_name of this TaxLine.

        Name of the tax type.  # noqa: E501

        :param tax_type_name: The tax_type_name of this TaxLine.  # noqa: E501
        :type: str
        """

        self._tax_type_name = tax_type_name

    @property
    def description(self):
        """Gets the description of this TaxLine.  # noqa: E501

        Description of the tax line.  # noqa: E501

        :return: The description of this TaxLine.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaxLine.

        Description of the tax line.  # noqa: E501

        :param description: The description of this TaxLine.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def manual_tax_type(self):
        """Gets the manual_tax_type of this TaxLine.  # noqa: E501


        :return: The manual_tax_type of this TaxLine.  # noqa: E501
        :rtype: ManualTaxType
        """
        return self._manual_tax_type

    @manual_tax_type.setter
    def manual_tax_type(self, manual_tax_type):
        """Sets the manual_tax_type of this TaxLine.


        :param manual_tax_type: The manual_tax_type of this TaxLine.  # noqa: E501
        :type: ManualTaxType
        """

        self._manual_tax_type = manual_tax_type

    @property
    def liability_account(self):
        """Gets the liability_account of this TaxLine.  # noqa: E501

        The tax line liability account code. For posted pay run you should be able to see liability account code  # noqa: E501

        :return: The liability_account of this TaxLine.  # noqa: E501
        :rtype: str
        """
        return self._liability_account

    @liability_account.setter
    def liability_account(self, liability_account):
        """Sets the liability_account of this TaxLine.

        The tax line liability account code. For posted pay run you should be able to see liability account code  # noqa: E501

        :param liability_account: The liability_account of this TaxLine.  # noqa: E501
        :type: str
        """

        self._liability_account = liability_account

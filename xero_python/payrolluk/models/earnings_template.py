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


class EarningsTemplate(BaseModel):
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
        "pay_template_earning_id": "str",
        "rate_per_unit": "float",
        "number_of_units": "float",
        "fixed_amount": "float",
        "earnings_rate_id": "str",
        "name": "str",
    }

    attribute_map = {
        "pay_template_earning_id": "payTemplateEarningID",
        "rate_per_unit": "ratePerUnit",
        "number_of_units": "numberOfUnits",
        "fixed_amount": "fixedAmount",
        "earnings_rate_id": "earningsRateID",
        "name": "name",
    }

    def __init__(
        self,
        pay_template_earning_id=None,
        rate_per_unit=None,
        number_of_units=None,
        fixed_amount=None,
        earnings_rate_id=None,
        name=None,
    ):  # noqa: E501
        """EarningsTemplate - a model defined in OpenAPI"""  # noqa: E501

        self._pay_template_earning_id = None
        self._rate_per_unit = None
        self._number_of_units = None
        self._fixed_amount = None
        self._earnings_rate_id = None
        self._name = None
        self.discriminator = None

        if pay_template_earning_id is not None:
            self.pay_template_earning_id = pay_template_earning_id
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if name is not None:
            self.name = name

    @property
    def pay_template_earning_id(self):
        """Gets the pay_template_earning_id of this EarningsTemplate.  # noqa: E501

        The Xero identifier for the earnings template  # noqa: E501

        :return: The pay_template_earning_id of this EarningsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._pay_template_earning_id

    @pay_template_earning_id.setter
    def pay_template_earning_id(self, pay_template_earning_id):
        """Sets the pay_template_earning_id of this EarningsTemplate.

        The Xero identifier for the earnings template  # noqa: E501

        :param pay_template_earning_id: The pay_template_earning_id of this EarningsTemplate.  # noqa: E501
        :type: str
        """

        self._pay_template_earning_id = pay_template_earning_id

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this EarningsTemplate.  # noqa: E501

        The rate per unit  # noqa: E501

        :return: The rate_per_unit of this EarningsTemplate.  # noqa: E501
        :rtype: float
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this EarningsTemplate.

        The rate per unit  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this EarningsTemplate.  # noqa: E501
        :type: float
        """

        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units(self):
        """Gets the number_of_units of this EarningsTemplate.  # noqa: E501

        The rate per unit  # noqa: E501

        :return: The number_of_units of this EarningsTemplate.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this EarningsTemplate.

        The rate per unit  # noqa: E501

        :param number_of_units: The number_of_units of this EarningsTemplate.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this EarningsTemplate.  # noqa: E501

        The fixed amount per period  # noqa: E501

        :return: The fixed_amount of this EarningsTemplate.  # noqa: E501
        :rtype: float
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this EarningsTemplate.

        The fixed amount per period  # noqa: E501

        :param fixed_amount: The fixed_amount of this EarningsTemplate.  # noqa: E501
        :type: float
        """

        self._fixed_amount = fixed_amount

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this EarningsTemplate.  # noqa: E501

        The corresponding earnings rate identifier  # noqa: E501

        :return: The earnings_rate_id of this EarningsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this EarningsTemplate.

        The corresponding earnings rate identifier  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this EarningsTemplate.  # noqa: E501
        :type: str
        """

        self._earnings_rate_id = earnings_rate_id

    @property
    def name(self):
        """Gets the name of this EarningsTemplate.  # noqa: E501

        The read-only name of the Earning Template.  # noqa: E501

        :return: The name of this EarningsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EarningsTemplate.

        The read-only name of the Earning Template.  # noqa: E501

        :param name: The name of this EarningsTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

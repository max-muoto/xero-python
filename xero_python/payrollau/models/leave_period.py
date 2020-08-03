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


class LeavePeriod(BaseModel):
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
        "number_of_units": "float",
        "pay_period_end_date": "date[ms-format]",
        "pay_period_start_date": "date[ms-format]",
        "leave_period_status": "LeavePeriodStatus",
    }

    attribute_map = {
        "number_of_units": "NumberOfUnits",
        "pay_period_end_date": "PayPeriodEndDate",
        "pay_period_start_date": "PayPeriodStartDate",
        "leave_period_status": "LeavePeriodStatus",
    }

    def __init__(
        self,
        number_of_units=None,
        pay_period_end_date=None,
        pay_period_start_date=None,
        leave_period_status=None,
    ):  # noqa: E501
        """LeavePeriod - a model defined in OpenAPI"""  # noqa: E501

        self._number_of_units = None
        self._pay_period_end_date = None
        self._pay_period_start_date = None
        self._leave_period_status = None
        self.discriminator = None

        if number_of_units is not None:
            self.number_of_units = number_of_units
        if pay_period_end_date is not None:
            self.pay_period_end_date = pay_period_end_date
        if pay_period_start_date is not None:
            self.pay_period_start_date = pay_period_start_date
        if leave_period_status is not None:
            self.leave_period_status = leave_period_status

    @property
    def number_of_units(self):
        """Gets the number_of_units of this LeavePeriod.  # noqa: E501

        The Number of Units for the leave  # noqa: E501

        :return: The number_of_units of this LeavePeriod.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this LeavePeriod.

        The Number of Units for the leave  # noqa: E501

        :param number_of_units: The number_of_units of this LeavePeriod.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units

    @property
    def pay_period_end_date(self):
        """Gets the pay_period_end_date of this LeavePeriod.  # noqa: E501

        The Pay Period End Date (YYYY-MM-DD)  # noqa: E501

        :return: The pay_period_end_date of this LeavePeriod.  # noqa: E501
        :rtype: date
        """
        return self._pay_period_end_date

    @pay_period_end_date.setter
    def pay_period_end_date(self, pay_period_end_date):
        """Sets the pay_period_end_date of this LeavePeriod.

        The Pay Period End Date (YYYY-MM-DD)  # noqa: E501

        :param pay_period_end_date: The pay_period_end_date of this LeavePeriod.  # noqa: E501
        :type: date
        """

        self._pay_period_end_date = pay_period_end_date

    @property
    def pay_period_start_date(self):
        """Gets the pay_period_start_date of this LeavePeriod.  # noqa: E501

        The Pay Period Start Date (YYYY-MM-DD)  # noqa: E501

        :return: The pay_period_start_date of this LeavePeriod.  # noqa: E501
        :rtype: date
        """
        return self._pay_period_start_date

    @pay_period_start_date.setter
    def pay_period_start_date(self, pay_period_start_date):
        """Sets the pay_period_start_date of this LeavePeriod.

        The Pay Period Start Date (YYYY-MM-DD)  # noqa: E501

        :param pay_period_start_date: The pay_period_start_date of this LeavePeriod.  # noqa: E501
        :type: date
        """

        self._pay_period_start_date = pay_period_start_date

    @property
    def leave_period_status(self):
        """Gets the leave_period_status of this LeavePeriod.  # noqa: E501


        :return: The leave_period_status of this LeavePeriod.  # noqa: E501
        :rtype: LeavePeriodStatus
        """
        return self._leave_period_status

    @leave_period_status.setter
    def leave_period_status(self, leave_period_status):
        """Sets the leave_period_status of this LeavePeriod.


        :param leave_period_status: The leave_period_status of this LeavePeriod.  # noqa: E501
        :type: LeavePeriodStatus
        """

        self._leave_period_status = leave_period_status

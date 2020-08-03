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


class ReimbursementType(BaseModel):
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
        "account_code": "str",
        "reimbursement_type_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "current_record": "bool",
    }

    attribute_map = {
        "name": "Name",
        "account_code": "AccountCode",
        "reimbursement_type_id": "ReimbursementTypeID",
        "updated_date_utc": "UpdatedDateUTC",
        "current_record": "CurrentRecord",
    }

    def __init__(
        self,
        name=None,
        account_code=None,
        reimbursement_type_id=None,
        updated_date_utc=None,
        current_record=None,
    ):  # noqa: E501
        """ReimbursementType - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._account_code = None
        self._reimbursement_type_id = None
        self._updated_date_utc = None
        self._current_record = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if reimbursement_type_id is not None:
            self.reimbursement_type_id = reimbursement_type_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if current_record is not None:
            self.current_record = current_record

    @property
    def name(self):
        """Gets the name of this ReimbursementType.  # noqa: E501

        Name of the earnings rate (max length = 100)  # noqa: E501

        :return: The name of this ReimbursementType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReimbursementType.

        Name of the earnings rate (max length = 100)  # noqa: E501

        :param name: The name of this ReimbursementType.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._name = name

    @property
    def account_code(self):
        """Gets the account_code of this ReimbursementType.  # noqa: E501

        See Accounts  # noqa: E501

        :return: The account_code of this ReimbursementType.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this ReimbursementType.

        See Accounts  # noqa: E501

        :param account_code: The account_code of this ReimbursementType.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def reimbursement_type_id(self):
        """Gets the reimbursement_type_id of this ReimbursementType.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The reimbursement_type_id of this ReimbursementType.  # noqa: E501
        :rtype: str
        """
        return self._reimbursement_type_id

    @reimbursement_type_id.setter
    def reimbursement_type_id(self, reimbursement_type_id):
        """Sets the reimbursement_type_id of this ReimbursementType.

        Xero identifier  # noqa: E501

        :param reimbursement_type_id: The reimbursement_type_id of this ReimbursementType.  # noqa: E501
        :type: str
        """

        self._reimbursement_type_id = reimbursement_type_id

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this ReimbursementType.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this ReimbursementType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this ReimbursementType.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this ReimbursementType.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def current_record(self):
        """Gets the current_record of this ReimbursementType.  # noqa: E501

        Is the current record  # noqa: E501

        :return: The current_record of this ReimbursementType.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this ReimbursementType.

        Is the current record  # noqa: E501

        :param current_record: The current_record of this ReimbursementType.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

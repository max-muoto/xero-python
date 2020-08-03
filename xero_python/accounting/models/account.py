# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Account(BaseModel):
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
        "code": "str",
        "name": "str",
        "account_id": "str",
        "type": "AccountType",
        "bank_account_number": "str",
        "status": "str",
        "description": "str",
        "bank_account_type": "str",
        "currency_code": "CurrencyCode",
        "tax_type": "str",
        "enable_payments_to_account": "bool",
        "show_in_expense_claims": "bool",
        "_class": "str",
        "system_account": "str",
        "reporting_code": "str",
        "reporting_code_name": "str",
        "has_attachments": "bool",
        "updated_date_utc": "datetime[ms-format]",
        "add_to_watchlist": "bool",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "code": "Code",
        "name": "Name",
        "account_id": "AccountID",
        "type": "Type",
        "bank_account_number": "BankAccountNumber",
        "status": "Status",
        "description": "Description",
        "bank_account_type": "BankAccountType",
        "currency_code": "CurrencyCode",
        "tax_type": "TaxType",
        "enable_payments_to_account": "EnablePaymentsToAccount",
        "show_in_expense_claims": "ShowInExpenseClaims",
        "_class": "Class",
        "system_account": "SystemAccount",
        "reporting_code": "ReportingCode",
        "reporting_code_name": "ReportingCodeName",
        "has_attachments": "HasAttachments",
        "updated_date_utc": "UpdatedDateUTC",
        "add_to_watchlist": "AddToWatchlist",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        code=None,
        name=None,
        account_id=None,
        type=None,
        bank_account_number=None,
        status=None,
        description=None,
        bank_account_type=None,
        currency_code=None,
        tax_type=None,
        enable_payments_to_account=None,
        show_in_expense_claims=None,
        _class=None,
        system_account=None,
        reporting_code=None,
        reporting_code_name=None,
        has_attachments=False,
        updated_date_utc=None,
        add_to_watchlist=None,
        validation_errors=None,
    ):  # noqa: E501
        """Account - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._name = None
        self._account_id = None
        self._type = None
        self._bank_account_number = None
        self._status = None
        self._description = None
        self._bank_account_type = None
        self._currency_code = None
        self._tax_type = None
        self._enable_payments_to_account = None
        self._show_in_expense_claims = None
        self.__class = None
        self._system_account = None
        self._reporting_code = None
        self._reporting_code_name = None
        self._has_attachments = None
        self._updated_date_utc = None
        self._add_to_watchlist = None
        self._validation_errors = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if account_id is not None:
            self.account_id = account_id
        if type is not None:
            self.type = type
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if bank_account_type is not None:
            self.bank_account_type = bank_account_type
        if currency_code is not None:
            self.currency_code = currency_code
        if tax_type is not None:
            self.tax_type = tax_type
        if enable_payments_to_account is not None:
            self.enable_payments_to_account = enable_payments_to_account
        if show_in_expense_claims is not None:
            self.show_in_expense_claims = show_in_expense_claims
        if _class is not None:
            self._class = _class
        if system_account is not None:
            self.system_account = system_account
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if reporting_code_name is not None:
            self.reporting_code_name = reporting_code_name
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if add_to_watchlist is not None:
            self.add_to_watchlist = add_to_watchlist
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def code(self):
        """Gets the code of this Account.  # noqa: E501

        Customer defined alpha numeric account code e.g 200 or SALES (max length = 10)  # noqa: E501

        :return: The code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Account.

        Customer defined alpha numeric account code e.g 200 or SALES (max length = 10)  # noqa: E501

        :param code: The code of this Account.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 10:
            raise ValueError(
                "Invalid value for `code`, " "length must be less than or equal to `10`"
            )  # noqa: E501

        self._code = code

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501

        Name of account (max length = 150)  # noqa: E501

        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.

        Name of account (max length = 150)  # noqa: E501

        :param name: The name of this Account.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 150:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `150`"
            )  # noqa: E501

        self._name = name

    @property
    def account_id(self):
        """Gets the account_id of this Account.  # noqa: E501

        The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :return: The account_id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Account.

        The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :param account_id: The account_id of this Account.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def type(self):
        """Gets the type of this Account.  # noqa: E501


        :return: The type of this Account.  # noqa: E501
        :rtype: AccountType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.


        :param type: The type of this Account.  # noqa: E501
        :type: AccountType
        """

        self._type = type

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this Account.  # noqa: E501

        For bank accounts only (Account Type BANK)  # noqa: E501

        :return: The bank_account_number of this Account.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this Account.

        For bank accounts only (Account Type BANK)  # noqa: E501

        :param bank_account_number: The bank_account_number of this Account.  # noqa: E501
        :type: str
        """

        self._bank_account_number = bank_account_number

    @property
    def status(self):
        """Gets the status of this Account.  # noqa: E501

        Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes  # noqa: E501

        :return: The status of this Account.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Account.

        Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes  # noqa: E501

        :param status: The status of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ARCHIVED", "DELETED", "None"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def description(self):
        """Gets the description of this Account.  # noqa: E501

        Description of the Account. Valid for all types of accounts except bank accounts (max length = 4000)  # noqa: E501

        :return: The description of this Account.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Account.

        Description of the Account. Valid for all types of accounts except bank accounts (max length = 4000)  # noqa: E501

        :param description: The description of this Account.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def bank_account_type(self):
        """Gets the bank_account_type of this Account.  # noqa: E501

        For bank accounts only. See Bank Account types  # noqa: E501

        :return: The bank_account_type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_type

    @bank_account_type.setter
    def bank_account_type(self, bank_account_type):
        """Sets the bank_account_type of this Account.

        For bank accounts only. See Bank Account types  # noqa: E501

        :param bank_account_type: The bank_account_type of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "BANK",
            "CREDITCARD",
            "PAYPAL",
            "NONE",
            "",
            "None",
        ]  # noqa: E501
        if bank_account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `bank_account_type` ({0}), must be one of {1}".format(  # noqa: E501
                    bank_account_type, allowed_values
                )
            )

        self._bank_account_type = bank_account_type

    @property
    def currency_code(self):
        """Gets the currency_code of this Account.  # noqa: E501


        :return: The currency_code of this Account.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Account.


        :param currency_code: The currency_code of this Account.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def tax_type(self):
        """Gets the tax_type of this Account.  # noqa: E501

        The tax type from TaxRates  # noqa: E501

        :return: The tax_type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this Account.

        The tax type from TaxRates  # noqa: E501

        :param tax_type: The tax_type of this Account.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

    @property
    def enable_payments_to_account(self):
        """Gets the enable_payments_to_account of this Account.  # noqa: E501

        Boolean – describes whether account can have payments applied to it  # noqa: E501

        :return: The enable_payments_to_account of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._enable_payments_to_account

    @enable_payments_to_account.setter
    def enable_payments_to_account(self, enable_payments_to_account):
        """Sets the enable_payments_to_account of this Account.

        Boolean – describes whether account can have payments applied to it  # noqa: E501

        :param enable_payments_to_account: The enable_payments_to_account of this Account.  # noqa: E501
        :type: bool
        """

        self._enable_payments_to_account = enable_payments_to_account

    @property
    def show_in_expense_claims(self):
        """Gets the show_in_expense_claims of this Account.  # noqa: E501

        Boolean – describes whether account code is available for use with expense claims  # noqa: E501

        :return: The show_in_expense_claims of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_expense_claims

    @show_in_expense_claims.setter
    def show_in_expense_claims(self, show_in_expense_claims):
        """Sets the show_in_expense_claims of this Account.

        Boolean – describes whether account code is available for use with expense claims  # noqa: E501

        :param show_in_expense_claims: The show_in_expense_claims of this Account.  # noqa: E501
        :type: bool
        """

        self._show_in_expense_claims = show_in_expense_claims

    @property
    def _class(self):
        """Gets the _class of this Account.  # noqa: E501

        See Account Class Types  # noqa: E501

        :return: The _class of this Account.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Account.

        See Account Class Types  # noqa: E501

        :param _class: The _class of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ASSET",
            "EQUITY",
            "EXPENSE",
            "LIABILITY",
            "REVENUE",
            "None",
        ]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}".format(  # noqa: E501
                    _class, allowed_values
                )
            )

        self.__class = _class

    @property
    def system_account(self):
        """Gets the system_account of this Account.  # noqa: E501

        If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null.  # noqa: E501

        :return: The system_account of this Account.  # noqa: E501
        :rtype: str
        """
        return self._system_account

    @system_account.setter
    def system_account(self, system_account):
        """Sets the system_account of this Account.

        If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null.  # noqa: E501

        :param system_account: The system_account of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DEBTORS",
            "CREDITORS",
            "BANKCURRENCYGAIN",
            "GST",
            "GSTONIMPORTS",
            "HISTORICAL",
            "REALISEDCURRENCYGAIN",
            "RETAINEDEARNINGS",
            "ROUNDING",
            "TRACKINGTRANSFERS",
            "UNPAIDEXPCLM",
            "UNREALISEDCURRENCYGAIN",
            "WAGEPAYABLES",
            "CISASSETS",
            "CISASSET",
            "CISLABOUR",
            "CISLABOUREXPENSE",
            "CISLABOURINCOME",
            "CISLIABILITY",
            "CISMATERIALS",
            "",
            "None",
        ]  # noqa: E501
        if system_account not in allowed_values:
            raise ValueError(
                "Invalid value for `system_account` ({0}), must be one of {1}".format(  # noqa: E501
                    system_account, allowed_values
                )
            )

        self._system_account = system_account

    @property
    def reporting_code(self):
        """Gets the reporting_code of this Account.  # noqa: E501

        Shown if set  # noqa: E501

        :return: The reporting_code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        """Sets the reporting_code of this Account.

        Shown if set  # noqa: E501

        :param reporting_code: The reporting_code of this Account.  # noqa: E501
        :type: str
        """

        self._reporting_code = reporting_code

    @property
    def reporting_code_name(self):
        """Gets the reporting_code_name of this Account.  # noqa: E501

        Shown if set  # noqa: E501

        :return: The reporting_code_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._reporting_code_name

    @reporting_code_name.setter
    def reporting_code_name(self, reporting_code_name):
        """Sets the reporting_code_name of this Account.

        Shown if set  # noqa: E501

        :param reporting_code_name: The reporting_code_name of this Account.  # noqa: E501
        :type: str
        """

        self._reporting_code_name = reporting_code_name

    @property
    def has_attachments(self):
        """Gets the has_attachments of this Account.  # noqa: E501

        boolean to indicate if an account has an attachment (read only)  # noqa: E501

        :return: The has_attachments of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this Account.

        boolean to indicate if an account has an attachment (read only)  # noqa: E501

        :param has_attachments: The has_attachments of this Account.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Account.  # noqa: E501

        Last modified date UTC format  # noqa: E501

        :return: The updated_date_utc of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Account.

        Last modified date UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Account.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def add_to_watchlist(self):
        """Gets the add_to_watchlist of this Account.  # noqa: E501

        Boolean – describes whether the account is shown in the watchlist widget on the dashboard  # noqa: E501

        :return: The add_to_watchlist of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._add_to_watchlist

    @add_to_watchlist.setter
    def add_to_watchlist(self, add_to_watchlist):
        """Sets the add_to_watchlist of this Account.

        Boolean – describes whether the account is shown in the watchlist widget on the dashboard  # noqa: E501

        :param add_to_watchlist: The add_to_watchlist of this Account.  # noqa: E501
        :type: bool
        """

        self._add_to_watchlist = add_to_watchlist

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Account.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Account.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Account.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Account.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

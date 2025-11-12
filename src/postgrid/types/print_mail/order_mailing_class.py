# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OrderMailingClass"]

OrderMailingClass: TypeAlias = Literal[
    "first_class",
    "standard_class",
    "express",
    "certified",
    "certified_return_receipt",
    "registered",
    "usps_first_class",
    "usps_standard_class",
    "usps_eddm",
    "usps_express_2_day",
    "usps_express_3_day",
    "usps_first_class_certified",
    "usps_first_class_certified_return_receipt",
    "usps_first_class_registered",
    "usps_express_3_day_signature_confirmation",
    "usps_express_3_day_certified",
    "usps_express_3_day_certified_return_receipt",
    "ca_post_lettermail",
    "ca_post_personalized",
    "ca_post_neighbourhood_mail",
    "ups_express_overnight",
    "ups_express_2_day",
    "ups_express_3_day",
    "royal_mail_first_class",
    "royal_mail_second_class",
    "au_post_second_class",
]

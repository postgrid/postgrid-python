# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .contact import Contact
from ..._models import BaseModel

__all__ = ["SnapPackRetrieveResponse", "Cancellation"]


class Cancellation(BaseModel):
    """The cancellation details of this order.

    Populated if the order has been cancelled.
    """

    reason: Literal["user_initiated", "invalid_content", "invalid_order_mailing_class"]
    """The reason for the cancellation."""

    cancelled_by_user: Optional[str] = FieldInfo(alias="cancelledByUser", default=None)
    """The user ID who cancelled the order."""

    note: Optional[str] = None
    """An optional note provided by the user who cancelled the order."""


class SnapPackRetrieveResponse(BaseModel):
    id: str
    """A unique ID prefixed with snap*pack*"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    from_: Contact = FieldInfo(alias="from")
    """The contact information of the sender."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    mailing_class: Literal[
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
    ] = FieldInfo(alias="mailingClass")
    """The mailing class of this order.

    This determines the speed and cost of delivery. See `OrderMailingClass` for more
    details.
    """

    object: Literal["snap_pack"]
    """Always `snap_pack`."""

    send_date: datetime = FieldInfo(alias="sendDate")
    """This order will transition from `ready` to `printing` on the day after this
    date.

    For example, if this is a date on Tuesday, the order will transition to
    `printing` on Wednesday at midnight eastern time.
    """

    size: Literal["8.5x11_bifold_v"]
    """Enum representing the supported snap pack sizes."""

    status: Literal["ready", "printing", "processed_for_delivery", "completed", "cancelled"]
    """See `OrderStatus` for more details on the status of this order."""

    to: Contact
    """The recipient of this order.

    This will be provided even if you delete the underlying contact.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    cancellation: Optional[Cancellation] = None
    """The cancellation details of this order.

    Populated if the order has been cancelled.
    """

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    imb_date: Optional[datetime] = FieldInfo(alias="imbDate", default=None)
    """The last date that the IMB status was updated.

    See `imbStatus` for more details.
    """

    imb_status: Optional[Literal["entered_mail_stream", "out_for_delivery", "returned_to_sender"]] = FieldInfo(
        alias="imbStatus", default=None
    )
    """The Intelligent Mail Barcode (IMB) status of this order.

    Only populated for US-printed and US-destined orders. This is the most detailed
    way to track non-express/certified orders.
    """

    imb_zip_code: Optional[str] = FieldInfo(alias="imbZIPCode", default=None)
    """
    The most recent ZIP code of the USPS facility that the order has been processed
    through. Only populated when an `imbStatus` is present.
    """

    inside_html: Optional[str] = FieldInfo(alias="insideHTML", default=None)
    """
    The HTML content for the inside of the snap pack, when provided instead of a
    template or PDF.
    """

    inside_template: Optional[str] = FieldInfo(alias="insideTemplate", default=None)
    """
    The template ID for the inside of the snap pack, when provided instead of HTML
    or PDF.
    """

    merge_variables: Optional[Dict[str, builtins.object]] = FieldInfo(alias="mergeVariables", default=None)
    """
    These will be merged with the variables in the template or HTML you create this
    order with. The keys in this object should match the variable names in the
    template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
    PDFs uploaded with the order.
    """

    metadata: Optional[Dict[str, builtins.object]] = None
    """See the section on Metadata."""

    outside_html: Optional[str] = FieldInfo(alias="outsideHTML", default=None)
    """
    The HTML content for the outside of the snap pack, when provided instead of a
    template or PDF.
    """

    outside_template: Optional[str] = FieldInfo(alias="outsideTemplate", default=None)
    """
    The template ID for the outside of the snap pack, when provided instead of HTML
    or PDF.
    """

    tracking_number: Optional[str] = FieldInfo(alias="trackingNumber", default=None)
    """The tracking number of this order.

    Populated after an express/certified order has been processed for delivery.
    """

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """
    A signed URL to the uploaded PDF provided at creation time, if a PDF was
    supplied.
    """

    url: Optional[str] = None
    """PostGrid renders a PDF preview for all orders.

    This should be inspected to ensure that the order is correct before it is sent
    out because it shows what will be printed and mailed to the recipient. Once the
    PDF preview is generated, this field will be returned by all `GET` endpoints
    which produce this order.

    This URL is a signed link to the PDF preview. It will expire after a short
    period of time. If you need to access this URL after it has expired, you can
    regenerate it by calling the `GET` endpoint again.
    """

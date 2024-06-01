from .api import stripe_api as stripe
from .customers import get_or_create_stripe_user
from ..settings import drf_stripe_settings


def stripe_api_create_billing_portal_session(user_pk):
    """
    Creates a Stripe Customer Portal Session.

    :param str user_pk: Django User id
    """
    stripe_user = get_or_create_stripe_user(user_pk=user_pk)

    session = stripe.billing_portal.Session.create(
        customer=stripe_user.customer_id,
        return_url=f"{drf_stripe_settings.FRONT_END_BASE_URL}/manage-subscription/"
    )

    return session

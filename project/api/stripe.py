def set_stripe_secret_key() -> None:
    '''
    Set StripeAPI secret key from environment.
    '''
    try:
        import stripe
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Stripe. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    from project.utils import getenv

    stripe.api_key = getenv('STRIPE_SECRET_KEY', default='')

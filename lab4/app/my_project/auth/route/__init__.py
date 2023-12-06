from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    from .orders.account_route import account_bp
    from .orders.loan_route import loan_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(loan_bp)
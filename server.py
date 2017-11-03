from flask import Flask

from handlers import site
from products import Product
from store import Store

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    app.register_blueprint(site)

    app.store = Store()
    app.store.add_product(Product('Cake'))
    app.store.add_product(Product('Cookies', quantity = 10))

    return app


def main():
    app = create_app()
    #debug = app.config['DEBUG']
    port = app.config.get('PORT', 8080)
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
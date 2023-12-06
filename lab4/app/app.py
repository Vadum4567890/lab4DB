import os

from waitress import serve
import yaml


DEVELOPMENT_PORT = 3000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"


if __name__ == '__main__':
    from my_project import create_app

    flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()
    config_yaml_path = os.path.join(os.getcwd(), 'config', 'app.yml')

    # Explicitly set the environment variables
    os.environ["MYSQL_ROOT_USER"] = "root"
    os.environ["MYSQL_ROOT_PASSWORD"] = "1234"

    with open(config_yaml_path, "r", encoding='utf-8') as yaml_file:
        config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
        additional_config = config_data_dict.get(ADDITIONAL_CONFIG, {})
        additional_config.update({
            "MYSQL_ROOT_USER": os.environ["MYSQL_ROOT_USER"],
            "MYSQL_ROOT_PASSWORD": os.environ["MYSQL_ROOT_PASSWORD"],
        })

        if flask_env == DEVELOPMENT:
            config_data = config_data_dict[DEVELOPMENT]
            print("Config Data:", config_data)
            create_app(config_data, additional_config).run(port=DEVELOPMENT_PORT, debug=True)

        elif flask_env == PRODUCTION:
            config_data = config_data_dict[PRODUCTION]
            serve(create_app(config_data, additional_config), host=HOST, port=PRODUCTION_PORT)

        else:
            raise ValueError(f"Check OS environment variable '{FLASK_ENV}'")

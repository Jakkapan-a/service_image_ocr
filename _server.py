from app import create_app
from tabulate import tabulate
app = create_app()

if __name__ == '__main__':
    # print routes
    route_list = []
    for rule in app.url_map.iter_rules():
        methods = ', '.join(sorted(rule.methods))
        route_list.append([rule.rule, methods, rule.endpoint])

    print(tabulate(route_list, headers=["Route", "Methods", "Endpoint"], tablefmt="grid"))

    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=app.config['PORT'])
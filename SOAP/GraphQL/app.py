from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Định nghĩa Schema GraphQL
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return f"Hello {name}!"

schema = graphene.Schema(query=Query)

# Flask app
app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)  # graphiql=True mở giao diện test
)

if __name__ == "__main__":
    app.run(debug=True)

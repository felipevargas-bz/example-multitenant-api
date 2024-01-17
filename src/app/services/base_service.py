# Python Imports

# Flask Imports
from flask import g
from pymysql.err import OperationalError

# Third-Party Imports
from sqlalchemy import text, or_

# App Imports
from app import db
from app.exceptions import BadRequest, MySQLConnectionError


class BaseService:
    def __init__(self, model, schema):
        self.model = model
        self.schema = schema

    @staticmethod
    def make_query(op, attribute, value, query):

        if op == "eq":
            return query.filter(attribute == value)
        elif op == "in":
            values = value.split(",")
            return query.filter(attribute.in_(values))
        elif op == "contains":
            return attribute.contains(value)
        elif op == "ne":
            return query.filter(attribute != value)
        elif op == "not_in":
            values = value.split(",")
            return query.filter(~attribute.in_(values))
        else:
            raise BadRequest(f"El operador {op} no está soportado")

    def get_all(self, query_parameters):
        """
        :param query_parameters:
        :return:
        """

        try:
            query = g.session.query(self.model)
            or_query = []

            for param, value in query_parameters.items():
                param, op = param.split("__") if "__" in param else (param, "eq")
                attribute = getattr(self.model, param, None)
                if not attribute:
                    raise BadRequest(
                        f"El parámetro {param} no existe en la tabla {self.model.__name__}"
                    )
                rs_query = self.make_query(op, attribute, value, query)
                if op == "contains":
                    or_query.append(rs_query)
                else:
                    query = rs_query

            if or_query:
                query = query.filter(or_(*or_query))

            results = self.schema(many=True).dump(query.all())
            return results

        except OperationalError as e:
            raise MySQLConnectionError(str(e))

    def get_one(self, query_parameters, dict_format=True):
        """
        :param dict_format:
        :param query_parameters:
        :return:
        """

        try:
            query = g.session.query(self.model)

            for param, value in query_parameters.items():
                param, op = param.split("__") if "__" in param else (param, "eq")
                attribute = getattr(self.model, param, None)
                if not attribute:
                    raise BadRequest(
                        f"El parámetro {param} no existe en la tabla {self.model.__name__}"
                    )
                query = self.make_query(op, attribute, value, query)

            result = query.first()

            return self.schema().dump(result) if dict_format else result

        except OperationalError as e:
            raise MySQLConnectionError(str(e))

    def get_by_id(self, pk):
        try:
            obj = g.session.query(self.model).get(pk)
            return self.schema().dump(obj)
        except OperationalError as e:
            raise MySQLConnectionError(str(e))

    def create(self, data):
        instance = self.schema().load(data, session=db.session)
        instance.save()
        return instance

    def update(self, pk, data):
        instance = self.get_one({"id__eq": pk}, dict_format=False)
        if not instance:
            raise ValueError(
                f"No se encontró el registro con el id {pk} en la tabla {self.model.__name__}"
            )

        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()

    def delete(self, pk):
        instance = self.get_one({"id__eq": pk}, dict_format=False)
        if not instance:
            raise ValueError(
                f"No se encontró el registro con el id {pk} en la tabla {self.model.__name__}"
            )
        instance.remove()
        return {"ok": True}

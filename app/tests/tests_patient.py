import json

from graphene_django.utils.testing import GraphQLTestCase
from app.schema import schema
from app.models import Patient

class MyFancyTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = '/graphql'

    def setUp(self):
        self.patient = Patient.objects.create(name="Emmanuel")

    def test_create_patient(self):

        response = self.query('mutation { createPatient(name: "Isabella Angulo") { id name } }')

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        data = content['data']['createPatient']

        self.assertEqual(data['name'], 'Isabella Angulo')

    def test_update_patient(self):

        response = self.query('mutation { updatePatient(id: "%s" name: "Isabella Angulo") { id name } }' % (str(self.patient.id)))

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        data = content['data']['updatePatient']

        self.assertEqual(data['name'], 'Isabella Angulo')

    def test_patient(self):
        
        response = self.query('{ Patient(id: "%s") { id name } }' % (str(self.patient.id)))

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        data = content['data']['Patient']

        self.assertEqual(data['name'], 'Emmanuel')

    def test__all_patients_meta(self):
        
        response = self.query('{ _allPatientsMeta{ count } }')

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        data = content['data']['_allPatientsMeta']

        self.assertEqual(data['count'], 1)

    def test_delete_patient(self):
        
        response = self.query('mutation { deletePatient(id: "%s") { name } }' % (str(self.patient.id)))

        self.assertResponseNoErrors(response)

        content = json.loads(response.content)

        data = content['data']['deletePatient']

        self.assertEqual(data['name'], 'Emmanuel')
        
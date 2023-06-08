import graphene
from graphene_django.types import DjangoObjectType
from apps.minimal.models import Patient


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        name = "Patient"

class ListMetadata(graphene.ObjectType):
    count = graphene.Field(graphene.Int)

class PatientCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    class Meta:
        description = "Create a patient"
        model = Patient

    id = graphene.Field(graphene.ID)
    name = graphene.Field(graphene.String)

    def mutate(self, info, name):
        patient = Patient()
        patient.name = name
        patient.save()
        return PatientCreate(id=patient.id, name=patient.name)

class PatientUpdate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    id = graphene.Field(graphene.ID)
    name = graphene.Field(graphene.String)

    def mutate(self, info, name, id):
        patient = Patient.objects.get(pk=id)
        patient.name = name
        patient.save()
        return PatientUpdate(id=patient.id, name=patient.name)

class PatientDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    id = graphene.Field(graphene.ID)
    name = graphene.Field(graphene.String)

    def mutate(self, info, id):
        patient = Patient.objects.get(pk=id)
        patient.delete()
        return PatientDelete(id=patient.id, name=patient.name)

class Query(graphene.ObjectType):
    patient = graphene.Field(PatientType, name='Patient', id=graphene.ID())
    all_patients = graphene.List(PatientType)
    all_patients_meta = graphene.Field(ListMetadata, name="_allPatientsMeta")

    def resolve_patient(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Patient.objects.get(pk=id)

        return None

    def resolve_all_patients(self, info, **kwargs):
        return Patient.objects.all()

    def resolve_all_patients_meta(self, info, **kwargs):
        return { "count": Patient.objects.all().count()}

class Mutation(graphene.ObjectType):
    create_patient = PatientCreate.Field()
    update_patient = PatientUpdate.Field()
    delete_patient = PatientDelete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
from django.test import TestCase
from landman.models import AgreementType, SubjectType

# Create your tests here.

class AgreementTypeTestCase(TestCase):
    def setUp(self) -> None:
        contract_subject_type = SubjectType.objects.create(code='CTR', description='Contract')
        AgreementType.objects.create(code = 'ROW', description='Right of Way', category=contract_subject_type)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_to_string_output(self):
        agreement_type = AgreementType.objects.get(code='ROW')
        self.assertIsNotNone(agreement_type)
        self.assertEqual(str(agreement_type), 'CTR-ROW : Right of Way')
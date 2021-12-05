from django.db.models.deletion import ProtectedError
from django.test import TestCase
from landman.models import AgreementType, SubjectType

class SubjectTypeModelTestCase(TestCase):
    def setUp(self) -> None:
        # Subject Types
        lease_subject_type = SubjectType.objects.create(code='LSE', description='Lease')
        contract_subject_type = SubjectType.objects.create(code='CTR', description='Contract')

        # Agreement Types
        lease_agreement_type = AgreementType.objects.create(code = 'ROW', description='Right of Way', category=contract_subject_type)

        # Super
        return super().setUp()

    def tearDown(self) -> None:
        # Super
        return super().tearDown()

    # Test to make sure we can create Subjet Type objects
    def test_objects_exist(self):
        lease = SubjectType.objects.get(code='LSE')
        contract = SubjectType.objects.get(code='CTR')
        self.assertEqual(lease.description, 'Lease')
        self.assertEqual(contract.description, 'Contract')

    # Test the Agreement Type to Subject Type relationship
    def test_agreement_type_to_subject_type_relationship(self):
        contract_subject_type = SubjectType.objects.get(code='CTR')
        row_agreement_type = AgreementType.objects.get(code='ROW')
        self.assertIsNotNone(contract_subject_type)
        self.assertEqual(contract_subject_type.agreement_types.first(), row_agreement_type)

    # Test the delete protection on the foreign key constraint
    def test_agreement_type_delete_protection(self):
        ctr_subject_type = SubjectType.objects.get(code='CTR')
        row_agreement_type = AgreementType.objects.get(code='ROW')
        self.assertIsNotNone(row_agreement_type)
        self.assertIsNotNone(ctr_subject_type)
        self.assertEqual(ctr_subject_type.agreement_types.first(), row_agreement_type)
        with self.assertRaises(ProtectedError):
            ctr_subject_type.delete()
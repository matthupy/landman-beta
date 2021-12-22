from datetime import datetime
from django.db.models.deletion import ProtectedError
from django.test import TestCase
from landman.models import Agreement, AgreementStage, AgreementStatus, AgreementType, LandDivision, SubjectType, Right

# Create your tests here.

class RightsTestCase(TestCase):
    def setUp(self) -> None:
        east_land_division = LandDivision.objects.create(code='E', description='East Division')
        active_agreement_status = AgreementStatus.objects.create(code='A', description='Active')
        contract_subject_type = SubjectType.objects.create(code='CTR', description='Contract')
        row_agreement_type = AgreementType.objects.create(code = 'ROW', description='Right of Way', category=contract_subject_type)
        new_agreement_stage = AgreementStage.objects.create(code='NEW', description='New', index=0)

        mineral_rights = Right.objects.create(code='MRL', description = 'Mineral Rights')

        test_agreement = Agreement.objects.create(
            name = 'Rights Test Agreement',
            number = 'TST000001000',
            type = row_agreement_type,
            status = active_agreement_status,
            stage = new_agreement_stage,
            landDivision = east_land_division,
            originalLessee = 'James Potter',
            agreementDate = datetime.now(),
            effectiveDate = datetime.now(),
            term = 60,
            rights = mineral_rights
        )

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_foreign_key_deletion(self):
        test_agreement = Agreement.objects.first()
        mineral_rights = Right.objects.first()
        self.assertIsNotNone(test_agreement)
        self.assertIsNotNone(mineral_rights)
        with (self.assertRaises(ProtectedError)):
            mineral_rights.delete()
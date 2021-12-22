from datetime import datetime
from django.test import TestCase
from landman.models import Agreement, AgreementType, AgreementStage, AgreementStatus, LandDivision, Right, SubjectType, Well, WellStatus

# Create your tests here.
class AgreementTestCase(TestCase):
    def setUp(self) -> None:

        # Subject Type Setup
        ctr_subject_type = SubjectType.objects.create(code='CTR', description='Contract')

        # Agreement Type Setup
        row_agreement_type = AgreementType.objects.create(code='ROW', description='Right of Way', category=ctr_subject_type)

        # Agreement Stage Setup
        new_agreement_stage = AgreementStage.objects.create(code='NEW', description='New', index=0)

        # Agreement Status Setup
        active_agreement_status = AgreementStatus.objects.create(code='A', description='Active')
        inactive_agreement_status = AgreementStatus.objects.create(code='IN', description='Inactive')

        # Land Division Setup
        test_land_division = LandDivision.objects.create(code='TST', description='Test Land Division')

        # Right Setup
        ogm_rights = Right.objects.create(code='OGM', description='Oil, Gas, and Minerals')

        # Well Status Setup
        prod_well_status = WellStatus.objects.create(code='PRD', description='Producing')

        # Well Setup
        test_well = Well.objects.create(name='Agreement Test Well', status = prod_well_status, latitude=0, longitude=0)

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_create_agreement_object(self):
        row_agreement_type = AgreementType.objects.get(code='ROW')
        new_agreement_stage = AgreementStage.objects.get(code='NEW')
        active_agreement_status = AgreementStatus.objects.get(code='A')
        ogm_rights = Right.objects.get(code='OGM')
        test_land_division = LandDivision.objects.get(code='TST')
        test_well = Well.objects.first()
        agreement = Agreement.objects.create(
            name='Test Agreement',
            number='TST0123456789',
            status=active_agreement_status,
            rights=ogm_rights,
            type=row_agreement_type,
            stage=new_agreement_stage,
            landDivision=test_land_division,
            agreementDate=datetime.now(),
            effectiveDate=datetime.now(),
            term=60,
        )
        agreement.wells.set([ test_well ])
        self.assertIsNotNone(agreement)
        self.assertEqual(agreement.name, 'Test Agreement')
        self.assertEqual(agreement.wells.first(), test_well)

    def test_inactivate_agreement(self):
        row_agreement_type = AgreementType.objects.get(code='ROW')
        new_agreement_stage = AgreementStage.objects.get(code='NEW')
        active_agreement_status = AgreementStatus.objects.get(code='A')
        ogm_rights = Right.objects.get(code='OGM')
        test_land_division = LandDivision.objects.get(code='TST')
        test_well = Well.objects.first()
        agreement = Agreement.objects.create(
            name='Test Agreement',
            number='TST0123456789',
            status=active_agreement_status,
            rights=ogm_rights,
            type=row_agreement_type,
            stage=new_agreement_stage,
            landDivision=test_land_division,
            agreementDate=datetime.now(),
            effectiveDate=datetime.now(),
            term=60,
        )
        agreement.wells.set([ test_well ])
        self.assertIsNotNone(agreement)
        self.assertEqual(active_agreement_status, agreement.status)

        inactive_agreement_status = AgreementStatus.objects.get(code='IN')

        agreement.inactivate()

        self.assertEqual(inactive_agreement_status, agreement.status)
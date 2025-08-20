from odoo.tests.common import TransactionCase

class TestFarmer(TransactionCase):

    def setUp(self):
        super().setUp()
        # Create a farmer record
        self.farmer = self.env['farmer.management'].create({
            'name': 'Abebe Kebede',
            'phone': '0912345678',
            'land_size': 10,
            'crop_type': 'wheat',
            'partner_id': 2,
        })

    def test_farmer_creation(self):
        """Test that farmer record is created successfully"""
        self.assertTrue(self.farmer.id, "Farmer should be created")
        self.assertEqual(self.farmer.name, "Abebe Kebede")
        self.assertEqual(self.farmer.crop_type, "wheat")
        self.assertEqual(self.farmer.partner_id, 2)

    def test_large_scale_computation(self):
        """Test computed field is_large_scale"""
        self.assertTrue(self.farmer.is_large_scale, "Farmer with 10 Ha should be large scale")

        # Update land size
        self.farmer.write({'land_size': 2})
        self.assertFalse(self.farmer.is_large_scale, "Farmer with 2 Ha should not be large scale")

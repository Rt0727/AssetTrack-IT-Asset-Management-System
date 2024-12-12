# test_asset_manager.py

import unittest
from asset_manager import add_asset, update_asset, delete_asset, get_all_assets

class TestAssetManager(unittest.TestCase):

    def test_add_asset(self):
        add_asset('Laptop', 'Electronics', '2022-03-15', 1200.00)
        assets = get_all_assets()
        self.assertGreater(len(assets), 0)

    def test_update_asset(self):
        # Assuming an asset with ID 1 exists
        update_asset(1, 'Laptop', 'Electronics', '2022-03-15', 1300.00)
        assets = get_all_assets()
        updated_asset = next((asset for asset in assets if asset[0] == 1), None)
        self.assertEqual(updated_asset[4], 1300.00)

    def test_delete_asset(self):
        # Assuming an asset with ID 1 exists
        delete_asset(1)
        assets = get_all_assets()
        deleted_asset = next((asset for asset in assets if asset[0] == 1), None)
        self.assertIsNone(deleted_asset)
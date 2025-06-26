import unittest
import json
from app import app

class WalkModuleAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_step_route(self):
        response = self.app.get('/step?from=left&to=right')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['from'], 'left')
        self.assertEqual(data['to'], 'right')
        self.assertIn('Stepping from left to right', data['result'])

    def test_foot_route(self):
        response = self.app.get('/foot?from=heel&to=toe&size=42')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['from'], 'heel')
        self.assertEqual(data['to'], 'toe')
        self.assertEqual(data['size'], '42')
        self.assertIn('Foot from heel to toe with size 42', data['result'])

    def test_method_route(self):
        response = self.app.get('/method/slowly')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['method'], 'slowly')
        self.assertIn('Walking slowly', data['result'])

    def test_model_route(self):
        response = self.app.get('/model/leg')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('leg', data)
        self.assertIn('left', data['leg'])
        self.assertIn('right', data['leg'])

    def test_mix_route(self):
        response = self.app.get('/mix/footleg')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('footleg', data)
        self.assertIn('heel', data['footleg'])

    def test_map_route(self):
        response = self.app.get('/map/legs')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('legs', data)
        self.assertIn('left', data['legs'])

    def test_magma_route(self):
        response = self.app.get('/magma/foot_attributes')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('foot_attributes', data)
        self.assertIn('arch', data['foot_attributes'])

    def test_meanings_route(self):
        response = self.app.get('/meanings')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('meanings', data)
        self.assertIsInstance(data['meanings'], list)

    def test_mantras_route(self):
        response = self.app.get('/mantras')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('mantras', data)
        self.assertIsInstance(data['mantras'], list)

if __name__ == '__main__':
    unittest.main()
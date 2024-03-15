from tank import Tank
import unittest

me: Tank = Tank(name='Василий', hp=500, defence=200, speed=18, attack_speed=20, aggression=1, power=9)


class TestTank(unittest.TestCase):
    def test_get_dpm_against_tank_damage_expected(self):
        other: Tank = Tank(name='Other tank', hp=500, defence=200, speed=18, attack_speed=20, aggression=1, power=9)
        self.assertEqual(me.get_dpm(other), 0.045, "Внезапно не тот дамаг")

#    def test_failed(self):
#        self.assertTrue(False)

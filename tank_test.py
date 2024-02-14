from tank import Tank
import unittest

class TestTank(unittest.TestCase):
    def get_dpm_test_true(self, other)
        me: Tank = Tank(name='Василий', hp=500, defence=200, speed=18, attack_speed=20, aggression=1, power=9)
        other: Tank = Tank(name='Василий', hp=500, defence=200, speed=18, attack_speed=20, aggression=1, power=9)
        self.assertEquals(me.get_dpm(other), 0.045)

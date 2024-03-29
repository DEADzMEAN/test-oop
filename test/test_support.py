from core.support import Support
import unittest


class TestSupport(unittest.TestCase):
    def test_heal_expect_health_increased(self):
        me: Support = Support(name="me", hp=50, defence=15, speed=15, attack_speed=10, heal_power=1, buff=1, power=1)
        other: Support = Support(name="Other", hp=50, defence=15, speed=15, attack_speed=10, heal_power=1, buff=1, power=1)
        hp_before = other.hp
        me.heal(other)
        self.assertGreater(other.hp, hp_before)

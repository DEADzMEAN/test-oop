from character import Character
import unittest


class TestCharacter(unittest.TestCase):
    def test_should_leave_expect_true(self):
        me: Character = Character(name="Me", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        other: Character = Character(name="Other", hp=10, defence=1, speed=1, attack_speed=1, power=1000)
        self.assertTrue(me.should_leave(other), "Не съебал, хотя должен был")

    def test_should_leave_expect_false(self):
        me: Character = Character(name="Me", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        other: Character = Character(name="Other", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        self.assertFalse(me.should_leave(other), "Съебал, хотя не должен был")


if __name__ == '__main__':
    unittest.main(verbosity=2)

from core.character import Character
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

    def test_can_leave_true(self):
        me: Character = Character(name="Me", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        other: Character = Character(name="Other", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        self.assertTrue(me.can_leave(other), "Съебал, так запланировано")

    def test_can_leave_false(self):
        me: Character = Character(name="Me", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        other: Character = Character(name="Other", hp=10, defence=1, speed=11, attack_speed=1, power=1)
        self.assertFalse(me.can_leave(other), "Съебал, так НЕ запланировано")

    def test_fight_true(self):
        me: Character = Character(name="Me", hp=101, defence=11, speed=1, attack_speed=11, power=11)
        other: Character = Character(name="Other", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        self.assertTrue(me.fight(other), "Просрал бой, так НЕ запланировано")

    def test_fight_false(self):
        me: Character = Character(name="Me", hp=10, defence=1, speed=1, attack_speed=1, power=1)
        other: Character = Character(name="Other", hp=101, defence=11, speed=1, attack_speed=11, power=11)
        self.assertFalse(me.fight(other), "Победил бой, так НЕ запланировано")


if __name__ == '__main__':
    unittest.main(verbosity=2)

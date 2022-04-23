import logging

import mathlib as ml

class Test_ADD:
    def test_add_positive(self):
        assert ml.add(1, 2) == 3
        assert ml.add(2, 0) == 2
        assert ml.add(0, 0) == 0
        assert ml.add(130, 200) == 330

    def test_add_negative(self):
        assert ml.add(-3, -4) == -7
        assert ml.add(-10, 0) == -10
        assert ml.add(-1000, -200) == -1200

    def test_add_different(self):
        assert ml.add(-4, 5) == 1
        assert ml.add(8, -10) == -2
        assert ml.add(805, -1120) == -315

    def test_add_decimal(self):
        assert ml.add(3.1, 4.5) == 7.6
        assert ml.add(-2.6, 5.2) == 2.6
        assert ml.add(8.9, -6.9) == 2
        assert ml.add(-3.3, -4.9) == -8.2

class Test_Sub():
    def test_sub_positive(self):
        assert ml.sub(3, 1) == 2
        assert ml.sub(4, 4) == 0
        assert ml.sub(4, 0) == 4
        assert ml.sub(4, 5) == -1

    def test_sub_negative(self):
        assert ml.sub(-4, -4) == 0
        assert ml.sub(-5, -4) == -1
        assert ml.sub(-6, -8) == 2
        assert ml.sub(-546, -300) == -246

    def test_sub_diff(self):
        assert ml.sub(-3, 3) == -6
        assert ml.sub(4, -4) == 8
        assert ml.sub(66, -30) == 96

    def test_sub_dec(self):
        assert ml.sub(2.45, 6.83) == -4.38
        assert ml.sub(7.3, 2.4) == 4.9
        assert ml.sub(-143.5, 83.56) == -227.06

class Test_Mul():
    def test_mul_positive(self):
        assert ml.mul(3, 4) == 12
        assert ml.mul(4, 0) == 0
        assert ml.mul(14, 0) == 0
        assert ml.mul(14, 7) == 98

    def test_mul_negative(self):
        assert ml.mul(-4, -5) == 20
        assert ml.mul(-5, -44) == 220
        assert ml.mul(-14, -7) == 98

    def test_mul_diff(self):
        assert ml.mul(-3, 3) == -9
        assert ml.mul(4, -4) == -16
        assert ml.mul(66, -33) == -2178

    def test_mul_dec(self):
        assert ml.mul(2.5, 4.5) == 11.25
        assert ml.mul(-3.8, 11.1) == -42.18
        assert ml.mul(-11.1, 3.8) == -42.18

class Test_Div():
    def test_div_positive(self):
        assert ml.div(12, 4) == 3
        assert ml.div(4, 16) == 0.25
        assert ml.div(0, 4) == 0
        assert ml.div(5, 0) == ml.error_message_1

    def test_div_negative(self):
        assert ml.div(-10, -5) == 2
        assert ml.div(-5, -10) == 0.5
        assert ml.div(-400, -50) == 8

    def test_div_diff(self):
        assert ml.div(24, -4) == -6
        assert ml.div(-4, 16) == -0.25
        assert ml.div(-240, -48) == 5

    def test_div_dec(self):
        assert ml.div(43.5, 3.8) == 11.447368421052632
        assert ml.div(-53.4, 2.2) == -24.27272727272727
        assert ml.div(-48.43, 53.3) == -0.9086303939962477

class Test_Root():
    def test_root_neg_bad(self):
        assert ml.root(-2, 2) == ml.error_message_root
        assert ml.root(-48, 10) == ml.error_message_root

    def test_root_zero(self):
        assert ml.root(0, 2) == 0

    def test_root_pos(self):
        assert ml.root(4, 2) == 2
        assert ml.root(16, 4) == 2
        assert ml.root(81, 3) == 4.3267487109222245

    def test_root_neg_good(self):
        assert ml.root(27, 3) == 3
        assert ml.root(-27, 3) == -3
        assert ml.root(-280, 9) == -1.8702792171149192

class Test_Fact():
    def test_fact_bad(self):
        assert ml.factorial(-2) == ml.error_message_fact;
        assert ml.factorial(3.3) == ml.error_message_fact
        assert ml.factorial(-44.55) == ml.error_message_fact

    def test_fact_zero(self):
        assert ml.factorial(0) == 1

    def test_fact_good(self):
        assert ml.factorial(3) == 6
        assert ml.factorial(4) == 24
        assert ml.factorial(10) == 3628800

class Test_Power():
    def test_power_posit(self):
        assert ml.pow(2, 2) == 4
        assert ml.pow(4, 3) == 64
        assert ml.pow(-3, 3) == -27
        assert ml.pow(-4, 2) == 16

    def test_power_neg(self):
        assert ml.pow(2, -2) == 0.25
        assert ml.pow(-4, -4) == 1/256
        assert ml.pow(2, -3) == 1/8
        assert ml.pow(-3, -3) == -1/27

    def test_pow_decim(self):
        assert ml.pow(1.5, 2) == 2.25
        assert ml.pow(4, 1.5) == 8
        assert ml.pow(-2, 3.99) == ml.error_message_root

class Test_Sin():
    def test_sin(self):
        assert ml.sin(0) == 0
        assert ml.sin(-1) == -0.8414709848078965
        assert ml.sin(1) == 0.8414709848078965
        assert ml.sin(20.1) == 0.9491245536478946
        assert ml.sin(-541.32) == -0.8226540731980578

class Test_Cos():
    def test_cos(self):
        assert ml.cos(0) == 1
        assert ml.cos(1) == 0.5403023058681398
        assert ml.cos(-1) == 0.5403023058681398
        assert ml.cos(25.24) == 0.9942532905535724

import time


class TestCalculator:

    def test_calculator(self, calculator):

        delay = "45"
        calculator.set_delay(delay)
        calculator.push_btn("7")
        calculator.push_btn("+")
        calculator.push_btn("8")
        calculator.push_btn("=")
        start_time = time.time()
        calculator.wait_result(int(delay), "15")
        end_time = time.time()
        elapsed_time = int(end_time - start_time)

        assert elapsed_time == int(delay)

from captcha_solver import CaptchaSolver

solver = CaptchaSolver('browser')
with open('captcha.jpeg', 'rb') as inp:
    data = inp.read()
print(solver.solve_captcha(data))
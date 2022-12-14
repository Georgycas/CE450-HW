TARGET = 100


class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.prev_error = 0
        self.integral = 0

    def update(self, error, dt):
        derivative = (error - self.prev_error) / dt
        self.integral += error * dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output


pid = PID(Kp=8, Ki=5, Kd=1.6)

error = TARGET - 70
output = pid.update(error, dt=1)
print(f"t = {0}, error = {error}, output = {output}")

error = TARGET - 80
output = pid.update(error, dt=1)
print(f"t = {1}, error = {error}, output = {output}")

error = TARGET - 90
output = pid.update(error, dt=1)
print(f"t = {2}, error = {error}, output = {output}")

error = TARGET - 93
output = pid.update(error, dt=1)
print(f"t = {3}, error = {error}, output = {output}")

error = TARGET - 95
output = pid.update(error, dt=1)
print(f"t = {4}, error = {error}, output = {output}")

error = TARGET - 98
output = pid.update(error, dt=1)
print(f"t = {5}, error = {error}, output = {output}")

error = TARGET - 99
output = pid.update(error, dt=1)
print(f"t = {6}, error = {error}, output = {output}")

error = TARGET - 103
output = pid.update(error, dt=1)
print(f"t = {7}, error = {error}, output = {output}")

error = TARGET - 97
output = pid.update(error, dt=1)
print(f"t = {8}, error = {error}, output = {output}")

from buckinghampy import BuckinghamPi

# Initialize BuckinghamPi
example = BuckinghamPi()

# Add the variables and their dimensions
# Displacement (s) has dimensions L
example.add_variable(name='s', dimensions='L')

# Time (t) has dimensions T
example.add_variable(name='t', dimensions='T', non_repeating=True)

# Initial velocity (v) has dimensions L/T
example.add_variable(name='v0', dimensions='L/T')

# Acceleration due to gravity (g) has dimensions L/T^2
example.add_variable(name='g', dimensions='L/T^2')

# Initial position (s0) has dimensions L
example.add_variable(name='s0', dimensions='L')

# Generate and print the dimensionless π terms
example.generate_pi_terms()
example.print_all()

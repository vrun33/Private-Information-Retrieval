import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define maximum plot range
max_range = 5

# Define number of points to show for different degrees
num_points = [1, 2, 3]  # One point for degree 1, two points for degree 2, etc.
degrees = [n - 1 for n in num_points]  # Corresponding degrees

# Create the animation
fig, ax = plt.subplots()
lines, points = [], []  # Lists to store lines and points

def init():
  ax.set_xlim(-max_range, max_range)
  ax.set_ylim(-max_range, max_range)
  ax.set_xlabel("X")
  ax.set_ylabel("Y")
  ax.set_title("Points and Polynomials")
  return lines, points

def animate(frame_num):
  degree = degrees[frame_num]
  num_point = num_points[frame_num]

  # Clear existing elements
  for line in lines:
    line.remove()
  for point in points:
    point.remove()
  lines.clear()
  points.clear()

  # Create points with random coordinates
  for _ in range(num_point):
    x = np.random.uniform(-max_range, max_range)
    y = np.random.uniform(-max_range, max_range)
    point, = ax.plot(x, y, 'o', markersize=15, color='blue')
    points.append(point)

  # Simulate a polynomial curve (invisible for degree 1)
  if degree > 0:
    x = np.linspace(-max_range, max_range, 100)  # 100 points for the curve
    y = np.random.rand(100)  # Random y-values for demonstration (not a true polynomial)
    line, = ax.plot(x, y, color='red', linewidth=2, alpha=0.7 if degree == 1 else 1)  # Faded line for degree 1
    lines.append(line)

  # Update title based on degree and number of points
  ax.set_title(f"{num_point} Points to Define a Degree-{degree} Polynomial")
  return lines, points

anim = FuncAnimation(fig, animate, init_func=init, frames=len(degrees), interval=2000)
plt.show()
import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path

# Paths relative to this script so Code Runner / any cwd works
SCRIPT_DIR = Path(__file__).resolve().parent
assets_dir = SCRIPT_DIR / "assets"

butterfly_path = assets_dir / "buter.jpg"
lion_path = assets_dir / "lion.jpeg"

butterfly_img = cv.imread(str(butterfly_path))
lion_img = cv.imread(str(lion_path))

if butterfly_img is None:
    raise FileNotFoundError(f"Could not load image: {butterfly_path}")
if lion_img is None:
    raise FileNotFoundError(f"Could not load image: {lion_path}")

# Matplotlib display (convert BGR → RGB)
plt.imshow(cv.cvtColor(butterfly_img, cv.COLOR_BGR2RGB))
plt.title("Matplotlib Display")
plt.axis("off")
plt.show()

# OpenCV windows
cv.imshow("Butterfly", butterfly_img)
cv.waitKey(5000)
cv.destroyWindow("Butterfly")

cv.imshow("Lion", lion_img)
cv.waitKey(5000)
cv.destroyWindow("Lion")

# Close when q pressed
while True:
    cv.imshow("Press q to exit", lion_img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()

import matplotlib.pyplot as plt

from src.microspotreader import *

# Load image
loader = ImageLoader()
loader.set(invert_image=True)
test_image = loader.prepare_image(r"example_files\part2_a12-l22.tif")

spot_detector = SpotDetector(test_image)
spot_detector.change_settings_dict({"edge_detection": {"sigma": 5}})
print(spot_detector.settings, spot_detector.keyword_list)
spot_list = spot_detector.initial_detection(132)

grid = GridDetector(test_image, spot_list).detect_grid()

SpotCorrector(spot_list).gridbased_spotcorrection(grid)

SpotIndexer(spot_list).assign_indexes()

spot_list.get_spot_intensities(test_image)
spot_list.normalize_by_median()

halo_detector = HaloDetector(test_image)
halo_detector.perform_halo_detection()
halo_detector.assign_halos_to_spots(spot_list)

spot_list.scale_halos_to_intensity(0.04)

spot_list.plot_heatmap()
plt.show()

#Helper functions needed in the script
#processing.algorithmHelp("gdal:warpreproject")
#https://docs.qgis.org/3.4/en/docs/user_manual/processing/console.html
import processing
import os
from qgis.core import QgsRasterLayer

def change_resolution(image_path, new_resolution, upsampling_method):
	"""Changes resolution of a given image. The parameters are image_path, new_resolution and upsampling_method.
	upsampling_method is used for increasing artificially the rosultion in order to use another raster available originally in this resolution
	Available values for upsampling_method:
		- 0: Nearest neighbour
		- 1: Bilinear
		- 2: Cubic
		- 3: Cubic spline
		- 4: Lanczos windowed sinc
		- 5: Average
		- 6: Mode
		- 7: Maximum
		- 8: Minimum
		- 9: Median
		- 10: First quartile
		- 11: Third quartile"""
	Image2beUpsampled = QgsRasterLayer(image_path)

	newImageBaseName = os.path.basename(image_path).replace(str(int(Image2beUpsampled.rasterUnitsPerPixelX())) + 'm', str(new_resolution)+'m')
	param = {}
	param['INPUT'] = Image2beUpsampled
	param['TARGET_CRS'] = Image2beUpsampled.crs()
	# print("image path: " + image_path)
	param['OUTPUT'] = os.path.join(os.path.dirname(image_path).replace(os.path.dirname(image_path)[-3:], str(new_resolution)+'m'), newImageBaseName.replace('jp2','tiff'))
	# print("output path: " + param['OUTPUT'])#,'D:\\test\\R60m\\testOutput10Channel7.tiff')
	param['RESAMPLING'] = upsampling_method
	param['TARGET_RESOLUTION'] = new_resolution
	print("before processing")
	result  = processing.run("gdal:warpreproject",param)
	print("after processing")
	#delete a
	return result['OUTPUT']
	
def check_resolution_compability(sentinelImage, channel_list):
	resolutions = []
	for i in channel_list:
		res, path = sentinelImage.highest_resolution_and_path_for_band(i)
		resolutions.append(res)
	print("Resolutions: " + str(resolutions))
	return len(set(resolutions)) == 1, resolutions

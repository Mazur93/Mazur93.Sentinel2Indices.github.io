#Helper functions needed in the script
#processing.algorithmHelp("gdal:warpreproject")
#https://docs.qgis.org/3.4/en/docs/user_manual/processing/console.html
import processing

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
	Image2beUpsampled = QgsRasterLayer(imagePath)

	newImageBaseName = os.path.basename(imagePath).replace(str(int(Image2beUpsampled.rasterUnitsPerPixelX())) + 'm', str(new_resolution)+'m')
	param = {}
	param['INPUT'] = Image2beUpsampled
	param['TARGET_CRS'] = Image2beUpsampled.crs()
	#os.path.dirname(imagePath) os.path.basename(imagePath)
	#TODO resolution_folder create dictionary with 10,20,60 resolution folder paths
	param['OUTPUT'] = os.path.join(resolution_folder[new_resolution], newImageBaseName)'D:\\test\\R60m\\testOutput10Channel7.tiff'
	param['RESAMPLING'] = upsampling_method
	param['TARGET_RESOLUTION'] = new_resolution
	result  = processing.run("gdal:warpreproject",param)
	delete a
	return result['OUTPUT']
	

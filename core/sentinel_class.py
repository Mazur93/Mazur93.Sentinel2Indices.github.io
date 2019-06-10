import os
import gdal


class sentinelImage:
    def __init__(self,path):
        self.path = path
        self.product_name = os.path.basename(self.path)
        self.tile_name = os.path.basename(self.path).split('_')[-2]
        self.granule_folder = os.path.join(self.path, 'GRANULE')
        self.under_granule_folder = next(os.walk(self.granule_folder))[1][0]
        self.resolution_folder_path = os.path.join(self.granule_folder, self.under_granule_folder, 'IMG_DATA')
        self.resolution_folder_names = ['R10m', 'R20m', 'R60m']

    def get_band(self, bandString, resolution):
        highest_resolution_available = highest_resolution_for_band(self, bandString)
        if resolution == highest_resolution_available:
            pass #get image from folder
        #create image in resolution
        else:
            if resolution < highest_resolution_available:
                raise Exception('The requested resolution is better than the highest available')
            else:
                # sampling to coarser resolution
                pass

    def highest_resolution_and_path_for_band(self, bandString):
        potential10m = [image for image in os.listdir(os.path.join(self.resolution_folder_path, 'R10m')) if
                        image.endswith(bandString + '_10m.jp2')]
        potential20m = [image for image in os.listdir(os.path.join(self.resolution_folder_path, 'R20m')) if
                        image.endswith(bandString + '_20m.jp2')]
        potential60m = [image for image in os.listdir(os.path.join(self.resolution_folder_path, 'R60m')) if
                        image.endswith(bandString + '_60m.jp2')]
        if len(potential10m) == 1:
            return 10, os.path.join(self.resolution_folder_path,'R10m',potential10m[0])
        elif len(potential20m) == 1:
            return 20, os.path.join(self.resolution_folder_path,'R20m',potential20m[0])
        elif len(potential60m) == 1:
            return 60, os.path.join(self.resolution_folder_path,'R60m',potential60m[0])
        else:
            raise("Band not available")

    def band_to_numpy_array(self, image_path):
        """Opens image in JP2 file and returns it casted to a numpy array
                """
        #load image
        img = gdal.Open(image_path)
        #get bands
        band = img.GetRasterBand(1)
        #convert into numpy arrays. Floats because of the subsequent division
        band_np = band.ReadAsArray().astype(float)
        return band_np

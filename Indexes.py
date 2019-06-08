class SatelliteIndex:
    def __init__(self,name):
        self.name = name




indexes = {}


#Basic index function, which calculates (channel1 - channel2)/(channel1 + channel2)
#input: 2 x 2D-numpy array, output = 1 x 2D-numpy array
def build_simple_index(channel1, channel2):
    # calculate index
    idx = channel1 - channel2
    idx = np.divide(idx, (channel1 + channel2))
    return idx


#Normalized Difference Vegetation Index
NDVI = SatelliteIndex('Normalized Difference Vegetation Index')
NDVI.abbreviation = 'NDVI'
NDVI.channels = ['B08', 'B04']
NDVI.function = build_simple_index
NDVI.use = 'Detection of vegetation'
NDVI.Source = 'https://www.sentinel-hub.com/eoproducts/ndvi-normalized-difference-vegetation-index'
indexes['NDVI'] = NDVI

#Normalized Difference Water Index
NDWI = SatelliteIndex('Normalized Difference Water Index')
NDWI.abbreviation = 'NDWI'
NDWI.channels = ['B08', 'B11']
NDWI.function = build_simple_index
NDWI.use = 'Detection of water'
NDWI.Source = 'https://www.sentinel-hub.com/develop/documentation/eo_products/Sentinel2EOproducts'
indexes['NDWI'] = NDWI

#Modified Normalized Difference Water Index
MNDWI = SatelliteIndex('Modified Normalized Difference Water Index')
MNDWI.abbreviation = 'MNDWI'
MNDWI.channels = ['B03', 'B11']
MNDWI.function = build_simple_index
MNDWI.use = 'Detection of water'
MNDWI.Source = 'https://www.mdpi.com/2072-4292/8/4/354'
indexes['MNDWI'] = MNDWI


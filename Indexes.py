indexes = {}


#Basic index function, which calculates (channel1 - channel2)/(channel1 + channel2)
#input: 2 x 2D-numpy array, output = 1 x 2D-numpy array
def build_simple_index(channel1, channel2):
    # calculate index
    idx = channel1 - channel2
    idx = np.divide(idx, (channel1 + channel2))
    return idx


#Normalized Difference Vegetation Index
NDVI={}
NDVI['name'] = 'Normalized Difference Vegetation Index'
NDVI['channels'] = ['B08','B04']
NDVI['function'] = build_simple_index
NDVI['use'] = 'Detection of vegetation'
NDVI['Source'] = 'https://www.sentinel-hub.com/eoproducts/ndvi-normalized-difference-vegetation-index'

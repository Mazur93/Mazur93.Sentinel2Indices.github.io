class SatelliteProduct:
    def __init__(self, name, channels, abbreviation, source):
        self.name = name
        self.channels = channels
        self.abbreviation = abbreviation
        self.source = source

products = {}

#The order is always red, green and blue.

TrueColour = SatelliteProduct("True Colour Image", ["B04", "B03", "B02"], "True Colour", "https://www.sentinel-hub.com/eoproducts/true-color")
products['True Colour'] = TrueColour

FalseColour = SatelliteProduct("False Colour Composite", ["B08", "B04", "B03"], "False Colour", "https://www.sentinel-hub.com/eoproducts/false-color")
products['False Colour'] = FalseColour

ShortWaveIR = SatelliteProduct("Short-wave Infrared", ["B12", "B08", "B04"], "Short-wave Infrared", "https://www.sentinel-hub.com/develop/documentation/eo_products/Sentinel2EOproducts")
products['Short-wave Infrared'] = ShortWaveIR

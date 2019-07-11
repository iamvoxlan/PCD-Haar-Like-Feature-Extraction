import SumRegion as sr
def enum(**enums):
    return type('Enum', (), enums)

FeatureType = enum(TWO_VERTICAL=(1, 2), TWO_HORIZONTAL=(2, 1), THREE_HORIZONTAL=(3, 1), THREE_VERTICAL=(1, 3), FOUR=(2, 2))
FeatureTypes = [FeatureType.TWO_VERTICAL, FeatureType.TWO_HORIZONTAL, FeatureType.THREE_HORIZONTAL, FeatureType.THREE_VERTICAL, FeatureType.FOUR]

class HaarLike(object):
    def __init__(self, f_type, position, width, height, polarity):
        self.type = f_type
        self.top_left = position
        self.bottom_right = (position[0]+height, position[1]+width)
        self.width = width
        self.height = height
        self.polarity = polarity

    def hitung_skor(self, int_img):
	    score = 0
	    if self.type == FeatureType.TWO_VERTICAL:
	            first = sr.sum_region(int_img, self.top_left, (self.top_left[0] + self.width, int(self.top_left[1] + self.height / 2)))
	            second = sr.sum_region(int_img, (self.top_left[0], int(self.top_left[1] + self.height / 2)), self.bottom_right)
	            score = first - second
	    elif self.type == FeatureType.TWO_HORIZONTAL:
	            first = sr.sum_region(int_img, self.top_left, (int(self.top_left[0] + self.width / 2), self.top_left[1] + self.height))
	            second = sr.sum_region(int_img, (int(self.top_left[0] + self.width / 2), self.top_left[1]), self.bottom_right)
	            score = first - second
	    elif self.type == FeatureType.THREE_HORIZONTAL:
	            first = sr.sum_region(int_img, self.top_left, (int(self.top_left[0] + self.width / 3), self.top_left[1] + self.height))
	            second = sr.sum_region(int_img, (int(self.top_left[0] + self.width / 3), self.top_left[1]), (int(self.top_left[0] + 2 * self.width / 3), self.top_left[1] + self.height))
	            third = sr.sum_region(int_img, (int(self.top_left[0] + 2 * self.width / 3), self.top_left[1]), self.bottom_right)
	            score = first - second + third
	    elif self.type == FeatureType.THREE_VERTICAL:
	            first = sr.sum_region(int_img, self.top_left, (self.bottom_right[0], int(self.top_left[1] + self.height / 3)))
	            second = sr.sum_region(int_img, (self.top_left[0], int(self.top_left[1] + self.height / 3)), (self.bottom_right[0], int(self.top_left[1] + 2 * self.height / 3)))
	            third = sr.sum_region(int_img, (self.top_left[0], int(self.top_left[1] + 2 * self.height / 3)), self.bottom_right)
	            score = first - second + third
	    elif self.type == FeatureType.FOUR:
	            first = sr.sum_region(int_img, self.top_left, (int(self.top_left[0] + self.width / 2), int(self.top_left[1] + self.height / 2)))
	            second = sr.sum_region(int_img, (int(self.top_left[0] + self.width / 2), self.top_left[1]), (self.bottom_right[0], int(self.top_left[1] + self.height / 2)))
	            third = sr.sum_region(int_img, (self.top_left[0], int(self.top_left[1] + self.height / 2)), (int(self.top_left[0] + self.width / 2), self.bottom_right[1]))
	            fourth = sr.sum_region(int_img, (int(self.top_left[0] + self.width / 2), int(self.top_left[1] + self.height / 2)), self.bottom_right)
	            score = first - second - third + fourth

	            
	    return score
from PIL import Image
from random import randint
Image.MAX_IMAGE_PIXELS = None

def transposeImg(out_ras, out_vec, seed):
	"""
	Saves a transposed version of cropped images
	@param ras: Image, cropped portion of raster image
	@param vec: Image, cropped portion of vector image
	@param seed: int unique filename
	"""
	out_ras.transpose(Image.FLIP_LEFT_RIGHT).save('./out/'+str(seed)+'_tran_x'+'.png')
	out_vec.transpose(Image.FLIP_LEFT_RIGHT).save('./out/'+str(seed)+'_tran_y'+'.png')

def rotImg(out_ras, out_vec, seed):
	"""
	Saves a rotated version of cropped images
	@param ras: Image, cropped portion of raster image
	@param vec: Image, cropped portion of vector image
	@param seed: int unique filename
	"""
	rotation = randint(0,365)
	out_ras.rotate(rotation).save('./out/'+str(seed)+'_rot_x'+'.png')
	out_vec.rotate(rotation).save('./out/'+str(seed)+'_rot_y'+'.png')

def genCoord(crop_size,img_size):
	"""
	generates random coordinates for a crop_size pixel square
	@param crop_size: int pixel size of output img
	@param img_size: Image size of image in pixelse
	ret: (left, upper, right, lower)
	"""
	width,height = img_size
	xaxis = randint(0,width-crop_size)
	yaxis = randint(0,height-crop_size)
	return (xaxis,yaxis,xaxis+crop_size,yaxis+crop_size)

def cropImg(img_ras, img_vec, coordinates, seed):
	"""
	crops images of given coordinates, x=raster, y=vector
	@param: img_ras: PIL.image input raster image
	@param img_vec: PIL.image input vecor image
	@param coordinates: tuple (x1,y2,x2,y2)
	@param seed: int unique filename
	"""
	out_ras = img_ras.crop(coordinates)
	out_vec = img_vec.crop(coordinates)

	out_ras.save('./out/'+str(seed)+'_x'+'.png')
	out_vec.save('./out/'+str(seed)+'_y'+'.png')

	rotImg(out_ras, out_vec, seed)
	transposeImg(out_ras, out_vec, seed)
	

if __name__ == '__main__':
	crop_size = 500 #size out output img in pizels
	num_gen = 100 #Number of generated images per map
	raster_image = "./raster.png"
	vector_image = "./vector.png"
	
	ras_obj = Image.open(raster_image)
	vec_obj = Image.open(vector_image)
	for seed in range (num_gen):
		cropImg(ras_obj, vec_obj, genCoord(crop_size,ras_obj.size), seed)
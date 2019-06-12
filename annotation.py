import os
import ast
import cv2
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))

annotation_file = open('train_annotations.txt', 'r+')

for line in annotation_file:
	d = ast.literal_eval(line)
	# print(d['ID'])
	img = cv2.imread(d['ID'] + '.jpg')
	if type(img) is np.ndarray:
		img_height, img_width = img.shape[:2]
		# print(img_width, img_height)
		file = open(d['ID'] + '.txt', 'w')

		for i in range(len(d['gtboxes'])):
			if d['gtboxes'][i]['tag'] == 'person':
				l = d['gtboxes'][i]['fbox']
				# print(l)

				file.write('0 ' + str((l[0]+l[2]/2)/img_width) + ' ' + str((l[1]+l[3]/2)/img_height)
					+ ' ' + str(l[2]/img_width) + ' ' + str(l[3]/img_height) + '\n')

				#cv2.rectangle(img, (l[0], l[1]), (l[0]+l[2], l[1]+l[3]), (0, 0, 255), 2)
				#cv2.imwrite(d['ID'] + '2.jpg', img)

annotation_file.close()

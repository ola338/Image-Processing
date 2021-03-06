import numpy as np

def my_median_filter(image, filter_size=(5,5)):
  ii = filter_size[0] // 2
  ij = filter_size[1] // 2
  median_image = np.zeros(image.shape)
  for i in range(1, ii+1):                 
    for j in range(1, ij+1):               
      for y in range(image.shape[0]):      
        for x in range(image.shape[1]):
          if (y-ii >= 0) and (x-ij >= 0) and (y+ii < image.shape[0]) and (x+ij < image.shape[1]):          # środek
            median_image[y, x] = np.median(image[y-ii: y+ii+1, x-ij: x+ij+1])
            
          elif (y-ii == -i and x-ij == -j):             #+(0,1)                                            # l-g róg
            median_image[y, x] = np.median(image[y-ii+i: y+ii+1, x-ij+j: x+ij+1])
          elif (y-ii == -i and x+ij == image.shape[1]-1+j):                                                # p-g róg
            median_image[y, x] = np.median(image[y-ii+i: y+ii+1, x-ij: x+ij+1-j])
          elif (x-ij == -j and y+ii == image.shape[0]-1+i):                                                # l-d róg
            median_image[y, x] = np.median(image[y-ii: y+ii+1-i, x-ij+j: x+ij+1])
          elif (y+ii == image.shape[0]-1+i and x+ij == image.shape[1]-1+j):                                # p-d róg
            median_image[y, x] = np.median(image[y-ii: y+ii+1-i, x-ij: x+ij-j])

          if median_image[y, x] == 0:
            if (y-ii == -i):                                                                               # lewy brzeg
              median_image[y, x] = np.median(image[y-ii+i: y+ii+1, x-ij: x+ij+1])
            elif (y+ii == image.shape[0]-1+i):                                                             # prawy brzeg
              median_image[y, x] = np.median(image[y-ii: y+ii+1-i, x-ij: x+ij+1])
            elif (x-ij == -j):                      #-(0,1)                                                # górny brzeg
              median_image[y, x] = np.median(image[y-ii: y+ii+1, x-ij+j: x+ij+1])
            elif (x+ij == image.shape[1]-1+j):                                                             # dolny brzeg
              median_image[y, x] = np.median(image[y-ii: y+ii+1, x-ij: x+ij+1-j])

  return median_image